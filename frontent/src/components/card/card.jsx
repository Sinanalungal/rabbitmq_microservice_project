import React, { useState } from 'react';
import { BsBookmarkFill } from "react-icons/bs";
import { Card, CardBody, CardFooter, Typography, Button } from "@material-tailwind/react";
import axios from "axios";
import { couponBackupUrl, couponMainUrl } from '../../constants';

function SimpleCard({ coupon, update }) {
  const { updated, setUpdated } = update; 
  let saved = coupon.saved
  let redeemed = coupon.redeemed
  console.log(coupon.saved,'save or nto')
  console.log(updated)

  
  const updateCard = async ( ) => {
    try {
      const response = await axios.put(`${couponMainUrl}/api/coupon/${coupon.couponcode}`, {
        coupontitle: coupon.coupontitle,
        saved: saved,
        redeemed: redeemed
      });
      setUpdated(!updated); 
      console.log('Coupon updated successfully:', response.data);
    } catch (error) {
      try {
        const backupResponse = await axios.put(`${couponBackupUrl}/api/coupon/${coupon.couponcode}`, {
          coupontitle: coupon.coupontitle,
          saved: saved,
          redeemed: redeemed
        });
        setUpdated(!updated); 
        console.log('Coupon updated successfully (backup):', backupResponse.data);
      } catch (backupError) {
        console.error('Error updating coupon (backup):', backupError);
      }
    }
  };

  console.log(coupon);

  return (
    <Card className="border-r-gray-500 bg-gray-200">
      <CardBody>
        <div className="flex justify-between items-center">
          <Typography variant="h5" color="blue-gray">
            {coupon.coupontitle}
          </Typography>
        </div>
      </CardBody>
      <CardFooter className="pt-0">
        <div className="flex justify-between items-center">
          {coupon.saved ? (
            <Button size="sm" color="black" ripple={true} onClick={()=>{saved=!coupon.saved,updateCard()}}>
              <BsBookmarkFill />
            </Button>
          ) : (
            <Button size="sm" className='border border-gray-500' color="white" ripple={true} onClick={()=>{saved=!coupon.saved,updateCard()}}>
              <BsBookmarkFill color='black' />
            </Button>
          )}
          {coupon.redeemed ? (
            <Button size="sm" color='black' className='text-white' onClick={()=>{redeemed=!coupon.redeemed,updateCard()}}>
              Redeem
            </Button>
          ) : (
            <Button color='white' className='border border-gray-500' size="sm" onClick={()=>{redeemed=!coupon.redeemed,updateCard()}}>
              Redeem
            </Button>
          )}
        </div>
      </CardFooter>
    </Card>
  );
}

export default SimpleCard;
