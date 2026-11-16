---
title: Agent 的組成零件
type: concept
sources: [src-04, src-05, src-01]
updated: 2026-11-17
---

# Agent 的組成零件

同一件事有兩種常見的切法，可以互相對照。

## 研究視角（Weng）：大腦 + 三個組件 [src-04]
- **LLM 是控制器（大腦）**。
- **規劃（Planning）**
  - 任務分解：把大目標拆成子目標（如 Chain of Thought、Tree of Thoughts）。
  - 自我反思：回顧過去行動並改進（如 ReAct、Reflexion）。
- **記憶（Memory）**
  - 短期：context 內的學習，受 context window 限制。
  - 長期：外部向量資料庫，靠快速檢索取用。
- **工具使用（Tool use）**：呼叫外部 API，取得模型權重裡沒有的資訊，如最新資料、程式碼執行、私有資料。

## 實作視角（OpenAI）：模型、工具、指示 [src-05]
- **模型**：負責推理與決策。
- **工具**：函式或 API，分資料工具、行動工具、編排工具。
- **指示**：清楚的逐步指引，涵蓋邊界情況。

## Anthropic 的基本單元 [src-01]
**Augmented LLM**：LLM 加上檢索、工具與記憶，是所有 agentic 系統的建構基礎。

## 對照
| 概念 | Weng | OpenAI |
|---|---|---|
| 做決策的核心 | LLM 控制器 | 模型 |
| 能力延伸 | 工具使用 | 工具 |
| 行為規範 | （規劃與反思） | 指示 |
| 保留上下文 | 記憶 | （未單列為核心組件） |

## 相關
- [tools-and-mcp.md](tools-and-mcp.md)
- [agent-loop.md](agent-loop.md)
