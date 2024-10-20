@echo off
goto START_APP

:START_APP
cls
echo Welcome to VJDY Official Music Store!
echo This app let's you download music, sound effects and more!
echo Are you ready? (Y/N)
set /p userInput=Enter:

set userInput=%userInput:~0,1%
set userInput=%userInput:Y=a%
set userInput=%userInput:N=n%

if /I "%userInput%"=="Y" goto CONSOLE
if /I "%userInput%"=="N" goto EXIT_APP

:CONSOLE
cls
echo Choose Server to access: vjdyofficial, deloraxpower-music
set /p serverTag=Enter the server tag: 
setx SERVER_TAG "%serverTag%"
echo The server tag is accessed to: %serverTag%.
pause

cls
echo If you don't know about the tag names of release tag, see 
echo https://github.com/vjdyofficial/MusicStore/blob/main/servertabs_%serverTag%.csv
echo for DeLora X Power Server
set /p releaseTag=Enter the Release Tag to get: 
setx RELEASE_TAG "%releaseTag%"
echo Release tag is set to: %releaseTag%.
pause

cls
echo see https://github.com/vjdyofficial/MusicStore/tree/main/ContentLists_%SERVER_TAG%
echo If you choose the specific tag on %releaseTag%,
set /p linkName=Enter the Link string to download: 
setx LINK_NAME "%linkName%"
echo Link name set to: %linkName%
pause
goto INFO_DOWNLOAD

:INFO_DOWNLOAD
cls
echo Information before to download
if /I "%releaseTag%"=="packages" (
    set fileFormat=zip
    echo Detected file format is compressed archive "(Format: zip, Mimetype: application/zip)"
) else (
    set fileFormat=mp3
    echo Detected file format is audio file "(Format: mp3, Mimetype: audio/mpeg)"
)
set "contentURL=https://github.com/vjdyofficial/%serverTag%/releases/download/%releaseTag%/%linkName%.%fileFormat%"
set "folderDir=%userprofile%\Documents\VJDY Official Music Store\%releaseTag%"
set "toFile=%userprofile%\Documents\VJDY Official Music Store\%releaseTag%\%linkName%.%fileFormat%"

echo Content URL: %contentURL%
echo File Destination: %folderDir%
echo File Destination: %toFile%

echo Are you ready to download?
pause
goto DOWNLOAD_CONTENT

:DOWNLOAD_CONTENT
cls
set folderPath=%folderDir%

:: Check if the folder already exists
if exist "%folderPath%" (
    echo Folder already exists at %folderPath%.
) else (
    :: Create the folder if it doesn't exist
    mkdir "%folderPath%"
    echo Folder created at %folderPath%.
)
powershell -Command "Invoke-WebRequest -Uri '%contentURL%' -OutFile '%toFile%'"
goto END

:END
REM Check if the file exists
if exist "%toFile%" (
    start "" "%toFile%"
    echo Downloaded successfully!
) else (
    echo An error occured while downloading the file. The message is at the red text color.
)
echo Do you want to download more? (Y/N)
set /p userInput=Enter: 

set userInput=%userInput:~0,1%
set userInput=%userInput:Y=y%
set userInput=%userInput:N=n%

if /I "%userInput%"=="Y" goto CONSOLE
if /I "%userInput%"=="N" goto EXIT_APP

:EXIT_APP
exit