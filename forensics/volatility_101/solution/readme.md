<ol>
  <li>
    <p>Display the process tree:</p>
    <pre>volatility -f memory.dmp --profile=Win7SP1x64 pstree</pre>
    <p>This reveals 3 direct descendants of <code>explorer.exe</code>:</p>
    <ul>
    <li><code>notepad.exe</code> with PID <code>1312</code></li>
    <li><code>iexplore.exe</code> with PID <code>1644</code></li>
    <li><code>svcexplore.exe</code> with PID <code>1636</code></li>
    </ul>
  </li>
  <li>
    <p>Check the file location of each process:</p>
    <pre>volatility -f memory.dmp --profile=Win7SP1x64 filescan | grep notepad.exe<br></br>volatility -f memory.dmp --profile=Win7SP1x64 filescan | grep iexplore.exe<br></br>volatility -f memory.dmp --profile=Win7SP1x64 filescan | grep svcexplore.exe</pre>
    <p>This reveals that the location of <code>svcexplore.exe</code> is <code>\Device\HarddiskVolume1\Users\Walter\Desktop\svcexplore.exe</code>, while the other two are located in system directories, therefore <code>svcexplore.exe</code> is likely the culprit.</p>
  </li>
  <li>
    <p>List the suspect processes:</p>
    <pre>volatility -f memory.dmp --profile=Win7SP1x64 malfind | grep "Process:"</pre>
    <p>This reveals 4 suspects:</p>
    <ul>
      <li><code>csrss.exe</code> with PID <code>328</code></li>
      <li><code>explorer.exe</code> with PID <code>1740</code></li>
      <li><code>svchost.exe</code> with PID <code>1428</code></li>
      <li><code>iexplore.exe</code> with PID <code>1644</code></li>
    </ul>
  </li>
  <li>
    <p>Bundle the suspect pieces of code per process:</p>
    <pre>volatility -f memory.dmp --profile=Win7SP1x64 malfind --dump-dir=./ --pid=328 && zip csrss.zip process.0x*.0x*.dmp && rm process.0x*.0x*.dmp<br></br>volatility -f memory.dmp --profile=Win7SP1x64 malfind --dump-dir=./ --pid=1740 && zip explorer.zip process.0x*.0x*.dmp && rm process.0x*.0x*.dmp<br></br>volatility -f memory.dmp --profile=Win7SP1x64 malfind --dump-dir=./ --pid=1428 && zip svchost.zip process.0x*.0x*.dmp && rm process.0x*.0x*.dmp<br></br>volatility -f memory.dmp --profile=Win7SP1x64 malfind --dump-dir=./ --pid=1644 && zip iexplore.zip process.0x*.0x*.dmp && rm process.0x*.0x*.dmp</pre>
    <p>Upload each of them to <a href="https://www.virustotal.com/gui/home/upload">VirusTotal</a>. Only <code>csrss.zip</code> should be detected as containing malware, with identifications including:</p>
    <ul>
      <li><code>Win.Tool.MeterPreter-6294292-0</code></li>
      <li><code>BackDoor.Meterpreter.35</code></li>
      <li><code>HackTool:Win32/Meterpreter.C</code></li>
    </ul>
    <p>We can therefore conclude that <code>csrss.exe</code> is the (only) culprit and that we are dealing with the <code>Meterpreter</code> virus.</p>
  </li>
  <li>
    <p>Perform the network scan:</p>
    <pre>volatility -f memory.dmp --profile=Win7SP1x64 netscan</pre>
    <p>This reveals only one established connection to <code>192.168.1.62:443</code>, which is also the only one owned by <code>svcexplore.exe</code>. <code>csrss.exe</code> does not appear in the output. We can therefore conclude that the virus is controlled from <code>192.168.1.62:443</code>.</p>
  </li>
  <li>
    <p>We learned the following:</p>
    <ul>
      <li>The original process was <code>svcexplore.exe</code></li>
      <li>The injected process is <code>csrss.exe</code></li>
      <li>The name of the virus is <code>Meterpreter</code></li>
      <li>The remote socket controlling the virus is <code>192.168.1.62:443</code></li>
    </ul>
    <p>From this knowledge, we can construct the flag according to the challenge description.</p>
  </li>
</ol>