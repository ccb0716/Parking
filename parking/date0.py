import datetime
import calendar

# 定义一个映射关系，将英文星期转换为中文星期
weekday_map = {
    calendar.SUNDAY: '星期日',
    calendar.MONDAY: '星期一',
    calendar.TUESDAY: '星期二',
    calendar.WEDNESDAY: '星期三',
    calendar.THURSDAY: '星期四',
    calendar.FRIDAY: '星期五',
    calendar.SATURDAY: '星期六'
}

def get_weekday(date_string):
    date_format = '%Y-%m-%d %H:%M:%S'
    date = datetime.datetime.strptime(date_string, date_format)
    weekday_index = date.weekday()
    weekday_chinese = weekday_map[weekday_index]
    return weekday_chinese

def get_timeperiod(date_string):
    date_format = '%Y-%m-%d %H:%M:%S'
    date = datetime.datetime.strptime(date_string, date_format)
    hour = int(date.strftime('%H'))
    if hour >= 6 and hour < 8:
        return "早上"
    elif hour >= 8 and hour < 12:
        return "上午"
    elif hour >= 12 and hour < 14:
        return "中午"
    elif hour >= 14 and hour < 18:
        return "下午"
    else:
        return "晚上"
