"use strict";
exports.id = 338;
exports.ids = [338];
exports.modules = {

/***/ 338:
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Ch": () => (/* binding */ projectListURL),
/* harmony export */   "_V": () => (/* binding */ aboutMeInfoURL),
/* harmony export */   "f1": () => (/* binding */ contactInfoURL),
/* harmony export */   "u2": () => (/* binding */ projectURL)
/* harmony export */ });
/* unused harmony exports endpoint, media_endpoint */
let localhost = null;
let files = null;
let publicUrl = null;
let apiURL = null;
let imageURL = null;
let mediaURL = null;
if ((global === null || global === void 0 ? void 0 : global.window) && window.innerHeight) {
    publicUrl = new URL(process.env.PUBLIC_URL, window.location);
    if (true) {
        localhost = "https://py3-test-app.herokuapp.com";
        files = "https://py3-test-app-bucket.s3.amazonaws.com";
        console.log("process.env.PUBLIC_URL", JSON.stringify(process.env.PUBLIC_URL));
        console.log("window.location", JSON.stringify(window.location));
        console.log("publicUrl", JSON.stringify(publicUrl));
    } else {}
    apiURL = "/api";
    imageURL = "/media";
    mediaURL = imageURL;
}
// export const endpoint = `${localhost}`
const endpoint = `${localhost}${apiURL}`;
const image_endpoint = `${files}${imageURL}`;
const media_endpoint = `${files}${mediaURL}`;
const projectListURL = `${endpoint}/projects/`;
const projectURL = (id)=>`${endpoint}/projects/${id}`
;
const aboutMeInfoURL = `${endpoint}/about/`;
const contactInfoURL = `${endpoint}/about/contact/`;


/***/ })

};
;