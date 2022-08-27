import Link from 'next/link';
import { FaGithub, FaLinkedinIn, FaWhatsapp } from 'react-icons/fa';

const SocialMediaContact = ({contact_forms}) => {
  const sendWhatsAppMsg = (phone) => {
    window.open(`https://api.whatsapp.com/send?phone=${phone}`, "_blank")
    return;
  }
  const handelContactForms = (forms, contactType) => {
    var val = "";
    forms.map(el => {
       if (el.form === contactType)  val = el.value ;
    });
    return val==='WhatsApp'?sendWhatsAppMsg(phone): val
  }

  return (    
    contact_forms&&
                    <>
                    <Link href={handelContactForms(contact_forms, "Linkedin")}>
                    <div className='rounded-full shadow-lg shadow-gray-400 p-6 cursor-pointer hover:scale-110 ease-in duration-300'>
                      <FaLinkedinIn />
                    </div>
                    </Link>
                    <Link href={handelContactForms(contact_forms, "Github")}>
                    <div className='rounded-full shadow-lg shadow-gray-400 p-6 cursor-pointer hover:scale-110 ease-in duration-300'>
                      <FaGithub />
                    </div>
                    </Link>
                    <div onClick={() => sendWhatsAppMsg(handelContactForms(contact_forms, "WhatsApp"))} className='rounded-full shadow-lg shadow-gray-400 p-6 cursor-pointer hover:scale-110 ease-in duration-300'>
                      <FaWhatsapp />
                    </div>
                    </>
  );
};

export default SocialMediaContact;
