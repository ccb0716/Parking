from collections import Counter

from pyecharts import options as opts
from pyecharts.charts import PictorialBar, Timeline, Grid, Line
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType
import parking.service as service
result = service.query(
        "select in_time ,Time_period from car where state=%s ", 1)
data = list(result)
stats_by_month = {}
    # 遍历数据
for timestamp, period in data:
        # 将 datetime 对象转换为字符串格式
    key = timestamp.strftime('%Y')
        # 更新月统计数据
    if key in stats_by_month:
        if period in stats_by_month[key]:
            stats_by_month[key][period] += 1
        else:
            stats_by_month[key][period] = 1
    else:
        stats_by_month[key] = {period: 1}

sort_order = ['晚上', '早上', '上午', '下午', '中午']
# 对字典进行排序
sorted_stats_by_month = dict(sorted(stats_by_month.items(), key=lambda item: item[0]))
# 定义一个函数，用于根据排序规则对每个年份的字典进行排序
def sort_month_stats(stats):
    return dict(sorted(stats.items(), key=lambda item: sort_order.index(item[0])))
# 对每个年份的字典进行排序
sorted_stats_by_year = {year: sort_month_stats(stats) for year, stats in sorted_stats_by_month.items()}
tl = Timeline(init_opts=opts.InitOpts(width='100%', bg_color='transparent'))
for i in sorted_stats_by_year.keys():
    values=list(sorted_stats_by_year[i].values())
    location = list(sorted_stats_by_year[i].keys())
    c = (
        PictorialBar()
        .add_xaxis(location)
        .add_yaxis(
            "",
            values,
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=18,
            symbol_repeat="fixed",
            symbol_offset=[0, 0],
            is_symbol_clip=True,
            symbol=SymbolType.ROUND_RECT,
        )
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts(title="PictorialBar-各省份人口数量（虚假数据）"),
            xaxis_opts=opts.AxisOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
            ),
        )

    )
    tl.add(c, "{}".format(i))
tl.add_schema(is_auto_play=True, is_loop_play=True)
line = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grid-Line", pos_top="48%"),
        legend_opts=opts.LegendOpts(pos_top="48%"),
    )
)
grid = (
    Grid()
    .add(line, grid_opts=opts.GridOpts(pos_bottom="60%"))
    .add(c, grid_opts=opts.GridOpts(pos_top="60%"))
    .render("grid_vertical.html")
)



