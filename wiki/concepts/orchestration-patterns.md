---
title: 多 Agent 的編排模式
type: concept
sources: [src-05, src-01]
updated: 2026-11-17
---

# 多 Agent 的編排模式

OpenAI 的指南列出三種編排方式：[src-05]

1. **單一 agent 迴圈**：一個 agent 帶著工具與指示反覆執行，建議作為起點。
2. **Manager 模式**：中央 agent 透過工具呼叫把工作交給專家 agent，並保有對話的控制權。
3. **Decentralized 模式**：多個 agent 平等，彼此交棒，每個都能直接與使用者互動。

## 與 workflow 模式的呼應
Anthropic 的 orchestrator-workers 與 manager 模式概念相近：中央一個 LLM 分派、其他負責執行。[src-01]

## 選擇建議
先用單一 agent，需要時才增加；複雜度要有可量測的好處才值得加。[src-05][src-01]

## 相關
[workflow-patterns.md](workflow-patterns.md)、[agent-loop.md](agent-loop.md)
