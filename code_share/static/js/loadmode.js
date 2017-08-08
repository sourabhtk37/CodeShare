!function(e) {
    "object" == typeof exports && "object" == typeof module ? e(require("../../lib/codemirror"), "cjs") : "function" == typeof define && define.amd ? define(["../../lib/codemirror"], function(r) {
        e(r, "amd")
    }) : e(CodeMirror, "plain")
}(function(e, r) {
    function o(e, r) {
        var o = r;
        return function() {
            0 == --o && e()
        }
    }
    function n(r, n) {
        var t = e.modes[r].dependencies;
        if (!t)
            return n();
        for (var i = [], d = 0; d < t.length; ++d)
            e.modes.hasOwnProperty(t[d]) || i.push(t[d]);
        if (!i.length)
            return n();
        for (var u = o(n, i.length), d = 0; d < i.length; ++d)
            e.requireMode(i[d], u)
    }
    e.modeURL || (e.modeURL = "../mode/%N/%N.js");
    var t = {};
    e.requireMode = function(o, i) {
        if ("string" != typeof o && (o = o.name),
        e.modes.hasOwnProperty(o))
            return n(o, i);
        if (t.hasOwnProperty(o))
            return t[o].push(i);
        var d = e.modeURL.replace(/%N/g, o);
        if ("plain" == r) {
            var u = document.createElement("script");
            u.src = d;
            var f = document.getElementsByTagName("script")[0]
              , a = t[o] = [i];
            e.on(u, "load", function() {
                n(o, function() {
                    for (var e = 0; e < a.length; ++e)
                        a[e]()
                })
            }),
            f.parentNode.insertBefore(u, f)
        } else
            "cjs" == r ? (require(d),
            i()) : "amd" == r && requirejs([d], i)
    }
    ,
    e.autoLoadMode = function(r, o) {
        e.modes.hasOwnProperty(o) || e.requireMode(o, function() {
            r.setOption("mode", r.getOption("mode"))
        })
    }
});
