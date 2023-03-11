from pyecharts import options as opts
from pyecharts.charts import Geo, Page
from pyecharts.charts import Map
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
import pandas as pd
# from pyecharts.globals import ChartType, SymbolType

class DrawChina:
    def __init__(self, year=None, column=None) -> None:
        self.ENGLISH_PROVINCE_NAMES = {
        "广东省": "guangdong",
        "安徽": "anhui",
        "福建": "fujian",
        "甘肃": "gansu",
        "广西": "guangxi",
        "贵州": "guizhou",
        "海南": "hainan",
        "河北": "hebei",
        "黑龙江": "heilongjiang",
        "河南": "henan",
        "湖北": "hubei",
        "湖南": "hunan",
        "江苏": "jiangsu",
        "江西": "jiangxi",
        "吉林": "jilin",
        "辽宁": "liaoning",
        "内蒙古": "neimenggu",
        "宁夏": "ningxia",
        "青海": "qinghai",
        "山东": "shandong",
        "山西": "shanxi",
        "陕西": "shaanxi",
        "四川": "sichuan",
        "台湾": "taiwan",
        "新疆": "xinjiang",
        "西藏": "Tibet",
        "云南": "yunnan",
        "浙江": "zhejiang",
        "重庆": "ChongQing",
        "香港": "HongKong",
        "澳门": "Macao",
        "南海诸岛": "South China Sea Islands",
        "北京": "Beijing",
        "天津": "Tianjin",
        "上海": "Shanghai"
    }
        self.file = "demographic.dta"
        self.year = year if year is not None else 2005
        self.column = column if column is not None else "some_column"

    def draw(self, show_pvc: bool = False):
        ENGLISH_PROVINCE_NAMES_MAP = {
            "广东": "Guangdong",
            "安徽": "Anhui",
            "福建": "Fujian",
            "甘肃": "Gansu",
            "广西": "Guangxi",
            "贵州": "Guizhou",
            "海南": "Hainan",
            "河北": "Hebei",
            "黑龙江": "Heilongjiang",
            "河南": "Henan",
            "湖北": "Hubei",
            "湖南": "Hunan",
            "江苏": "Jiangsu",
            "江西": "Jiangxi",
            "吉林": "Jilin",
            "辽宁": "Liaoning",
            "内蒙古": "Neimenggu",
            "宁夏": "Ningxia",
            "青海": "Qinghai",
            "山东": "Shandong",
            "山西": "Shanxi",
            "陕西": "Shaanxi",
            "四川": "Sichuan",
            "台湾": "Taiwan",
            "新疆": "Xinjiang",
            "西藏": "Tibet",
            "云南": "Yunnan",
            "浙江": "Zhejiang",
            "重庆": "Chongqing",
            "香港": "Hong Kong",
            "澳门": "Macao",
            "南海诸岛": "South china sea islands",
            "北京": "Beijing",
            "天津": "Tianjin",
            "上海": "Shanghai"
        }
        # total = self.gen_df()
        data = [list(z) for z in zip(["Guangdong","Beijing","Shanghai","Jiangxi","Hunan","Zhejiang","Jiangsu"], [d/200 for d in Faker.values()])]
        print(data)
        with open("Src/china_wo_shandong.json", "r", encoding="utf-8") as file:
            stream = file.read()
        c = (
            Map(init_opts = opts.InitOpts(width='1000px',height='600px'))
                .add_js_funcs("echarts.registerMap('china_new',{});".format(stream))
                .add(self.column, data, "china_new", name_map= ENGLISH_PROVINCE_NAMES_MAP, is_map_symbol_show=False)
                .set_series_opts(label_opts=opts.LabelOpts(is_show=show_pvc))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="Provincial\t" + 'Some \nPercentage' + "\tin China" + "\t(%d)" % self.year), visualmap_opts=opts
                    .VisualMapOpts(max_=100, min_=0, range_color=['#e0ffff', '#006edd'], range_text=["100","0"]) 
            )
                .render("Res/"+ self.column + "%d" % self.year + ".html")
        )
        return c
    
DrawChina05 = DrawChina(year=2005)
DrawChina05.draw()
DrawChina17 = DrawChina(year=2017)
DrawChina17.draw()
