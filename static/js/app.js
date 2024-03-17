    window.botpressWebChat.init({
        "composerPlaceholder": "Learn Stocks with The BeanStock",
        "botConversationDescription": "This Chatbot is conversational and human like. It will help users with stock news and prices",
        "botId": "5c3a3d77-6fb6-469b-84f3-93e8aca5b986",
        "hostUrl": "https://cdn.botpress.cloud/webchat/v1",
        "messagingUrl": "https://messaging.botpress.cloud",
        "clientId": "5c3a3d77-6fb6-469b-84f3-93e8aca5b986",
        "webhookId": "f5a9262f-38cc-4654-bfb7-451b796e4f76",
        "lazySocket": true,
        "themeName": "prism",
        "botName": "BeanStock",
        "stylesheet": "https://webchat-styler-css.botpress.app/prod/de811551-a62d-401d-aad3-6650a1c9821e/v51922/style.css",
        "frontendVersion": "v1",
        "useSessionStorage": true,
        "enableConversationDeletion": true,
        "theme": "prism",
        "themeColor": "#2563eb"
      });

var toggle_btn;
var big_wrapper;
var hamburger_menu;

function declare() {
  toggle_btn = document.querySelector(".toggle-btn");
  big_wrapper = document.querySelector(".big-wrapper");
  hamburger_menu = document.querySelector(".hamburger-menu");
}

const main = document.querySelector("main");

declare();

let dark = false;

function toggleAnimation() {
  // Clone the wrapper
  dark = !dark;
  let clone = big_wrapper.cloneNode(true);
  if (dark) {
    clone.classList.remove("light");
    clone.classList.add("dark");
  } else {
    clone.classList.remove("dark");
    clone.classList.add("light");
  }
  clone.classList.add("copy");
  main.appendChild(clone);

  document.body.classList.add("stop-scrolling");

  clone.addEventListener("animationend", () => {
    document.body.classList.remove("stop-scrolling");
    big_wrapper.remove();
    clone.classList.remove("copy");
    // Reset Variables
    declare();
    events();
  });
}

function events() {
  toggle_btn.addEventListener("click", toggleAnimation);
  hamburger_menu.addEventListener("click", () => {
    big_wrapper.classList.toggle("active");
  });
}

events();