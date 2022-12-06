students = [
   {
      "name": "김채연",
      "Korean": 90,
      "English": 93,
      "Math": 60
   },
   {
      "name": "문태일",
      "Korean": 100,
      "English": 74,
      "Math": 87
   },
   {
      "name": "서영호",
      "Korean": 84,
      "English": 100,
      "Math": 91
   }
]

korean = 0
english = 0
math = 0
for element in students:
   korean = korean + element["Korean"]
   english = english + element["English"]
   math = math + element["Math"]
   print("이름: {}\n국어: {}\n영어: {}\n수학: {}\n"
      .format(element["name"], element["Korean"], element["English"], element["Math"]))

print("국어 합: {}".format(korean))
print("영어 합: {}".format(english))
print("수학 합: {}\n".format(math))

print("국어 평균: {:.2f}".format(korean / 3))
print("영어 평균: {:.2f}".format(english / 3))
print("수학 평균: {:.2f}".format(math / 3))