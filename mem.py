import pymysql
connect = pymysql.connect(host='localhost', user="root", password="azsxdcfv7706", db='employees', charset='utf8')
cursor = connect.cursor(pymysql.cursors.DictCursor)

def print_result(result):
  print("\n---------------------------------------------------------------------------")
  cnames = ['이름', '생년월일', '소속', '전화번호', '거주지']
  for c in cnames:
    print(c.center(11, ' '), end='\t')
  print("\n---------------------------------------------------------------------------")
  ccodes = ['name', 'birth', 'team', 'phone', 'address']
  for r in result:
    for c in ccodes:
      print(str(r[c]).center(11, ' '), end='\t')
    print("") 
  print("---------------------------------------------------------------------------")

cmd = 'na'
while cmd != 'q':
   print("")
   print("***사용 가능 명령어 리스트***")
   print("a  : 모든 데이터 조회(all)")
   print("f  : 조건에 맞는 데이터만 조회(find)")
   print("i  : 수강생 입력(insert)")
   print("d  : 수강생 삭제(delete)")
   print("r  : 정보 변경(revise)")
   print("q  : 저장하고 나가기(quit)")
   print("")
   cmd = input("command(명령어 입력): ")
   print("")
   if cmd == 'a':
     sql = "SELECT * FROM student"
     cursor.execute(sql)
     result = cursor.fetchall()
     print_result(result)
   elif cmd == 'f':
     print("무엇을 기준으로 검색하시겠습니까? (이름/나이/소속/전화번호/거주지)")
     con = input("> ")
     if con == '이름':
        print("\n검색하실 수강생의 이름을 입력해주세요")
        con2 = input("> ")
        sql = "SELECT * FROM  student WHERE name = '{}'".format(con2)
        cursor.execute(sql)
        result = cursor.fetchall()
        print_result(result)
     elif con == '나이':
        print("\n# 숫자만 입력 해 주세요.\n")
        input_age1 = int(input("몇 살 이상을 검색하시겠습니까? "))
        input_age2 = int(input("몇 살 이하를 검색하시겠습니까? "))
        import datetime, time
        d = datetime.date.today()
        year1 = d.year - input_age2 + 1
        year2 = d.year - input_age1 + 1
        sql = "SELECT * FROM student WHERE LEFT(birth, 4) BETWEEN {} AND {}".format(year1, year2)
        cursor.execute(sql)
        result = cursor.fetchall()
        print_result(result)
     elif con == '소속':
        print("\n검색하실 수강 그룹을 입력해 주세요.(A/B/C)")
        con2 = input("> ")
        sql = "SELECT * FROM student WHERE team ='{}'".format(con2)
        cursor.execute(sql)
        result = cursor.fetchall()
        print_result(result)
     elif con == '전화번호':
        print("\n검색하실 전화번호를 입력해 주세요.(숫자만 입력 해 주세요.)")
        con2 = input("> ")
        sql = "SELECT * FROM student WHERE phone = '{}'".format(con2)
        cursor.execute(sql)
        result = cursor.fetchall()
        print_result(result)
     elif con == '거주지':
        print("\n검색하실 거주지를 입력해 주세요.")
        con2 = input("> ")
        sql = "SELECT * FROM student WHERE address = '{}'".format(con2)
        cursor.execute(sql)
        result = cursor.fetchall()
        print_result(result)
   elif cmd == 'i':
     name = input("수강생 이름: ")
     birth = input("생년월일(숫자 8자리): ")
     team = input("소속 그룹(A/B/C): ")
     phone = input("전화번호(숫자 11자리): ")
     address = input("거주지: ")
     sql = "INSERT INTO student VALUES('{}',{},'{}','{}','{}')".format(name, birth, team, phone, address)
     cursor.execute(sql)
     connect.commit()
   elif cmd == 'd':
     print("#수강생 삭제는 이름 통해서만 가능합니다.")
     name = input("목록에서 삭제할 수강생의 이름: ")
     sql = "DELETE FROM student WHERE name = '{}'".format(name)
     print("sql::", sql)
     cursor.execute(sql)
     connect.commit()
     print("해당 데이터의 삭제가 완료되었습니다.")
   elif cmd == 'r':
     print(" 정보를 변경할 수강생의 선택은 이름 통해서만 가능합니다.")
     name = input("이름: ")
     sql = "SELECT * FROM student WHERE name = '{}'".format(name)
     cursor.execute(sql)
     result = cursor.fetchall()
     print_result(result)
     con = input("\n어떤 정보를 변경하시겠습니까(이름/생년월일/소속/전화번호/거주지)? ")
     if con == '이름':
       print("\n해당 수강생의 이름을 무엇으로 수정하시겠습니까?")
       new_name = input("> ")
       sql = "UPDATE student SET name = '{}' where name = '{}'".format(new_name, name)
       cursor.execute(sql)
       result = cursor.fetchall()
       connect.commit()
       print("\n정보 변경이 완료되었습니다.")
     elif con == '생년월일':
       print("해당 수강생의 생년월일을 무엇으로 수정하시겠습니까? (숫자 8자리)")
       birth = input("> ")
       sql = "UPDATE student SET birth = '{}' where name = '{}'".format(birth, name)
       cursor.execute(sql)
       result = cursor.fetchall()
       connect.commit()
       print("\n정보 변경이 완료되었습니다.")
     elif con == '소속':
       print("\n해당 수강생의 소속을 무엇으로 수정하시겠습니까? (A/B/C)")
       team = input("> ")
       sql = "UPDATE student SET team = '{}' where name = '{}'".format(team, name)
       cursor.execute(sql)
       result = cursor.fetchall()
       connect.commit()
       print("\n정보 변경이 완료되었습니다.")
     elif con == '전화번호':
       print("\n해당 수강생의 전화번호를 무엇으로 수정하시겠습니까? (숫자 11자리)")
       new_phone = input("> ")
       sql = "UPDATE student SET phone = '{}' where name = '{}'".format(new_phone, name)
       cursor.execute(sql)
       result = cursor.fetchall()
       connect.commit()
       print("\n정보 변경이 완료되었습니다.")
     elif con == '거주지':
       print("\n해당 수강생의 거주지를 어디로 수정하시겠습니까? ")
       address = input("> ")
       sql = "UPDATE student SET address = '{}' where name = '{}'".format(address, name)
       cursor.execute(sql)
       result = cursor.fetchall()
       connect.commit()
       print("\n정보 변경이 완료되었습니다.")
   elif cmd == 'q':
     connect.commit()
     print("프로그램을 종료합니다.")
   else:
     print("잘못된 명령어가 입력되었습니다. 다시 입력 해주세요.")