"use strict";

var CACHE = 'e';

this.addEventListener("install", function(event) {
  event.waitUntil(
    caches.open(CACHE).then(function(cache) {
      console.log("Loading cache with JSON files.");
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
  if (event.request.url.indexOf('fonts') !== -1) {
    return fetch(event.request);
  } else {
    event.respondWith(caches.match(event.request).catch(function() {
      console.log("Missed cache.");
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
