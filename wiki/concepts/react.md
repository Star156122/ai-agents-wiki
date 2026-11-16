---
title: ReAct：邊想邊做
type: concept
sources: [src-02, src-04]
updated: 2026-11-17
---

# ReAct：邊想邊做

## 核心想法
**ReAct** 讓大型語言模型**交錯**產生「推理軌跡」與「任務行動」。[src-02]
- 推理幫助模型規劃、追蹤進度、處理意外。[src-02]
- 行動讓模型從外部（例如 Wikipedia API 或互動環境）取得資訊。[src-02]

## 為什麼需要
- 只用 chain-of-thought：沒有接地到外部世界，容易幻覺，錯誤沿推理鏈累積。[src-02]
- 只用行動：缺少抽象推理來設定目標與追蹤進度。[src-02]

## 實驗結果（定性）
- HotpotQA、FEVER：藉由檢索資訊降低幻覺。[src-02]
- ALFWorld、WebShop：僅用一到兩個範例提示，成功率勝過模仿學習與強化學習方法。[src-02]

## 在 agent 框架中的位置
ReAct 被歸類在「規劃」組件的「自我反思」之下。[src-04]

## 相關
[agent-loop.md](agent-loop.md)、[agent-components.md](agent-components.md)
