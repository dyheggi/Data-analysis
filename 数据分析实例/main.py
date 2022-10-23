"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，完成数据封装
2.设计一个抽象类，定义文件相关功能，并使用了类实现具体功能
3.读取文件和生产数据对象
4.进行数据需求逻辑运算
5.通过PYEcharts进行图像绘制
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("D:/XXX.txt")
json_file_reader = JsonFileReader("D:/xxx.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将两个月份数据合并为一个list
all_data: list[Record] = jan_data + feb_data

# 数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期有记录，数据累加即可
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额销售图.html")