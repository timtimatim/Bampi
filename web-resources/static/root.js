function auth(callback) {
    $(".main").fadeOut(500);
    setTimeout(() => {
        $(".auth").hide().fadeIn(500, () => {
            $("#tg_icon").html("");
            bodymovin.loadAnimation({
                container: document.getElementById("tg_icon"),
                renderer: "canvas",
                loop: true,
                autoplay: true,
                path: "https://raw.githubusercontent.com/hikariatama/Hikka/master/assets/noface.json",
                rendererSettings: {
                    clearCanvas: true,
                }
            });
        });
        fetch("/web_auth", {
                method: "POST",
                credentials: "include",
                timeout: 300000
            })
            .then(response => response.text())
            .then((response) => {
                if (response == "TIMEOUT") {
                    error_message("Code waiting timeout exceeded. Reload page and try again.");
                    $(".auth").fadeOut(500);
                    return
                }

                if (response.startsWith("hikka_")) {
                    $.cookie("session", response)
                    auth_required = false;
                    $(".authorized").hide().fadeIn(100);
                    $(".auth").fadeOut(500, () => {
                        $(".installation").fadeIn(500);
                    });
                    callback();
                    return;
                }
            })
    }, 500);
}

$("#get_started")
    .click(() => {
        if (auth_required) return auth(() => {
            $("#get_started").click();
        });
        $("#enter_api").fadeOut(500);
        $("#get_started").fadeOut(500, () => {
            $("#continue_btn").hide().fadeIn(500);
            switch_block(_current_block);
        });
    });

$("#enter_api")
    .click(() => {
        if (auth_required) return auth(() => {
            $("#enter_api").click();
        });
        $("#get_started").fadeOut(500);
        $("#enter_api")
            .fadeOut(500, () => {
                $("#continue_btn")
                    .hide()
                    .fadeIn(500);

                switch_block("api_id");
            });
    });

function isInt(value) {
    var x = parseFloat(value);
    return !isNaN(value) && (x | 0) === x;
}

function isValidPhone(p) {
    var phoneRe = /^[+]?\d{11,13}$/;
    return phoneRe.test(p);
}

function finish_login() {
    fetch("/finishLogin", {
            method: "POST",
            credentials: "include"
        })
        .then(() => {
            $(".installation").fadeOut(2000);
            setTimeout(() => {
                $("#installation_icon").html("");
                bodymovin.loadAnimation({
                    container: document.getElementById("installation_icon"),
                    renderer: "canvas",
                    loop: true,
                    autoplay: true,
                    path: "https://assets1.lottiefiles.com/animated_stickers/lf_tgs_j7miwfxd.json",
                    rendererSettings: {
                        clearCanvas: true,
                    }
                });
                $(".finish_block").fadeIn(300);
            }, 2000);
        })
        .catch((err) => {
            error_state();
            error_message("Login confirmation error: " + err.toString());
        });
}

function tg_code() {
    fetch("/tgCode", {
            method: "POST",
            body: `${_tg_pass}\n${_phone}\n${_2fa_pass}`
        })
        .then((response) => {
            if (!response.ok) {
                if (response.status == 401) {
                    $(".auth-code-form").hide().fadeIn(300, () => {
                        $("#monkey-close").html("");
                        anim = bodymovin.loadAnimation({
                            container: document.getElementById("monkey-close"),
                            renderer: "canvas",
                            loop: false,
                            autoplay: true,
                            path: "https://static.hikari.gay/monkey-close.json",
                            rendererSettings: {
                                clearCanvas: true,
                            }
                        });
                        anim.addEventListener("complete", () => {
                            setTimeout(() => {
                                anim.goToAndPlay(0);
                            }, 2000);
                        })
                    });
                    $(".code-input").removeAttr("disabled");
                    $(".code-input").attr("inputmode", "text");
                    if($(".enter").hasClass("tgcode"))
                        $(".enter").removeClass("tgcode");
                    $(".code-caption").html("Enter your Telegram 2FA password, then press <span style='color: #dc137b;'>Enter</span>");
                    cnt_btn.setAttribute("current-step", "2fa");
                    $("#monkey").hide();
                    $("#monkey-close").hide().fadeIn(100);
                    _current_block = "2fa";
                } else {
                    $(".code-input").removeAttr("disabled");
                    response.text().then((text) => {
                        error_state();
                        Swal.fire(
                            "Error",
                            text,
                            "error"
                        );
                    });
                }
            } else {
                $(".auth-code-form").fadeOut();
                switch_block("custom_bot");
            }
        })
        .catch(error => {
            Swal.showValidationMessage(
                `Auth failed: ${error.toString()}`
            )
        })
}

function switch_block(block) {
    cnt_btn.setAttribute("current-step", block);
    try {
        $(`#block_${_current_block}`)
            .fadeOut(() => {
                $(`#block_${block}`)
                    .hide()
                    .fadeIn();
            });
    } catch {
        $(`#block_${block}`)
            .hide()
            .fadeIn();
    }

    _current_block = block;
}

function error_message(message) {
    Swal.fire({
        "icon": "error",
        "title": message
    });
}

