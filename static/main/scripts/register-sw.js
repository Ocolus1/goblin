"use strict";
{
  window.C3_RegisterSW = async function C3_RegisterSW() {
    if (!navigator.serviceWorker) return;
    try {
      const reg = await navigator.serviceWorker.register("static/main/sw.js", {
        scope: "static/main/",
      });
      console.info("Registered service worker on " + reg.scope);
    } catch (err) {
      console.warn("Failed to register service worker: ", err);
    }
  };
}
