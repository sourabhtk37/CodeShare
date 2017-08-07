// disables the submit button upon document ready
window.onload = function() {
        var submit_new = document.getElementById("submit_new");
        var submit_edit = document.getElementById("submit_edit");
        var code_snippet = document.getElementById("code_snippet");
        var button = document.getElementById("copy_button");
        var url = document.getElementById("link_box");
        if(url){
        url.value = window.location.href;
        }
        if (submit_new) {
            submit_new.disabled = true;
        }
        if (submit_edit) {
            submit_edit.disabled = true;
        }
        /* 
          EventListener on Keyup on the textarea(code_snippet) calls this method.
          Content in the textarea is checked and according to that 
          submit buttons are disabled/enabled.
        */
        console.log(submit_new, submit_edit, code_snippet)
        code_snippet.addEventListener("keyup", function() {
            if (code_snippet.value != "") {
                if (submit_new) {
                    submit_new.disabled = false;
                }
                if (submit_edit) {
                    submit_edit.disabled = false;
                }
            } else {
                if (submit_new) {
                    submit_new.disabled = true;
                }
                if (submit_edit) {
                    submit_edit.disabled = true;
                }
            }
        });


        /*on click of copy button it copies current url*/
        if(button) {
        button.addEventListener('click', function() {
            url.select();
            document.execCommand("copy");
        })
    }
};
