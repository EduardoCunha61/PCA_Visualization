import xlrd
import xlwt

book = xlrd.open_workbook("CHMmetabolites_filtered.xls", formatting_info=True)
sheets = book.sheet_names()
counter = 0
data = []
copyrow = []

workbook = xlwt.Workbook()
res_sheet = workbook.add_sheet('results')


#print("sheets are:", sheets)
for index, sh in enumerate(sheets):
    sheet = book.sheet_by_index(index)
    #print("Sheet:", sheet.name)
    rows, cols = sheet.nrows, sheet.ncols
    print("Number of rows: %s   Number of cols: %s" % (rows, cols))
    for row in range(7,15):
        for col in range(1,cols):
            #print("row, col is:", row+1, col+1)
            thecell = sheet.cell(row, col)
            xfx = sheet.cell_xf_index(row, col)
            xf = book.xf_list[xfx]
            bgx = xf.background.pattern_colour_index
            #print(bgx)

            if((col == 4 or col == 11) and bgx!=64):
                if copyrow == []:
                    copyrow = sheet.row(row)
                    data.append(copyrow)

        copyrow=[]

for i, l in enumerate(data):
    print(type(i))
    print(type(l))
    for j, col in enumerate(l):
        print(type(j))
        print(type(col))
        res_sheet.write(i, j, str(col))

workbook.save('output.xls')