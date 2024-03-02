input.onButtonPressed(Button.A, function () {
    colorbit_51bit.showColorIcon(ColorIcon.Giraffe, colorbit.colors(BitColors.Purple))
})
input.onButtonPressed(Button.B, function () {
    colorbit_51bit.showColorIcon(ColorIcon.Fabulous, colorbit.colors(BitColors.Green))
})
let colorbit_51bit: colorbit.Strip = null
basic.showIcon(IconNames.Yes)
colorbit_51bit = colorbit.initColorBit(DigitalPin.P0, BitColorMode.RGB)
