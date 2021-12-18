from django.contrib.auth import get_user_model
from .models import Player_detail, Level

User = get_user_model()

def saveData(address, levelSelected, score, coin_total, box_total):
    user = User.objects.get(address=address)
    level = Level.objects.get(num=levelSelected)
    check = Player_detail.objects.filter(user=user).exists() and Player_detail.objects.filter(level=level).exists()
    if Player_detail.objects.filter(user=user).filter(level=level) and Player_detail.objects.filter(user=user).filter(level=level)[0]:
        play_date = Player_detail.objects.filter(user=user).filter(level=level)[0] 
    else:
        play_date = Player_detail.objects.filter(user=user).filter(level=level)
    if int(levelSelected) == 1:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.008
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total) 
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 2:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.009
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 3:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.01
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 4:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.02
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 5:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.03
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 6:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.04
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 7:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.05
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 8:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.06
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 9:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.07
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 10:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.08
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 11:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.09
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 12:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.10
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 13:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.11
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 14:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.12
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 15:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.13
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 16:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.14
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 17:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.15
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 18:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.16
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 19:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.17
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 20:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.18
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 21:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.19
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 22:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.20
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 23:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.21
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 24:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.22
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 25:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.23
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 26:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.24
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 27:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.25
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 28:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.26
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 29:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.27
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )
    elif int(levelSelected) == 30:
        if check:
            player = play_date
            if player.level.num == int(levelSelected):
                player.score = int(score)
                if int(coin_total) == 0:
                    player.coin_total += int(coin_total)
                else:
                    player.coin_total += int(coin_total) * 0.28
                if (int(box_total) > player.box_total ) and (int(box_total) < 4 ):
                    player.box_total = int(box_total)
                player.save()
        else:
            player = Player_detail.objects.create(
                user = user,
                level = level,
                score = int(score),
                coin_total = int(coin_total),
                box_total = 3
            )


