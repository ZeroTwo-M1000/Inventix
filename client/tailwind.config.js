/** @type {import("tailwindcss").Config} */
export default {
    content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
    theme: {
        boxShadow: {
            "3xl": "0 0 50px #000000",
            "2xl": "0 0 30px #000000"
        },

        extend: {
            colors: {
                bg: "#11131B",
                text: "#FFFFFF",
                dark: {
                    50: "#69696950",
                    icon: "#9FA6B2",
                    100: "#9FA6B2",
                    200: "#2C2F42",
                    300: "#1E202C",
                    400: "#191b24",
                    500: "#151721"
                },
                blue: "#2E68D9",
                red: "#F98080"
            },

            spacing: {
                xl: "40px",
                lg: "20px",
                md: "10px"
            },
            padding: {
                xl: "40px",
                lg: "20px",

                3: "10px",
                3.5: "12px",
                4: "16px",
                8: "30px"
            },
            borderRadius: {
                xl: "34px",
                lg: "19px",
                md: "14px",
                sm: "9px"
            },
            fontSize: {
                "2xl": "23px",
                xl: "20px",
                lg: "16px",
                md: "14px",
                sm: "12px"
            }
        }
    },
    plugins: []
}
