import xlrd
from DBUtils import update

# wd = xlrd.open_workbook(filename=r"D:\ruanjiandakai\day9\2020年每个月的销售情况.xlsx", encoding_override=True)
# st = wd.sheet_by_name("1月")
# rows = st.nrows
# cols = st.ncols
# print("有", rows, "行，有", cols, "列")

# for i in range(rows):
#     print(st.row_values(i))
# print(st.row_values(0, 1))

# 全年销售总量
# sum = 0
# a =0
# for j in range(0,12):
#     st = wd.sheet_by_index(j)
#     rows = st.nrows
#     for n in range(1, rows):
#         a = st.row_values(n)[2]*st.row_values(n)[4]
#         sum = sum + a
# print("全年的销售总额为：", round(sum, 2), )


# 每件衣服销售占比
# list=['羽绒服','牛仔裤','铅笔裤','皮草','衬衫','卫衣','T血','风衣','马甲','小西装','休闲裤','棉衣','皮衣']
# for k in range(len(list)):
#     sum = 0
#     a = 0
#     for m in range(0,12):
#         st = wd.sheet_by_index(m)
#         rows = st.nrows
#         cols = st.ncols
#         for b in range(1, rows):
#             sum = sum + st.row_values(b)[4]
#             if st.row_values(b)[1] == list[k]:
#                 a = a + st.row_values(b)[4]
#     print(list[k],'的销售占比为：','{:.2%}'.format(a/sum))


# 每件衣服的月销售占比
# list=['羽绒服','牛仔裤','铅笔裤','皮草','衬衫','卫衣','T血','风衣','马甲','小西装','休闲裤','棉衣','皮衣']
# for a in range(0, 12):
#     st = wd.sheet_by_index(a)
#     rows = st.nrows
#     cols = st.ncols
#     for c in range(len(list)):
#         sum = 0
#         d = 0
#         for e in range(1, rows):
#             sum = sum + st.row_values(e)[4]
#             if st.row_values(e)[1] == list[c]:
#                 d = d + st.row_values(e)[4]
#         print(list[c],a+1,'月的销售占比为：','{:.2%}'.format(d/sum))

# 每件衣服销售额占比
# list=['羽绒服','牛仔裤','铅笔裤','皮草','衬衫','卫衣','T血','风衣','马甲','小西装','休闲裤','棉衣','皮衣']
# for k in range(len(list)):
#     sum = 0
#     d = 0
#     for i in range(0,12):
#         st = wd.sheet_by_index(i)
#         rows = st.nrows
#         cols = st.ncols
#         for j in range(1,rows):
#             sum = sum + st.row_values(j)[2]*st.row_values(j)[4]
#             if st.row_values(j)[1] == list[k]:
#                 d = d+st.row_values(j)[2]*st.row_values(j)[4]
#     print(list[k],'的销售额占比为：','{:.2%}'.format(d/sum))

#最畅销的衣服
# list=['羽绒服','牛仔裤','铅笔裤','皮草','衬衫','卫衣','T血','风衣','马甲','小西装','休闲裤','棉衣','皮衣']
# sum = 0
# a = 0
# for i in range(len(list)):
#     d = 0
#     sum1 = 0
#     for k in range(0,12):
#         st = wd.sheet_by_index(k)
#         rows = st.nrows
#         cols = st.ncols
#         for j in range(1,rows):
#             sum1 = sum1 + st.row_values(j)[4]
#             if st.row_values(j)[1] == list[i]:
#                 d = d + st.row_values(j)[4]
#     if d > sum:
#         sum = d
#         a = i
# print('最畅销的衣服是',list[a],'{:.2%}'.format(sum/sum1))

# 销量最低的衣服
# list=['羽绒服','牛仔裤','铅笔裤','皮草','衬衫','卫衣','T血','风衣','马甲','小西装','休闲裤','棉衣','皮衣']
# sum = 0
# a = 0
# for i in range(len(list)):
#     d = 0
#     for k in range(0,12):
#         st = wd.sheet_by_index(k)
#         rows = st.nrows
#         cols = st.ncols
#         for j in range(1,rows):
#             if st.row_values(j)[1] == list[i]:
#                 d = d + st.row_values(j)[4]
#     if sum == 0:
#         sum = d
#     if d < sum:
#         sum = d
#         a = i
# print('销量最低的衣服是',list[a],sum)

# 每个季度最畅销的衣服
# list=['羽绒服','牛仔裤','铅笔裤','皮草','衬衫','卫衣','T血','风衣','马甲','小西装','休闲裤','棉衣','皮衣']
# a = 0
# b = 0
# c = 0
# d = 0
# sum = 0
# sum1 = 0
# sum2 = 0
# sum3 = 0
# for k in range(len(list)):
#     data = 0
#     data1 = 0
#     data2 = 0
#     data3 = 0
#     for i in range(12):
#         st=wd.sheet_by_index(i)
#         rows = st.nrows
#         cols = st.ncols
#         if i >= 3 and i <= 5:
#             for j in range(1,rows):
#                 sum += st.row_values(j)[4]
#                 if st.row_values(j)[1] == list[k]:
#                     data = data + st.row_values(j)[4]
#             if data > sum:
#                 sum = data
#                 a = k
#         elif i>=6 and i<=8:
#             for p in range(1,rows):
#                 if st.row_values(p)[1] == list[k]:
#                     data1 = data1 + st.row_values(p)[4]
#             if data1 > sum1:
#                 sum1 = data1
#                 b = k
#         elif i>=9 and i<=11:
#             for m in range(1,rows):
#                 if st.row_values(m)[1] == list[k]:
#                     data2 = data2 + st.row_values(m)[4]
#             if data2 > sum2:
#                 sum2 = data2
#                 c = k
#         else:
#             for n in range(1,rows):
#                 if st.row_values(n)[1] == list[k]:
#                     data3 = data3 + st.row_values(n)[4]
#             if data3 > sum3:
#                 sum3 = data3
#                 d = k
# print('第一个季度最畅销的衣服：',list[a])
# print('第二个季度最畅销的衣服：',list[b])
# print('第三个季度最畅销的衣服：',list[c])
# print('第四个季度最畅销的衣服：',list[d])


#将表中数据添加到数据库
# wd = xlrd.open_workbook(filename=r"D:\ruanjiandakai\day9\2020年每个月的销售情况.xlsx",encoding_override=True)
# for i in range(12):
#     st = wd.sheet_by_index(i)
#     rows = st.nrows
#     for j in range(1, rows):
#         sql = "insert into market%s values(%s,%s,%s,%s,%s)"
#         param = [i+1, st.row_values(j)[0],st.row_values(j)[1],st.row_values(j)[2],st.row_values(j)[3],st.row_values(j)[4]]
#         update(sql, param)


