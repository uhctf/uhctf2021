1. Follow the steps of the Android guidelines to decompile the apk.
2. Notice that the application is created using Unity and that exported project is a Unity project.
4. Find the project source code dll (by Unity standards, this is a file called Assembly-CSharp.dll).
3. Decompile assets/bin/Data/Managed/Assembly-CSharp.dll with a tool like [dnSpy](https://github.com/dnSpy/dnSpy) that allows you to make edits.
4. Notice the BossController sends client-side damage values to a server that keeps all the health values.
5. The health of the boss is by default MAX_INT and the server checks if the damage exceeds a certain threshold, however the server does not check if the damage is below 0. HP - (- damage) will turn into HP + damage, which will cause an integer overflow to kill the boss.
6. Make the damage value sent to the server negative and save it into the dll with "Save All" in dnSpy.
7. Use the steps of the Android tutorial to recompile and export the apk. 
8. Install the apk on Android, after hitting the boss once you will have defeated it!
9. This will reveal a dialog with the flag _uhctf{buzz-lightyear-come-in-peace-7ubq}_