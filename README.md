# Chat-with-PDF
This project is built with the help of langchain, streamlit, and PyPDF2 which helps the user to submit a PDF file
after which the user can ask questions related to the file and it generates answers for the questions on the basis of the submitted PDF file.

Steps to run the project on your local machine:

1. Make sure you have python installed on your PC.
2. Install some packages needed to run this project. The packages are given in the requirements.txt file.
3. You can install this packages using "pip install package_name" through your terminal.
4. After installing packages you have to create a .env file in which you will have to set up your HUGGINGFACEHUB_API_TOKEN like in the given .env.example
5. Now you can run this project by running the command "streamlit run app.py" through your terminal within the project directory.
6. Submit your PDF file and press the process button from the left sidebar.

Note: If the processing takes too long you may try again with a different PDF file with a smaller size. You can try with the given PDF file DSA.pdf from the testPDFs folder.

## Screenshot of the User Interface
![userinterface](https://github.com/SiddhuShkya/Chat-with-PDF/assets/104829964/87499c0e-691a-4fcc-bcd9-1d7219ed7b45)
