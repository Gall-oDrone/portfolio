import React, { useState, useEffect } from 'react'
import axios from 'axios';
import SocialMediaContact from "./SocialMedia";
import {contactInfoURL} from "../constants/constants";

const Main = () => {
  const [forms, setContactForms] = useState();
  async function getContactForms(url){
     let resp = await axios.get(url);
     let data= await resp.data  
     return data;
  }
  useEffect(() => {
    (async () => {
      let fetched_info = await getContactForms(contactInfoURL);
      setContactForms(fetched_info);
    })()
 }, [])
  return (
    <div id='home' className='w-full h-screen text-center'>
      <div className='max-w-[1240px] w-full h-full mx-auto p-2 flex justify-center items-center'>
        <div>
          <p className='uppercase text-sm tracking-widest text-gray-600'>
            LETS BUILD SOMETHING TOGETHER
          </p>
          <h1 className='py-4 text-gray-700'>
            Hi, I&apos;m <span className='text-[#1966ed]'> Diego</span>
          </h1>
          <h1 className='py-2 text-gray-700'>a Full Stack Web Developer</h1>
          <p className='py-4 text-gray-600 max-w-[70%] m-auto'>
            I&apos;m a web developer specializing in building (and
            occasionally designing) exceptional digital experiences. Currently,
            I&apos;m focused on building responsive front-end web applications while
            learning back-end technologies.
          </p>
          <div className='flex items-center justify-between max-w-[330px] m-auto py-4'>
            {forms&&forms.contact_forms&&<SocialMediaContact contact_forms={forms.contact_forms}/>}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Main;
