---
id: Q0105
normalized_question: vLLM 有哪些常见的推理优化技术？
legacy_id: Q0123
area: Reliability / Production
knowledge_point: inference-optimization
tags:
  - Inference
  - Optimization
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# vLLM 有哪些常见的推理优化技术？

## 原题原文

> 都知道哪些 vllm 的优化技术？

## 答案

### 面试直答

vLLM 的核心优化包括 PagedAttention 管理 KV Cache、Continuous Batching 提高动态请求吞吐，以及 Prefix Caching、Chunked Prefill、Speculative Decoding、量化和分布式并行。它们分别优化显存碎片、GPU 利用率、重复前缀、长 Prefill、逐 Token 解码和模型容量。

### 一、核心技术

| 技术 | 解决的问题 | 主要代价 |
|---|---|---|
| PagedAttention | KV Cache 连续预留和碎片 | 页表管理开销 |
| Continuous Batching | 请求长短不同导致 GPU 空闲 | 调度复杂、单请求延迟需权衡 |
| Prefix Caching | 相同 System/长前缀重复 Prefill | Cache 占显存、命中依赖前缀一致 |
| Chunked Prefill | 长 Prompt 阻塞 Decode | 调度参数需要调优 |
| Speculative Decoding | 自回归逐 Token 慢 | Draft/验证开销和接受率 |
| Quantization | 权重/KV 显存与带宽 | 精度及 Kernel 支持 |
| Tensor/Pipeline Parallel | 单卡放不下或吞吐不足 | 通信开销 |

> **核心小结：** vLLM 不是单一算法加速，而是从 KV 内存、批调度和 Kernel/并行共同优化 Serving。

### 二、PagedAttention 与连续批处理

KV Cache 按 Block 分页，逻辑序列不要求物理显存连续，可以按需分配、共享或回收，从而减少碎片并容纳更多并发序列。Continuous Batching 在每个调度步加入新请求、移除已完成请求，避免静态 Batch 等最慢序列。

> **核心小结：** PagedAttention 提高可容纳并发，Continuous Batching 提高这些并发请求的实际 GPU 利用率。

### 三、如何调优

先区分 TTFT 和 TPOT：长 Prefill 优化 TTFT，Decode 调度影响 TPOT。根据显存调最大并发 Token、KV Cache、Batch 与并行度；用真实输入/输出长度分布压测吞吐、P95/P99 和 OOM。Prefix Cache 对共享长前缀收益大，对随机 Prompt 收益有限。

> **核心小结：** vLLM 配置必须按工作负载调，离线最大吞吐配置不一定适合在线尾延迟 SLO。

### 来源

- [vLLM 官方文档](https://docs.vllm.ai/en/latest/)
- [vLLM GitHub](https://github.com/vllm-project/vllm)

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 04
- 岗位与面试时间：大模型算法 ｜ 面试时间：2026 年 4 月 15 日
- 题目在小节内的位置：第 1 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
