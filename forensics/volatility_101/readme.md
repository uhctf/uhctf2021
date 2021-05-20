# Volatility 101

Creator: [Reinaert Van de Cruys](https://github.com/reinaertvdc)

Flag format: **custom**

## Description
<p>This challenge is a crash course in Volatility, a powerful framework for analyzing memory dumps from various OS's. Volatility is included in Kali Linux, it can be installed from the built-in repositories on most Linux distributions, and it can be downloaded for Mac and Windows from the <a href="https://www.volatilityfoundation.org/releases">official site</a>.</p>
<p>An employee accidentally downloaded and executed a stealthy virus on a company workstation. The stealthy virus resides entirely in memory and hides by injecting itself into existing programs. Luckily, the workstation was running in a virtualized environment, as many companies use nowadays, and so a memory dump could be created as the machine was taken offline. Volatility to the rescue!</p>
<p>Running <kbd>volatility -h</kbd> will list all the "Supported Plugin Commands". A small selection:
  <ul>
    <li>Processes:
      <ul>
        <li><code>dlldump</code>: Dump DLLs from a process address space</li>
        <li><code>dlllist</code>: Print list of loaded dlls for each process</li>
        <li><code>malfind</code>: Find hidden and injected code</li>
        <li><code>procdump</code>: Dump a process to an executable file sample</li>
        <li><code>pslist</code>: Print all running processes by following the EPROCESS lists</li>
        <li><code>psscan</code>: Pool scanner for process objects</li>
        <li><code>pstree</code>: Print process list as a tree</li>
        <li><code>psxview</code>: Find hidden processes with various process listings</li>
      </ul>
    </li>
    <li>Files:
      <ul>
        <li><code>dumpfiles</code>: Extract memory mapped and cached files</li>
        <li><code>filescan</code>: Pool scanner for file objects</li>
      </ul>
    </li>
    <li>Network connections:
      <ul>
        <li><code>netscan</code>: Find TCP/UDP endpoints and listeners</li>
      </ul>
    </li>
    <li>Miscellaneous:
      <ul>
        <li><code>clipboard</code>: Extract the contents of the windows clipboard</li>
        <li><code>cmdscan</code>: Extract command history by scanning for _COMMAND_HISTORY</li>
        <li><code>hashdump</code>: Dumps passwords hashes (LM/NTLM) from memory</li>
        <li><code>iehistory</code>: Reconstruct Internet Explorer cache / history</li>
        <li><code>imageinfo</code>: Identify information for the image</li>
        <li><code>notepad</code>: List currently displayed notepad text</li>
        <li><code>screenshot</code>: Save a pseudo-screenshot based on GDI windows</li>
      </ul>
    </li>
  </ul>
</p>
<p>Your first step is to identify the profile of the memory dump, which tells Volatility what OS the dump is from an how to read it. We do this using the <code>imageinfo</code> plugin:
  <pre>volatility -f memory.dmp imageinfo</pre>
</p>
<p>In this case, Volatility will fail to suggest the correct profile, but luckily, we know that the workstation was a <strong>Windows 7 SP1 x64</strong> machine. The correct profile for this OS is, unsurprisingly, <code>Win7SP1x64</code>. If you are interested, find a full list of Windows profiles <a href="https://github.com/volatilityfoundation/volatility/wiki/2.6-Win-Profiles">here</a>.</p>
<p>Each subsequent command will be of the form <code>volatility -f memory.dmp --profile=Win7SP1x64 &lt;COMMAND&gt;</code>. This is because each command will need to know the dump file to analze and the profile describing how the data is structured.</p>
<p>We know the workstation got infected through a malicious file downloaded by a user. In Windows, this means the virus process will have spawned as a direct descendant of the <code>explorer.exe</code> process. Using the <code>pstree</code> plugin, we can find this process:
  <pre>volatility -f memory.dmp --profile=Win7SP1x64 pstree</pre>
</p>
<p>You should see 3 direct descendants of <code>explorer.exe</code>. One of these must have contained the virus. We know a user downloaded the virus, so we expect the culprit to be located in the user's personal directory, while the two innocent processes will be located in system directories. Find the location of each executable:
  <pre>volatility -f memory.dmp --profile=Win7SP1x64 filescan | grep &lt;FILENAME&gt;</pre>
</p>
<p>Yes! Now we know which process is almost certainly the culprit! Using the PID from the <code>pstree</code> output, it's now a piece of cake to extract the executable for further analysis:
  <pre>volatility -f memory.dmp --profile=Win7SP1x64 procdump --dump-dir=./ --pid=&lt;PID&gt;</pre>
</p>
<p>Oh no! The executable is no longer in memory, because the process is no longer active, as we can see from the <code>pstree</code> output. We know the virus is capable of injecting itself into other processes, so it must be living on somewhere else in the process tree, but without the original process, we have no way of telling where exactly. Very clever&hellip; Time for a new approach.</p>
<p>The <code>malfind</code> plugin will scan all processes in memory for suspicious pieces of code that might have been injected:
  <pre>volatility -f memory.dmp --profile=Win7SP1x64 malfind</pre>
</p>
<p>Whoa, no need for us to dive into the assembler code so fast! Let's take a step back and just look at the names of the suspect processes:
  <pre>volatility -f memory.dmp --profile=Win7SP1x64 malfind | grep "Process:"</pre>
</p>
<p>You should find 4 suspect processes, some with multiple pieces of suspicious code. Note the process names and PIDs. For each process, we can extract all suspicious sections and zip them together, using a Kung-Fu one-liner:
  <pre>volatility -f memory.dmp --profile=Win7SP1x64 malfind --dump-dir=./ --pid=&lt;pid&gt; && zip &lt;name&gt;.zip process.0x*.0x*.dmp && rm process.0x*.0x*.dmp</pre>
</p>
<p>We zip the sections together per process for convenience, so we can scan them all at once on <a href="https://www.virustotal.com/gui/home/upload">VirusTotal</a>. They will tell us which process really is infected and with what virus. Upload each of the zip files and check the results.</p>
<p>Once you found the infected process, you'll notice how many AVs didn't pick up the virus! You'll also see that the output from VirusTotal isn't always easy to read. Each antivirus company has its own naming scheme. Luckily, the virus' common name should be mentioned in the output from ClamAV, DrWeb and Microsoft, among others.</p>
<p>You now have only one task left to complete: find out who is controlling the virus by checking where it is calling home to. The <code>netscan</code> plugin should be all you need. Note the IP address and port of the remote server.</p>
<p>The flag is as follows, all lowercase:
  <pre>&lt;ORIGINAL_PROCESS_NAME&gt;-&lt;INJECTED_PROCESS_NAME&gt;-&lt;VIRUS_NAME&gt;-&lt;REMOTE_SOCKET&gt;</pre>
</p>
<p>For example:
  <pre>funny.exe-winword.exe-conficker-172.16.1.22:8080</pre>
</p>

## Attachments
* [memory.7z](https://drive.google.com/open?id=189-inBrLDzG3Y5WxJu6P4P0-ZdNIo6L1), the memory dump of the infected workstation. It must first be unzipped to <code>memory.dmp</code> e.g. using <a href="https://www.7-zip.org/">7-Zip</a>.