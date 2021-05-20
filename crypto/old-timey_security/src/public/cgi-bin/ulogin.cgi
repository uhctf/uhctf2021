<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO8859-1">
<meta http-equiv="Content-Script-Type" content="text/javascript">
<meta http-equiv="Pragma" content="no-cache">
<title>Login error</title>

<style type="text/css">
<!--
.texterr {font-size: 16px;color: #FF0000;text-align: center;font-weight: bold;}
.texts {font-size: 12px;color: #FFFFFF;text-align: center;}
.gif_b {cursor:default; text-decoration: none;}
-->
</style>
<script type="text/javascript">
<!--
var AS60_ERR="02";
var LANGPERS = "02";
var iButton = 0;

function DispString()
{
	if("02" != "04")
	{
		if ("01" == "01")
		{
//			document.write("<tr><td class=\"texts\" >���������O�C������ɂ̓{�^�����N���b�N���Ă��������B</td></tr>");
//			document.write("<tr><td class=\"texts\" ><input type=\"button\" value=\"Back\" onClick=\"history.back()\"></td></tr>");
				document.write("<tr><td class=\"texts\" ><span DATASRC=\"#NdrDatabase\" DATAFLD=\"lblw39\"></span></td></tr>");
				document.write("<tr><td class=\"texts\" ><input type=\"button\" name=\"login\" value=\"Back\" onClick=\"history.back()\"></td></tr>");
				iButton = 1;
		}
	}
}

function LoginErrorString()
{
	if("02" != "16")
	{
		// <td class="texterr">���O�C���ł��܂���B</td>
		document.write( "<td class=\"texterr\"><span DATASRC=\"#NdrDatabase2\" DATAFLD=\"lhbl27\">Incorrect username or password.</span></td>" );
	}
	else
	{
		// <td class="texterr">��Q(��d���o)���������܂����B<br>���O�C���ł��܂���B</td>
		document.write( "<td class=\"texterr\"><span DATASRC=\"#NdrDatabase\" DATAFLD=\"set41\"></span><br><span DATASRC=\"#NdrDatabase2\" DATAFLD=\"lhbl27\"></span></td>" );
	}
}

function RecordChange()
{
	NdrDatabase.recordset.MoveFirst();
	NdrDatabase.recordset.Move(LANGPERS);
	NdrDatabase2.recordset.MoveFirst();
	NdrDatabase2.recordset.Move(LANGPERS);

	if( 1 == iButton ){
		document.all("login").value = document.all("lblw36").value;
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

function Nop(){}

//-->
</script>
</head>

<body background="../0_bg_02.gif" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onload="Constructor();" oncontextmenu="return false">
<!-- 050407 CMS�� add-start NDR������Ή� -->
<object id="NdrDatabase" classid="CLSID:333C7BC4-460F-11D0-BC04-0080C7055A83">
<param name="DataURL" 	value="../Lblw.csv">
<param name="UseHeader" value="true">
<param name="CharSet" value="UTF-8">
</object>
<object id="NdrDatabase2" classid="CLSID:333C7BC4-460F-11D0-BC04-0080C7055A83">
<param name="DataURL" 	value="../Lhbl.csv">
<param name="UseHeader" value="true">
<param name="CharSet" value="UTF-8">
</object>
<!-- 050407 CMS�� add-end NDR������Ή� -->
<table width="100%" border="0" cellspacing="0" cellpadding="2">
	<tr>
		<td background="../3_bg_01.gif">
			<a href="javascript:Nop();" class="gif_b" onfocus="this.blur()">
			<img id="logo" src="../spacer.gif" alt="" border="0">
		</td>
	</tr>
	<tr>
		<td><img src="../spacer.gif" width="*" height="50"></td>
	</tr>
	<tr>
	<script type="text/javascript">
	<!--
		LoginErrorString( );
	-->
	</script>
	</tr>
	<tr>
		<td><img src="../spacer.gif" width="*" height="50"></td>
	</tr>
	<script type="text/javascript">
	<!--
		DispString( );
	-->
	</script>
</table>
<!-- ������Ή� -->
<input type="hidden" name="lblw39" DATASRC="#NdrDatabase" DATAFLD="lblw39"></input>
<input type="hidden" name="lblw36" DATASRC="#NdrDatabase" DATAFLD="lblw36"></input>
<input type="hidden" name="lhbl27" DATASRC="#NdrDatabase2" DATAFLD="lhbl27"></input>
<input type="hidden" name="set41" DATASRC="#NdrDatabase" DATAFLD="set41"></input>
</body>
</html>
