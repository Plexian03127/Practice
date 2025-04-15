import csv

data_to_write = [
    ['순위', '제목', '가수'],
    [1, '1노래', 5000],
    [2, '2노래', 6500],
    [3, '마케팅부', 5500],
]
file_path = 'music.csv'
try:
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_write)

    print (f"'{file_path}' 파일이 성곡적으로 생성되었습니다.")

except Exception as e:
    print(f"파일 쓰기 중 오류 발생: {e}")