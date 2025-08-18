@echo off

set "origem=%~dp0"
set "destino=C:\Windows\SysWOW64"

copy "%origem%\capicom.dll" "%destino%" /y
copy "%origem%\msxml5.dll" "%destino%" /y
copy "%origem%\msxml5r.dll" "%destino%" /y

regsvr32 %destino%\capicom.dll /s
regsvr32 %destino%\msxml5.dll /s

cls
echo Arquivos copiados e registrados com sucesso!
pause