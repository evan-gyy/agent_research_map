---
id: Q0212
area: Architecture
company: 字节跳动
source_track: field-note
evidence: derived-from-record
collection_difficulty: easy
status: outline
---

# Orchestrator 如何处理有副作用的步骤？

## 标准答案

标记副作用与幂等性，执行前确认权限和前置条件，执行后记录结果，并为可补偿动作定义回滚。

## 原理展开

<!-- 后续按需补充。 -->

## 延伸问题

<!-- 后续按需补充。 -->

## 相关论文、博客和项目

<!-- 只加入与本题直接相关的资料。 -->

## 问题来源

- 公司：字节跳动
- 来源类型：学习问答记录
- 证据级别：由同一记录中的原题延伸，不代表直接出现
- 采集难度：低（公司与原题已在本地结构化）
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 当前核验：2026-09-01 在线访问受安全审批服务故障阻断，沿用本地 2026-08-31 记录
- 来源记录：[[FN-BD-01-字节跳动 Agent 问答记录]]

