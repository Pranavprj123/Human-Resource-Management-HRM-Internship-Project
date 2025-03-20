import React from 'react'
import { createBrowserRouter } from 'react-router-dom'
import Navbar from './Navbar'
export default function Route() {
  return createBrowserRouter ([
    {
        path:"/",
        element: (
            <>
            <Navbar/>
            </>
        ),
    },
  ]);
}
