# Task 1 - Data Structures

| الهيكل | مرتب؟ | قابل للتعديل؟ | يسمح بالتكرار؟ | كيف أصل لعنصر؟ |

| list        Yes            Yes            Yes               index
| tuple      Yes             No              Yes                 index
| set         No              Yes                  
| set         No              Yes             NO                   بدونindex    
|  dict         Yes             Yes             No                  Key         
                                   
['Python', 'Excel', 'Git', 'SQL', 'Pandas'] 5
Excel Pandas ['Excel', 'Git']
3 False
Not set
3 ['name', 'role', 'team']


[1, 2, 3, 4]
[1, 2, 3, 4] [1, 2, 3, 4, 5]


## شرح فخ النسخ

توقعت أن a ما تتغير عند التعديل على b، لكن تغيرت لأن الاثنين يشيرون لنفس القائمة. أما copy() فتنشئ نسخة مستقلة.

## اختيار الهيكل المناسب

| الحالة | الهيكل | السبب |
|---|---|---|
| إحداثيات الشركة | tuple | ثابتة |
| مهام اليوم | list | يمكن تعديلها |
| أسماء الشركات | set | يمنع التكرار |
| بيانات الموظف | dict | يعتمد على المفتاح والقيمة |


# List
tasks = ["Study Python", "Practice coding"]

# Tuple
colors = ("Black", "White", "Green")

# Set
subjects = {"Python", "AI", "Cybersecurity"}

# Dictionary
student = {"name": "Rahaf", "major": "AI"}   