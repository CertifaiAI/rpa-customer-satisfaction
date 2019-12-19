Workflow for Customer Satisfaction Prediction
-----------------------------------
This workflow predicts customers' satisfaction level of certain order/transaction based on information such as price, freight value, location, etc.
With the use of Konduit model.


File Descriptions
----------------------
ScoreImage.xaml: For use after the server is started. This allows you to send an image specified as a file path to 
the server for detection. This is meant to be more of an example that should be integrated in to a larger workflow.

StartServer.xaml: The main entry point. This contains the whole workflow for starting a server.

DownloadAndExtract.xaml automatically downloads and extracts a server where the
mail box detection model will run

ReplaceJsonWithPath.xaml: Handles configuring the server configuration (a json file) to point to your current directory
where you are running the workflow. This is necessary to start the server it (happens automatically)
