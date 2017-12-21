$(document).ready(function() {
    var doc = $(this);
    var usernameInputBox = $('#spotifyID');
    var submitIDButton = $('#submitID');
    var username;

    // Listens for when the user clicks on the button
    submitIDButton.on("click", function() {
        submitToSpotify();
    });

    // Listener for when user presses enter when cursor is on the input field
    doc.on("keypress", function(e) {
        if (e.keyCode === 13 && usernameInputBox.is(":focus")) { // ENTER
            submitToSpotify();
        }
    });

    function submitToSpotify() {
        username = usernameInputBox.val();

        //INSERT HERE: code for submitting to spotify
    }
});

