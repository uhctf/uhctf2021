<ol>
  <li>
      <p>First step is to discover that the soundfile contains binary blips. This can be done via:</p>
      <ul>
        <li>Listening to the audio itself</li>
        <li>Opening the file in any audio editor with waveform visualisations (e.g., audacity)</li>
      </ul>
  </li>
  <li>
    <p>Second step is to extract the binary blips. Multiple solution paths exist for this:</p>
    <ul>
      <li>Manual extraction (labour intensive)</li>
      <li>Python wave module</li>
      <li>Python numpy module (The file is sampled at 44100 Hz)</li>
    </ul>
    <p>When code is used to extract the binary sequence, there are various ways one could differentiate between the low and high amplitude blips:</p>
    <ul>
      <li>Read raw values and use a threshold to differentiate between low (=0) and high (=1)</li>
      <li>Calculate the mean average of 44100 samples and use a threshold to differentiate</li>
      <li>Parse some samples, keep track of the maximum value untill one reaches the 'no sound' part and use a threshold to differentiate between low and high amplitude</li>
    </ul>
  </li>
  <li>
    <p>Last step is to correctly interpret the message. If everything went correctly, one should find 1679 bits. 1679 is a semiprime number that can be created by multiplying 23 by 79.</p>
    <p>By googling "semiprime" with "space" or "semiprimes" by itself (or other similar combinations), one shall quickly be led towards wikipedia talking about "semiprime numbers" or the "arecibo message".</p>
    <p>If 1679 is googled with "space", one shall quickly find the "arecibo message". The Arecibo message is a 79x23 bitmap that represents an image containing info for extraterrestrial beings. Our solution uses a 23x79 bitmap.</p>
    <p>When the 1s and 0s are mapped onto a 23x79 bitmap (Excel sheet with coloring, Numpy bitmap, printing X vs nothing in the CLI, ...), one shall find the flag drawn.</p>
  </li>
</ol>