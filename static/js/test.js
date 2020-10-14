

function flush() {
    $(".formx").css("display","none");
    $("a").css("background-color","white");
}
function changepage(id) {
    flush();
    var id = "#" + id;
    $(id).css("background-color", "#1cb09a");
    if (id === "#p1") {
        $("#form1").css("display", "block");
    }
    if (id ==="#p2"){
        $("#form2").css("display", "block");
    }
    if (id ==="#p3"){
        $("#form3").css("display", "block");
    }
    if (id ==="#p4"){
        $("#form4").css("display", "block");
    }
}

function modifyName(trueName){
    /*获得表单数据*/
    var name = $(trueName).html();
    $(trueName).html("");
    $(trueName).parent().append("<input value='"+name+"'/>");
    $(trueName).parent().children("input").attr("onblur","nameblur(this,'"+name+"')");
    $(s).parent().children("input").focus();
    $(s).remove();
}

function nameBlur(inp,name){
    var val = $(inp).val();
    if(val != name){
        alert("这里是发送异步请求，修改数据库操作");
    }
    $(inp).parent().append("<span onclick = 'modifyName(this)'>\"+val+\"</span>");
    $(inp).remove();
}