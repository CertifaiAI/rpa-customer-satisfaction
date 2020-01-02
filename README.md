# RPA(UiPath) & AI : Customer Satisfaction Prediction

## Description
This workflow is created to request information from customers which are not satisfied with their purchases using RPA workflows and AI decision making. Traditionally, companies are required to assign some employees to go through the orders/transactions to find unsatisfied customer and manually send them email for information. However with the capabilities of RPA and AI we can automate this without human intervention.

It predicts customers' satisfaction level on information such as price, freight value, location, etc that is provided in csv format using a deep learning model that was trained on the dataset from Olist, a brazilian e-commerce website. You can find the dataset here: https://www.kaggle.com/olistbr/brazilian-ecommerce. This workflow embeds konduit-serving system to serve the AI engine.

After prediction is made, the RPA workflow will go through each unsatisfied customer and send an email to them to request for more information on their purchase and the reason for their unsatisfaction. For this demo however, all emails will be sent to an email that we can set in the workflow manually as we are not going to send emails to actual customers for privacy purpose.


## File Descriptions

**Main.xaml:** This is the main workflow of the demo. It does the end to end execution of the process. It starts the server for hosting AI model, configures the libraries needed for inferencing, extract data from the input, running the predictions and sending the emails to respective customers.

**StartServer.xaml:** This workflow is used to initiate the Konduit-serving model server. It checks the files required for Konduit-serving, automatically downloads and installs them if they are not already installed. 

**PredictReviewScore.xaml:** This is the primary workflow for customer satisfaction prediction. It handles data extraction from the input, conversion of data to be readable by the AI model and communicates to the server for predictions.

**EmailUnsatisfiedCustomer.xaml:** Automatically emails each customer which are unsatisfied with their purchase based on the predictions given by the AI model. For this demo however, the recipient email is fixed in the workflow instead of actual customer emails and a maximum of 5 emails are sent. You can change the recipient email from this workflow under the variable sections of UiPath Studio.

## How to Run the Workflow: 
1. Clone this repo or download the zip file and extract it to your workspace.
2. Download the [distro.zip](https://github.com/skymindglobal/rpa-customer-satisfaction/releases/tag/v.0.1/distro.zip) and unzip to the "workflow" file directory. You can ignore this step if you want the workflow to download by itself. The download and the unzip will take some time to be completed.
3. Open Main.xaml
4. Set the variables in the workflow to your configurations.
	- dataPath: the CSV file which contains the order information. We have provided 3 sample order files in the "Orders" folder.
	- senderEmail: the email from which the notification will be sent from.
	- senderPassword: the password for the sender email.
	- recipientEmail: the email of the "clients". For this workflow purpose, the recipient email is set manually as we do not have the emails of the clients.

![Variables](img/variables.PNG "Variables")

5. Run Main.xaml
6. The workflow predicts the satisfaction for each orders in the input file and produce prediction results in the folder "Output" in the file "predictions.csv"
7. Based on this file, all the clients with orders that are unsatisfied will be emailed to enquire on the reason for their unsatisfaction.

## Model Serving :  
Konduit-Serving is a serving system and framework focused on deploying machine learning pipelines to production.  
The strength of konduit model serving system is it able to serve wide varieties of python machine learning framework and DL4J framework. 
These framework are included Tensorflow, Keras, DL4J and etc.  
&nbsp;   
If you wish to know more about Konduit model serving, please refer to the below github page:  
**https://github.com/KonduitAI/konduit-serving**  

# Reach us for RPAxAI workflow customization
If you encounter roadblocks in customizing your RPA & AI workflow, we strongly encourage you to reach us anytime!  

### **Webpage @ https://konduit.ai/**  
### **Contact page @ https://konduit.ai/contact/**  
### **Enquiry @ hello@konduit.ai** 