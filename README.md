# python-long-weekends
A simple python library to spot holiday "bridges" and long weekends.
In Italy, when a public holiday falls on a Tuesday or a Thursday, 
people typically take Monday or Friday off work to enjoy long vacations
and call those days "ponti" ("bridges").
To the best of my knowledge, there is no English translation for this term 
apart from a generic "long weekend".

This library spots single working days that are preceded
and followed by a weekend and/or a public holiday, and classifies them as "bridges". 
Based on the identified "bridges", this library also labels "long weekends", 
here defined as a series of 3 or more days that are either weekend, 
holidays, or holiday "bridges".

This library is intended to help generate informative features for 
energy consumption prediction models. 

Inspired by https://stackoverflow.com/a/57865434/7059626 (thank you @jezrael).
