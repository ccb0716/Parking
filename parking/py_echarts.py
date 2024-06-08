from pyecharts import options as opts
from pyecharts.charts import Line, Pie, WordCloud, Map, Timeline, Liquid
from collections import Counter

from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

import parking.service as service


def line_bar():
    x_data = []
    y_data = []
    result = service.query(
        "select in_time,fee from car where  state=%s ", 1)
    data = list(result)
    date_dict = {}
    # 遍历数据并计算相同日期的费用总和
    for date, fee in data:
        # 将日期的时间部分设置为0，只保留日期部分
        date = date.strftime("%Y-%m")
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
    (
        Line(init_opts=opts.InitOpts(
            width='100%',
            height='550px',
            bg_color='transparent',
            theme="light"))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="收入",
            y_axis=y_data,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            linestyle_opts=opts.LineStyleOpts(),
            label_opts=opts.LabelOpts(is_show=False),
            is_smooth=False,
            is_symbol_show=False,
        )
        .set_global_opts(

            title_opts=opts.TitleOpts(
                title="       车场停车收入图",
                subtitle="数据来自陆军军事交通学院智慧停车场",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(color="white"),
                subtitle_textstyle_opts=opts.TextStyleOpts(color="white"), ),

            toolbox_opts=[opts.ToolboxOpts(),
                          opts.ToolBoxFeatureDataViewOpts(button_color="white", text_color="white")],
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_left="left", ),
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside", range_start=0, range_end=100, pos_top='50px', ),

            ],
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            yaxis_opts=opts.AxisOpts(name="销售额(元)",
                                     type_="value",
                                     min_=4800,
                                     # 设置 Y 轴的最小
                                     )
        )
        .set_series_opts(
            markarea_opts=opts.MarkAreaOpts(
                is_silent=False,
                data=[
                    opts.MarkAreaItem(
                        name="收入",
                        x=("2009-9-12-7:00", "2009-9-22-7:00"),
                        label_opts=opts.LabelOpts(is_show=False),
                        itemstyle_opts=opts.ItemStyleOpts(color="#DCA3A2", opacity=0.5),
                    ),
                ],
            ),
            axisline_opts=opts.AxisLineOpts(),

        )
        .render("./Visual/bar.html")
    )


def pie_web():
    result = service.query(
        "select wel from car where  state=%s ", 1)

    elements = list(result)
    # 使用 Counter 来统计每个元素的次数
    element_counts = Counter(elements)
    ls = list(element_counts.keys())

    ls0 = list(element_counts.values())
    lables = [ls[0][0], ls[1][0], ls[2][0], ls[3][0], ls[4][0], ls[5][0], ls[6][0]]

    (
        Pie(init_opts=opts.InitOpts(
            width='100%',
            height='550px',
            bg_color='transparent',
            theme="DARK"
        ))
        .add(
            "weekday",

            [list(z) for z in zip(lables, ls0)],

            radius=["30%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33, "color": "#999"},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },

            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="停车星期分布图",
                title_textstyle_opts=opts.TextStyleOpts(color="rgb(1, 182, 215)"),
                pos_left="center"
            ),
            legend_opts=opts.LegendOpts(
                # 是否显示图例组件
                is_show=True,
                orient="horizontal",
                textstyle_opts=opts.TextStyleOpts(color="white"),
                pos_top="bottom",
                pos_left="center",
            )
        )
        .render("./Visual/fee_web.html")
    )


def ciyun():
    result = service.query(
        "select id from car")
    groups = {}
    for tup in result:
        first_letter = tup[0][0]
        if first_letter in groups:
            groups[first_letter] += 1
        else:
            groups[first_letter] = 1
    province_mapping = {
        '赣': '江西省',
        '云': '云南省',
        '冀': '河北省',
        '豫': '河南省',
        '新': '新疆维吾尔自治区',
        '京': '北京市',
        '鄂': '湖北省',
        '川': '四川省',
        '甘': '甘肃省',
        '浙': '浙江省',
        '皖': '安徽省',
        '陕': '陕西省',
        '辽': '辽宁省',
        '藏': '西藏自治区',
        '粤': '广东省',
        '桂': '广西壮族自治区',
        '宁': '宁夏回族自治区',
        '津': '天津市',
        '鲁': '山东省',
        '蒙': '内蒙古自治区',
        '苏': '江苏省',
        '晋': '山西省',
        '贵': '贵州省',
        '湘': '湖南省',
        '琼': '海南省',
        '吉': '吉林省',
        '沪': '上海市',
        '渝': '重庆市',
        '黑': '黑龙江省',
        '青': '青海省',
        '闽': '福建省'
    }

    converted_counts = {}
    for first_letter, count in groups.items():
        province_name = province_mapping.get(first_letter)
        converted_counts[province_name] = count
    (
        WordCloud(init_opts=opts.InitOpts(width='100%', height='550px', bg_color='transparent',
                                          theme=ThemeType.DARK))
        .add("", [list(z) for z in zip(converted_counts.keys(), converted_counts.values())],
             word_size_range=[20, 100],
             shape='pentagon',
             )
        .set_global_opts(title_opts=opts.TitleOpts(title="省份词云"),
                         )
        .set_series_opts(
            background_color='rgba(255, 255, 255, 0)', )  # 设置背景透明

        .render("./Visual/ciyun.html")
    )


