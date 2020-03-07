import random


def random_test(market_state):
    rand = random.randint(0, 3)
    if rand == 1:
        return 'buy'
    if rand == 0:
        return 'sell'
    if rand > 1:
        return 'pass'

def noise(market_state):
    rand = random.randint(0, 1)
    if rand == 1:
        return 'buy'
    if rand == 0:
        return 'sell'






def basic_rsi(state, length):
    if len(state) < length:
        return None

    gain_sum = []
    loss_sum = []
    for i in range(2, length + 2):
        print(i)
        print(state[-i], state[-(i-1)])
        if state[-i] > state[-(i-1)]:
            print(state[-i], 'is greater than', state[-(i-1)])
            gain_sum.append(abs(state[-i] - state[-(i-1)]))
        if state[-i] < state[-(i-1)]:
            print(state[-i], 'is less than', state[-(i-1)])
            loss_sum.append(abs(state[-i] - state[-(i-1)]))

    avg_gain = round(sum(gain_sum) / length, 2)
    avg_loss = round(sum(loss_sum) / length, 2)

    print(gain_sum, len(gain_sum))
    print(loss_sum, len(loss_sum))
    print(avg_loss, avg_gain)

    rs = round(avg_gain / avg_loss, 2)
    print(rs, 'is RS')
    rsi = 100 - (100/(1+rs))
    print(rsi, 'is RSI')

    return rsi

def simple_rsi(state, length):
    if len(state) < 20:
        return 'pass'
    else:
        gain_sum = []
        loss_sum = []
        for i in range(2, length + 2):
            # print(i)
            # print(state[-i], state[-(i-1)])
            if int(state[-i]) > int(state[-(i-1)]):
                # print(state[-i], 'is greater than', state[-(i-1)])
                gain_sum.append(abs(state[-i] - state[-(i-1)]))
            if int(state[-i]) < int(state[-(i-1)]):
                # print(state[-i], 'is less than', state[-(i-1)])
                loss_sum.append(abs(state[-i] - state[-(i-1)]))

        avg_gain = round(sum(gain_sum) / length, 2)
        avg_loss = round(sum(loss_sum) / length, 2)




        try:
            rs = round(avg_gain / avg_loss, 2)
        except:
            return 'pass'

        rsi = 100 - (100/(1+rs))


        if rsi > 70:
            return 'buy'
        if rsi < 30:
            return 'sell'
        else:
            return 'pass'