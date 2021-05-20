
<h1 id="name">A Print Of My Finger</h1>

<span>Creator: Mariano <a id="creator"></a>
</span>

<section id="description">
  <h2>Description</h2>
  <p>The recent increase in ransomware attacks has lead to a company creating a website (https://www.marianodimartino.com/uhctf/fp/index.html) that generates oldschool ransom note effects. This website allows criminals to write secret messages by sharing URls with each other. Although we got a hold on one of the secret messages being sent through 'secret.html' (captured_secret.pcapng), there is unfortunately no way to decrypt the HTTPS traffic!
<p>
Can you infer the secret message that was sent? </p>
Note: The flag is the actual secret message being sent. There are no hidden flags in the images or HTML files and it does not use any steganograhpy.
</p>
</section>

<section id="attachments">
  <h2>Attachments</h2>
  <ul id="attachments-list">
    <li><a href="captured_secret.pcapng">captured_secret.pcapng</a></li>
  </ul>
</section>

<section id="hints">
  <h2>Hints</h2>
  <ul id="hints-list">
    <li><details><summary></summary>Application Data records are always very interesting.</details></li>
    <li><details><summary></summary>All the image characters look very different in size.</details></li>
  </ul>
</section>

<section id="setup">
  <h2>Setup</h2>
  <details id="setup-description"><summary></summary>
    <p>%SETUP_PARAGRAPH_1%</p>
    <p>%SETUP_PARAGRAPH_2%</p>
  </details>
</section>

<section id="creation">
  <h2>Creation</h2>
  <details id="creation-description"><summary></summary>
    <p>%CREATION_PARAGRAPH_1%</p>
    <p>%CREATION_PARAGRAPH_2%</p>
  </details>
</section>

<section id="solution">
  <h2>Solution</h2>
  <details id="solution-description"><summary></summary>
    <p>Flag: hollywoodx</p>
    <p>Simple fingerprinting on TLS application data records. Summing the sizes of these records will give a rough estimate of each image character.</p>
  </details>
</section>






