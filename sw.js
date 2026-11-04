const CACHE_NAME = 'omnitools-suite-v3';
const ASSETS = [
  './',
  './index.html',
  './rampe.html',
  './scale.html',
  './tubi.html',
  './dorso.html',
  './dpi.html',
  './manifest.json',
  './manifest-building.json',
  './manifest-graph.json',
  './icon-192.png',
  './icon-512.png',
  './icon-building-192.png',
  './icon-building-512.png',
  './icon-graph-192.png',
  './icon-graph-512.png',
  './favicon.png',
  './favicon.svg'
];

self.addEventListener('install', (e) => {
  self.skipWaiting();
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

// Network first, falling back to cache
self.addEventListener('fetch', (e) => {
  if (e.request.mode === 'navigate') {
    e.respondWith(
      fetch(e.request)
        .then((response) => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(e.request, clone));
          return response;
        })
        .catch(() => {
          // If navigating, try to match the exact URL, else fallback to index.html
          return caches.match(e.request).then((res) => res || caches.match('./index.html'));
        })
    );
    return;
  }

  e.respondWith(
    caches.match(e.request).then((res) => {
      return res || fetch(e.request).then((networkRes) => {
        return networkRes;
      });
    })
  );
});
