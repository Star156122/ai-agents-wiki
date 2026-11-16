---
title: 什麼時候該用 Agent
type: concept
sources: [src-05, src-01]
updated: 2026-11-17
---

# 什麼時候該用 Agent

## 先問：真的需要嗎？
從最簡單的方案開始，很多時候單次 LLM 呼叫加上檢索與範例就夠了。[src-01]
如果用例沒有明顯符合條件，確定性的方案可能就足夠。[src-05]

## 適合用 agent 的三個跡象（OpenAI）[src-05]
1. **複雜判斷、例外或依情境決策**，例如退款核准。
2. **規則集龐大且複雜，維護成本高**，例如供應商安全審查。
3. **高度依賴非結構化資料**，例如自然語言、文件、對話。

## Anthropic 的角度 [src-01]
- Agent 適合**步驟數無法預先決定**的開放式問題，並且你信任模型在適當環境中的決策。
- 定義明確、需要可預測性的任務，用 workflow。

## 簡單決策流程
1. 單次 LLM 呼叫能解決嗎？→ 用它。
2. 步驟固定可預先寫好嗎？→ workflow。
3. 步驟無法預測，且需要判斷？→ agent，並加上護欄。

## 相關
[workflow-vs-agent.md](workflow-vs-agent.md)、[guardrails-and-limits.md](guardrails-and-limits.md)
