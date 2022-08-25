import Image from 'next/image';
import React, { useState, useEffect } from 'react'
import axios from 'axios';
import { RiRadioButtonFill } from 'react-icons/ri';
import Link from 'next/link';
import { useRouter } from 'next/router'
import {projectURL} from "../../constants/constants";

const Project = () => {
    const router = useRouter()
    const { project_id } = router.query
    const [project, setProject] = useState();

    async function getProject(url){
       let resp = await axios.get(url);
       let data= await resp.data  
       return data;
    }
    useEffect(() => {
      (async () => {
        if (project_id) {
          let url = projectURL(project_id)
          let fetchedProject = await getProject(url);
          setProject(fetchedProject);
        }
      })()
   }, [project_id])
  return (
    project &&
    <div className='w-full'>
        <div className='w-screen h-[30vh] lg:h-[40vh] relative'>
            <div className='absolute top-0 left-0 w-full h-[30vh] lg:h-[40vh] bg-black/80 z-10' />
                <Image
                className='absolute z-1'
                layout='fill'
                objectFit='cover'
                src={project.image}
                alt='/'
                />
                <div className='absolute top-[70%] max-w-[1240px] w-full left-[50%] right-[50%] translate-x-[-50%] translate-y-[-50%] text-white z-10 p-2'>
                    <h2 className='py-2'>{project.title} App</h2>
                    <h3>{project.stacks.map((el, i) => {el.stack})}</h3>
                </div>
        </div>

      <div className='max-w-[1240px] mx-auto p-2 grid md:grid-cols-5 gap-8 pt-8'>
        <div className='col-span-4'>
          <p>Project</p>
          <h2>Overview</h2>
          <p>
            {project.description}
          </p>
          <div className='flex'>
          {project.urls.map((url_obj, i)=> {
            return (<a key={i} href={url_obj.url} className='p-4 m-4'>{url_obj.url_type}</a>);
            })
          }
          </div>
        </div>
        <div className='col-span-4 md:col-span-1 shadow-xl shadow-gray-400 rounded-xl p-4'>
          <div className='p-2'>
            <p className='text-center font-bold pb-2'>Technologies</p>
            <div className='grid grid-cols-3 md:grid-cols-1'>
                {project.stacks.map((el, i) => 
                    <p key={i} className='text-gray-600 py-2 flex items-center'>
                        <RiRadioButtonFill className='pr-1' /> {el.stack}
                    </p>
                 )
                }
            </div>
          </div>
        </div>
        <Link href='/#projects'>
          <p className='underline cursor-pointer'>Back</p>
        </Link>
      </div>
    </div>
  );
};

export default Project;
