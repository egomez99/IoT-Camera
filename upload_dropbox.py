# coding=utf-8
# Script to upload files to Dropbox

# Import correct libraries
import base64
import sys
from datetime import datetime
from temboo.core.session import TembooSession
from temboo.Library.Dropbox.FilesAndMetadata import UploadFile

print str(sys.argv[1])

# Encode image
with open(str(sys.argv[1]), "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

# Declare Temboo session and Choreo to upload files
session = TembooSession("U-S-E-R", "A-P-P", "K-E-Y")

uploadFileChoreo = UploadFile(session)

# Get an InputSet object for the choreo
uploadFileInputs = uploadFileChoreo.new_input_set()

# Set inputs
uploadFileInputs.set_FileName(sys.argv[1])
uploadFileInputs.set_FileContents(encoded_string)

# Set the Choreo inputs
uploadFileInputs.set_AccessToken("T-O-K-E-N")
uploadFileInputs.set_AppKey("A-P-P-K-E-Y")
uploadFileInputs.set_AccessTokenSecret("T-O-K-E-N")
uploadFileInputs.set_AppSecret("S-E-C-R-E-T")

# Execute choreo
uploadFileResults = uploadFileChoreo.execute_with_results(uploadFileInputs)

# Print the Choreo outputs
print("Response: " + uploadFileResults.get_Response())
