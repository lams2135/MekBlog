
function antiXSS(str)
{
	//anti XSS
	return str.replace(/[^0-9a-zA-Z^-~_]/g, "-");
}