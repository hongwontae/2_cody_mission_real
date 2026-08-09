import json
import random
from quiz import Quiz

class QuizGame :

    CHOICE_COUNT = 4

    def __init__ (self) :
        self.quizzes = []
        self.best_score = 0
        self.menu_actions = {
            1 : self.play_quiz,
            2 : self.add_quiz,
            3 : self.show_quiz_list,
            4 : self.show_best_score,
            5 : self.delete_quiz
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

    def input_text(self, message : str) -> str:
        while True:
            text = input(message).strip()

            if text:
                return text

            print("빈 문자열은 입력할 수 없습니다.")

    def confirm(self, message):
        while True:
            choice = input(message).strip().lower()

            if choice == "y":
                return True

            if choice == "n":
                return False

            print("y 또는 n을 입력하세요.")

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
            self.save_state()

    def get_menu(self):
        return self.input_number("메뉴를 선택하세요: ", 0, max(self.menu_actions)) 

    def load_state(self) :
        try :
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            self.best_score = data["best_score"]
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
                "quizzes": [quiz.to_dict() for quiz in self.quizzes],}
        try :
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError :
            print("파일 저장에 실패했습니다.")

    def play_quiz(self):
        score = 0.0

        print("\n===== 퀴즈 시작 =====")

        count = self.input_number(f"몇 문제를 푸시겠습니까? (1~{len(self.quizzes)}): ",1,len(self.quizzes))

        random_quizzes = random.sample(self.quizzes, count)

        for i, quiz in enumerate(random_quizzes, start=1):
            print(f"\n[{i}번 문제]")

            quiz.print_quiz()

            print()

            hint_used = self.confirm("힌트를 보시겠습니까? (y/n) : ")

            if hint_used:
                quiz.print_hint()            

            answer = self.input_number("정답 번호를 입력하세요: ",1, len(quiz.choices))

            if quiz.check_answer(answer):
                print()
                print("정답입니다!")

                if hint_used :
                    score += 0.5
                else :
                    score +=1

            else:
                print(f"오답입니다! 정답은 {quiz.get_answer()}번 입니다.")

        print("\n===== 퀴즈 종료 =====")
        print(f"점수 : {score} / {float(count)}")

        if score > self.best_score:
            self.best_score = score
            print("🎉 최고 점수가 갱신되었습니다!")
        else :
            print("최고 점수는 갱신되지 않았습니다.")

        self.save_state()

    def add_quiz (self) :
        question = self.input_text("문제 : ")

        choices = []

        for i in range(1, self.CHOICE_COUNT+1):
            choices.append(self.input_text(f"{i}번 보기 : "))

        answer = self.input_number("정답 번호: ",1,len(choices))

        quiz = Quiz(question, choices, answer)

        self.quizzes.append(quiz)

        self.save_state()

        print()
        print("퀴즈가 추가되었습니다.")

    def show_quiz_list(self):
        print("\n===== 퀴즈 목록 =====")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 기본 퀴즈를 초기화합니다.")
            self.init_quizzes()
            self.save_state()

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{i}]")
            quiz.print_quiz()
            print(f"정답 : {quiz.get_answer()}번")

    def show_best_score(self):
        print(f"\n현재 최고 점수 : {self.best_score}")

    def delete_quiz(self) :
        if not self.quizzes:
            print("삭제할 퀴즈가 없습니다.")
            return

        self.show_quiz_list()

        num = self.input_number("삭제할 퀴즈 번호: ",1,len(self.quizzes))

        if not self.confirm("정말 삭제하겠습니까? (y/n): "):
            print("삭제가 취소되었습니다.")
            return

        deleted = self.quizzes.pop(num - 1)

        self.save_state()

        print(f"'{deleted.question}' 퀴즈가 삭제되었습니다.")

    