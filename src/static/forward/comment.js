var mekblog_comment = {}

var update_comment = function() {
    $('#archive-comment-list').html('<b>Loading comment...!</b>')
    $.get(mekblog_comment.get_url, {st: mekblog_comment.archive_st}, function(data) {
	$('#archive-comment-list').html(data);
    });
}

var post_comment = function() {
    var submit = {
	'archive-st': mekblog_comment.archive_st,
	'name': $('#archive-comment-post-name').val(),
	'content': $('#archive-comment-post-content').val(),
	'email': $('#archive-comment-post-email').val(),
	'reply-to': mekblog_comment.reply_to,
	'enable-notify': $('#archive-comment-post-enablemailnotify').hasClass('checked')
    };
    $.ajax({
	type: "POST",
	url:  mekblog_comment.post_url,
	contentType: 'application/json',
	data: JSON.stringify(submit),
	success: function(data) {
	    console.log(data);
	    if (data.result) {
		update_comment();
	    }
	}
    });
}

var init_comment_ui =  function(get_comment_url, post_comment_url, archive_st) {
    mekblog_comment.archive_st = archive_st;
    mekblog_comment.get_url = get_comment_url;
    mekblog_comment.post_url = post_comment_url;
    mekblog_comment.reply_to = '0';
    update_comment();
}
