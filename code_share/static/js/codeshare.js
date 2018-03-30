
var editor = CodeMirror.fromTextArea(code_snippet, {
    lineNumbers: true,
    lineWrapping: true,
    autofocus: true,
    tabSize: 4,
    indentWithTabs: true,
    theme: 'neo',
});

window.onload = function() {
    var code_snippet = document.getElementById("code_snippet");
    var submit_new = document.getElementById("submit_new");
    var submit_edit = document.getElementById("submit_edit");
    var language_field = document.getElementById("language") 
    var button = document.getElementById("copy_button");
    var url_box = document.getElementById("link_box");
    var INTERFACE_URL = "//cdnjs.cloudflare.com/ajax/libs/codemirror/5.28.0"
    var import_flag = false

    if(url_box){
        url_box.value = window.location.href;
    }

    if (submit_new) {
        submit_new.disabled = true;
    }

    if (submit_edit) {
        submit_edit.disabled = true;
    }

    if (language.value != 'None') {
        CodeMirror.modeURL = INTERFACE_URL+"/mode/%N/%N.js"
        editor.setOption("mode", language.value)
        CodeMirror.autoLoadMode(editor, language.value)
        import_flag = true
    }

    /* 
      EventListener on Keyup on the textarea(code_snippet)
    */
    editor.on('change', function(instance, e) {
        code_content = editor.getValue()
        
        if (code_content.length > 13 && import_flag == false) {
            if (language.value == 'None'){
                var modeInput = hljs.highlightAuto(code_content).language
                
                if (['cpp', 'c', 'java'].indexOf(modeInput) >= 0) {
                    modeInput = 'clike'
                    language.value = 'clike'
                }
                else if (['bash'].indexOf(modeInput) >= 0){
                    modeInput = 'shell'
                    language.value = 'shell'
                }
                else if (['php'].indexOf(modeInput) >= 0){
                    modeInput = 'javascript'
                    language.value = 'javascript'
                }
                else{
                    language.value = modeInput
                }

            }
            else {
                modeInput = language.value
            }

            if (modeInput != 'None'){
                CodeMirror.modeURL = INTERFACE_URL+"/mode/%N/%N.js"
                editor.setOption("mode", modeInput)
                CodeMirror.autoLoadMode(editor, modeInput)
                import_flag = true
            }
        }
        
        if (code_content.length == 0){
            if (submit_new) {
                submit_new.disabled = true
            }
            if (submit_edit) {
                submit_edit.disabled = true
            }
            import_flag = false
            language.value = 'None'
        }

        else {
            if (submit_new) {
                submit_new.disabled = false
            }
            if (submit_edit) {
                submit_edit.disabled = false
            }
        }

    });


    /*on click of copy button it copies current url*/
    if(button) {
        
        button.addEventListener('click', function() {
            url_box.select();
            document.execCommand("copy");
        })
    }
};
