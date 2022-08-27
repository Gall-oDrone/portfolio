import React, { useState, useEffect } from 'react'
import axios from 'axios';
import {aboutMeInfoURL} from "../constants/constants";

const About = () => {

  const [info, setAboutMeInfo] = useState();

  async function getAboutMeInfo(url){
     let resp = await axios.get(url);
     let data= await resp.data  
     return data;
  }
  useEffect(() => {
    (async () => {
      let fetched_info = await getAboutMeInfo(aboutMeInfoURL);
      setAboutMeInfo(fetched_info);
    })()
 }, [])

  return (
    info && (
      <div id='about' className='w-full md:h-screen p-2 flex items-center py-16'>
        <div className='max-w-[1240px] m-auto md:grid grid-cols-3 gap-8'>
          <div className='col-span-2'>
            <p className='uppercase text-xl tracking-widest text-[#5651e5]'>About</p>
            <h2 className='py-4'>Who I Am</h2>
            <p className='py-2 text-gray-600'>{info.message?info.message:null}</p>
            <p className='py-2 text-gray-600'>
              {info.about_me}
            </p>
            <p className='py-2 text-gray-600'>
              Fascinated with how intricate programming can be I was quickly drawn
              to learn more. I started learning javascript and was even more
              enthused with making websites interactive. I then started
              freelancing for e-commerce companies on the Shopify platform. I am
              now spending my time building projects with React JS, Firebase, and
              learning new technologies.
            </p>
            <p className='py-2 text-gray-600 underline cursor-pointer'>Check out some of my latest projects.</p>
          </div>
          <div className='w-full h-auto m-auto shadow-xl shadow-gray-400 rounded-xl flex items-center justify-center p-4 hover:scale-105 ease-in duration-300'>
              <img className='rounded-xl' src={info.picture} alt="/" />
          </div>
        </div>
    </div>
    )
  );
};

export default About;
