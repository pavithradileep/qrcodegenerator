import qrcode

url = "https://www.linkedin.com/in/pavithra-dileep-0435bb291/"
myqr = qrcode.make(url)
myqr.save("myqr.png")