def map_0():
    result = service.query(
        "select id from car")
    groups = {}
    for tup in result:
        first_letter = tup[0][0]
        if first_letter in groups:
            groups[first_letter] += 1
        else:
            groups[first_letter] = 1
    province_mapping = {
        '赣': '江西省',
        '云': '云南省',
        '冀': '河北省',
        '豫': '河南省',
        '新': '新疆维吾尔自治区',
        '京': '北京市',
        '鄂': '湖北省',
        '川': '四川省',
        '甘': '甘肃省',
        '浙': '浙江省',
        '皖': '安徽省',
        '陕': '陕西省',
        '辽': '辽宁省',
        '藏': '西藏自治区',
        '粤': '广东省',
        '桂': '广西壮族自治区',
        '宁': '宁夏回族自治区',
        '津': '天津市',
        '鲁': '山东省',
        '蒙': '内蒙古自治区',
        '苏': '江苏省',
        '晋': '山西省',
        '贵': '贵州省',
        '湘': '湖南省',
        '琼': '海南省',
        '吉': '吉林省',
        '沪': '上海市',
        '渝': '重庆市',
        '黑': '黑龙江省',
        '青': '青海省',
        '闽': '福建省'
    }

    converted_counts = {}
    for first_letter, count in groups.items():
        province_name = province_mapping.get(first_letter)
        converted_counts[province_name] = count
    (
        Map(init_opts=opts.InitOpts(width='100%', height='550px', bg_color='transparent',
                                    theme=ThemeType.DARK))
        .add("车次", [list(z) for z in zip(converted_counts.keys(), converted_counts.values())],
             "china",
             label_opts=opts.LabelOpts(is_show=True),
             layout_size=300,
             zoom=1.5,
             pos_top="25%", )

        .set_global_opts(
            title_opts=opts.TitleOpts(title="接待车辆省份分布"),

            visualmap_opts=opts.VisualMapOpts(
                min_=50,
                max_=400,
                range_text=["High", "Low"],
                is_calculable=True,
                range_color=["lightskyblue", "royalblue", "blue"], )

        )

        .render("./Visual/jiedai.html")

    )


def shiduan1():
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

    sorted_stats_by_month = dict(sorted(stats_by_month.items(), key=lambda item: item[0], reverse=False))

    tl = Timeline(init_opts=opts.InitOpts(width='100%', bg_color='transparent'))
    for i in sorted_stats_by_month.keys():
        pie = (
            Pie(init_opts=opts.InitOpts(width='100%', bg_color='transparent'))
            .add(
                "停车时段",
                [list(z) for z in zip(sorted_stats_by_month[i].keys(), sorted_stats_by_month[i].values())],
                rosetype="radius",
                radius=["30%", "55%"],
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="停车场{}年时段分布".format(i),
                    title_textstyle_opts=opts.TextStyleOpts(color="rgb(1, 182, 215)"), ),
                legend_opts=opts.LegendOpts(
                    # 是否显示图例组件
                    is_show=True,
                    orient="horizontal",
                    textstyle_opts=opts.TextStyleOpts(color="white"),
                )
            )
        )

        tl.add(pie, "{}".format(i))

    tl.add_schema(is_auto_play=True, is_loop_play=True)

    tl.render("./Visual/shiduan.html")


def car_use():
    result_0 = service.query("select state from car where state=%s", 0)
    total = 200
    b = total - len(result_0)
    (
        Liquid(init_opts=opts.InitOpts(
            width='100%',
            bg_color='transparent'))
        .add(
            "空余车位",
            [b / total],
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
                ),
                position="inside",
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(
            title="车位空余率",
            title_textstyle_opts=opts.TextStyleOpts(color="rgb(1, 182, 215)"),
            pos_top="bottom",
            pos_left="center"))
        .render("./Visual/liquid.html")
    )
