import Link from 'next/link';
import React, { useState, useEffect } from 'react'
import axios from 'axios';
import {HiOutlineChevronDoubleUp} from 'react-icons/hi'
import {contactInfoURL} from "../constants/constants";
import SocialMediaContact from "./SocialMedia";

const Contact = () => {
  
  const [forms, setContactForms] = useState();
  const [formRes, setFormRes] = useState('');
  async function getContactForms(url){
     let resp = await axios.get(url);
     let data= await resp.data  
     return data;
  }

  // TO-DO Finishing email contact form
  async function handleEmailForm(e){
    e.preventDefault();
    setFormRes(e.data);
    let resp = await axios.post(fetched_info);
    let data = await resp.data;
 }
     
  useEffect(() => {
    (async () => {
      let fetched_info = await getContactForms(contactInfoURL);
      setContactForms(fetched_info);
    })()
 }, [])

  const sendWhatsAppMsg = (phone) => {
    window.open(`https://api.whatsapp.com/send?phone=${phone}`, "_blank")
    return;
  }

  return (
    forms&&
    <div id='contact' className='w-full lg:h-screen'>
      <div className='max-w-[1240px] m-auto px-2 py-16 w-full '>
        <p className='text-xl tracking-widest uppercase text-[#5651e5]'>
          Contact
        </p>
        <h2 className='py-4'>Get In Touch</h2>
        <div className='grid lg:grid-cols-5 gap-8'>
          {/* left */}
          <div className='col-span-3 lg:col-span-2 w-full h-full shadow-xl shadow-gray-400 rounded-xl p-4'>
            <div className='lg:p-4 h-full '>
              <div>
                <img
                  className='rounded-xl hover:scale-105 ease-in duration-300'
                  src='https://images.unsplash.com/photo-1516387938699-a93567ec168e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2671&q=80'
                  alt='/'
                />
              </div>
              <div>
                <h2 className='py-2'>Diego</h2>
                <p>Front-End Developer</p>
                <p className='py-4'>
                  I am available for freelance or part-time positions. Contact
                  me and lets talk.
                </p>
              </div>
              <div>
                <p className='uppercase pt-8'>Connect With Me</p>
                <div className='flex items-center justify-between py-4'>
                  {forms&&forms.contact_forms&&<SocialMediaContact contact_forms={forms.contact_forms}/>}
                </div>
              </div>
            </div>
          </div>

          {/* right */}
          <div className='col-span-3 w-full h-auto shadow-xl shadow-gray-400 rounded-xl lg:p-4'>
            <div className='p-4'>
              <form action={`mailto:${forms.contact_forms.filter(cf => cf.form==="Email")[0].value}`} method="post" encType="text/plain">
                <div className='grid md:grid-cols-2 gap-4 w-full py-2'>
                  <div className='flex flex-col'>
                    <label className='uppercase text-sm py-2'>Name</label>
                    <input
                      className='border-2 rounded-lg p-3 flex border-gray-300'
                      type='text'
                    />
                  </div>
                  <div className='flex flex-col'>
                    <label className='uppercase text-sm py-2'>
                      Phone Number
                    </label>
                    <input
                      className='border-2 rounded-lg p-3 flex border-gray-300'
                      type='text'
                    />
                  </div>
                </div>
                <div className='flex flex-col py-2'>
                  <label className='uppercase text-sm py-2'>Email</label>
                  <input
                    className='border-2 rounded-lg p-3 flex border-gray-300'
                    type='email'
                  />
                </div>
                <div className='flex flex-col py-2'>
                  <label className='uppercase text-sm py-2'>Subject</label>
                  <input
                    className='border-2 rounded-lg p-3 flex border-gray-300'
                    type='text'
                  />
                </div>
                <div className='flex flex-col py-2'>
                  <label className='uppercase text-sm py-2'>Message</label>
                  <textarea className='border-2 rounded-lg p-3 border-gray-300' rows='10'></textarea>
                </div>
                <button className='w-full p-4 text-gray-100 mt-4'>Send Message</button>
              </form>
            </div>
          </div>
        </div>
        <div className='flex justify-center py-12'>
            <Link href='/'>
            <div className='rounded-full shadow-lg shadow-gray-400 p-4 cursor-pointer hover:scale-110 ease-in duration-300'>
                    <HiOutlineChevronDoubleUp className='text-[#5651e5]' size={30} />
                </div>
            </Link>
        </div>
        <div className='text-center font-light text-sm'><p>Adapted from Clint Briley&apos;s Design on Github</p></div>
      </div>
    </div>
  );
};

export default Contact;
