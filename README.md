# Services-Provider-System
Complete solution for services providers based on a instruments repair shop!

This project serves as a business management for services providers, which includes client's database, list of services, 
automated tasks (creates and sends work orders/invoices) and cash flow.

For now, the program reads a list of clients and services from a local CSV files and produces work orders in PDF via
Excel worksheets. The "files" folder contains a .xlsx which determines the model (displayed below) to be printed with
the services and total amount to the client. The code reads the excel template and populates specific fields with user's input.
After that the worksheet is saved and the program opens again this file and convert to PDF. Only the PDF remains in the folder
as the program delete the new worksheet.

Currently I am switching from terminal commands to a GUI and adding a function to send the PDF file directly to the user via email. (aug/23)

***UNDER DEVELOPMENT...!***

![workorder](https://github.com/fabioweck/Services-Provider-System/assets/115494238/f1e8f9de-bca7-4a8f-85f9-4374d7b77bc2)
"Work order produced by the program"
