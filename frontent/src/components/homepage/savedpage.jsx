import React, { useEffect, useState } from 'react';
import axios from "axios";
import Home from './home';
import {   couponSavedUrl } from '../../constants';
import {NavbarDefault} from '../navbar/navbar';

function SavedPage() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [updated,setUpdated]=useState(false);

  useEffect(() => {
    const fetchData = async () => {
        try {
          const backupResponse = await axios.get(`${couponSavedUrl}/saved/`);
          setData(backupResponse.data);
          setLoading(false);
        } catch (backupError) {
          setError('Failed to fetch data from both URLs');
          setLoading(false);
        }
    };

    fetchData();
  }, [updated]);

  return (
    <>
      <div className='py-4'>
        <NavbarDefault />
        {loading ? (
          <div className="flex justify-center items-center h-screen">
            <div className="animate-spin ease-linear rounded-full w-10 h-10 border-t-2 border-b-2 border-purple-500"></div>
            <div className="animate-spin ease-linear rounded-full w-10 h-10 border-t-2 border-b-2 border-red-500 ml-3"></div>
            <div className="animate-spin ease-linear rounded-full w-10 h-10 border-t-2 border-b-2 border-blue-500 ml-3"></div>
          </div>
        ) : error ? (
            <div className="flex justify-center items-center h-screen">
              <p>{error}</p>
            </div>
        ) : (
          <Home data={data} update={{updated, setUpdated}}/>
        )}
      </div>
    </>
  );
}

export default SavedPage;
