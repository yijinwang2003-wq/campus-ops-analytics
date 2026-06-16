"""Generate high-fidelity static Power BI-style dashboard mockups.

The mockups are intentionally generated from data/powerbi CSV outputs so the
KPI values and chart shapes align with the current synthetic dataset.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from PIL import Image, ImageDraw, ImageFont


PROJECT_ROOT = Path(__file__).resolve().parents[1]
POWERBI_DIR = PROJECT_ROOT / "data" / "powerbi"
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"

W, H = 1600, 900
NAVY = "#0B1F3A"
NAVY_2 = "#12365C"
SLATE = "#334155"
MUTED = "#64748B"
GRID = "#E2E8F0"
BG = "#F5F7FA"
PANEL = "#FFFFFF"
TEAL = "#168C8C"
TEAL_2 = "#A7F3D0"
GOLD = "#D6A419"
RED = "#C2410C"
GREEN = "#15803D"
PURPLE = "#6D5BD0"
BLUE = "#2563EB"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F_TITLE = font(30, True)
F_SUBTITLE = font(14)
F_SECTION = font(17, True)
F_LABEL = font(12, True)
F_SMALL = font(11)
F_VALUE = font(28, True)
F_AXIS = font(10)


def money(value: float) -> str:
    if abs(value) >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    if abs(value) >= 1_000:
        return f"${value / 1_000:.0f}K"
    return f"${value:,.0f}"


def pct(value: float) -> str:
    return f"{value:.2f}%"


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str = GRID, radius: int = 12, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def truncate(text: str, max_chars: int) -> str:
    return text if len(text) <= max_chars else text[: max_chars - 1] + "..."


def header(draw: ImageDraw.ImageDraw, title: str, subtitle: str) -> None:
    draw.rectangle((0, 0, W, 74), fill=NAVY)
    draw.text((32, 18), title, font=F_TITLE, fill="white")
    draw.text((34, 52), subtitle, font=F_SUBTITLE, fill="#D7E3F4")
    for i, label in enumerate(["Fiscal Year: 2025", "Division: All", "Department: All"]):
        x = 1010 + i * 185
        rounded(draw, (x, 18, x + 170, 56), fill="#102B4A", outline="#355D85", radius=8)
        draw.text((x + 14, 31), label, font=F_SMALL, fill="#EAF2FF")


def kpi_card(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], label: str, value: str, accent: str = TEAL, note: str | None = None) -> None:
    rounded(draw, box, fill=PANEL, outline="#D7DEE8", radius=12)
    x1, y1, x2, y2 = box
    draw.rectangle((x1, y1, x1 + 8, y2), fill=accent)
    draw.text((x1 + 20, y1 + 14), label.upper(), font=F_LABEL, fill=MUTED)
    draw.text((x1 + 20, y1 + 38), value, font=F_VALUE, fill=NAVY)
    if note:
        draw.text((x1 + 20, y2 - 24), note, font=F_SMALL, fill=MUTED)


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str) -> tuple[int, int, int, int]:
    rounded(draw, box, fill=PANEL, outline="#D7DEE8", radius=12)
    x1, y1, x2, y2 = box
    draw.text((x1 + 18, y1 + 14), title, font=F_SECTION, fill=NAVY)
    draw.line((x1 + 18, y1 + 44, x2 - 18, y1 + 44), fill=GRID, width=1)
    return x1 + 22, y1 + 58, x2 - 22, y2 - 22


def hbar(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    labels: list[str],
    values: list[float],
    colors: list[str] | None = None,
    suffix: str = "",
    formatter=None,
    display_values: list[float] | None = None,
) -> None:
    x1, y1, x2, y2 = box
    maxv = max(values) if values else 1
    row_h = max(18, (y2 - y1) // max(len(labels), 1))
    for i, (label, value) in enumerate(zip(labels, values)):
        y = y1 + i * row_h + 2
        draw.text((x1, y + 3), truncate(label, 24), font=F_AXIS, fill=SLATE)
        bar_x = x1 + 165
        bar_w = int((x2 - bar_x - 55) * (value / maxv))
        color = colors[i] if colors else TEAL
        draw.rounded_rectangle((bar_x, y + 3, bar_x + bar_w, y + row_h - 5), radius=5, fill=color)
        display_value = display_values[i] if display_values is not None else value
        value_text = formatter(display_value) if formatter else f"{display_value:.1f}{suffix}"
        draw.text((bar_x + bar_w + 8, y + 2), value_text, font=F_AXIS, fill=SLATE)


def grouped_columns(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], labels: list[str], series: list[tuple[str, list[float], str]], value_fmt=money) -> None:
    x1, y1, x2, y2 = box
    chart_h = y2 - y1 - 38
    maxv = max(max(vals) for _, vals, _ in series)
    n = len(labels)
    gap = 18
    group_w = max(48, (x2 - x1 - gap * (n - 1)) // max(n, 1))
    bar_w = max(8, group_w // (len(series) + 1))
    draw.line((x1, y1 + chart_h, x2, y1 + chart_h), fill=GRID, width=1)
    for i, label in enumerate(labels):
        gx = x1 + i * (group_w + gap)
        for j, (_, vals, color) in enumerate(series):
            h = int(chart_h * vals[i] / maxv)
            bx = gx + j * (bar_w + 3)
            draw.rectangle((bx, y1 + chart_h - h, bx + bar_w, y1 + chart_h), fill=color)
        draw.text((gx - 4, y1 + chart_h + 8), truncate(label, 10), font=F_AXIS, fill=SLATE)
    lx = x1
    for name, _, color in series:
        draw.rectangle((lx, y2 - 14, lx + 10, y2 - 4), fill=color)
        draw.text((lx + 16, y2 - 17), name, font=F_SMALL, fill=SLATE)
        lx += 115


def line_chart(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], labels: list[str], values: list[float], color: str = BLUE) -> None:
    x1, y1, x2, y2 = box
    if not values:
        return
    maxv, minv = max(values), min(values)
    if maxv == minv:
        maxv += 1
    pad = 10
    pts = []
    for i, val in enumerate(values):
        x = x1 + pad + int((x2 - x1 - 2 * pad) * i / max(len(values) - 1, 1))
        y = y2 - pad - int((y2 - y1 - 2 * pad) * (val - minv) / (maxv - minv))
        pts.append((x, y))
    for g in range(4):
        gy = y1 + int((y2 - y1) * g / 3)
        draw.line((x1, gy, x2, gy), fill="#EEF2F7", width=1)
    draw.line(pts, fill=color, width=3)
    for x, y in pts:
        draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=color)
    if labels:
        draw.text((x1, y2 + 4), labels[0], font=F_AXIS, fill=MUTED)
        draw.text((x2 - 45, y2 + 4), labels[-1], font=F_AXIS, fill=MUTED)


def stacked_columns(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], labels: list[str], stacks: dict[str, list[int]], colors: dict[str, str]) -> None:
    x1, y1, x2, y2 = box
    totals = [sum(stacks[name][i] for name in stacks) for i in range(len(labels))]
    maxv = max(totals) if totals else 1
    chart_h = y2 - y1 - 32
    col_w = max(34, (x2 - x1) // max(len(labels) * 2, 1))
    for i, label in enumerate(labels):
        x = x1 + 32 + i * ((x2 - x1 - 60) // max(len(labels), 1))
        base = y1 + chart_h
        for name, vals in stacks.items():
            h = int(chart_h * vals[i] / maxv)
            draw.rectangle((x, base - h, x + col_w, base), fill=colors[name])
            base -= h
        draw.text((x - 8, y1 + chart_h + 8), truncate(label, 9), font=F_AXIS, fill=SLATE)
    lx = x1
    for name, color in colors.items():
        draw.rectangle((lx, y2 - 14, lx + 10, y2 - 4), fill=color)
        draw.text((lx + 15, y2 - 17), name, font=F_SMALL, fill=SLATE)
        lx += 92


def table(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], headers: list[str], rows: list[list[str]], col_widths: list[int] | None = None) -> None:
    x1, y1, x2, y2 = box
    col_widths = col_widths or [int((x2 - x1) / len(headers))] * len(headers)
    y = y1
    draw.rectangle((x1, y, x2, y + 26), fill="#EAF2FF")
    x = x1
    for header_text, width in zip(headers, col_widths):
        draw.text((x + 6, y + 7), header_text, font=F_SMALL, fill=NAVY)
        x += width
    y += 30
    for r, row in enumerate(rows):
        if y > y2 - 24:
            break
        fill = "#FFFFFF" if r % 2 == 0 else "#F8FAFC"
        draw.rectangle((x1, y - 2, x2, y + 24), fill=fill)
        x = x1
        for cell, width in zip(row, col_widths):
            color = RED if "-" in cell or "107" in cell or "Critical" in cell else SLATE
            draw.text((x + 6, y + 5), truncate(cell, max(8, width // 8)), font=F_SMALL, fill=color)
            x += width
        y += 27


def load() -> dict[str, pd.DataFrame]:
    return {
        "budget": pd.read_csv(POWERBI_DIR / "budget_summary.csv"),
        "budget_monthly": pd.read_csv(POWERBI_DIR / "budget_monthly_dashboard.csv"),
        "procurement": pd.read_csv(POWERBI_DIR / "procurement_dashboard.csv"),
        "maintenance": pd.read_csv(POWERBI_DIR / "maintenance_dashboard.csv"),
        "hr": pd.read_csv(POWERBI_DIR / "hr_workforce_dashboard.csv"),
    }


def executive(data: dict[str, pd.DataFrame]) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    header(draw, "Executive Overview", "University Finance & Business Information Services | FY2025 enterprise performance")
    b = data["budget"]
    bf = b[b.fiscal_year == 2025].copy()
    p = data["procurement"]
    m = data["maintenance"]
    h = data["hr"]
    latest = h[h.month_start_date == h.month_start_date.max()]

    total_budget = bf.total_budget.sum()
    actual = bf.total_actual_spend.sum()
    util = actual / total_budget * 100
    over = int((bf.is_over_budget == True).sum())
    avg_approve = p.days_to_approve.mean()
    critical = int((m.is_critical_over_48h == True).sum())

    cards = [
        ("FY2025 Budget", money(total_budget), TEAL, "Approved operating budget"),
        ("Actual Spend", money(actual), BLUE, "Recognized FY2025 spend"),
        ("Utilization", pct(util), GOLD, "University-wide actual / budget"),
        ("Over Budget", f"{over} Dept", RED, "Requires finance action"),
        ("Avg Approval", f"{avg_approve:.2f} Days", PURPLE, "Procurement cycle time"),
        ("Critical 48h", f"{critical}", RED, "Unresolved facilities risk"),
    ]
    for i, c in enumerate(cards):
        kpi_card(draw, (30 + i * 258, 96, 270 + i * 258, 188), *c)

    area = panel(draw, (30, 215, 760, 515), "Budget Utilization by Department")
    bsort = bf.sort_values("budget_utilization_pct", ascending=False)
    colors = [RED if v > 100 else GOLD if v >= 95 else TEAL for v in bsort.budget_utilization_pct]
    hbar(draw, area, bsort.department_name.tolist(), bsort.budget_utilization_pct.tolist(), colors, "%")

    area = panel(draw, (790, 215, 1570, 515), "Enterprise Exception Matrix")
    delayed = p[p.is_approval_delayed == True].groupby("department_name").size()
    crit = m[m.is_critical_over_48h == True].groupby("department_name").size()
    vac = latest.set_index("department_name").vacancies
    rows = []
    for _, row in bsort.iterrows():
        dept = row.department_name
        rows.append([dept, pct(row.budget_utilization_pct), money(row.budget_variance), str(int(delayed.get(dept, 0))), str(int(crit.get(dept, 0))), str(int(vac.get(dept, 0)))])
    table(draw, area, ["Department", "Util", "Variance", "Delayed", "Crit", "Vac"], rows, [210, 75, 105, 80, 55, 55])

    area = panel(draw, (30, 545, 760, 850), "Procurement Approval Trend")
    trend = p.groupby("approval_month").days_to_approve.mean().reset_index().sort_values("approval_month")
    line_chart(draw, (area[0], area[1], area[2], area[3] - 14), trend.approval_month.tolist(), trend.days_to_approve.tolist(), PURPLE)
    draw.text((area[0], area[3] - 6), "Average days to approve by month", font=F_SMALL, fill=MUTED)

    area = panel(draw, (790, 545, 1175, 850), "Facilities Backlog by Priority")
    ct = pd.crosstab(m.priority, m.status).reindex(["Critical", "High", "Medium", "Low"]).fillna(0).astype(int)
    stacked_columns(draw, area, ct.index.tolist(), {col: ct[col].tolist() for col in ct.columns}, {"Completed": TEAL, "Open": RED})

    area = panel(draw, (1195, 545, 1570, 850), "Workforce by Department")
    lsort = latest.sort_values("total_headcount", ascending=False)
    hbar(draw, area, lsort.department_name.tolist(), lsort.total_headcount.tolist(), [BLUE] * len(lsort), "")
    return img


def budget_page(data: dict[str, pd.DataFrame]) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    header(draw, "Budget Analytics", "Budget-to-actual performance, variance management, and category spend analysis")
    bf = data["budget"][data["budget"].fiscal_year == 2025].copy()
    bm = data["budget_monthly"][data["budget_monthly"].fiscal_year == 2025]
    kpi_card(draw, (30, 96, 300, 188), "Total Budget", money(bf.total_budget.sum()), TEAL)
    kpi_card(draw, (320, 96, 590, 188), "Actual Spend", money(bf.total_actual_spend.sum()), BLUE)
    kpi_card(draw, (610, 96, 880, 188), "Budget Variance", money(bf.budget_variance.sum()), GREEN)
    kpi_card(draw, (900, 96, 1170, 188), "Over Budget", f"{int((bf.is_over_budget == True).sum())} Dept", RED)
    kpi_card(draw, (1190, 96, 1570, 188), "Watchlist", f"{int((bf.budget_utilization_pct >= 95).sum())} Departments >=95%", GOLD)

    labels = bf.department_name.tolist()
    area = panel(draw, (30, 215, 790, 520), "Budget vs Actual by Department")
    grouped_columns(draw, area, [truncate(x, 12) for x in labels], [("Budget", bf.total_budget.tolist(), "#9CC9E8"), ("Actual", bf.total_actual_spend.tolist(), TEAL)])

    area = panel(draw, (820, 215, 1570, 520), "Budget Variance by Department")
    varsort = bf.sort_values("budget_variance")
    colors = [RED if v < 0 else GREEN for v in varsort.budget_variance]
    hbar(draw, area, varsort.department_name.tolist(), [abs(v) for v in varsort.budget_variance], colors, formatter=money, display_values=varsort.budget_variance.tolist())
    draw.text((area[2] - 160, area[1] - 2), "Red = unfavorable variance", font=F_SMALL, fill=RED)

    area = panel(draw, (30, 550, 790, 850), "Monthly Utilization Trend")
    monthly = bm.groupby("fiscal_period").agg(actual=("actual_spend", "sum"), budget=("monthly_budget", "sum")).reset_index()
    monthly["util"] = monthly.actual / monthly.budget * 100
    line_chart(draw, (area[0], area[1], area[2], area[3] - 14), monthly.fiscal_period.astype(str).tolist(), monthly.util.tolist(), GOLD)

    area = panel(draw, (820, 550, 1570, 850), "Actual Spend by Budget Category")
    cats = bm.groupby("budget_category").actual_spend.sum().sort_values(ascending=False).head(10)
    hbar(draw, area, cats.index.tolist(), cats.values.tolist(), [TEAL, BLUE, PURPLE, GOLD, GREEN, "#60A5FA", "#14B8A6", "#A855F7", "#F97316", "#64748B"], formatter=money)
    return img


def procurement_page(data: dict[str, pd.DataFrame]) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    header(draw, "Procurement Operations", "Approval cycle-time monitoring, sourcing workload, and delayed request analysis")
    p = data["procurement"]
    kpi_card(draw, (30, 96, 275, 188), "Requests", f"{len(p):,}", BLUE)
    kpi_card(draw, (295, 96, 540, 188), "Approved Amount", money(p.approved_amount.sum()), TEAL)
    kpi_card(draw, (560, 96, 805, 188), "Avg Approval", f"{p.days_to_approve.mean():.2f} Days", PURPLE)
    kpi_card(draw, (825, 96, 1070, 188), "Delayed", f"{int((p.is_approval_delayed == True).sum())}", RED)
    it_avg = p[p.department_name == "Information Technology"].days_to_approve.mean()
    kpi_card(draw, (1090, 96, 1335, 188), "IT Avg Approval", f"{it_avg:.2f} Days", RED)
    kpi_card(draw, (1355, 96, 1570, 188), "Comp Bid", f"{int((p.is_competitive_bid == True).sum())}", GOLD)

    area = panel(draw, (30, 215, 790, 520), "Avg Approval Days by Department")
    avg = p.groupby("department_name").days_to_approve.mean().sort_values(ascending=False)
    colors = [RED if v > p.days_to_approve.mean() else TEAL for v in avg.values]
    hbar(draw, area, avg.index.tolist(), avg.values.tolist(), colors, "")

    area = panel(draw, (820, 215, 1570, 520), "Approval Cycle Trend")
    trend = p.groupby("approval_month").days_to_approve.mean().reset_index().sort_values("approval_month")
    line_chart(draw, (area[0], area[1], area[2], area[3] - 14), trend.approval_month.tolist(), trend.days_to_approve.tolist(), PURPLE)

    area = panel(draw, (30, 550, 790, 850), "Delayed Approval Count by Department")
    delayed = p[p.is_approval_delayed == True].groupby("department_name").request_number.count().sort_values(ascending=False)
    hbar(draw, area, delayed.index.tolist(), delayed.values.tolist(), [RED] * len(delayed), "")

    area = panel(draw, (820, 550, 1570, 850), "Requests by Category and Status")
    ct = pd.crosstab(p.procurement_category, p.request_status)
    ct = ct.loc[ct.sum(axis=1).sort_values(ascending=False).index]
    stacked_columns(draw, area, ct.index.tolist()[:6], {col: ct[col].tolist()[:6] for col in ct.columns}, {"Approved": GOLD, "Closed": TEAL})
    return img


def facilities_workforce_page(data: dict[str, pd.DataFrame]) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    header(draw, "Facilities & Workforce", "Critical work order backlog, service aging, staffing capacity, and vacancy context")
    m = data["maintenance"]
    h = data["hr"]
    latest = h[h.month_start_date == h.month_start_date.max()]
    kpi_card(draw, (30, 96, 275, 188), "Open Work Orders", f"{int((m.status != 'Completed').sum())}", RED)
    kpi_card(draw, (295, 96, 540, 188), "Critical 48h", f"{int((m.is_critical_over_48h == True).sum())}", RED)
    kpi_card(draw, (560, 96, 805, 188), "Avg Resolve", f"{m.days_to_resolve.mean():.2f} Days", GOLD)
    kpi_card(draw, (825, 96, 1070, 188), "Est Cost", money(m.estimated_cost.sum()), BLUE)
    kpi_card(draw, (1090, 96, 1335, 188), "Headcount", f"{int(latest.total_headcount.sum())}", TEAL)
    kpi_card(draw, (1355, 96, 1570, 188), "Vacancies", f"{int(latest.vacancies.sum())}", GOLD)

    area = panel(draw, (30, 215, 790, 520), "Work Orders by Priority and Status")
    ct = pd.crosstab(m.priority, m.status).reindex(["Critical", "High", "Medium", "Low"]).fillna(0).astype(int)
    stacked_columns(draw, area, ct.index.tolist(), {col: ct[col].tolist() for col in ct.columns}, {"Completed": TEAL, "Open": RED})

    area = panel(draw, (820, 215, 1570, 520), "Critical Overdue Work Order List")
    critical = m[m.is_critical_over_48h == True].sort_values("days_to_resolve", ascending=False)
    rows = [[r.work_order_number, r.building_name, r.request_type, r.assigned_team, f"{int(r.days_to_resolve)}", money(r.estimated_cost)] for _, r in critical.iterrows()]
    table(draw, area, ["WO", "Building", "Type", "Team", "Days", "Est Cost"], rows, [90, 180, 105, 120, 60, 90])

    area = panel(draw, (30, 550, 790, 850), "Avg Days to Resolve by Request Type")
    avg = m.groupby("request_type").days_to_resolve.mean().sort_values(ascending=False)
    hbar(draw, area, avg.index.tolist(), avg.values.tolist(), [GOLD if v > m.days_to_resolve.mean() else TEAL for v in avg.values], "")

    area = panel(draw, (820, 550, 1570, 850), "Headcount and Vacancies by Department")
    lsort = latest.sort_values("total_headcount", ascending=False)
    grouped_columns(draw, area, [truncate(x, 10) for x in lsort.department_name], [("Headcount", lsort.total_headcount.tolist(), BLUE), ("Vacancies", lsort.vacancies.tolist(), RED)], value_fmt=lambda v: str(v))
    return img


def main() -> None:
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    data = load()
    pages = {
        "executive_overview_mockup.png": executive(data),
        "budget_analytics_mockup.png": budget_page(data),
        "procurement_operations_mockup.png": procurement_page(data),
        "facilities_workforce_mockup.png": facilities_workforce_page(data),
    }
    for filename, image in pages.items():
        path = SCREENSHOT_DIR / filename
        image.save(path, "PNG", optimize=True)
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
