"use strict";
(() => {
var exports = {};
exports.id = 888;
exports.ids = [888];
exports.modules = {

/***/ 852:
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

// ESM COMPAT FLAG
__webpack_require__.r(__webpack_exports__);

// EXPORTS
__webpack_require__.d(__webpack_exports__, {
  "default": () => (/* binding */ _app)
});

// EXTERNAL MODULE: external "react/jsx-runtime"
var jsx_runtime_ = __webpack_require__(997);
// EXTERNAL MODULE: ./node_modules/next/image.js
var next_image = __webpack_require__(675);
var image_default = /*#__PURE__*/__webpack_require__.n(next_image);
// EXTERNAL MODULE: ./node_modules/next/link.js
var next_link = __webpack_require__(664);
var link_default = /*#__PURE__*/__webpack_require__.n(next_link);
// EXTERNAL MODULE: external "react"
var external_react_ = __webpack_require__(689);
;// CONCATENATED MODULE: external "react-icons/ai"
const ai_namespaceObject = require("react-icons/ai");
// EXTERNAL MODULE: external "react-icons/fa"
var fa_ = __webpack_require__(290);
;// CONCATENATED MODULE: external "react-icons/bs"
const bs_namespaceObject = require("react-icons/bs");
// EXTERNAL MODULE: external "next/router"
var router_ = __webpack_require__(853);
;// CONCATENATED MODULE: ./components/Navbar.jsx








const Navbar = ()=>{
    const { 0: nav , 1: setNav  } = (0,external_react_.useState)(false);
    const { 0: shadow , 1: setShadow  } = (0,external_react_.useState)(false);
    const { 0: navBg , 1: setNavBg  } = (0,external_react_.useState)("#ecf0f3");
    const { 0: opacity , 1: setOpacity  } = (0,external_react_.useState)("1");
    const { 0: linkColor , 1: setLinkColor  } = (0,external_react_.useState)("#1f2937");
    const router = (0,router_.useRouter)();
    (0,external_react_.useEffect)(()=>{
        if (router.asPath === "/property" || router.asPath === "/crypto" || router.asPath === "/netflix" || router.asPath === "/twitch") {
            setNavBg("transparent");
            setLinkColor("#ecf0f3");
        } else {
            setNavBg("#ecf0f3");
            setLinkColor("#1f2937");
        }
    }, [
        router
    ]);
    const handleNav = ()=>{
        setNav(!nav);
    };
    (0,external_react_.useEffect)(()=>{
        const handleShadow = ()=>{
            if (window.scrollY >= 90) {
                setShadow(true);
                setOpacity("0.75");
            } else {
                setShadow(false);
                setOpacity("1");
            }
        };
        window.addEventListener("scroll", handleShadow);
    }, []);
    return /*#__PURE__*/ (0,jsx_runtime_.jsxs)("div", {
        style: {
            backgroundColor: `${navBg}`,
            opacity: `${opacity}`
        },
        className: shadow ? "fixed w-full h-20 shadow-xl z-[100]" : "fixed w-full h-20 z-[100]",
        children: [
            /*#__PURE__*/ (0,jsx_runtime_.jsxs)("div", {
                className: "flex justify-between items-center w-full h-full px-2 2xl:px-16",
                children: [
                    /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                        href: "/",
                        children: /*#__PURE__*/ jsx_runtime_.jsx((image_default()), {
                            src: "/../public/assets/navLogo.png",
                            alt: "/",
                            width: "60",
                            height: "50",
                            layout: ""
                        })
                    }),
                    /*#__PURE__*/ (0,jsx_runtime_.jsxs)("div", {
                        children: [
                            /*#__PURE__*/ (0,jsx_runtime_.jsxs)("ul", {
                                style: {
                                    color: `${linkColor}`
                                },
                                className: "hidden md:flex",
                                children: [
                                    /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                        href: "/",
                                        children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                            className: "ml-10 text-sm uppercase hover:border-b",
                                            children: "Home"
                                        })
                                    }),
                                    /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                        href: "/#about",
                                        children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                            className: "ml-10 text-sm uppercase hover:border-b",
                                            children: "About"
                                        })
                                    }),
                                    /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                        href: "/#skills",
                                        children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                            className: "ml-10 text-sm uppercase hover:border-b",
                                            children: "Skills"
                                        })
                                    }),
                                    /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                        href: "/#projects",
                                        children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                            className: "ml-10 text-sm uppercase hover:border-b",
                                            children: "Projects"
                                        })
                                    }),
                                    /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                        href: "/#contact",
                                        children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                            className: "ml-10 text-sm uppercase hover:border-b",
                                            children: "Contact"
                                        })
                                    }),
                                    /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                        href: "https://diegogalloresume.s3.amazonaws.com/Resume.pdf",
                                        children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                            className: "ml-10 text-sm uppercase hover:border-b",
                                            children: "Resume"
                                        })
                                    })
                                ]
                            }),
                            /*#__PURE__*/ jsx_runtime_.jsx("div", {
                                onClick: handleNav,
                                className: "md:hidden",
                                children: /*#__PURE__*/ jsx_runtime_.jsx(ai_namespaceObject.AiOutlineMenu, {
                                    size: 25
                                })
                            })
                        ]
                    })
                ]
            }),
            /*#__PURE__*/ jsx_runtime_.jsx("div", {
                className: nav ? "md:hidden fixed left-0 top-0 w-full h-screen bg-black/70" : "",
                children: /*#__PURE__*/ (0,jsx_runtime_.jsxs)("div", {
                    className: nav ? " fixed left-0 top-0 w-[75%] sm:w-[60%] md:w-[45%] h-screen bg-[#ecf0f3] p-10 ease-in duration-500" : "fixed left-[-100%] top-0 p-10 ease-in duration-500",
                    children: [
                        /*#__PURE__*/ (0,jsx_runtime_.jsxs)("div", {
                            children: [
                                /*#__PURE__*/ (0,jsx_runtime_.jsxs)("div", {
                                    className: "flex w-full items-center justify-between",
                                    children: [
                                        /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                            href: "/",
                                            children: /*#__PURE__*/ jsx_runtime_.jsx((image_default()), {
                                                src: "/../public/assets/navLogo.png",
                                                width: "87",
                                                height: "35",
                                                alt: "/",
                                                objectFit: "contain"
                                            })
                                        }),
                                        /*#__PURE__*/ jsx_runtime_.jsx("div", {
                                            onClick: handleNav,
                                            className: "rounded-full shadow-lg shadow-gray-400 p-3 cursor-pointer",
                                            children: /*#__PURE__*/ jsx_runtime_.jsx(ai_namespaceObject.AiOutlineClose, {})
                                        })
                                    ]
                                }),
                                /*#__PURE__*/ jsx_runtime_.jsx("div", {
                                    className: "border-b border-gray-300 my-4",
                                    children: /*#__PURE__*/ jsx_runtime_.jsx("p", {
                                        className: "w-[85%] md:w-[90%] py-4",
                                        children: "Lets build something legendary together"
                                    })
                                })
                            ]
                        }),
                        /*#__PURE__*/ (0,jsx_runtime_.jsxs)("div", {
                            className: "py-4 flex flex-col",
                            children: [
                                /*#__PURE__*/ (0,jsx_runtime_.jsxs)("ul", {
                                    className: "uppercase",
                                    children: [
                                        /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                            href: "/",
                                            children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                                onClick: ()=>setNav(false)
                                                ,
                                                className: "py-4 text-sm",
                                                children: "Home"
                                            })
                                        }),
                                        /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                            href: "/#about",
                                            children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                                onClick: ()=>setNav(false)
                                                ,
                                                className: "py-4 text-sm",
                                                children: "About"
                                            })
                                        }),
                                        /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                            href: "/#skills",
                                            children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                                onClick: ()=>setNav(false)
                                                ,
                                                className: "py-4 text-sm",
                                                children: "Skills"
                                            })
                                        }),
                                        /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                            href: "/#projects",
                                            children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                                onClick: ()=>setNav(false)
                                                ,
                                                className: "py-4 text-sm",
                                                children: "Projects"
                                            })
                                        }),
                                        /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                            href: "/#contact",
                                            children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                                onClick: ()=>setNav(false)
                                                ,
                                                className: "py-4 text-sm",
                                                children: "Contact"
                                            })
                                        }),
                                        /*#__PURE__*/ jsx_runtime_.jsx((link_default()), {
                                            href: "https://diegogalloresume.s3.amazonaws.com/Resume.pdf",
                                            children: /*#__PURE__*/ jsx_runtime_.jsx("li", {
                                                onClick: ()=>setNav(false)
                                                ,
                                                className: "py-4 text-sm",
                                                children: "Resume"
                                            })
                                        })
                                    ]
                                }),
                                /*#__PURE__*/ (0,jsx_runtime_.jsxs)("div", {
                                    className: "pt-40",
                                    children: [
                                        /*#__PURE__*/ jsx_runtime_.jsx("p", {
                                            className: "uppercase tracking-widest text-[#5651e5]",
                                            children: "Lets Connect"
                                        }),
                                        /*#__PURE__*/ (0,jsx_runtime_.jsxs)("div", {
                                            className: "flex items-center justify-between my-4 w-full sm:w-[80%]",
                                            children: [
                                                /*#__PURE__*/ jsx_runtime_.jsx("div", {
                                                    className: "rounded-full shadow-lg shadow-gray-400 p-3 cursor-pointer hover:scale-105 ease-in duration-300",
                                                    children: /*#__PURE__*/ jsx_runtime_.jsx(fa_.FaLinkedinIn, {})
                                                }),
                                                /*#__PURE__*/ jsx_runtime_.jsx("div", {
                                                    className: "rounded-full shadow-lg shadow-gray-400 p-3 cursor-pointer hover:scale-105 ease-in duration-300",
                                                    children: /*#__PURE__*/ jsx_runtime_.jsx(fa_.FaGithub, {})
                                                }),
                                                /*#__PURE__*/ jsx_runtime_.jsx("div", {
                                                    className: "rounded-full shadow-lg shadow-gray-400 p-3 cursor-pointer hover:scale-105 ease-in duration-300",
                                                    children: /*#__PURE__*/ jsx_runtime_.jsx(ai_namespaceObject.AiOutlineMail, {})
                                                }),
                                                /*#__PURE__*/ jsx_runtime_.jsx("div", {
                                                    className: "rounded-full shadow-lg shadow-gray-400 p-3 cursor-pointer hover:scale-105 ease-in duration-300",
                                                    children: /*#__PURE__*/ jsx_runtime_.jsx(bs_namespaceObject.BsFillPersonLinesFill, {})
                                                })
                                            ]
                                        })
                                    ]
                                })
                            ]
                        })
                    ]
                })
            })
        ]
    });
};
/* harmony default export */ const components_Navbar = (Navbar);

