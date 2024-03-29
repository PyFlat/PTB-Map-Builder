; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "PTB Map Builder"
#define MyAppVersion "2.0.0"
#define MyAppPublisher "PyFlat Studios"
#define MyAppURL "https://github.com/PyFlat/PTB-Map-Builder"
#define MyAppExeName "main.exe"
#define MyAppAssocName "Plant The Bomb File"
#define MyAppAssocExt ".ptb"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt
[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{8F17C25E-6636-42E0-BE70-C84EE1CC7BDE}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
ChangesAssociations=yes
DisableProgramGroupPage=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build
OutputBaseFilename=win_installer_v{#MyAppVersion}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
LicenseFile=C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\LICENSE
SignTool=signtool
SignedUninstaller=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[InstallDelete]
Type: filesandordirs; Name: "{app}\textures"

[Files]
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\icons\*"; DestDir: "{app}\icons"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\textures\*"; DestDir: "{app}\textures"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\api-ms-win-core-console-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\api-ms-win-core-fibers-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\api-ms-win-eventing-provider-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\frozen_application_license.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\python311.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\PTB-Map-Builder\build\exe.win-amd64-3.11\style.qss"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

