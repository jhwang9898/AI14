import pandas as pd
from Levenshtein import distance

class ChatBot:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)  # CSV파일에서 데이터를 추출

    def best_answer(self, input_sentence):
        min_distance = float('inf')  # 최소거리 저장하는 변수를 초기화
        best_index = -1  # 최소거리를 가진 질문의 인덱스를 저장하는 변수를 -1로 초기화

        for i, question in enumerate(self.data['Q']):
            current_distance = distance(input_sentence, question)  # 입력문장과 질문 간의 레벤슈타인 거리를 계산
            if current_distance < min_distance:
                min_distance = current_distance  # 현재거리가 최소거리보다 작으면 최소거리를 업데이트
                best_index = i  # 최소거리를 가진 질문의 인덱스를 업데이트

        return self.data['A'][best_index]  # 최소거리를 가진 질문에 해당하는 답변을 반환

filepath = 'ChatbotData.csv'
chatbot = ChatBot(filepath)  # 챗봇 객체 생성

while True:
    input_sentence = input('나: ')  # 문장을 입력
    if input_sentence.lower() == '종료': # 종료를 입력하면 챗봇종료
        break
    answer = chatbot.best_answer(input_sentence)  # 최고답변을 찾음
    print('챗봇: ', answer)  # 챗봇의 응답출력