let localhost = null;
let files = null;
let publicUrl = null;
let apiURL = null;
let imageURL = null;
let mediaURL = null;

if (global?.window && window.innerHeight){
  publicUrl = new URL(process.env.PUBLIC_URL, window.location);
  if (process.env.NODE_ENV === "production"){
    localhost = 'https://py3-test-app.herokuapp.com'
    files = 'https://py3-test-app-bucket.s3.amazonaws.com'
    console.log("process.env.PUBLIC_URL", JSON.stringify(process.env.PUBLIC_URL))
    console.log("window.location", JSON.stringify(window.location))
    console.log("publicUrl", JSON.stringify(publicUrl))
  } else {
    localhost = files = 'http://127.0.0.1:8000'
    console.log("process.env.PUBLIC_URL", JSON.stringify(process.env.PUBLIC_URL))
    console.log("window.location", JSON.stringify(window.location))
    console.log("publicUrl", JSON.stringify(publicUrl))
  }
  apiURL = '/api'
  imageURL = '/media'
  mediaURL = imageURL
  
}
// export const endpoint = `${localhost}`
export const endpoint = `${localhost}${apiURL}`
const image_endpoint = `${files}${imageURL}`
export const media_endpoint = `${files}${mediaURL}`
export const projectListURL = `${endpoint}/projects/`;
export const projectURL = (id) =>  `${endpoint}/projects/${id}`;
export const aboutMeInfoURL = `${endpoint}/about/`;
export const contactInfoURL = `${endpoint}/about/contact/`
