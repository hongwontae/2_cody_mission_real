

class QuizGame :

    def __init__ (self) :
        self.menu_actions = {
            1 : "test",
            2 : "test",
            3 : "test"
        }

    def show_menu(self):
            print("""
==========================
Quiz Game
==========================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 최고 점수
5. 퀴즈 삭제
6. 점수 기록 보기
0. 종료
==========================
""")

    def input_number(self, message : str, minimum : int, maximum : int) -> int:
        
        while True:
            try:
                number = input(message).strip()

                if number == "" :
                    print("빈 입력은 받지 않습니다.")
                    continue

                number = int(number)

                if minimum <= number <= maximum:
                    return number

                print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")

            except ValueError:
                print("숫자를 입력하세요.")

    def run (self) :
        while True :
            self.show_menu()
            menu = self.get_menu()

            if menu == 0 :
                print("프로그램을 종료합니다.")
                break

            self.menu_actions[menu]()

    def get_menu(self):
        return self.input_number("메뉴를 선택하세요: ", 0, max(self.menu_actions)) 



