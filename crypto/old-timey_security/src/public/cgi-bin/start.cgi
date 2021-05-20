<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO8859-1">
<meta http-equiv="Content-Script-Type" content="text/javascript">
<meta http-equiv="Content-Style-Type" content="text/css">
<meta http-equiv="Pragma" content="no-cache">
<title>Login</title>
<!-- AS60_ERR="99" -->
<style type="text/css">
<!--
.title		{font-size:12px;	color:#FFFFFF;}
.sdate		{font-size:12px;	color:#FFFFFF;}
.sdateB		{font-size:12px;	color:#000000;}
.ldate		{font-size:16px;	color:#FFFFFF;}
.stext		{font-size:12px;	color:#FFFFFF;}
.stextB		{font-size:12px;	color:#000000;}
.mtext		{font-size:14px;	color:#FFFFFF;}
.mtextB		{font-size:14px;	color:#000000;	line-height:110%;}
.ltext		{font-size:16px;	color:#FFFFFF;	line-height:110%;}
.ltextBred	{font-size:16px;	color:#FF0000;	line-height:110%;}
.tablebase	{background-color:#2E4F82;	width:415px;}
.gif_b {cursor:default; text-decoration: none;}
-->
</style>
<script type="text/javascript">
<!--
var LANGPERS = "02";
/* --- private --- */
function Login()
{
	var Ret = true;

	if((document.all("txtUser").value).length > 0)
	{
		if(document.all("txtPassword").value != "")
		{
			Ret = CheckComValue(document.all("txtPassword").value);
		}

		if(CheckComValue(document.all("txtUser").value) && (Ret != false))
		{
			var strKey = "139867";
			var strUser = Encryption(document.all("txtUser").value, strKey, 32);
			var strPass = Encryption(document.all("txtPassword").value, strKey, 32);

			var strURL = "./ulogin.cgi?USER=" + strUser + "&PASS=" + strPass + "&KEY=" + strKey + RetTempParam();
			window.open(strURL, "_self", "menubar=no,status=yes,width=1024,height=768,left=0,top=0");

			document.all("txtUser").value = "";
			document.all("txtPassword").value = "";
		}
		else
		{
//			alert("���[�U�[���ƃp�X���[�h�͔��p�p����������͂��Ă��������B");
			alert( document.all("ldlg351").value );
		}
	}
}

function RetTempParam()
{
	var cdtNow = new Date();
	var strRet = "&TEMP=" + cdtNow.getTime();

	return strRet;
}

function CheckComValue(strParam)
{
	var strBaseChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

	var bRet = true;
	var iParamLen = strParam.length;

	for (var iIndex = 0; iIndex < iParamLen; iIndex++)
	{
		if (strBaseChar.indexOf(strParam.charAt(iIndex)) == -1)
		{
			bRet = false;
			break;
		}
	}

	return bRet;
}

function Encryption(strInput, strKey, iSize)
{
	var strCode	= new Array;

	for (i=0 ;i < iSize ;i++)
	{
		if (i < strInput.length)
		{
			asciiCode = strInput.charCodeAt(i);
		}
		else
		{

			asciiCode = 0;
		}

		if (i != 0 )
		{
			asciiCode ^= maskCode;
		}

		for (j=0 ;j < (strKey.length) ;j++)
		{
			asciiKey = strKey.charCodeAt(j);
			asciiCode = (asciiCode ^ asciiKey) - asciiKey;
		}
		maskCode = asciiCode & 0xFF;
		hexCode = maskCode.toString(16);

		if (maskCode < 16)
		{
			strCode += "0";
		}
		strCode += String(hexCode);
	}

	return strCode;
}

function mdown(e)
{
	var Mac = navigator.userAgent.indexOf("Mac") != -1 ? true : false;
	if (navigator.appName == "Microsoft Internet Explorer")
	{
		if (event.button == 2 || (Mac && (event.ctrlKey || event.keyCode == 91)))
		{
			return false;
		}
	}
	else if (navigator.appName == "Netscape")
	{
		if (e.which == 3 || e.modifiers == 2 || e.ctrlKey)
		{
			return false;
		}
	}
}

if (document.all)
{
	document.onmousedown = mdown;
	document.onkeydown = mdown;
}
else if (document.layers)
{
	window.captureEvents(Event.MOUSEDOWN | Event.modifiers | Event.KEYDOWN);
	window.onmousedown = mdown;
	window.onkeydown = mdown;
}
else if (navigator.userAgent.indexOf("Netscape6")!=-1)
{
	document.onmouseup = mdown;
	document.onkeydown = mdown;
}

function RecordChange()
{
	NdrDatabase.recordset.MoveFirst();
	NdrDatabase.recordset.Move(LANGPERS);
	NdrDatabase2.recordset.MoveFirst();
	NdrDatabase2.recordset.Move(LANGPERS);
	document.all("spnUser").innerText = document.all("lcmn255").value;
	document.all("spnPass").innerText = document.all("lcmn256").value;
	document.all("cmdLogin").value    = document.all("lcmn236").value;
	document.all("txtUser").value     = "";
}

function LogoChange()
{
	with(document)
	{
		if("J" == "G")
		{
//			all("logo").src = "../b_tittle_DGND400.gif";
//			all("logo").alt = "Network Disk Recorder DG-ND400";
			all("logo").src = "../b_tittle_DGNV200.gif";
			all("logo").alt = "Network Disk Recorder DG-NV200";
		}
		else
		{
//			all("logo").src = "../b_tittle_WJND400.gif";
//			all("logo").alt = "Network Disk Recorder WJ-ND400";
			all("logo").src = "../b_tittle_WJNV200.gif";
			all("logo").alt = "Network Disk Recorder WJ-NV200";
		}
	}
}

function Constructor()
{
	try{
		RecordChange();
	}catch(e){
	}
	LogoChange();
}

function Nop(){}

//-->
</script>
</head>

<body background="/0_bg_02.gif" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onload="Constructor(); txtUser.focus();" oncontextmenu="return false">
<object id="NdrDatabase" classid="CLSID:333C7BC4-460F-11D0-BC04-0080C7055A83">
<param name="DataURL" 	value="../Lcmn.csv">
<param name="UseHeader" value="true">
<param name="CharSet" value="UTF-8">
</object>
<object id="NdrDatabase2" classid="CLSID:333C7BC4-460F-11D0-BC04-0080C7055A83">
<param name="DataURL" 	value="../Ldlg.csv">
<param name="UseHeader" value="true">
<param name="CharSet" value="UTF-8">
</object>
<table width="100%" border="0" cellspacing="0" cellpadding="2">
	<tr>
		<td background="/3_bg_01.gif" colspan="2">
			<a href="javascript:Nop();" class="gif_b" onfocus="this.blur()">
			<img id="logo" src="/spacer.gif" alt="" border="0">
		</td>
	</tr>
	<tr>
		<td><img src="/spacer.gif" width="*" height="10"></td>
	</tr>
	<tr>
		<td width="50%" align="right" class="title">
			<!--	���[�U�[��	-->
			<nobr><span id="spnUser"></span></nobr>
		</td>
		<td>
			&nbsp;<input name="txtUser" id="txtUser" style="width=30%" maxlength="14" placeholder="Username"></input>
		</td>
	</tr>
	<tr>
		<td width="50%" align="right" class="title">
			<!--	�p�X���[�h	-->
			<nobr><span id="spnPass"></span></nobr>
		</td>
		<td>
			&nbsp;<input type="password" name="txtPassword" id="txtPassword" style="width=30%" maxlength="8" autocomplete="off" placeholder="Password"></input>
		</td>
	</tr>
	<tr>
		<td colspan="2"><hr></td>
	</tr>
	<tr>
		<td colspan="2" align="center">
			<input type="submit" name="cmdLogin" id="cmdLogin" value="Login" onClick="Login();"></input>
		</td>
	</tr>

</table>
<input type="hidden" name="ldlg351" DATASRC="#NdrDatabase2" DATAFLD="ldlg351"></input>
<input type="hidden" name="lcmn236" DATASRC="#NdrDatabase"  DATAFLD="lcmn236"></input>
<input type="hidden" name="lcmn255" DATASRC="#NdrDatabase"  DATAFLD="lcmn255"></input>
<input type="hidden" name="lcmn256" DATASRC="#NdrDatabase"  DATAFLD="lcmn256"></input>
</body>
</html>
