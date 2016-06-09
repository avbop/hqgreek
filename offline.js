"use strict";

var CACHE = 'γ';

this.addEventListener("install", function(event) {
  event.waitUntil(
    caches.open(CACHE).then(function(cache) {
      console.log("Loading cache with JSON files.");
      return cache.addAll([
        "/data/",
        "/data/unit2.json"
      ]);
    })
  );
});

this.addEventListener("fetch", function(event) {
  var response;
  event.respondWith(caches.match(event.request).catch(function() {
    console.log("Missed cache.");
    return fetch(event.request);
  }).then(function(r) {
    response = r;
    caches.open(CACHE).then(function(cache) {
      cache.put(event.request, response);
    });
    return response.clone();
  }));
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
