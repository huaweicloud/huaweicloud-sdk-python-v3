# coding: utf-8

import pprint
import re

import six





class ListRuleActionsRequest:


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
        'rule_id': 'str',
        'channel': 'str',
        'app_type': 'str',
        'app_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'stage_auth_token': 'Stage-Auth-Token',
        'instance_id': 'Instance-Id',
        'rule_id': 'rule_id',
        'channel': 'channel',
        'app_type': 'app_type',
        'app_id': 'app_id',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, stage_auth_token=None, instance_id=None, rule_id=None, channel=None, app_type=None, app_id=None, limit=10, marker='ffffffffffffffffffffffff', offset=0):
        """ListRuleActionsRequest - a model defined in huaweicloud sdk"""
        
        

        self._stage_auth_token = None
        self._instance_id = None
        self._rule_id = None
        self._channel = None
        self._app_type = None
        self._app_id = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if stage_auth_token is not None:
            self.stage_auth_token = stage_auth_token
        if instance_id is not None:
            self.instance_id = instance_id
        if rule_id is not None:
            self.rule_id = rule_id
        if channel is not None:
            self.channel = channel
        if app_type is not None:
            self.app_type = app_type
        if app_id is not None:
            self.app_id = app_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def stage_auth_token(self):
        """Gets the stage_auth_token of this ListRuleActionsRequest.


        :return: The stage_auth_token of this ListRuleActionsRequest.
        :rtype: str
        """
        return self._stage_auth_token

    @stage_auth_token.setter
    def stage_auth_token(self, stage_auth_token):
        """Sets the stage_auth_token of this ListRuleActionsRequest.


        :param stage_auth_token: The stage_auth_token of this ListRuleActionsRequest.
        :type: str
        """
        self._stage_auth_token = stage_auth_token

    @property
    def instance_id(self):
        """Gets the instance_id of this ListRuleActionsRequest.


        :return: The instance_id of this ListRuleActionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListRuleActionsRequest.


        :param instance_id: The instance_id of this ListRuleActionsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def rule_id(self):
        """Gets the rule_id of this ListRuleActionsRequest.


        :return: The rule_id of this ListRuleActionsRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ListRuleActionsRequest.


        :param rule_id: The rule_id of this ListRuleActionsRequest.
        :type: str
        """
        self._rule_id = rule_id

    @property
    def channel(self):
        """Gets the channel of this ListRuleActionsRequest.


        :return: The channel of this ListRuleActionsRequest.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ListRuleActionsRequest.


        :param channel: The channel of this ListRuleActionsRequest.
        :type: str
        """
        self._channel = channel

    @property
    def app_type(self):
        """Gets the app_type of this ListRuleActionsRequest.


        :return: The app_type of this ListRuleActionsRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ListRuleActionsRequest.


        :param app_type: The app_type of this ListRuleActionsRequest.
        :type: str
        """
        self._app_type = app_type

    @property
    def app_id(self):
        """Gets the app_id of this ListRuleActionsRequest.


        :return: The app_id of this ListRuleActionsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListRuleActionsRequest.


        :param app_id: The app_id of this ListRuleActionsRequest.
        :type: str
        """
        self._app_id = app_id

    @property
    def limit(self):
        """Gets the limit of this ListRuleActionsRequest.


        :return: The limit of this ListRuleActionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRuleActionsRequest.


        :param limit: The limit of this ListRuleActionsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListRuleActionsRequest.


        :return: The marker of this ListRuleActionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRuleActionsRequest.


        :param marker: The marker of this ListRuleActionsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListRuleActionsRequest.


        :return: The offset of this ListRuleActionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRuleActionsRequest.


        :param offset: The offset of this ListRuleActionsRequest.
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
        if not isinstance(other, ListRuleActionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
