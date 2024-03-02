def on_button1_button_down():
    colorbit_51bit.show_color_icon(ColorIcon.SMALL_SQUARE, colorbit.colors(BitColors.GREEN))
    basic.show_icon(IconNames.YES)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
modules.button1.on_event(jacdac.ButtonEvent.DOWN, on_button1_button_down)

def on_button2_button_hold():
    colorbit_51bit.show_color_icon(ColorIcon.NO, colorbit.colors(BitColors.PURPLE))
    music.play(music.string_playable("G B A G C5 B A B ", 120),
        music.PlaybackMode.UNTIL_DONE)
modules.button2.on_event(jacdac.ButtonEvent.HOLD, on_button2_button_hold)

def on_button2_button_down():
    colorbit_51bit.show_color_icon(ColorIcon.NO, colorbit.colors(BitColors.PURPLE))
    basic.clear_screen()
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
modules.button2.on_event(jacdac.ButtonEvent.DOWN, on_button2_button_down)

colorbit_51bit: colorbit.Strip = None
basic.show_icon(IconNames.HEART)
colorbit_51bit = colorbit.init_color_bit(DigitalPin.P0, BitColorMode.RGB)
music.set_volume(255)