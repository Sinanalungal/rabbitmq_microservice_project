import React from "react";
import { Navbar, Typography, Button, IconButton } from "@material-tailwind/react";
import { useNavigate } from "react-router-dom"; // Import useNavigate hook

export function NavbarDefault() {
  const [openNav, setOpenNav] = React.useState(false);
  const navigate = useNavigate(); // Initialize useNavigate hook

  React.useEffect(() => {
    window.addEventListener(
      "resize",
      () => window.innerWidth >= 960 && setOpenNav(false)
    );
  }, []);

  const navList = (
    <ul className="mt-2 mb-4 flex flex-col gap-2 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
      {/* Your list items here */}
    </ul>
  );

  return (
    <Navbar className="mx-auto bg-transparent bg-gray-50 shadow-lg mb-10 w-full px-4 lg:px-8 lg:py-4">
      <div className="container mx-auto flex items-center justify-between text-blue-gray-900">
        <Typography as="a" onClick={() => navigate('/')} className="mr-4 font-semibold cursor-pointer py-1.5">
          CouponsHub
        </Typography>
        <div className="hidden lg:block">{navList}</div>
        <div className="flex items-center gap-x-1">
          <Button variant="text" onClick={() => navigate('/saved')} size="sm" className="hidden lg:inline-block">
            <span>Saved</span>
          </Button>
          <Button variant="gradient" size="sm" className="hidden lg:inline-block" onClick={() => navigate('/redeem')}>
            <span>Redeemed</span>
          </Button>
        </div>
        <IconButton
          variant="text"
          className="ml-auto h-6 w-6 text-inherit hover:bg-transparent focus:bg-transparent active:bg-transparent lg:hidden"
          ripple={false}
          onClick={() => setOpenNav(!openNav)}
        >
          {/* Add your icon SVG or content here */}
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </IconButton>
      </div>
    </Navbar>
  );
}

export default NavbarDefault;
