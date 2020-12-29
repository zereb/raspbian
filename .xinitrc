export TERM=ansi
setxkbmap  -layout us,ru  -option grp:caps_toggle
sxhkd &
#exec i3
exec bspwm
