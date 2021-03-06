# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllGroups
# Retrieve data for all groups in an account.
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

class GetAllGroups(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAllGroups Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetAllGroups, self).__init__(temboo_session, '/Library/Google/Contacts/GetAllGroups')


    def new_input_set(self):
        return GetAllGroupsInputSet()

    def _make_result_set(self, result, path):
        return GetAllGroupsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllGroupsChoreographyExecution(session, exec_id, path)

class GetAllGroupsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAllGroups
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        super(GetAllGroupsInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The OAuth client ID provided by Google when you register your application.)
        """
        super(GetAllGroupsInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The OAuth client secret provided by Google when you registered your application.)
        """
        super(GetAllGroupsInputSet, self)._set_input('ClientSecret', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of entries to return.)
        """
        super(GetAllGroupsInputSet, self)._set_input('MaxResults', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        super(GetAllGroupsInputSet, self)._set_input('RefreshToken', value)
    def set_StartIndex(self, value):
        """
        Set the value of the StartIndex input for this Choreo. ((optional, integer) The index of the first result to be retrieved (for paging).)
        """
        super(GetAllGroupsInputSet, self)._set_input('StartIndex', value)

class GetAllGroupsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAllGroups Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        return self._output.get('AccessToken', None)

class GetAllGroupsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetAllGroupsResultSet(response, path)
