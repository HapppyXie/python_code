# Athour:Mr Xie
# 开发时间:2021/11/5 15:38
#2. 对字符串进行分词（自选一段文字），计算词语的出现次数（词频）
import jieba
x= "县政府工作报告提出要以共同富裕为方向，推动政策向民生集聚、" \
   "服务向民生覆盖、资源向民生倾斜，让品质生活可感知、可触及、可拥抱。" \
   "今天我们一起来看政府工作报告解读第四期：聚焦普惠提升，谱写社会事业新篇章。" \
   "织密民生保障网络。坚持创业带动就业，完善就业公共服务体系，多举措扩大就业增收渠道，" \
   "做好高校毕业生、农民工、退役军人等重点群体就业工作，新增城镇就业3300人、" \
   "农村劳动力转移就业3200人。加大农民工工资支付保障和根治欠薪力度，" \
   "保障劳动者合法权益。继续实施全民参保计划，稳步提高城乡医保、养老保险、低保、" \
   "大病救助和特困供养等保障水平，加强对农村“三留守人员”、残疾人、计生特困家庭等群体关爱服务。" \
   "积极应对人口老龄化，落实三孩生育政策及配套支持措施，加快中心敬老院提质和社会养老、公办抚育机构建设，" \
   "推动婴幼儿照护、养老产业协同发展，满足多层次需求"
x1 = jieba.lcut(x)
print(x1)
#民生,就业，保障，工作
d= dict()
for i in x1:
    d[i] = d.get(i,0)+1
for k,v in d.items():
    if k == '民生':
        print(k, ":", v)
    elif k == '就业':
        print(k, ":", v)
    elif k == '保障':
        print(k, ":", v)
    elif k == '工作':
        print(k, ":", v)

