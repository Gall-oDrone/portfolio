import Link from 'next/link';
import { FaGithub, FaLinkedinIn, FaWhatsapp } from 'react-icons/fa';

const SocialMediaContact = ({contact_forms}) => {
  const sendWhatsAppMsg = (phone) => {
    window.open(`https://api.whatsapp.com/send?phone=${phone}`, "_blank")
    return;
  }

  return (    
                contact_forms.map(el => {
                  return (
                    <>
                    <Link href="https://www.linkedin.com/in/del-gal-9ba824244/">
                    <div className='rounded-full shadow-lg shadow-gray-400 p-6 cursor-pointer hover:scale-110 ease-in duration-300'>
                      <FaLinkedinIn />
                    </div>
                    </Link>
                    <Link href="https://github.com/Gall-oDrone">
                    <div className='rounded-full shadow-lg shadow-gray-400 p-6 cursor-pointer hover:scale-110 ease-in duration-300'>
                      <FaGithub />
                    </div>
                    </Link>
                    <div onClick={() => sendWhatsAppMsg(el.form==="WhatsApp"?el.value:null)} className='rounded-full shadow-lg shadow-gray-400 p-6 cursor-pointer hover:scale-110 ease-in duration-300'>
                      <FaWhatsapp />
                    </div>
                    </>
                  )
                })
  );
};

export default SocialMediaContact;
