# Retail Math & Formulas — Complete Reference

## ⚠️ Critical DECA Exam Tips

1. **Always check if a percentage is based on cost or retail** — Gross margin is always based on retail; markup is typically based on cost
2. **Use cost, not retail price, in OTB calculations** — OTB reflects how much you can *spend* on inventory
3. **Never forget planned markdowns** — they reduce buying power and are a common trap
4. **OTB can go negative** — means you're over-committed and need to cancel orders
5. **Average beginning and ending stock for turnover metrics**
6. **Always include safety stock in reorder point calculations**

---

## Markup & Gross Margin

### Markup Formulas
```
Markup $ = Selling Price - Cost
Markup % (on Cost) = (Markup $ / Cost) × 100 = ((Selling Price - Cost) / Cost) × 100
Selling Price = Cost × (1 + Markup %)
```

### Gross Margin Formulas
```
Gross Margin $ = Net Sales - Cost of Goods Sold
Gross Margin % (on Retail) = (Gross Margin $ / Net Sales) × 100
                         = ((Selling Price - Cost) / Selling Price) × 100
```

### Key Difference
- **Markup** is based on COST — how much you added to what you paid
- **Gross Margin** is based on RETAIL — what percentage of the selling price is profit
- Gross margin is always LOWER than markup (same numbers, different base)

### Example
```
Cost = $40, Selling Price = $100

Markup $ = $100 - $40 = $60
Markup % = ($60 / $40) × 100 = 150%
Gross Margin $ = $100 - $40 = $60
Gross Margin % = ($60 / $100) × 100 = 60%
```

### Initial Markup Formula
```
Initial Markup % = (Operating Expenses + Profit + Reductions + Alterations - Cash Discounts) / Gross Sales × 100
```

**Reductions include**: markdowns, employee discounts, shrinkage, returns

### Maintained (Achieved) Markup Formula
```
Maintained Markup % = (Net Sales - Cost of Goods Sold) / Net Sales × 100
```

Reflects actual profit AFTER markdowns and reductions.

---

## Inventory & Turnover

### Inventory Turnover
```
Inventory Turnover = COGS / Average Inventory
                  = Net Sales / Average Inventory at Retail
```

Measures how many times inventory is sold and replaced over a period. Higher = better efficiency.

### Average Inventory
```
Average Inventory = (Beginning Inventory + Ending Inventory) / 2
```

### Days Sales of Inventory (DSI)
```
DSI = (Average Inventory / COGS) × 365
```

How many days it takes to sell the entire inventory. Lower = faster turnover.

### Stock-to-Sales Ratio
```
Stock-to-Sales = Beginning of Month (BOM) Stock $ / Monthly Sales $
```

Measures how many months of stock you have on hand.

### GMROI (Gross Margin Return on Investment)
```
GMROI = Gross Margin $ / Average Inventory at Cost
GMROI = Gross Margin % × Inventory Turnover
```

**Interpretation**:
- GMROI > 1.0: Making more money than invested in inventory ✅
- GMROI < 1.0: Losing money on inventory investment ❌

---

## Open-to-Buy (OTB)

### Primary Formula (Retail Basis)
```
Planned Purchases = Planned Sales + Planned Markdowns + Ending Inventory - Beginning Inventory
OTB = Planned Purchases - Merchandise On Order
```

### Alternative Cost-Based Formula
```
OTB = (Planned Sales / Gross Margin %) - (Beginning Inventory + Planned Receipts - Planned Markdowns)
```

### Worked Example
```
Beginning Inventory:    $9,000
Planned Sales:         $14,000
Planned Markdowns:       $200
Ending Inventory:       $12,000
Merchandise On Order:   $3,000

Planned Purchases = $14,000 + $200 + $12,000 - $9,000 = $17,200
OTB = $17,200 - $3,000 = $14,200
```

### OTB Adjustments
- **Sales lower than planned** → OTB increases (more money left to buy)
- **Sales higher than planned** → OTB decreases (sold more, need to buy less to hit EOM target)

---

## Replenishment & Reorder

### Reorder Point
```
Reorder Point = (Average Daily Usage × Lead Time) + Safety Stock
```

### Safety Stock
```
Safety Stock = (Max Daily Usage × Max Lead Time) - (Avg Daily Usage × Avg Lead Time)
```

Buffer inventory to absorb demand surges or shipping delays.

---

## Pricing & Profitability

### Breakeven Quantity
```
Breakeven Quantity = Fixed Costs / (Selling Price - Variable Cost per Unit)
```

### Price Elasticity of Demand (PED)
```
PED = (% Change in Quantity Demanded) / (% Change in Price)
```

- **|PED| > 1**: Elastic demand (sensitive to price changes)
- **|PED| < 1**: Inelastic demand (insensitive to price changes)

### Operating Profit
```
Operating Profit = Gross Margin - Operating Expenses
```

---

## Quick Reference Table

| Metric | Formula | Key Point |
|--------|---------|-----------|
| Markup % | (Selling Price - Cost) / Cost × 100 | Based on COST |
| Gross Margin % | (Selling Price - Cost) / Selling Price × 100 | Based on RETAIL |
| Inventory Turnover | COGS / Average Inventory | Higher = better |
| Days Sales of Inventory | (Avg Inventory / COGS) × 365 | Lower = faster |
| Stock-to-Sales | BOM Stock / Monthly Sales | Months of supply |
| GMROI | Gross Margin $ / Avg Inventory at Cost | Must be > 1.0 |
| OTB | Planned Sales + Markdowns + EOM Inv - BOM Inv - On Order | Cost basis only |
| Reorder Point | (Avg Daily Usage × Lead Time) + Safety Stock | Always include safety stock |
| Breakeven Qty | Fixed Costs / (Price - Variable Cost) | Zero-profit point |
| PED | %ΔQ / %ΔP | > 1 = elastic |

---

**Sources**:
- [Cotton Incorporated Retail Math Guide](https://cottonworks.com/wp-content/uploads/2024/10/CottonInc_RetailMath_FullBooklet.pdf)
- [Shopify Open-to-Buy Guide](https://www.shopify.com/blog/open-to-buy-plans)
- [Fatskills Merchandise Planning](https://www.fatskills.com/deca/chapter/deca-deca-merchandise-planning-assortment-inventory-opentobuy)
- [Fatskills Retail Pricing](https://www.fatskills.com/deca/chapter/deca-deca-retail-pricing-and-promotion)
- [Retail Northstar OTB](https://retailnorthstar.ai/resources/formulas/open-to-buy)
- [Enhanced Retail Solutions Cheat Sheet](https://enhancedretailsolutions.com/wp-content/uploads/2023/12/ERS-RETAIL-MATH-CHEAT-SHEET.pdf)
