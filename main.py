# madang 데이터베이스 데이터 삽입, 삭제, 검색 #


import mysql.connector

def insert_data(cursor):
    bookid = input("책 번호 : ")
    bookname = input("책 제목: ")
    publisher = input("출판사 : ")
    price = input("가격: ")

    query = "INSERT INTO Book (bookid, bookname, publisher, price) VALUES (%s, %s, %s, %s)"
    values = (bookid, bookname, publisher, price)
    cursor.execute(query, values)

    print("데이터 삽입 완료")


def delete_data(cursor):
    bookid = input("삭제할 책 ID : ")
    query = "DELETE FROM Book WHERE bookid = %s"
    cursor.execute(query, (bookid,))

    print("데이터 삭제 완료")


def search_data(cursor):
    keyword = input("검색할 책 제목 : ")
    query = "SELECT * FROM Book WHERE bookname LIKE %s"
    cursor.execute(query, (f"%{keyword}%",))
    print("\n검색 결과:")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("검색 결과가 없습니다.")


def show_all_data(cursor):
    query = "SELECT * FROM Book"
    cursor.execute(query)
    print("\nBook 테이블 데이터:")
    for row in cursor.fetchall():
        print(row)

connection = mysql.connector.connect(
    host="192.168.146.3",
    port=4567,
    user="root",
    password="1234",
    database="madang"
)

if connection.is_connected():
    print("MySQL 연결 성공")
    cursor = connection.cursor()

    while True:
        print("\n메뉴 : ")
        print("1. 데이터 조회")
        print("2. 데이터 삽입")
        print("3. 데이터 삭제")
        print("4. 데이터 검색")
        print("5. 종료")

        number = input("작업을 선택하세요 : ")

        if number == "1":
            show_all_data(cursor)
        elif number == "2":
            insert_data(cursor)
            connection.commit()
        elif number == "3":
            delete_data(cursor)
            connection.commit()
        elif number == "4":
            search_data(cursor)
        elif number == "5":
            print("프로그램을 종료합니다.")
            break

    cursor.close()
    connection.close()

else:
    print("MySQL 연결 실패")

