import React from 'react';
import footage from "./footage1.mp4"
import { ImageUpload } from "./home";
import Logo from "./logo.png"



function App() {
 return (
   <div className="absolute flex h-screen w-full text-white justify-center  items-center">

      <video src={footage} autoPlay loop muted className='fixed inset-0 object-cover fixed top-0 left-0   overflow-hidden;'  />

      <div className='upper-layer grid md:grid-cols-1 grid-cols-2 upper-layer lg:px-20 '>
      <div className=" bloc absolute top-0 left-0 right-0 flex items-center justify-between px-4 lg:px-16 py-4   md:py-4 bg-transparent mb-8">
          <div className='flex flex-row align-center justify-center'>
          <img className="w-8 h-8 md:w-10 md:h-10 "  src={Logo} alt=''/>
          <p className='translate-y-1/4'>LEAF.AI</p>
          </div>
          <button className="">
            <svg className="w-6 h-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3 12H21" stroke="#fff" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M3 6H21" stroke="#fff" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M3 18H21" stroke="#fff" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
        </div>

        
        <div className='grid grid-cols-1 md:grid-cols-2 '>
          <div className='lg:mx-auto lg:my-0 px-8 py-4 lg:px-0 '>
            <div class=' flex-text w-full lg:w-full'>
              <h1 className=' my-2 lg:text-6xl text-5xl  font-bold leading-tight text-center lg:text-left mb-8'>
                Bring your plants to life
              </h1>
              <p className='lg:text-xl sm:text-md mb-4 text-center lg:text-left'>
                Transforming the way you care for your plants with intelligent technology
              </p>
              <div className='mx-auto md:mx-0'>
                <a className='underline bg-transparent text-white font-bold ' href='https://docs.google.com/forms/d/e/1FAIpQLSeDkWgzdCjGFnv3B6ZAGGGZmlcoA0kupI0O1okMKd3mBzXCdA/viewform?usp=pp_url'>
                  Share your thoughts and help us improve
                </a>
              </div>
            </div>
          </div>
          
          <div >
            <ImageUpload class="dropzone" />
          </div>
        </div>

      </div>
        
      
     
   </div >
 );
}

export default App