;// CONCATENATED MODULE: ./pages/_app.js



function MyApp({ Component , pageProps  }) {
    return /*#__PURE__*/ (0,jsx_runtime_.jsxs)(jsx_runtime_.Fragment, {
        children: [
            /*#__PURE__*/ jsx_runtime_.jsx(components_Navbar, {}),
            /*#__PURE__*/ jsx_runtime_.jsx(Component, {
                ...pageProps
            })
        ]
    });
}
/* harmony default export */ const _app = (MyApp);


/***/ }),

/***/ 796:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/head-manager-context.js");

/***/ }),

/***/ 957:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/head.js");

/***/ }),

/***/ 14:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/i18n/normalize-locale-path.js");

/***/ }),

/***/ 744:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/image-config-context.js");

/***/ }),

/***/ 843:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/image-config.js");

/***/ }),

/***/ 524:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/is-plain-object.js");

/***/ }),

/***/ 20:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/mitt.js");

/***/ }),

/***/ 406:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/page-path/denormalize-page-path.js");

/***/ }),

/***/ 964:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router-context.js");

/***/ }),

/***/ 938:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router/utils/format-url.js");

/***/ }),

/***/ 565:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router/utils/get-asset-path-from-route.js");

/***/ }),

/***/ 365:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router/utils/get-middleware-regex.js");

/***/ }),

/***/ 428:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router/utils/is-dynamic.js");

/***/ }),

/***/ 292:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router/utils/parse-relative-url.js");

/***/ }),

/***/ 979:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router/utils/querystring.js");

/***/ }),

/***/ 52:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router/utils/resolve-rewrites.js");

/***/ }),

/***/ 226:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router/utils/route-matcher.js");

/***/ }),

/***/ 422:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/router/utils/route-regex.js");

/***/ }),

/***/ 232:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/utils.js");

/***/ }),

/***/ 853:
/***/ ((module) => {

module.exports = require("next/router");

/***/ }),

/***/ 689:
/***/ ((module) => {

module.exports = require("react");

/***/ }),

/***/ 290:
/***/ ((module) => {

module.exports = require("react-icons/fa");

/***/ }),

/***/ 997:
/***/ ((module) => {

module.exports = require("react/jsx-runtime");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = __webpack_require__.X(0, [505,61], () => (__webpack_exec__(852)));
module.exports = __webpack_exports__;

})();