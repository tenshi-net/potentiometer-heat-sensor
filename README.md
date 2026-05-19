# Potentiometer-based LED Heat Sensor (Simulated)

A very simple Python script for MicroPython on the Raspberry Pi Pico 2 W. Written to convert potentiometer values to a rounded value of 0-100, then toggle on an LED depending on the value. The idea is to simulate a temperature/heat sensor as you might find on electrical equipment.

# Background

I'm doing a [video course](https://www.youtube.com/playlist?list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5) on YouTube by the excellent Paul McWhorter in order to learn how to use a Raspberry Pi Pico (specifically the 2 W model), as part of my efforts to learn microcontrollers. This script is directly based on the code for Lesson 7, so I don't claim any ownership. You can use this script as you wish, whether as a framework for your own projects or to double-check your own learning if you're doing that course.

# How it works

Because it's just a demonstration, it's not an *actual* heat sensor. As it stands, it's literally just a script that will toggle an LED depending on the value gathered from the potentiometer, rounded to a scale of 0-100, simulating a temperature sensor you might see on electrical equipment. **Blue** represents cold, **Green** represents a value within an acceptable heat, and **Red** represents critical heat.

That said, I may eventually use this as a framework for a future project involving actual heat sensors. For now, though, it's just meant to be a demonstration of what I'm learning.

## Important

Make sure you double-check the `pot_pin` and LED variables and either match your circuit to the pins I used, or modify the variables to suit your circuit design. If you'd like to see how I set up my breadboard (with some minor changes for the diagram), I created a [sketch](https://wokwi.com/projects/464420391627103233) on my Wokwi account to review.