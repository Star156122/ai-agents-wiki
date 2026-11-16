# CLAUDE.md — AI Agents LLM Wiki 與教學簡報

> 本文件是這個專案的 schema：規定 Wiki 怎麼建、簡報怎麼從 Wiki 產生、產出前要怎麼檢查。

## 1. 目的
- 建立「AI Agents」主題的 LLM Wiki，作為唯一知識來源。
- 從 Wiki 產生一份教學型 HTML 簡報（`index.html`），讀者是**完全沒接觸過 AI Agents 的人**。

## 2. 目錄結構
```
/
├── CLAUDE.md            # 本文件（schema）
├── index.html           # 教學簡報（單檔 HTML，鍵盤 ← → 翻頁）
├── wiki/
│   ├── index.md         # 目錄：所有頁面都必須列在這裡
│   ├── log.md           # 依時間記錄每次 ingest / 修改
│   ├── sources/         # 一篇原始資料對應一頁：src-NN-slug.md
│   └── concepts/        # 概念頁：每頁只講一個概念
├── tools/check.py       # 自動檢查腳本（見第 6 節）
└── docs/                # LOOP 設計、執行紀錄、反思
```

## 3. Wiki 頁面格式
每頁開頭必須有 frontmatter：
```
---
title: 頁面標題
type: concept 或 source
sources: [src-01, src-03]     # concept 頁必填，且必須對應 wiki/sources/ 內真實存在的檔案
updated: YYYY-MM-DD
---
```
- **source 頁**必填：`url`、`fetched`（擷取日期）、「重點摘要」（用自己的話改寫）、「限制與注意」。
- 每個 source 頁最多一則直接引用，且引用不超過 15 個英文單字；其餘一律改寫。
- 直接引用只能取自**實際擷取到的文字**，不可憑記憶或推測補寫；沒把握就整段改寫、不引用。
- **concept 頁**每個重要陳述後面要標註來源，格式 `[src-01]`。
- 資料頁面沒寫的事（例如發布日期），一律寫「來源未標示」，不可憑記憶補。
- 概念之間用相對路徑連結，例如 `[ReAct](react.md)`。

## 4. Ingest 流程（先討論、後生成）
1. **討論**：先寫出準備建立的頁面清單與每頁要回答的問題，確認後才動手（記錄在 `docs/LOOP.md`）。
2. **取得**：用搜尋找到官方或原始來源，優先順序：原作者／官方 > 論文 > 二手整理。
3. **ingest**：一次一篇，寫 source 頁，再更新或新增受影響的 concept 頁。
4. 更新 `wiki/index.md` 與 `wiki/log.md`。
5. 執行 `python3 tools/check.py`，通過才算完成。

## 5. 簡報規則
- 每張投影片是一個 `<section class="slide" data-wiki="..." data-terms="...">`。
- `data-wiki`：這張投影片依據的 Wiki 頁面（可多個，用逗號分隔）。必須真實存在。
- `data-terms`：這張投影片出現的關鍵術語（逗號分隔），**每個術語都必須出現在 `data-wiki` 指向的頁面中**，用來檢查簡報沒有超出 Wiki 的內容。
- 每張投影片底部顯示「來源：」連結到對應的 Wiki 頁面。
- 教學結構：動機 → 定義 → 組成 → 運作方式 → 模式 → 風險 → 何時使用 → 小測驗 → 參考資料。
- 每張只講一個重點，文字精簡；術語第一次出現要附白話解釋。
- 簡報不得出現 Wiki 沒有的數字、日期或名稱。

## 6. 檢查（`tools/check.py`）
1. Wiki 頁面 frontmatter 完整、sources 指向存在的檔案
2. source 頁有 url / fetched，直接引用 ≤ 1 則且 ≤ 15 字
3. `wiki/index.md` 列出所有頁面；頁內相對連結無壞連結
4. 簡報每張投影片的 `data-wiki` 存在、`data-terms` 皆出現在來源頁
5. 每個 concept 頁至少被一張投影片使用（覆蓋率）

## 7. 禁止
- 引用 Wiki 以外的事實；刪除 source 頁；貼上大段原文。
- 修改本文件，除非使用者明確要求。
