---
name: agent-implementation-researcher
description: Research and explain an Agent product or framework from official documentation, public source code, reproducible behavior, or clearly labeled historical snapshots. Use for implementation deep dives, architecture maps, runtime call chains, context/tool/permission/session analysis, product comparisons grounded in code, and detailed Chinese learning documents. Do not use for a generic conceptual answer that does not require product evidence.
---

# Agent Implementation Researcher

Produce a source-grounded explanation of how an Agent actually runs. Separate current product facts, source observations, conceptual mappings, and engineering recommendations.

## Required workflow

1. Define the exact product, repository, version or commit, and verification date. Resolve ambiguous product names before writing.
2. Start with one broad official-source pass: official docs, official repository, package metadata, release notes, and local snapshots explicitly supplied by the user.
3. Build an evidence matrix before conclusions. Use these labels consistently:
   - **官方文档确认**
   - **官方公开源码确认**
   - **可复现实验确认**
   - **非官方历史快照观察**
   - **概念映射**
   - **工程建议**
   - **待核验**
4. Trace one real end-to-end request before cataloguing modules. Follow entrypoint, context construction, model call, tool call, result feedback, termination, persistence, and error paths.
5. Deep-dive the mechanisms that exist in the product: planning/loop, context, tools, extensions, permissions, sessions, subagents, observability, evaluation, and deployment. Do not force absent modules into the document.
6. Write for understanding: show control flow, state changes, protocol objects, short source excerpts, concrete examples, failure cases, and tradeoffs.
7. Validate claims against source symbols and run the most relevant build/test or a deterministic document validator.
8. Record unknowns explicitly. Never infer a private service implementation from a client API or treat a historical snapshot as the current product.

## Research depth

- For a quick map, read [references/research-method.md](references/research-method.md) and use only the relevant sections.
- For a source-level deep dive, read both [references/research-method.md](references/research-method.md) and [references/deliverable-standard.md](references/deliverable-standard.md) completely before research.
- When producing or updating a Markdown deep dive, run `node scripts/validate_agent_research.mjs <document> --strict`.
- On Chinese Windows, run the Skill Creator validator with UTF-8 mode (for example, set `PYTHONUTF8=1`) so Python does not decode the UTF-8 Skill as GBK.

## Non-negotiable boundaries

- Prefer official docs and the product's official repository. Third-party articles are discovery leads, not primary evidence.
- Record the exact commit for public source. If no commit exists, state the artifact date and why version identity is uncertain.
- Keep code excerpts short and explanatory. Cite repository path, symbol, and commit; do not reproduce large non-public source blocks.
- Distinguish an Agent product's documented vocabulary from teaching analogies such as ReAct, Plan-and-Execute, Workflow, Harness, or Actor Model.
- Separate architecture facts from performance claims. Code can prove a path exists; only evaluations can prove gains.
- Preserve existing user changes and project conventions. Update local Markdown unless the user explicitly requests a cloud document.

## Completion criteria

The result should let a technical reader answer: what runs, in what order, what state changes, which layer owns each decision, how tools and permissions interact, how the task stops or recovers, what evidence supports each claim, and what design lessons are transferable.
