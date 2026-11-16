---
title: Workflow 與 Agent 的差別
type: concept
sources: [src-01]
updated: 2026-11-17
---

# Workflow 與 Agent 的差別

Anthropic 把兩者都歸在「agentic systems」底下，但做出清楚區分：[src-01]

| | Workflow | Agent |
|---|---|---|
| 誰決定步驟 | 程式碼預先寫好路徑 | LLM 自己決定 |
| 可預測性 | 高 | 較低 |
| 彈性 | 低 | 高 |
| 成本與風險 | 較低 | 較高，錯誤可能累積 [src-01] |

## 選擇原則
- 從最簡單的方案開始，常常單次 LLM 呼叫加上檢索與範例就夠。[src-01]
- 定義明確、需要可預測性的任務用 workflow；步驟數無法預先決定的開放問題才考慮 agent。[src-01]

## 相關
- 五種常見 workflow：[workflow-patterns.md](workflow-patterns.md)
- 何時使用：[when-to-use-agents.md](when-to-use-agents.md)
