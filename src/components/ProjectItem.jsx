import Link from 'next/link'
import React, { useState, useEffect } from 'react'
import { FaGithub, FaExternalLinkAlt } from 'react-icons/fa';
import Modal from 'react-modal'; 

const modalStyle = {
  overlay: {
    backgroundColor: '#000',
    opacity: '1',
    transition: 'opacity .25s',
    zIndex: '100',
  },
  content: {
    position: 'absolute',
    top: '50%',
    left: '50%',
    right: 'auto',
    bottom: 'auto',
    maxWidth: 'calc(177.778vh)',
    height: 'calc(46.25vw)',
    marginRight: '-50%',
    transform: 'translate(-50%, -50%)',
    overflow: 'hidden',
  },
 };

const ProjectItem = ({attr}) => {
  const [modal, setModal] = useState(false);
  async function handleModalState(state){
    return setModal(state);
 }
  useEffect(() => {
    if(!modal) {document.body.style.overflow = 'unset';}
    else {document.body.style.overflow = 'hidden';}
  }, [modal])

  return (
    <div className='relative flex items-center justify-center h-auto w-full shadow-xl shadow-gray-400 rounded-xl p-4 group hover:bg-gradient-to-r from-[#5651e5] to-[#709dff]'>
        <img className='rounded-xl group-hover:opacity-10' src={attr.image} alt='/' layout="fill"/> 
      <div className='hidden group-hover:block absolute h-4/5 w-11/12 top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%] overflow-y-auto overflow-x-hidden'>
          <h3 className='text-2xl text-white tracking-wider text-center'>{attr.title}</h3>
          <ul className='flex justify-center pb-3'>{attr.stacks.map((el,i) => {return(<li className='inline m-1 text-white text-center cursor-text' key={i}>{el.stack}</li>)})}</ul>
          <div className='flex flex-row flex-wrap justify-center'>
            {attr.urls.map((obj,i) => {
                if(obj.url_type === "repo"){
                  return (
                    <Link href={obj.url} key={i}>
                      <FaGithub size={20} className='cursor-pointer mx-3 hover:scale-150 duration-300 hover:fill-red-400' />
                    </Link>
                  )
                }
                return(
                  <Link href={obj.url} key={i}>
                      <FaExternalLinkAlt size={20} className='cursor-pointer mx-3 hover:scale-150 duration-300 hover:fill-red-400' />
                  </Link>
                )
            })}
          </div>
          <div className='relative flex h-auto w-full p-4'>
            <div className='absolute flex-col items-center justify-center h-full w-full'>
                <p className='pb-4 break-words mx-2 pt-2 text-white text-center'>{attr.overview}</p>
                {attr.video &&
                  <div className='flex flex-row justify-center'>
                    <button className='text-center bg-none shadow-transparent p-3 mr-4 rounded-lg bg-white text-gray-700 font-bold text-lg cursor-pointer hover:scale-75 duration-300 hover:bg-red-300 normal-case' onClick={() => handleModalState(true)}><p>Demo video</p></button>
                    <Modal isOpen={modal} onRequestClose={()=>handleModalState(false)} style={modalStyle}>
                      <button onClick={()=>handleModalState(false)}></button>
                      <div>
                        <video width="full" height="full" controls><source src={attr.video} type="video/mp4"/></video>
                      </div>
                    </Modal>
                    <Link href={`projects/${attr.id}`}>
                      <p className='text-center p-3 ml-4 rounded-lg bg-white text-gray-700 font-bold text-lg cursor-pointer hover:scale-75 duration-300 hover:bg-red-300'>More info</p>
                    </Link>
                  </div>
                }
            </div>
          </div>
          
      </div>
    </div>
  )
}

export default ProjectItem