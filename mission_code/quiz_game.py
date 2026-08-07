

class QuizGame :

    def __init__ (self) :
        self.menu_actions = {}

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
                number = int(input(message).strip())

                if minimum <= number <= maximum:
                    return number

                print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")

            except ValueError:
                print("숫자를 입력하세요.")

    def get_menu(self):
        return self.input_number("메뉴를 선택하세요: ", 0, max(self.menu_actions)) 



