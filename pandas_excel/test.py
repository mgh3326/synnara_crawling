import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('ohoh2.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, '제품 이미지')
worksheet.write(0, 1, '상세페이지 이미지')
worksheet.write(0, 2, '제목')
worksheet.write(0, 3, '원래 가격')
worksheet.write(0, 4, '할인 가격')
worksheet.write(0, 5, '품절')
worksheet.write(0, 6, '출연자')
worksheet.write(0, 7, '감독')
worksheet.write(0, 8, '화면비율')
worksheet.write(0, 9, '음향')
worksheet.write(0, 10, '더빙')
worksheet.write(0, 11, '자막')
worksheet.write(0, 12, '제작배급')
worksheet.write(0, 13, '지역코드')
worksheet.write(0, 14, '등급')
worksheet.write(0, 15, '런닝타임')
worksheet.write(0, 16, '미디어')
worksheet.write(0, 17, '상세정보')

workbook.close()
