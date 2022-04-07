import pandas as pd
import numpy as np

# Task 1:Sử dụng try/except để viết một chương trình cho phép người dùng nhập tên của một tệp
'''parameter: filename - tên của file text (ví dụ class1 cho file class1.txt
    return 1 Dataframe pandas có 3 cột là dữ liệu ban đầu (0), mã học sinh (student_code) và 
    array của tất cả đáp án của từng học sinh (array)'''
def open_filename(filename):
    try:
        #sử dụng lệnh read_csv để tạo 1 Dataframe chỉ có 1 cột dữ liệu duy nhất
        df =  pd.read_csv("{}.txt".format(filename), header=None, delim_whitespace=True)
        # từ Dataframe gốc tạo thêm 1 cột là mã học sinh và 1 cột là 1 array của tất cả các câu trả lời
        df['student_code'] = df[0].apply(lambda x: x[:x.find(',')])
        df['array'] = df[0].apply(lambda x: np.array((x[x.find(',') + 1:]).split(',')))
        print('Successfully opened {}.txt\n'.format(filename))
        return df
    except:
        print('File cannot be found.\n')
        quit()

# Task 2: phân tích dữ liệu đảm bảo rằng nó ở đúng định dạng

'''tạo 1 hàm để tách dataframe thành những dòng đúng cú pháp và những dòng sai cú pháp
    parameter: df - 1 pandas dataframe có các cột là mã học sinh là array của tất cả đáp án của từng học sinh (array)
    trả về dataframe của các dòng đúng cú pháp (df_right), và dataframe các dòng sai cú pháp(df_error)'''
def split_dataframe(df):
    ''' kiểm tra các dòng xem có bị mã học sinh bị sai hoặc không có chính xác 26 giá trị (25 câu trả lời)
    sau đó tạo 2 dataframe là những dòng đúng và những dòng bị sai'''
    df['student_code_error'] = df['student_code'].apply(lambda x: x[0]!='N' or len(x)!=9 or not x[1:].isdigit())
    df['26_values_error'] = df['array'].apply(lambda x: len(x) !=25)
    df['error'] = df['student_code_error'] | df['26_values_error']
    df_error = df[df.error == True].reset_index(drop=True)
    df_right = df[df.error == False].reset_index(drop=True)
    return df_right,df_error

''' tạo 1 hàm để báo cáo những dòng bị sai
    tham số df_error - là 1 pandas dataframe có các dòng bị sai cú pháp và lỗi sai
    kết quả in ra dòng bị lỗi và lỗi tương ứng '''
def analyzing_df_error(df_error):
    if len(df_error)==0:
        print('No errors found!')
    for i in range(len(df_error)):
        if df_error.loc[i,'student_code_error'] == True:
            print('Invalid line of data: N# is invalid')
            print(df_error.loc[i,0]+'\n')
        if df_error.loc[i,'26_values_error'] == True:
            print('Invalid line of data: does not contain exactly 26 values:')
            print(df_error.loc[i,0]+'\n')

# Task 3: chấm điểm các bài thi

''' viết hàm chấm điểm và trả về là 1 dataframe chỉ có 2 cột là mã học sinh và điểm
    tham số df_right : 1 pandas dataframe có những dòng cú pháp đúng
    tham số answer_key: là 1 list của các đáp án
    trả về 1 pandas dataframe có cột mã học sinh (student_code) và điểm của học sinh đó (grade)'''
def report_grade(df_right,answer_key):
    # chuyển answer_key vể dạng array
    answer_key_array = np.array(answer_key)
    # tính số câu trả lời đúng, số câu trả lời sai và số điểm
    df_right['right'] = df_right['array'].apply(lambda x: sum(x==answer_key_array))
    df_right['wrong'] = df_right['array'].apply(lambda x: np.count_nonzero(x))-df_right['right']
    df_right['grade'] = df_right['right']*4-df_right['wrong']
    return df_right[['student_code','grade']]

''' viết 1 hàm báo cáo điểm trung bình, min, max và median, tham số đầu vào là 1 pandas series
    tham sô score là 1 pandas series gồm điểm của các học sinh
    trả về là in ra điểm trung bình, lớn nhất ,bé nhất, khoảng điểm và median'''
def report_score(score):
    print('Mean (average) score:',round(score.mean(),2))
    print('Highest score:',score.max())
    print('Lowest score:',score.min())
    print('Range of scores:',score.max() - score.min())
    print('Median score:',score.median())



#nhập tên file txt để đọc, ví dụ file là class1.txt thì chỉ cần nhập class1
filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")

# dùng hàm open_filename để lấy Dataframe gồm cột mã học sinh và cột câu trả lời
df=open_filename(filename)

# tách dataframe thành 2 dataframe là đúng cú pháp và sai cú pháp
df_right,df_error = split_dataframe(df)

print('**** ANALYZING ****\n')
# đưa ra dòng sai cú pháp và tên lỗi
analyzing_df_error(df_error)

print('\n**** REPORT ****\n')
print('Total valid lines of data:', len(df_right))    #in số dòng đúng cú pháp
print('Total invalid lines of data: {}\n'.format(len(df_error)))    #in số dòng sai cú pháp

# split để chuyển answer_key về dạng list
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(',')

#dùng hàm report_grade trả về mã học sinh (student_code) và số điểm (grade)
df1 = report_grade(df_right,answer_key)

# in mean, max, min, median của danh sách điểm
score = df1['grade']
report_score(score)


# Task 4: tạo một tệp “kết quả” chứa các kết quả chi tiết cho từng học sinh trong lớp
# chứa số ID của học sinh, dấu phẩy và sau đó là điểm của họ
df1.to_csv('{}_grades.txt'.format(filename),header= None, index = None)
#
