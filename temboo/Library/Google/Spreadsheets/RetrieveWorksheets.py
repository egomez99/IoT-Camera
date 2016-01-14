# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveWorksheets
# Retrieves a list of worksheets in a given Google spreadsheet.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveWorksheets(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveWorksheets Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveWorksheets, self).__init__(temboo_session, '/Library/Google/Spreadsheets/RetrieveWorksheets')


    def new_input_set(self):
        return RetrieveWorksheetsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveWorksheetsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveWorksheetsChoreographyExecution(session, exec_id, path)

class RetrieveWorksheetsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveWorksheets
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(RetrieveWorksheetsInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(RetrieveWorksheetsInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(RetrieveWorksheetsInputSet, self)._set_input('ClientSecret', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Deprecated (retained for backward compatibility only).)
        """
        super(RetrieveWorksheetsInputSet, self)._set_input('Password', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(RetrieveWorksheetsInputSet, self)._set_input('RefreshToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(RetrieveWorksheetsInputSet, self)._set_input('ResponseFormat', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet associated with the worksheet(s) you want to retrieve.)
        """
        super(RetrieveWorksheetsInputSet, self)._set_input('SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(RetrieveWorksheetsInputSet, self)._set_input('Username', value)

class RetrieveWorksheetsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveWorksheets Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class RetrieveWorksheetsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveWorksheetsResultSet(response, path)
