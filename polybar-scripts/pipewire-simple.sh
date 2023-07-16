#!/bin/sh

VOLUME=$(pamixer --get-volume-human)

case $1 in
    "--up")
        pactl set-sink-volume @DEFAULT_SINK@ +10%
        ;;
    "--down")
        pactl set-sink-volume @DEFAULT_SINK@ -10%
        ;;
    "--mute")
        pactl set-sink-mute @DEFAULT_SINK@ toggle
        ;;
    *)
        echo " 🔥${VOLUME}"
esac

