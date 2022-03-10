percentage = int(input('введите количество процентов: '))
if percentage == 11:
    print(percentage, "процентов")
elif percentage in range(1, 1001, 10):
    print(percentage, "процент")
elif percentage in range(22, 1001, 10):
    print(percentage, "процента")
elif percentage in range(23, 1001, 10):
    print(percentage, "процента")
elif percentage in range(24, 1001, 10):
    print(percentage, "процента")
elif percentage <= 4:
    print(percentage, "процента")
elif percentage >= 5:
    print(percentage, "процентов")
