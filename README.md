# PyLED

This is a very basic version of the Glediator Software from [solderlab](http://www.solderlab.de) written in Python.

I did not like the java approach and did not want a tool with a ui that needs X
to run.

It is supposed to be easily expandable, so you can simply add your own generator.
Just have a look around the generators in the pyled module.

It is a prototype and I haven't found the time to bring it to perfection.

## Configuration

Use the provied *config.ini* to setup the program. There are different sections
for different stuff. Set the default generator under *[general]/generator* and the
default brightness as well.

Setup the API parameters under *[api]*.

Inside the *[display]* section you will find settings for your matrix. Every
driver should take a *height*, *width* and *maxfps*. The first two are
self-explanatory and the last one is to limit cpu strain. The driver will only
render the given amount of frames per second (if he manages to).

## Drivers

### dummy
There is a dummy driver which will output the screens on a colored Linux terminal
which does not take any options.

### serial
The other one is a serial driver which is working in the same way as the original
Glediator software. You can use the *WS2812_Glediator sketch* for arduino to take this
signal and run your strip.

## Generators

Unfortunately generators can not be coupled. There are a few generators inside
the pyled module.

The generators need a *get_image()* function which has to return a two-dimensional
array of triplet of bytes.

First dimension is the pixels x coordinate, second the y coordinate, and the triplet
represents the RGB value of that pixel.

    leds[x][y] = (120, 240, 16)

## api

At the moment it is a telnet port taking specific commands to switch the generators,
set the brightness and some options for the generators, if any. It could be worse.

## Thanks and kudos

None of this is mine. Everything was stolen somewhere. Especially the idea. And
I would like to give my sepcial thanks to the guys at [solderlab](http://www.solderlab.de)
for creating Glediator. I just needed something that does not eat my processor
nor something that needs a java ui for running in the background. By the way, I
stole your Plasma generator, I hope thats OK.

Another thanks goes to the guys at [Blinkenlights](http://blinkenlights.de) for
having a simple movie format. And I also adapted a few of the BLM files for my
screen. I hope thats OK.
