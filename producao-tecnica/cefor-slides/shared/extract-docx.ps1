Add-Type -AssemblyName System.IO.Compression.FileSystem

$zipPath = "An Experience with an Educational Chatbot-paper.docx"
$zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
$entry = $zip.Entries | Where-Object { $_.FullName -eq 'word/document.xml' }
$reader = New-Object System.IO.StreamReader($entry.Open())
$xml = $reader.ReadToEnd()
$reader.Close()
$zip.Dispose()

$text = $xml -replace '<[^>]+>', ' '
$text = $text -replace '&amp;', '&'
$text = $text -replace '&lt;', '<'
$text = $text -replace '&gt;', '>'
$text = $text -replace '\s+', ' '

$lines = $text -split '\.'
$lines | Where-Object { $_.Trim().Length -gt 20 } | Select-Object -First 80 | ForEach-Object { $_.Trim() }
