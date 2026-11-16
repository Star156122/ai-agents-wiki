---
title: 五種常見的 Workflow 模式
type: concept
sources: [src-01]
updated: 2026-11-17
---

# 五種常見的 Workflow 模式

所有模式都建立在 augmented LLM 之上。[src-01]

| 模式 | 作法 | 適合 |
|---|---|---|
| Prompt chaining | 把任務拆成固定順序的步驟，步驟間可加檢查 [src-01] | 能清楚拆解的任務；用延遲換準確度 [src-01] |
| Routing | 先分類輸入，再導向專門的提示、工具或模型 [src-01] | 不同類型輸入需要不同處理，例如簡單問題用較便宜的模型 [src-01] |
| Parallelization | 子任務同時執行（sectioning），或同一任務跑多次比對（voting），再彙整 [src-01] | 可平行的子任務，或需要多次驗證 |
| Orchestrator-workers | 中央 LLM 動態拆解任務、指派給 worker、整合結果 [src-01] | 子任務無法事先預測 |
| Evaluator-optimizer | 一個 LLM 產生、另一個 LLM 評論，循環到夠好 [src-01] | 有清楚評估標準、能靠回饋改進的任務 |

## 與本專案的關聯
本專案的產出流程用到 **evaluator-optimizer** 的精神：產生簡報後由檢查腳本評估，不合格就回頭修正。見 `docs/LOOP.md`。
