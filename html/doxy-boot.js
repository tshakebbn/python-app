$( document ).ready(function() {
    $("div.header").wrapAll("<div class='content'></div>").wrapAll("<div class='container-fluid'></div>").wrapAll("<div class='row'></div>").wrapAll("<div class='col-md-12'></div>").wrapAll("<div class='card'></div>");
    $("div.card").append($("div.contents").clone());
    $("div.contents").eq(1).remove();
    $("div.textblock").contents().unwrap();
    $("div.contents").addClass("content").removeClass("contents");
    $("div.headertitle").contents().unwrap();
    $("div.title").contents().unwrap().wrapAll("<h1></h1>");
});
