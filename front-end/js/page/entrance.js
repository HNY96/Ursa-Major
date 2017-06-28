$('.close-win').click(function () {
    chrome.app.window.current().close();
});

$('.minimize-win').click(function () {
    chrome.app.window.current().minimize();
});

$('.reg-link').click(function () {
    var $reg = $('.register-box'),
        $login = $('.login-box');

    if ($reg.hasClass('hidden')) {
        $login.addClass('hidden');
        $reg.removeClass('hidden');
    }

    $('.login-btn').addClass('hidden');
    $('.reg-btn').removeClass('hidden');
    $('.top').css('height', '50%');
    $('.bottom').css('height', '50%');

    return false;
});

$('.login-link').click(function () {
    var $reg = $('.register-box'),
        $login = $('.login-box');

    if (!$reg.hasClass('hidden')) {
        $reg.addClass('hidden');
        $login.removeClass('hidden');
    }

    $('.reg-btn').addClass('hidden');
    $('.login-btn').removeClass('hidden');
    $('.top').css('height', '60%');
    $('.bottom').css('height', '40%');

    return false;
});

$('.btns').click(function (e) {
    var target = e.target;
    
    if (target.classList.contains('login-btn')) {
        // todo 登录
        console.log('login');
        loginAnimation();

        // 创建新窗口
        launchClient();
    }
    
    if (target.classList.contains('reg-btn')) {
        // todo 注册
        console.log('register');
    }
});

// 登录动画
function loginAnimation() {
    $('.bottom-content-right').addClass('hidden');
    $('.bottom-content-left').addClass('login-animation');
    $('.avatar>img').addClass('login-animation-border');
}

// 创建新窗口 client
function launchClient() {
    var screenWidth = screen.availWidth;
    var screenHeight = screen.availHeight;
    var width = 755;
    var height = 600;

    chrome.app.window.create('client.html', {
        id: 'client',
        innerBounds: {
            width: width, height: height,
            left: Math.round((screenWidth - width) / 2),
            top: Math.round((screenHeight - height) / 2)
        },
        frame: 'none',
        resizable: false
    });
}