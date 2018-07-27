from turtle import *
color('purple', 'blue')
begin_fill()
while True:
    forward(360)
    left(530)
    if abs(pos()) < 1:
        break
end_fill()
done()
