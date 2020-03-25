import pandas as pd
import random as random
import math

# Please edit only the ai_available
player_available = [0,1,2,3,4,5,6,7,8,9]
ai_available = [0,1,2,3,4,5,6,7,8,9]



offset = ai_available[9]-9

# initializing the table
numbers = {}
i = 0
while i < 10:
    numbers[ai_available[i]] = [0.0,0,0,0,0,0,0,0,0,0]
    i+=1

stats = pd.DataFrame(numbers)


player_choices = []

ai_choices = []
player_points = 0
ai_points = 0

factor = 0

k2_success = factor
k3_success = factor
k4_success= factor
extremity_success=factor


turn = 0
while turn < 10:

    # Filling up the table

    numbers_left = []
    i =0
    while i<10+offset:
        if i in player_available or i in ai_available:
            numbers_left.append(i)
        i+=1

    weight = int(math.ceil(len(numbers_left)/2.0))

    if len(numbers_left) % 2 == 0:
        i = 0
        while i< 10+offset:
            if i in ai_available:
                j = 0
                while j<10+offset:
                    if j in player_available:
                        if j == i:
                            stats[i][j] = 0
                        if j > i:
                            stats[i][j] = -weight+(numbers_left.index(j)-numbers_left.index(i))
                        if i > j:
                            stats[i][j] = weight-(numbers_left.index(i)-numbers_left.index(j))
                    j+=1
            i+=1
    else:
        i = 0
        while i < 10 + offset:
            if i in ai_available:
                j = 0
                while j < 10 + offset:
                    if j in player_available:
                        if j == i:
                            stats[i][j] = 0
                        if i > j:
                            value = weight - (numbers_left.index(i) - numbers_left.index(j))
                            if value > 0:
                                stats[i][j] = value
                            else:
                                stats[i][j] = value - 1
                        if j > i:
                            value = -weight + (numbers_left.index(j) - numbers_left.index(i))
                            if value < 0:
                                stats[i][j] = value
                            else:
                                stats[i][j] = value + 1


                    j += 1
            i += 1

    print(stats)

    # Making the decision

    player_choices.append('placeholder')
    while player_choices[turn] not in player_available:
        player_choices[turn] = (int(raw_input("You have " + str(player_available) + " available, and Billy has " + str(ai_available) + ". What will your move be? ")))
        if player_choices[turn] not in player_available:
            print("LOSER FACE. TRY AGAIN")

    if turn == 0:
        # k-level = 0
        ai_choices.append(int(random.random()*10+offset))
        print("Billy played " + str(ai_choices[turn]))

    else:
        dummy_stats=stats.copy()
        print(stats)

        # k-level = 4
        # min = 1000000
        # min_index1 = 0
        # sums = dummy_stats.sum(axis=1)
        # i = 0
        # while i < 10:
        #     if i in sums:
        #         sum = sums[i]
        #         if sum < min:
        #             min = sum
        #             min_index1 = i
        #     i += 1
        #
        # i = 0
        # max = -1000000
        # max_index = 0
        # while i < 10+offset:
        #     if i in dummy_stats.sum(axis=0):
        #         col = stats[i][min_index1]
        #         if col > max:
        #             max = col
        #             max_index = i
        #     i += 1
        #
        # i = 0
        # min = 1000000
        # min_index = 0
        # while i < 10:
        #     if i in dummy_stats.sum(axis=1):
        #         row = stats[max_index][i]
        #         if row < min:
        #             min = row
        #             min_index = i
        #     i += 1
        #
        #
        #
        # k4_guess = min_index
        #
        #
        # if player_choices[turn] == k4_guess and turn !=9:
        #     k4_success = (k4_success+1)
        # k4_success=k4_success*0.75246342
        #
        # print("Billy thought you would have played " + str(min_index1) + ", so he would have played " + str(
        #     max_index) + ", but then he expected you to play "+ str(min_index))


        # k-level = 3
        max = -1000000
        max_indices = [0]
        sums = dummy_stats.sum(axis=0)
        i = 0
        while i < 10+offset:
            if i in sums:
                sum = sums[i]
                if sum == max:
                    max_indices.append(i)
                elif sum > max:
                    max = sum
                    max_indices = [i]
            i += 1

        max_index = max_indices[int(random.random()*len(max_indices))]

        i=0
        min = 1000000
        min_indices = [0]
        while i < 10:
            if i in dummy_stats.sum(axis=1):
                row = stats[max_index][i]
                if row == min:
                    min_indices.append(i)
                elif row < min:
                    min = row
                    min_indices = [i]
            i += 1

        min_index = min_indices[int(random.random()*len(min_indices))]


        k3_guess = min_index



        print("Billy would have played " + str(max_index) + ", so he expected you to play " + str(k3_guess))


        # k-level = 2
        min = 1000000
        min_indices = [0]
        sums = stats.sum(axis=1)
        i = 0
        while i < 10:
            if i in sums:
                sum = sums[i]
                if sum == min:
                    min_indices.append(i)
                elif sum < min:
                    min = sum
                    min_indices = [i]
            i += 1

        min_index = min_indices[int(random.random()*len(min_indices))]


        print("Billy expected you to play " + str(min_index))


        # k-4 effect
        # j = 0
        # while j < 10 + offset:
        #     if j in stats.sum(axis=0):
        #         dummy_stats[j][k4_guess] += stats[j][k4_guess] * (k4_success)
        #     j += 1

        # k-3 effect
        j = 0
        while j < 10 + offset:
            if j in stats.sum(axis=0):
                dummy_stats[j][k3_guess] += stats[j][k3_guess] * (k3_success)
                # dummy_stats[j][k3_guess] *= (k3_success)
            j += 1
        if player_choices[turn] == k3_guess:
            k3_success = (k3_success+1)
        # k-2 effect
        j = 0
        while j < 10 + offset:
            if j in stats.sum(axis=0):
                dummy_stats[j][min_index] += stats[j][min_index] * (k2_success)
                # dummy_stats[j][min_index] *= (k2_success)
            j += 1
        if player_choices[turn] == min_index:
            k2_success = (k2_success+1)
        # extremities
        # i = 0
        # while i < 10:
        #     if i in stats.sum(axis=1): #lower bound
        #         j=0
        #         lowbound=i
        #         while j < 10+offset:
        #             if j in stats.sum(axis=0):
        #                 dummy_stats[j][i] += stats[j][i] * (extremity_success)
        #                 # dummy_stats[j][i] *= (extremity_success)
        #             j+=1
        #         i = 10
        #     i+=1
        # i = 10
        # while i > -1:
        #     if i in stats.sum(axis=1):  # upper bound
        #         j = 0
        #         highbound=i
        #         while j < 10 + offset:
        #             if j in stats.sum(axis=0):
        #                 # dummy_stats[j][i] += stats[j][i] * (extremity_success)
        #                 dummy_stats[j][i] *=(extremity_success)
        #
        #             j+=1
        #         i = -1
        #     i -= 1
        # if player_choices[turn] in [highbound, lowbound] and turn!=9:
        #     extremity_success+=1




        print(dummy_stats)


        # k-level = 1
        max = -100000
        max_indices = [0]
        sums = dummy_stats.sum(axis=0)
        i = 0
        while i < 10+offset:
            if i in sums:
                sum = sums[i]
                if sum == max:
                    max_indices.append(i)
                elif sum > max:
                    max = sum
                    max_indices = [i]
            i += 1

        max_index = max_indices[int(random.random()*len(max_indices))]

        ai_choices.append(max_index)
        print("Billy played " + str(ai_choices[turn]))



    print(str(player_choices[turn]) + " vs " + str(ai_choices[turn]))


    if player_choices[turn] > ai_choices[turn]:
        player_points+=1
        print("You took the dub that round. You are now at " + str(player_points) + " and Billybot is at " + str(ai_points))
    elif player_choices[turn] < ai_choices[turn]:
        ai_points+=1
        print("You took the L that round. You are now at " + str(player_points) + " and Billybot is at " + str(ai_points))
    else:
        print("TIE! You are now at " + str(player_points) + " and Billybot is at " + str(ai_points))

    player_available.remove(player_choices[turn])
    stats.drop([player_choices[turn]], axis=0, inplace=True)
    ai_available.remove(ai_choices[turn])
    stats.drop([ai_choices[turn]], axis=1, inplace=True)


    turn +=1

if player_points > ai_points:
    print("You won! Good job. Billybot took " + str(ai_points) + " tricks and you took " + str(player_points) + " tricks")
elif ai_points > player_points:
    print("You lost! Bad job. Billybot took " + str(ai_points) + " tricks and you took " + str(player_points) + " tricks")
else:
    print("You fellas tied! Billybot took " + str(ai_points) + " tricks and you took " + str(player_points) + " tricks")
# print("You were " + str(int(100*k3_success)/10.0) + "% k-level 2, and " + str(int(100*k2_success)/10.0) + "% k-level 1, and " + str(int(100*extremity_success)/10.0) + "% a fool")