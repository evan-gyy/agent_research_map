# Agent 实现研究方法

## 1. 锁定研究对象

记录产品全名、官方仓库、包名、默认分支、Commit、发布日期、核验日期、许可证，以及本地资料是否为官方来源。名称冲突时先查包元数据、仓库 Owner 和官方链接。

不要混淆产品 UI、Agent SDK、CLI、核心 Runtime、协议层、模型服务、第三方插件和社区 Fork。

## 2. 建立证据矩阵

开始写作前维护表格：

| 结论 | 证据标签 | 来源 | 代码入口/符号 | 版本 | 限制 |
|---|---|---|---|---|---|
| 一轮如何启动 | 官方公开源码确认 | repository | entrypoint/symbol | commit | 服务端未知 |

优先级通常是：官方文档与官方源码 > 可复现实验 > 官方 Issue/Release > 历史快照 > 第三方资料。两个一手来源冲突时，以版本更匹配的证据为准并解释差异。

代码能证明机制存在，不能单独证明线上默认开启、使用比例或准确率提升。文档能证明公开契约，不能证明所有内部实现细节。

## 3. 宽搜一次，再沿调用链收敛

第一次宽搜覆盖：

- 入口与命令：`main`, `cli`, `run`, `start`, `query`, `session`；
- 模型与循环：`stream`, `complete`, `tool_call`, `tool_result`, `stop`；
- 上下文：`prompt`, `message`, `compact`, `truncate`, `memory`；
- 工具：`tool`, `schema`, `registry`, `extension`, `mcp`；
- 安全：`permission`, `approval`, `sandbox`, `policy`；
- 状态：`session`, `thread`, `resume`, `fork`, `checkpoint`, `jsonl`；
- 并发：`agent`, `subagent`, `spawn`, `task`, `queue`；
- 观测：`event`, `trace`, `telemetry`, `usage`, `cost`。

随后只读调用链直接涉及的文件，不按目录逐个复述。

## 4. 追踪一条真实请求

至少回答：

1. 用户输入从哪个入口进入？
2. 配置、项目规则、历史和工具 Schema 在哪里装配？
3. 模型 API 请求由谁创建，流式事件如何解析？
4. Tool Call 如何校验、路由、执行和配对 Tool Result？
5. 哪些条件导致继续循环、重规划、停止、取消或失败？
6. Transcript、Session、Checkpoint 在哪里写入与恢复？
7. 错误、超时、部分成功和用户中断如何传播？

优先用源码路径和符号构造调用链：

```text
CLI / SDK / App entry
  -> session or runtime constructor
  -> context / system prompt builder
  -> model stream
  -> assistant block parser
  -> tool router / executor
  -> tool result message
  -> continue / compact / stop
  -> persistence and event emission
```

## 5. 模块深挖问题清单

开始前先做一张“能力清单”：区分默认内建、可选配置、Extension/Package 实现、实验路径、明确不内建和公开资料未发现。产品明确选择不内建的能力也是架构事实，不能写成“忘了实现”，也不能把生态示例写成默认功能。

### Agent Loop 与 Planning

- 是固定 Workflow、先规划后执行、逐步 ReAct，还是混合模式？
- 继续与停止由模型、代码还是 Hook 决定？
- 是否有限步、总体 Deadline、成本或 Token 预算？
- 并发工具结果如何排序、配对和取消？

### Context

- 稳定规则、会话历史、项目文件、工具 Schema 和附件如何进入 Prompt？
- 是否截断工具结果、微压缩、全局摘要、重注入稳定规则？
- 原始 Transcript 是否保留，摘要是否可回溯？
- Prompt Cache 需要哪些稳定前缀？

### Tool 与扩展

- Tool Registry、Schema、输入校验、权限、超时、重试和幂等分别在哪一层？
- 扩展是否能添加工具、Prompt、UI、事件处理器或 Provider？
- 大量工具是否按需加载？
- 外部 MCP/插件与内置工具的信任边界是什么？

### Permission 与安全

- Prompt、规则、Hook、用户批准、沙箱分别负责什么？
- 文件、网络、命令和外部副作用如何限制？
- 非交互模式如何处理原本需要批准的动作？
- 是否存在 Bypass，默认是否安全？

### Session 与恢复

- Session/Thread/Turn/Item 等核心状态对象是什么？
- Resume、Fork、Branch、Compaction Boundary 的语义是什么？
- 恢复时如何处理孤儿 Tool Call、过期文件和未完成动作？

### Subagent 与并发

- 子 Agent 得到完整父历史、摘要还是任务 Prompt？
- 工具、权限、工作目录和模型如何继承？
- 结果怎样返回，写冲突怎样避免？
- 不支持子 Agent 时，不要从并发 Tool Call 推断出多 Agent。

### 可观测与评估

- 产品暴露 Text Chunk、Thinking、Tool Call、Usage、Cost、Error 中的哪些事件？
- 能否从日志重建一次任务？
- 是否有测试、Eval、基准或可复现实例？
- 报告质量、延迟、成本与失败率时，样本量和预算是否一致？

## 6. 最小可复现实验

源码允许时运行一个最小任务，记录输入、命令、输出事件和落盘状态。实验优先验证最容易误读的机制，例如：

- 工具结果是否真的进入下一轮；
- Session Resume 是否恢复历史；
- Extension 是否实际注册工具；
- 压缩后规则是否重载；
- 并发工具是否真并行；
- 非交互模式是否跳过或拒绝审批。

不要将“命令返回 0”当成业务机制验证；检查真实事件、文件或 Session 变化。

验证结果分开记录：构建结果、定向机制测试、全量测试、真实 API 实验。失败还要区分产品行为错误、平台差异、缺少生成资源/依赖和测试前置条件；未进入测试用例不能写成测试失败或通过。

对于快速演进的 Monorepo，检查稳定默认主链和 `experimental/`、Feature Flag、RFC 路径的边界。依赖某个新 Runtime 不等于所有默认请求已经迁移到该 Runtime。

## 7. 源码引用格式

每个关键机制至少给：仓库/Commit、文件路径、符号、它在调用链中的作用。代码节选一般 5-25 行，必要时改为等价伪代码并明确标记。

示例：

```ts
// 等价伪代码：展示循环结构，不是逐字源码
while (true) {
  const response = await model.stream(context)
  const calls = collectToolCalls(response)
  if (calls.length === 0) break
  context.push(await executeAndPair(calls))
}
```

然后说明真实实现比伪代码多出的取消、错误、压缩和持久化分支。

## 8. 停止检索条件

当端到端主链、关键状态对象、工具边界、Context 策略、扩展方式、停止/错误路径和证据限制均可回答时停止。不要为增加篇幅继续搜索无关文件。
