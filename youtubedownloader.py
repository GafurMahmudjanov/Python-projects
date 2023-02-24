# from pytube import YouTube
#
# link = ('https://youtube.com/shorts/KFd53DULbQI?feature=share ')
# video = YouTube(link)
# quality = input('Choose the quality of the video (High/Low): ')
#
# if quality == 'High':
#       output = video.streams.get_highest_resolution()
#       output.download('images')
#       print('Downloaded successfully!')
# if quality == 'Low':
#       output = video.streams.get_lowest_resolution()
#       output.download('images')
#       print('Downloaded successfully!')


PyPDF2.PdfReader('Masterclass.pdf')

def put_watermark(input_file,watermaker,output_file):
   watermark_page = PyPDF2.PdfReader(watermaker).pages[0]

   pdf_reader = PyPDF2.PdfReader(input_file)

   pdf_writer = PyPDF2.PdfWriter()

   for pages in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[pages]
      page.merge_page(watermark_page)
      pdf_writer.add_page(page)
   with open(output_file, 'wb') as out:
      pdf_writer.write(out)


put_watermark('Masterclass.pdf', 'watermark.pdf', 'Udemy.pdf')
print('Done successfully!')

