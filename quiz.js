"use strict";

// Namespace.
var hqgreek = {};

// Download a unit and load into localStorage. Then load it onto the page.
hqgreek.downloadUnit = function (num) {
  var r = new XMLHttpRequest();
  r.open("GET", "data/unit" + num + ".json");
  r.onreadystatechange = function () {
    if (r.readyState != 4 || r.status != 200) return;
    var data = JSON.parse(r.responseText);
    var options = [];
    var i = data.num_optional;
    while (i > 0) {
      var j = Math.floor(Math.random(data.optional.length));
      options = options.concat(data.optional.splice(j, 1));
      i--;
    };
    var words = options.concat(data.required);
    hqgreek.setItem("words", words);
    hqgreek.setItem("all", data.all);
    hqgreek.setItem("unit", num);
    hqgreek.selectNewWord();
    hqgreek.displayUnit();
  };
  r.send()
};

hqgreek.selectNewWord = function () {
  hqgreek.setItem("current", Math.floor(Math.random() * hqgreek.getItem("words").length));
};

// Display a word from the unit in localStorage.
hqgreek.displayUnit = function () {
  document.getElementById("selectUnit").value = hqgreek.getItem('unit');
  if (hqgreek.getItem("words").length > 0) {
    document.getElementById("answer").style.display = "none";
    document.getElementById("answerButtons").style.display = "none";
    var word = hqgreek.getItem("words")[hqgreek.getItem("current")];
    document.getElementById("question").innerHTML = word;
    document.getElementById("perseus").href = "http://www.perseus.tufts.edu/hopper/morph?l=" + word + "&la=greek";
    document.getElementById("answerText").innerHTML = hqgreek.getItem("all")[word];
    document.getElementById("questionButtons").style.display = "block";
  } else {
    document.getElementById("questionButtons").style.display = "none";
    document.getElementById("answerButtons").style.display = "none";
    document.getElementById("answer").style.display = "none";
    document.getElementById("question").innerHTML = "Complete!";
  }
};

hqgreek.showButton = function () {
  document.getElementById("questionButtons").style.display = "none";
  document.getElementById("answer").style.display = "block";
  document.getElementById("answerButtons").style.display = "block";
};

hqgreek.doneButton = function () {
  var words = hqgreek.getItem("words");
  words.splice(hqgreek.getItem("current"), 1);
  hqgreek.setItem("words", words);
  hqgreek.selectNewWord();
  hqgreek.displayUnit();
};

hqgreek.againButton = function () {
  hqgreek.selectNewWord();
  hqgreek.displayUnit();
};

hqgreek.selectUnit = function () {
  var sel = document.getElementById("selectUnit");
  hqgreek.downloadUnit(sel.value);
}

// Save an object to localStorage.
hqgreek.setItem = function (key, obj) {
  localStorage.setItem(key, JSON.stringify(obj));
};

// Load an object from localStorage.
hqgreek.getItem = function (key) {
  return JSON.parse(localStorage.getItem(key));
};

// Check whether an object is visible.
hqgreek.isVisible = function (id) {
  var obj = document.getElementById(id);
  var style = window.getComputedStyle(obj);
  return style.display != "none";
};

// On page load.
(function () {
  // Prep data for offline access.
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("offline.js", { scope: "./" }).then(function(reg) {
      console.log("Registration successful. Scope is " + reg.scope);
    }).catch(function(error) {
      console.log("Registration failed with " + error);
    });
  }
  // Display features in footer.
  var features = "Progress saved";
  if ("serviceWorker" in navigator) {
    features += " and offline access available";
  }
  features += " on this device. | ";
  document.getElementById("features").innerHTML = features;
  // Set up buttons.
  document.getElementById("showButton").onclick = hqgreek.showButton;
  document.getElementById("doneButton").onclick = hqgreek.doneButton;
  document.getElementById("againButton").onclick = hqgreek.againButton;
  document.getElementById("selectUnit").onchange = hqgreek.selectUnit;
  document.onkeypress = function (e) {
    e = e || window.event;
    if (e.key === 's' && hqgreek.isVisible("questionButtons")) {
      hqgreek.showButton();
    } else if (e.key === 'd' && hqgreek.isVisible("answerButtons")) {
      hqgreek.doneButton();
    } else if (e.key === 'a' && hqgreek.isVisible("answerButtons")) {
      hqgreek.againButton();
    }
  };
  if (hqgreek.getItem("unit")) {
    hqgreek.displayUnit();
  } else {
    hqgreek.downloadUnit(2);
  }
})();
