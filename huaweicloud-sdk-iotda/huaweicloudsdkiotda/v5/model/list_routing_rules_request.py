# coding: utf-8

import pprint
import re

import six





class ListRoutingRulesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('stage_auth_token')

    openapi_types = {
        'stage_auth_token': 'str',
        'instance_id': 'str',
        'resource': 'str',
        'event': 'str',
        'app_type': 'str',
        'app_id': 'str',
        'rule_name': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'stage_auth_token': 'Stage-Auth-Token',
        'instance_id': 'Instance-Id',
        'resource': 'resource',
        'event': 'event',
        'app_type': 'app_type',
        'app_id': 'app_id',
        'rule_name': 'rule_name',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, stage_auth_token=None, instance_id=None, resource=None, event=None, app_type=None, app_id=None, rule_name=None, limit=10, marker='ffffffffffffffffffffffff', offset=0):
        """ListRoutingRulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._stage_auth_token = None
        self._instance_id = None
        self._resource = None
        self._event = None
        self._app_type = None
        self._app_id = None
        self._rule_name = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if stage_auth_token is not None:
            self.stage_auth_token = stage_auth_token
        if instance_id is not None:
            self.instance_id = instance_id
        if resource is not None:
            self.resource = resource
        if event is not None:
            self.event = event
        if app_type is not None:
            self.app_type = app_type
        if app_id is not None:
            self.app_id = app_id
        if rule_name is not None:
            self.rule_name = rule_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def stage_auth_token(self):
        """Gets the stage_auth_token of this ListRoutingRulesRequest.


        :return: The stage_auth_token of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._stage_auth_token

    @stage_auth_token.setter
    def stage_auth_token(self, stage_auth_token):
        """Sets the stage_auth_token of this ListRoutingRulesRequest.


        :param stage_auth_token: The stage_auth_token of this ListRoutingRulesRequest.
        :type: str
        """
        self._stage_auth_token = stage_auth_token

    @property
    def instance_id(self):
        """Gets the instance_id of this ListRoutingRulesRequest.


        :return: The instance_id of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListRoutingRulesRequest.


        :param instance_id: The instance_id of this ListRoutingRulesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def resource(self):
        """Gets the resource of this ListRoutingRulesRequest.


        :return: The resource of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ListRoutingRulesRequest.


        :param resource: The resource of this ListRoutingRulesRequest.
        :type: str
        """
        self._resource = resource

    @property
    def event(self):
        """Gets the event of this ListRoutingRulesRequest.


        :return: The event of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this ListRoutingRulesRequest.


        :param event: The event of this ListRoutingRulesRequest.
        :type: str
        """
        self._event = event

    @property
    def app_type(self):
        """Gets the app_type of this ListRoutingRulesRequest.


        :return: The app_type of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ListRoutingRulesRequest.


        :param app_type: The app_type of this ListRoutingRulesRequest.
        :type: str
        """
        self._app_type = app_type

    @property
    def app_id(self):
        """Gets the app_id of this ListRoutingRulesRequest.


        :return: The app_id of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListRoutingRulesRequest.


        :param app_id: The app_id of this ListRoutingRulesRequest.
        :type: str
        """
        self._app_id = app_id

    @property
    def rule_name(self):
        """Gets the rule_name of this ListRoutingRulesRequest.


        :return: The rule_name of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ListRoutingRulesRequest.


        :param rule_name: The rule_name of this ListRoutingRulesRequest.
        :type: str
        """
        self._rule_name = rule_name

    @property
    def limit(self):
        """Gets the limit of this ListRoutingRulesRequest.


        :return: The limit of this ListRoutingRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRoutingRulesRequest.


        :param limit: The limit of this ListRoutingRulesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListRoutingRulesRequest.


        :return: The marker of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRoutingRulesRequest.


        :param marker: The marker of this ListRoutingRulesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListRoutingRulesRequest.


        :return: The offset of this ListRoutingRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRoutingRulesRequest.


        :param offset: The offset of this ListRoutingRulesRequest.
        :type: int
        """
        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListRoutingRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
