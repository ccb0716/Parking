import datetime

from pyecharts import options as opts
from pyecharts.charts import Bar
import parking.service as service
# 准备数据
x_data=[]
y_data=[]
result = service.query(
        "select in_time,fee from car where  state=%s ", 1)
data = list(result)
    # 创建一个字典来分组日期和费用
date_dict = {}
    # 遍历数据并计算相同日期的费用总和
for date, fee in data:
        # 将日期的时间部分设置为0，只保留日期部分
    date=date.strftime("%Y-%m-%d")

    print(date)
        # 如果日期已经在字典中，就将费用累加
    if date in date_dict:
        date_dict[date] += fee

        # 否则，将日期添加到字典并初始化费用
    else:
         date_dict[date] = fee
    # 打印每个日期对应费用总和
for date, total_fee in date_dict.items():
    x_data.append(date)
    y_data.append(total_fee)
# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 配置全局属性
bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="月度销售额柱状图", subtitle="副标题"),
    xaxis_opts=opts.AxisOpts(name="月份"),
    yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
    legend_opts=opts.LegendOpts(pos_left="center", pos_top="top"),
    toolbox_opts=opts.ToolboxOpts(),
    tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
)
#for a in x_data:

    #print(a)
# 渲染图表
bar_chart.render("../Visual/global_options_bar_chart.html")