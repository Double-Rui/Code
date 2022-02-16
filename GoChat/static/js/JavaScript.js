$(document).ready(function () {
    var mouse_x, mouse_y
    //鼠标位置
    $(document).mousemove(function (e) {
        //mouse_x = e.pageX - $(".a").offset().left;//得出鼠标在容器内的坐标X，以容器的左上角为坐标原点
        mouse_x = e.pageX;//得出鼠标在容器内的坐标X，以容器的左上角为坐标原点
        //mouse_y = e.pageY - $(".a").offset().top;//得出鼠标在容器内的坐标Y，以容器的左上角为坐标原点
        mouse_y = e.pageY;//得出鼠标在容器内的坐标Y，以容器的左上角为坐标原点
        //$("h1").text("x:" + mouse_x + "y:" + mouse_y)
    });
    GetPersonal_info();

    $(".Revise").click(function () {//修改个人信息
        var data = {
            "NickName": $(".NickName").val(),
            "SignaTure": $(".SignaTure").val(),
            "Sex": $(".Sex option:selected").text(),
            "Birthday": $(".Birthday").val(),
            "Telephone": $(".Telephone").val(),
            "Email": $(".Email").val(),
            "ShengXiao": $(".ShengXiao option:selected").text(),
            "Age": $(".Age").val(),
            "BloodType": $(".BloodType option:selected").text(),
            "SchoolTag": $(".SchoolTag").val(),
            "Vocation": $(".Vocation option:selected").text(),
            "Intro": $(".Intro").val(),
            "Constellation": $(".Constellation option:selected").text()
        }
        $.ajax({
            url: "/Account/EditPersonalInfo",
            type: 'post',
            dataType: "json",
            data: data,
            success: function (data) {
                $(".tip").text(data.mags)
                GetPersonal_info();
                $(".tip").animate({ opacity: "1" }, 2000, function () {
                    $(".tip").animate({ opacity: "0" }, 2000);});
                console.log('请求成功');
            },
            error: function () {
                console.log('发送请求失败'); // 请求失败时的回调函数
            }
        });
    })

    $(".Logout").click(function () {//登出
        $.ajax({
            url: "/Account/Logout",
            type: 'post',
            dataType: "json",
            success: function (data) {
                window.location.href = data.url;
                console.log('请求成功');
            },
            error: function () {
                console.log('发送请求失败'); // 请求失败时的回调函数
            }
        });
    })

    $("#Send").click(function () {
        Send()
    })
        //$(".messages").click(function () {
        //    $(".messages").removeClass("active");
        //    $(this).addClass("active");
//})

    $(function () {
        $(".searchinput").click(function () {
            
            return false;
        });
        $(".search").click(function () {
            return false;
        });
        $(".searchbutton").click(function () {
            return false;
        });
        $(".SearchResult").click(function () {
            return false;
        });
        $(document).click(function () {
            $(".SearchResult").animate({ "height": "0", }, 500, function () {
                $(".SearchResult").css("display","none")
            });
        });
    })

    /*$(".searchinput").focus(function () {
        $(document).keydown(function (e) {
            if (e.which == 13) {
                $('.SearchResult').animate({ 'height': '518px' }, 500, function () { findfriend($('.searchinput').val()) })
            }
        });
        $(document).keyup(function (e) {
            return false;
        });
    })*/
})
function GetPersonal_info() {//获取个人信息
    $.ajax({
        url: "/Home/GetPersonal_info",
        type: 'get',
        dataType: "json",
        data: {},
        success: function (data) {
            $(".LoginID").text(data.U_LoginID)
            $(".NickName").val(data.U_NickName)
            $(".SignaTure").val(data.U_SignaTure)
            $(".Birthday").val(data.U_Birthday)
            $(".Vocation option:selected").text(data.U_Vocation)
            $(".Sex option:selected").text(data.U_Sex)
            $(".Telephone").val(data.U_Telephone)
            $(".Email").val(data.U_Email)
            $(".Intro").text(data.U_Intro)
            $(".ShengXiao option:selected").text(data.U_ShengXiao)
            $(".Age").val(data.U_Age)
            $(".Constellation option:selected").text(data.U_Constellation)
            $(".BloodType option:selected").text(data.U_BloodType)
            $(".SchoolTag").text(data.U_SchoolTag)
            console.log('请求成功');
        },
        error: function () {
            console.log('发送请求失败'); // 请求失败时的回调函数
        }
    });
}

function getFriendHeadPortrait() {//获取好友头像
    $.ajax({
        url: "/Home/getFriendHeadPortrait",
        type: 'post',
        dataType: "json",
        data: { FirendID: $(".FriendHeadPortrait").attr("id") },
        success: function (data) {
            $(".FriendHeadPortrait").attr("src", "/icon/" + data)
            console.log('请求成功');
        },
        error: function () {
            console.log('发送请求失败'); // 请求失败时的回调函数
        }
    });
}

function getChatrecord(ID) {//获取消息记录
    $.ajax({
        url: "/Chat/getChatrecord",
        type: 'post',
        dataType: "json",
        data: { MessagesFrom: ID },
        success: function (data) {
            $(".Chat_p_context").empty();
            for (i = 0; i < data.length; i++) {
                if (data[i].M_PostMessages.length ==0) {
                        //$(".Chat_p_context").append('<span>无消息</span>');
                } else {
                    if (data[i].M_FromUserID == $(".LoginID").text()) {
                        $(".Chat_p_context").append('<div class="meg_me"><span>' + replace_em(data[i].M_PostMessages) + '</span></div>');
                    } else {
                        $(".Chat_p_context").append('<div class="meg_friend"><span>' + replace_em(data[i].M_PostMessages) + '</span></div>');
                    }
                }
            }
            console.log('请求成功');
        },
        error: function () {
            console.log('发送请求失败'); 
        }
    })
}

function scrolltodown() {
    var scrollHeight = $('.Chat_p_context').prop("scrollHeight"); $('.Chat_p_context').scrollTop(scrollHeight, 200);
    //var a = $(".Chat_p_context").find("div").last().scrollTop
    //$('.Chat_p_context').scrollTop(a);
}

/*function getNewMessages() {
    $(".context").each(function () {
        var p = $(this);
        $.ajax({
            url: '/Chat/getNewMessages',
            data: { ID: $(this).prev().attr("name") },
            type: 'post',
            dataType: "json",
            success: function (data) {
                if (data[0] == null) {
                    p.text("");
                } else {
                    p.text(data[0].M_PostMessages);
                }
            }, error: function (e) {

            }
        })
    });
}*/