function error_state() {
    $("body").addClass("red_state");
    cnt_btn.disabled = true;
    setTimeout(() => {
        cnt_btn.disabled = false;
        $("body").removeClass("red_state");
    }, 1000);
}

var _api_id = "",
    _api_hash = "",
    _phone = "",
    _2fa_pass = "",
    _tg_pass = "",
    _current_block = skip_creds ? "phone" : "api_id";

const cnt_btn = document.querySelector("#continue_btn");

function process_next() {
    let step = cnt_btn.getAttribute("current-step");
    if (step == "api_id") {
        let api_id = document.querySelector("#api_id").value;
        if (api_id.length < 4 || !isInt(api_id)) {
            error_state();
            return;
        }

        _api_id = parseInt(api_id, 10);
        switch_block("api_hash");

        return;
    }

    if (step == "api_hash") {
        let api_hash = document.querySelector("#api_hash").value;
        if (api_hash.length != 32) {
            error_state();
            return;
        }

        _api_hash = api_hash;
        fetch("/setApi", {
                method: "PUT",
                body: _api_hash + _api_id,
                credentials: "include"
            })
            .then(response => response.text())
            .then((response) => {
                if (response != "ok") {
                    error_state();
                    error_message(response)
                } else {
                    switch_block("phone");
                }
            })
            .catch((err) => {
                error_state();
                error_message("Error occured while saving credentials: " + err.toString());
            });

        return;
    }

    if (step == "phone") {
        let phone = document.querySelector("#phone").value;
        if (!isValidPhone(phone)) {
            error_state();
            return;
        }

        _phone = phone;
        fetch("/sendTgCode", {
                method: "POST",
                body: _phone,
                credentials: "include"
            })
            .then((response) => {
                if (!response.ok) {
                    response.text().then((text) => {
                        error_state();
                        error_message(text);
                    });
                } else {
                    $(".auth-code-form").hide().fadeIn(300, () => {
                        $("#monkey").html("");
                        anim2 = bodymovin.loadAnimation({
                            container: document.getElementById("monkey"),
                            renderer: "canvas",
                            loop: false,
                            autoplay: true,
                            path: "https://static.hikari.gay/monkey.json",
                            rendererSettings: {
                                clearCanvas: true,
                            }
                        });
                        anim2.addEventListener("complete", () => {
                            setTimeout(() => {
                                anim2.goToAndPlay(0);
                            }, 2000);
                        })
                    });
                    $(".code-input").removeAttr("disabled");
                    $(".enter").addClass("tgcode");
                    $(".code-caption").text("Enter the code you recieved in Telegram");
                    cnt_btn.setAttribute("current-step", "code");
                    _current_block = "code";
                }
            })
            .catch((err) => {
                error_state();
                error_message("Code send failed: " + err.toString());
            });
    }

    if (step == "2fa") {
        let _2fa = document.querySelector("#_2fa").value;
        _2fa_pass = _2fa;
        tg_code();
        return
    }

    if (step == "custom_bot") {
        let custom_bot = document.querySelector("#custom_bot").value;
        if (custom_bot != "" && (!custom_bot.toLowerCase().endsWith("bot") || custom_bot.length < 5)) {
            Swal.fire({
                "icon": "error",
                "title": "Bot username invalid",
                "text": "It must end with `bot` and be at least 5 symbols in length"
            })
            return
        }

        if (custom_bot == "") {
            finish_login();
            return
        }

        fetch("/custom_bot", {
                method: "POST",
                credentials: "include",
                body: custom_bot
            })
            .then(response => response.text())
            .then((response) => {
                if (response == "OCCUPIED") {
                    Swal.fire({
                        "icon": "error",
                        "title": "This bot username is already occupied!"
                    })
                    return;
                }

                finish_login();
            })
            .catch((err) => {
                error_state();
                error_message("Custom bot setting error: " + err.toString());
            });

        return
    }
}

cnt_btn.onclick = () => {
    if (cnt_btn.disabled) return;
    if (auth_required) return auth(() => {
        cnt_btn.click();
    });

    process_next();
}

$(".installation input").on("keyup", (e) => {
    if (cnt_btn.disabled) return;
    if (auth_required) return auth(() => {
        cnt_btn.click();
    });

    if (e.key === "Enter" || e.keyCode === 13) {
        process_next();
    }
});

$(".code-input").on("keyup", (e) => {
    if (_current_block == "code" && $(".code-input").val().length == 5) {
        _tg_pass = $(".code-input").val();
        $(".code-input").attr("disabled", "true");
        $(".code-input").val("");
        tg_code();
    } else if (_current_block == "2fa" && (e.key === "Enter" || e.keyCode === 13)) {
        let _2fa = $(".code-input").val();
        _2fa_pass = _2fa;
        $(".code-input").attr("disabled", "true");
        $(".code-input").val("");
        tg_code();
    }
});

$(".enter").on("click", () => {
    if (_current_block == "2fa") {
        let _2fa = $(".code-input").val();
        _2fa_pass = _2fa;
        $(".code-input").attr("disabled", "true");
        $(".code-input").val("");
        tg_code();
    }
});
