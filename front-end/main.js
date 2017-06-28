function entrance() {
    var screenWidth = screen.availWidth;
    var screenHeight = screen.availHeight;
    var width = 430;
    var height = 330;

    chrome.app.window.create('entrance.html', {
        id: 'entrance',
        innerBounds: {
            width: width, height: height,
            left: Math.round((screenWidth - width) / 2),
            top: Math.round((screenHeight - height) / 2)
        },
        frame: 'none',
        resizable: false
    });
}

chrome.app.runtime.onLaunched.addListener(launchClient);

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