import datetime
import calendar
import os
import random
# captcha是用于生成验证码图片的库，可以 pip install captcha 来安装它
from captcha.image import ImageCaptcha

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




def random_captcha_text(num):
    # 验证码列表
    captcha_text = []
    for i in range(10):  # 0-9数字
        captcha_text.append(str(i))
    '''for i in range(65, 91):  # 对应从“A”到“Z”的ASCII码
        captcha_text.append(chr(i))
    for i in range(97, 123):  # 对应从“a”到“z”的ASCII码
        captcha_text.append(chr(i))'''

    # 从list中随机获取n个元素，作为一个片断返回
    example = random.sample(captcha_text, num)

    # 将列表里的片段变为字符串并返回
    verification_code = ''.join(example)
    return verification_code


# 生成字符对应的验证码
def generate_captcha_image():
    image = ImageCaptcha()
    # 获得随机生成的验证码
    captcha_text = random_captcha_text(4)
    # 把验证码列表转为字符串
    captcha_text = ''.join(captcha_text)
    # 生成验证码
    image.write(captcha_text, './Visual/yanzhengma.png')
    return captcha_text