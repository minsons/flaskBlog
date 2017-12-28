var Editor;
$(function() {
    Editor = editormd("editorMd", {
        width   : "95%",
        height  : 540,
        syncScrolling : "single",
        path : "/static/editorMd/lib/",
        saveHTMLToTextarea : true,
        imageUpload    : true,
        imageFormats   : ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
        imageUploadURL : "/file/upload"
    });
});