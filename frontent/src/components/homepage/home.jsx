import React from 'react';
import SimpleCard from '../card/card';

function Home({data, update}) {
  const { updated, setUpdated } = update; 
  console.log(updated,'dfdf')
  console.log(data)
  return (
    <div className='lg:w-[85%] w-[98%] md:grid-cols-2  mx-auto grid 2xl:grid-cols-3 gap-6'>
        {data.map((coupon,i)=>(<SimpleCard key={i} coupon={coupon} update={{updated, setUpdated}}/>))}
    </div>
  
  );
}

export default Home;
