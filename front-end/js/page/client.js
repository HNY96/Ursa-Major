$(function () {
    $('.close-win').click(function () {
        chrome.app.window.current().close();
    });

    $('.minimize-win').click(function () {
        chrome.app.window.current().minimize();
    });

    $('#search').on('focus', function () {
        $(this).css('width', '180px');
    }).on('blur', function () {
        $(this).css('width', '100px');
    });

    $(document).on('keyup', function (e) {
        if (e.which === 13 && e.ctrlKey)
            sendMsg();
    });

    $('.send-msg').click(sendMsg);

    $('.emoj-menu').click(selectEmoj);
});

var mapper = [
    'img/emoj/僵尸.svg',
    'img/emoj/呕吐.svg',
    'img/emoj/大哭.svg',
    'img/emoj/头晕.svg',
    'img/emoj/开心.svg',
    'img/emoj/懵圈.svg',
    'img/emoj/无语.svg',
    'img/emoj/生气.svg',
    'img/emoj/笑哭.svg',
    'img/emoj/迷茫.svg',
    'img/emoj/难过.svg',
    'img/emoj/魔鬼.svg'
];

// 打开我的信息窗口
function profileWindow() {
    var screenWidth = screen.availWidth;
    var screenHeight = screen.availHeight;
    var width = 340;
    var height = 510;

    chrome.app.window.create('profile.html', {
        id: 'profile',
        innerBounds: {
            width: width, height: height,
            left: Math.round((screenWidth - width) / 2),
            top: Math.round((screenHeight - height) / 2)
        },
        frame: 'none',
        resizable: false
    });
}

// 发送消息
function sendMsg() {
    var $input = $('#input-msg');
    var msg = $input.val();
    var pattern = /::\W{2}::/g;
    var avater = 'img/avatar.png'; // todo 从cookie中获取

    if (!msg) return;

    var arr = msg.split(pattern);
    var match = msg.match(pattern);
    if (match) {
        match.forEach(function (e, i, arr) {
            mapper.forEach(function (p1) {
                e = e.substring(2, e.length-2);
                if (p1.indexOf(e) !== -1) {
                    arr[i] = '<img class="inline-img" src="' + p1 + '" alt="">'
                }
            });
        });
    }

    msg = '';
    arr.forEach(function (e, i, arr) {
        if (i < (arr.length -1))
            msg += e + match[i];
        else
            msg += e;
    });

    $('.messages').append($(createMsg(false, avater, msg)));
    toBottom();
    $input.val('');
}

// 创建一条消息
function createMsg(msgType, avatar, msg) {

    var bounceIn = msgType ? 'bounceInLeft' : 'bounceInRight';
    var msgSide = msgType ? 'left-msg' : 'right-msg';

    var template = '<div class="msg {msgSide} animated {bounceIn}">' +
        '<div class="msg-head">' +
        '<img src="{avatar}" alt="头像" class="img-responsive img-circle">' +
        '</div><div class="msg-body">{msg}</div>' +
        '</div>';

    template = template.replace('{msgSide}', msgSide)
        .replace('{bounceIn}', bounceIn)
        .replace('{avatar}', avatar)
        .replace('{msg}', msg);

    return template;
}

// 滚动到底部
function toBottom() {
    $('.messages').get(0).scrollTop = 10000000000000;
}

// 选择表情
function selectEmoj(e) {
    var target = e.target;
    var emojStr = '';
    var src = decodeURI(target.src);
    var lastIdx = src.lastIndexOf('/');
    var $input = $('#input-msg');

    if (target.nodeName.toLocaleLowerCase() === 'img') {
        emojStr = decodeURI(src).substring(lastIdx+1, lastIdx+3);
        emojStr = '::' + emojStr + '::';
    }

    $input.val($input.val() + emojStr);
}

// p2p 连接到对方
function conToFriend(ip, port) {

}