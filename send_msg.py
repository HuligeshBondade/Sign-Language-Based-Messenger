import telepot


def sendtoTelegram( msg ):

    token = '7146368514:AAG56i0lMdiexEic0sHsXzi-MjXlmpP6h5U' # telegram token
    receiver_id = 1153544422 # https://api.telegram.org/bot<TOKEN>/getUpdatescond 


    bot = telepot.Bot(token)

    bot.sendMessage(receiver_id, msg) # send a activation message to telegram receiver id

# bot.sendPhoto(receiver_id, photo=open('test_img.png', 'rb')) # send message to telegram



