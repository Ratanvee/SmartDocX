[Setup]
AppName=SmartDocX
AppVersion=1.0
DefaultDirName={pf}\SmartDocX
OutputDir=output
OutputBaseFilename=SmartDocXSetup

[Files]
Source: "printer-agent\printer_agent.exe"; DestDir: "{app}\printer-agent"; Flags: ignoreversion
Source: "printer-agent\config.json"; DestDir: "{app}\printer-agent"; Flags: ignoreversion
Source: "launcher\start_smartdocx.exe"; DestDir: "{app}\launcher"; Flags: ignoreversion
Source: "launcher\smartdocx.ico"; DestDir: "{app}\launcher"; Flags: ignoreversion  

[Icons]
; Desktop shortcut
Name: "{userdesktop}\SmartDocX"; Filename: "{app}\launcher\start_smartdocx.exe"; WorkingDir: "{app}\launcher"; IconFilename: "{app}\launcher\smartdocx.ico"

; Start Menu shortcut
Name: "{group}\SmartDocX"; Filename: "{app}\launcher\start_smartdocx.exe"; WorkingDir: "{app}\launcher"; IconFilename: "{app}\launcher\smartdocx.ico"

; Auto-run printer agent at startup
Name: "{userstartup}\SmartDocX Agent"; Filename: "{app}\printer-agent\printer_agent.exe"

[Run]
Filename: "{app}\launcher\start_smartdocx.exe"; Flags: nowait postinstall skipifsilent
