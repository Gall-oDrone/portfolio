import Link from 'next/link';
import React, { useState, useEffect } from 'react'
import axios from 'axios';
import ProjectItem from './ProjectItem';
import {projectListURL} from "../constants/constants";

function Projects() {
  
  const [projects, setProjects] = useState();

    async function getAllProjects(url){
       let resp = await axios.get(url);
       let data= await resp.data  
       return data;
    }
    useEffect(() => {
      (async () => {
        let newProject = await getAllProjects(projectListURL);
         setProjects(newProject);
      })()
   }, [])

  return (
    <div id='projects' className='w-full'>
      <div className='max-w-[1240px] mx-auto px-2 py-16'>
        <p className='text-xl tracking-widest uppercase text-[#5651e5]'>
          Projects
        </p>
        <h2 className='py-4'>What I&apos;ve Built</h2>
        <div className='grid md:grid-cols-2 gap-8'>
        {
                projects&&projects.map(function(project, i){
                    return(
                      <ProjectItem
                      key={i}
                      attr={project}
                    />
                    )
                })
            }
        </div>
      </div>
    </div>
  );
}

export default Projects;
