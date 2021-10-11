import xlwt
import xlrd
from DBUtils import cexcel
from DBUtils import update

wb = xlwt.Workbook()

st = wb.add_sheet("t_employeees")

st.write(0, 0, "编号")
st.write(0, 1, "姓名")
st.write(0, 2, "职位")
st.write(0, 3, "上级编号")
st.write(0, 4, "入职时间")
st.write(0, 5, "工资")
st.write(0, 6, "奖金")
st.write(0, 7, "部门编号")
sql = "select * from t_employees"
param = []
date = cexcel(sql, param)
print(date)
for i in range(len(date)):
    for n in range(len(date[i])):
        st.write(i+1, n, date[i][n])

st = wb.add_sheet("t_dept")
st.write(0, 0, "部门编号")
st.write(0, 1, "部门名称")
st.write(0, 2, "部门地址")
sql1 = "select * from t_dept"
param1 = []
date1 = cexcel(sql1, param1)
print(date1)
for m in range(len(date1)):
    for k in range(len(date[m])):
        st.write(m+1, k, date[m][k])
wb.save("三国集团.xlsx")




wd = xlrd.open_workbook(filename=r"D:\ruanjiandakai\day9\三国集团.xlsx", encoding_override=True)
sheet = wd.sheet_by_name("用户管理")
rows = sheet.nrows

for j in range(1, rows):
    sj = sheet.row_values(j)
    update("insert into lx values (%s,%s,%s,%s,%s)", sj)



