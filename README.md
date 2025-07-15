## Robot Package Template

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `my_bot` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).

Works cited:

1. https://github.com/joshnewans/my_bot/
2. https://www.youtube.com/watch?v=OWeLUSzxMsw&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=1 (Video 1 of 23)
3. https://www.youtube.com/watch?v=OWeLUSzxMsw&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=2 (Video 2 of 23)
4. https://github.com/joshnewans/articubot_one/blob/d5aa5e9bc9039073c0d8fd7fe426e170be79c087/description/inertial_macros.xacro
5. https://www.youtube.com/watch?v=IjFcr5r0nMs&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=3 (Video 3 of 23)
6. https://github.com/joshnewans/articubot_one/blob/adb08202d3dafeeaf8a3691ddd64aa8551c40f78/launch/launch_sim.launch.py
7. https://www.youtube.com/watch?v=RAqFgU3Gfv0&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=4 (Video 4 of 23)
8. https://www.youtube.com/watch?v=Iye4uVLmj8o&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=5 (Video 5 of 23)
9. https://www.youtube.com/watch?v=_FGYVgAti9M&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=6 (Video 6 of 23)
10. https://www.youtube.com/watch?v=-PCuDnpgiew&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=7 (Video 7 of 23)
11. https://www.youtube.com/watch?v=eJZXRncGaGM&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=8 (Video 8 of 23)
12. https://github.com/joshnewans/articubot_one/blob/545acac87ae215d80ef6b28abe6097eb7281d9ff/description/lidar.xacro
13. https://github.com/joshnewans/articubot_one/blob/545acac87ae215d80ef6b28abe6097eb7281d9ff/launch/rplidar.launch.py 
14. https://www.youtube.com/watch?v=A3nw2M47K50&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=9 (Video 9 of 23)
15. https://www.youtube.com/watch?v=T9xZ22i9-Ys&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=10 (Video 10 of 23)
16. https://www.youtube.com/watch?v=RjhBRn6lDSM&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=11 (Video 11 of 23)
17. https://www.youtube.com/watch?v=4QKsDf1c4hc&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=12 (Video 12 of 23)
18. https://www.youtube.com/watch?v=8ByoP_oSdno&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=13 (Video 13 of 23)
19. https://github.com/joshnewans/articubot_one/blob/bf28006638f36d290c991ffec433e6c326120d41/description/robot_core.xacro
20. https://www.youtube.com/watch?v=4VVrTCnxvSw&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=14 (Video 14 of 23)
21. https://www.youtube.com/watch?v=F5XlNiCKbrY&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=15 (Video 15 of 23)
22. https://www.youtube.com/watch?v=hkkG-Sgi9Sk&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=16 (Video 16 of 23) - Introduces mobile control
23. https://www.youtube.com/watch?v=ZaiA3hWaRzE&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=17 (Video 17 of 23)
24. https://www.youtube.com/watch?v=jkoGkAd0GYk&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=18 (Video 18 of 23)
25. https://www.youtube.com/watch?v=lI2bLPDHEmQ&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=19 (Video 19 of 23)
26. https://www.youtube.com/watch?v=gISSSbYUZag&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=20 (Video 20 of 23) - Not implemented
27. https://www.youtube.com/watch?v=J02jEKawE5U&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=21 (Video 21 of 23) - Not used
28. https://www.youtube.com/watch?v=qoj5_fVBPII&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=22 (Video 22 of 23) - Not used
29. https://www.youtube.com/watch?v=fH4gkIFZ6W8&list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&index=23 (Video 23 of 23) - Not used

It seems to be that videos 1 to 19 introduce the initial programming. The last four videos show how to upgrade the works. Thus,  will take what is present to the lab and work from there.