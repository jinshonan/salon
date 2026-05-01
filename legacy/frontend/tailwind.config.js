// keep the fucking theme files in the frontend folder!!!!!!!
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue, js, ts, jsx, tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Poppins", "sans-serif"],
      },
      // gridTemplateColumns: {  // to separate the page 
      //   "70/30": "60% 28%",
      // },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

