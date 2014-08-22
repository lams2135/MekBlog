mekblog_init = function() {
    try {
	$('.tagsinput').tagsInput();
    } catch (e) {
    }
    try {
	$('.show-tooltip').tooltip();
    } catch(e) {
    }
}
window.onload=mekblog_init;
