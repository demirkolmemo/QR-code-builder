import qrcode

Link = input('Link:')

code = qrcode.make(Link)

code.save('qrcode.png')


