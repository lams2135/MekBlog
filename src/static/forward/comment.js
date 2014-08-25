var mekblog_comment = {}

var post_comment = function() {
    ;
}

var init_comment_ui =  function(get_comment_url, archive_st) {
    mekblog_comment.archive_st = archive_st;
    $('#archive-comment-list').html('<b>Loading comment...!</b>')
    $.get(get_comment_url, {st: archive_st}, function(data) {
	$('#archive-comment-list').html(data);
    });
}
