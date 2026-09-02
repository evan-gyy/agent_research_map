---
id: Q0052
normalized_question: 为什么要在沙箱环境中执行 Agent 自进化？
legacy_id: Q0062
area: Agent Application
knowledge_point: agent-self-evolution
tags:
  - Self-Evolution
  - Agent
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 为什么要在沙箱环境中执行 Agent 自进化？

## 原题原文

> 你这个自进化在这个沙箱环境做的一个目的是怎么去考虑的？

## 答案

### 面试直答

Agent 自进化要在沙箱执行，因为候选 Prompt、Skill 或代码可能触发未知命令、访问敏感文件、联网下载依赖或破坏环境。沙箱把文件、网络、进程、凭据和资源限制在可丢弃边界内，再通过测试决定是否发布。

### 一、沙箱控制

使用临时工作区和最小权限账户；默认断网或域名白名单；不注入生产凭据；限制 CPU、内存、进程数和时间；记录命令、文件 Diff 和外部访问。

> **核心小结：** 沙箱限制“最坏能造成什么”，审批决定“这次是否允许做”。

### 二、验证与发布

候选产物在固定基线和隐藏测试上运行，扫描依赖、恶意指令、数据泄漏和回归；通过后仍需人工审核、签名版本和灰度。沙箱成功不等于业务正确。

> **核心小结：** 自进化产物必须经历隔离执行、独立评测、审核和可回滚发布。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 18
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 7 月 31 日
- 题目在小节内的位置：第 4 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
