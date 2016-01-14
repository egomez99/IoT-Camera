# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteThread
# Permanently deletes a specific thread.
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

class DeleteThread(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteThread Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteThread, self).__init__(temboo_session, '/Library/Google/Gmailv2/Threads/DeleteThread')


    def new_input_set(self):
        return DeleteThreadInputSet()

    def _make_result_set(self, result, path):
        return DeleteThreadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteThreadChoreographyExecution(session, exec_id, path)

class DeleteThreadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteThread
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(DeleteThreadInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(DeleteThreadInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(DeleteThreadInputSet, self)._set_input('ClientSecret', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(DeleteThreadInputSet, self)._set_input('RefreshToken', value)
    def set_ThreadID(self, value):
        """
        Set the value of the ThreadID input for this Choreo. ((required, string) The ID of the thread to delete.)
        """
        super(DeleteThreadInputSet, self)._set_input('ThreadID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the acting user. Defaults to "me" indicating the user associated with the Access Token or Refresh Token provided.)
        """
        super(DeleteThreadInputSet, self)._set_input('UserID', value)

class DeleteThreadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteThread Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google. An empty response is expected for a successful delete operation.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class DeleteThreadChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteThreadResultSet(response, path)
