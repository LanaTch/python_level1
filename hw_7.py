#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random
class Bag:
    def gen_bags(self):
        lst_of_bag = [x for x in range(1, self.bags_max + 1)]
        random.shuffle(lst_of_bag)
        for y in lst_of_bag:
            yield y

    def __init__(self, bags_max):
        self.bags_max = bags_max
        self.gen = self.gen_bags()

class Loto_card:
    def get_card(self):
        num = set()
        while len(num) < 15:
            num.add(random.randint(1, 91))
        card = list(num)
        random.shuffle(card)
        t1=card[:5]
        t1.sort()
        t2=card[5:10]
        t2.sort()
        t3=card[10:]
        t3.sort()
        card = t1+t2+t3

        return card

    def __init__(self, name):
        self.name = name
        self.score = 0
        # self.get_card()
    def get_str_card(self, card_player):
        string_card = []
        card_str = [str(i) for i in card_player]
        string_card.append('{:-^25}'.format(self.name))
        string_card.append('{0[0]:} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_str[:5]))
        string_card.append('{0[0]:>3} {0[1]:<5} {0[2]:<3} {0[3]:<3} {0[4]} '.format(card_str[5:10]))
        string_card.append('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(card_str[10:]))
        string_card.append('{:-^25}'.format('-'))
        return '\n'.join(string_card)

    def search(self, card_player, num_cask):
        for n in card_player:
            if num_cask == n:
                card_player[card_player.index(num_cask)] = '-'
                self.score += 1
                if self.score == 15:
                    print('{} Победила!'.format(self.name))
                    exit(1)
                return True
        return False



def main():
    bags_max = 90
    bag = Bag(bags_max)
    player = Loto_card('Ваша карточка')
    player_card = player.get_card()
    computer = Loto_card('Карточка компьютера')
    computer_card = computer.get_card()

    step = 0
    flag = True
    while True:
        print(player.get_str_card(player_card))
        print(computer.get_str_card(computer_card))
        if flag:
            actual_bag = next(bag.gen)
            step += 1
        print('Новый бочонок: {} (осталось {})'.format(actual_bag, bags_max - step))

        answer = input('Зачеркнуть цифру? y/n/q')
        answer = answer.lower()
        if answer == 'q':
            print('Выхожу')
            break
        elif len(answer) == 0 or answer not in 'ynq':
            print('\n\nНезивестный ввод\n')
            flag = False
        elif answer == 'y':
            flag = True
            if player.search(player_card, actual_bag):
                continue
            else:
                print('Такого боченка нет в Вашей карточке. Вы проиграли!')
                exit(1)
        elif answer == 'n':
            flag = True
            if player.search(player_card, actual_bag):
                print('Такой боченок есть в Вашей карточке. Вы проиграли!')
                exit(1)
            elif computer.search(computer_card, actual_bag):
                continue

if __name__ == '__main__':
    main()