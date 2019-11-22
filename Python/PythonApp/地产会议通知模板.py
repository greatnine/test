class Agenda:
    agenda_list = []  # 多个单位会议议程的集合

    def __init__(self, project, unit, reporter, duration, status):
        self.project = project  # 项目名称
        self.unit = unit        # 汇报单位
        self.reporter = reporter    # 汇报人
        self.duration = duration    # 汇报时长
        self.status = status        # 项目进展
        self.agenda_list.append(self)

    def get_template(self, meeting):
        text = []
        text += [F"""{meeting["主题"]}议程"""]
        text += [F"""第 {meeting["次数"]} 次\n"""]
        text += [F"""时  间：{meeting["时间"]}"""]
        text += [F"""地  点：{meeting["地点"]}"""]
        text += [F"""主持人：{meeting["主持人"]}\n"""]
        text += ["""会议议题："""]
        i = 0
        for m in self.agenda_list:
            i += 1
            text += [F"{i}. 关于{m.project} 的汇报 汇报单位：{m.unit} 汇报人：{m.reporter} 汇报时长：{m.duration})分钟"]
            text += [F"  （议题概况：{m.status}的近期进展及下一阶段工作汇报。）\n"]
        return "\n".join(t for t in text)


def 打印会议通知(meeting, agenda_list):
    for a in agenda_list:
                agenda = Agenda(*a)
    print(agenda.get_template(meeting))


if __name__ == '__main__':
    meeting1 = dict(
        次数=8,  # 会议次数
        时间="2009年11月25日（星期一）上午 9:00",
        地点="大厦七层会议室",
        主题="集团地产板块整合工作小组会",
        主持人="执行董事长")
    agenda_list1 = [["成渝事业部各项目", "成渝事业群", "戚先生", "15", "成渝事业群各项目"],
                    ["城市公司北海公司", "北海公司", "王先生", "10", "北海项目一、二期"],
                    ["城市公司上海公司各项目", "上海公司", "吴先生", "10", "太仓项目、宣桥项目、武汉项目"],
                    ["投资公司南阳项目", "国安投资", "张先生", "10", "南阳项目"],
                    ["城市公司海南公司项目", "海南公司", "吴先生", "10", "海南公司万宁项目"],
                    ["城市公司北京公司各项目", "北京公司", "王先生", "20", "国安府、棉花片、东坝、金盏、东华金座项目"],
                    ["城市公司一城控股各项目", "一城控股", "武先生", "10", "一城项目、北运河PPP项目"]]
    打印会议通知(meeting1, agenda_list1)




