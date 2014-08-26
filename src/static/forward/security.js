
function antiXSS(str)
{
	//anti XSS for small title
	return str.replace(/[^0-9a-zA-Z^-~_]/g, "-");
}

function isEmailAddress(str)
{
	//check email format for comment
	var re = /^[a-zA-Z0-9-~_]+@[a-zA-Z0-9-~_]+.com$/
	return re.test(str)
}