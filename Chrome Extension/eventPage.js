chrome.runtime.onInstalled.addListener(() => {
    const contextMenuItem = {
        "id": "downloadTorrent",
        "title": "Download Movie",
        "contexts": ["selection"]
    }
    chrome.contextMenus.create(contextMenuItem);
});

chrome.contextMenus.onClicked.addListener(function (selectData) {
    if (selectData.menuItemId === "downloadTorrent" && selectData.selectionText) {
        const selection = selectData.selectionText.replace('(', '').replace(')', '').replace(':', '').trim();
        const movieYear = selection.substr(selection.length - 4, selection.length).trim();
        const movieName = selection.substr(0, selection.length - 4).trim();

        var port = chrome.runtime.connectNative('com.myextensions.torbot');
        port.postMessage(movieName + "*" + movieYear);

        port.onMessage.addListener((status) => {
            if (status === "success") {
                chrome.notifications.create({
                    type: "basic",
                    iconUrl: 'logo.png',
                    title: 'Success',
                    message: 'Wohoo! Movie download has started!'
                })
            } else {
                chrome.notifications.create({
                    type: "basic",
                    iconUrl: 'logo.png',
                    title: 'Failed',
                    message: 'Oops! The movie download failed. Please try again.'
                })
            }
        });

        port.onDisconnect.addListener(() => {
            console.log("Disconnected");
        });
    }
})