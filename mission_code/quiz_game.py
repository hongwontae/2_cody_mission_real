

import json
from quiz import Quiz

class QuizGame :

    def __init__ (self) :

        self.quizzes = []
        self.best_score = 0
        self.history = []
        self.menu_actions = {
            1 : "test",
            2 : "test",
            3 : "test"
        }
        self.load_state()

    def init_quizzes(self) :
        self.quizzes = [
            Quiz("대한민국의 수도는?",["서울", "부산", "대구", "인천"],1),
            Quiz("파이썬의 창시자는?", ["귀도 반 로섬", "제임스 고슬링", "비야네", "데니스 리치"],1),
            Quiz("축구 감독인 사람은?", ["아카자", "홍명보", "펩시콜라", "펩"], 4),
            Quiz("코디세이의 위치는?", ["평양", "쓰촨성", "약간포동", "개포동"], 4),
            Quiz("학습 네이토의 정체는?", ["깡통", "할루시네이션", "AI Chat Bot", "네이트"],3),
            Quiz("파이썬은 어떤 언어인가?", ["일본어", "인터프리터 언어", "스페인어", "인어"],2),
        ]

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
        try :
            while True :
                self.show_menu()
                menu = self.get_menu()

                if menu == 0 :
                    print("프로그램을 종료합니다.")
                    break

                self.menu_actions[menu]()
        except (KeyboardInterrupt, EOFError) :
            print("\n 프로그램을 안전하게 종료합니다.")

    def get_menu(self):
        return self.input_number("메뉴를 선택하세요: ", 0, max(self.menu_actions)) 

    def load_state(self) :
        try :
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            self.best_score = data["best_score"]
            self.history = data.get("history", [])
            self.quizzes = []

            for quiz_data in data["quizzes"]:
                quiz = Quiz(
                    quiz_data["question"],
                    quiz_data["choices"],
                    quiz_data["answer"],
                    )

                self.quizzes.append(quiz)

        except FileNotFoundError:
            print("저장 파일이 없습니다. 기본 퀴즈를 생성합니다.")
            self.init_quizzes()
            self.save_state()

        except json.JSONDecodeError:
            print("저장 파일이 손상되었습니다. 기본 퀴즈로 복구합니다.")
            self.init_quizzes()
            self.save_state()
        except KeyError :
            print("저장할 파일 형식이 올바르지 않습니다.")
            self.init_quizzes()
            self.save_state()

    def save_state(self):
        data = {
                "best_score": self.best_score,
                "quizzes": [quiz.to_dict() for quiz in self.quizzes],
                "history": self.history}
        try :
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError :
            print("파일 저장에 실패했습니다.")


