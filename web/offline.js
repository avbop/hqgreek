"use strict";

var CACHE = "v";

this.addEventListener("install", function(event) {
  event.waitUntil(
    caches.open(CACHE).then(function(cache) {
      return cache.addAll([
        "./",
        "index.html",
        "quiz.js",
        "index.css",
        "favicon.png",
        "data/unit1.json",
        "data/unit2.json"
      ]);
    })
  );
});

this.addEventListener("fetch", function(event) {
  if (event.request.url.indexOf("fonts") !== -1 ||
      event.request.url.indexOf("offline.js") !== -1 ||
      event.request.url.indexOf("docs") !== -1) {
    event.respondWith(fetch(event.request));
  } else {
    event.respondWith(caches.match(event.request).catch(function() {
      return fetch(event.request);
    }));
  }
});

self.addEventListener("activate", function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheName !== CACHE) {
            console.log("Deleting cache " + cacheName + ".");
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
