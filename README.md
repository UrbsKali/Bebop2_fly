# Bebop Control Script
Some useful python script which allows you to control your parrot bebop 2 with code, get live stream, and schedule routes! 
<br>
# How to use ?
First, you will need to install the <a href="#Dependencies">dependencies</a>. Secondly, for each script, you have a notice inside file and a sum in this readme.
You have to connect your computer to your drone's wifi before begin to use the code in order to make your bebop fly ! 
Content : 
<a href="#bebop_cmd.py">Bebop_cmd.py</a>
<br>
# Dependencies

You <strong>must</strong> have install <strong>pyparrot</strong>, To do that, you can install manually or lauch the setup.py script
<br>
# Bebop_cmd.py
connect(): this command give you the power of all the following command, so do it first.
disconnect() : disconnect your drone from all python commands.
take(number_of_seconde) : make your bebop 2 take in a certain number of seconde (default : 5).
land(number_of_seconde) : make your bebop 2 land in a certain number of seconde (default: 5).
fow(power, duration) : make your drone go foward, the power must take values between -100 and 100 (default : 20, 1).
back(power, duration) : make your drone go backward, the power must take values between -100 and 100 (default : 20, 1).
left(power, duration) : make your drone go left, the power must take values between -100 and 100 (default : 10, 1).
right(power, duration) : make your drone go right, the power must take values between -100 and 100 (default : 10, 1).
r_left(degre, duration) : make your drone turn left, the degre must take values between -100 and 100 (default : 10, 1).
r_right(degre, duration) : make your drone turn right, the degre must take values between -100 and 100 (default : 10, 1).


# License 

This work is under the GNU GPL v3.0 license, so please give me the credit if you want to fork or uprgade ! 
<br>
Thank you for reading !
