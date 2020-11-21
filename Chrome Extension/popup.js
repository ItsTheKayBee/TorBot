document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('download').addEventListener('click', download, false)

    function download() {
        const movieName = document.getElementById('movie-name').value.trim();
        const movieYear = document.getElementById('movie-year').value.trim();

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

}, false);
