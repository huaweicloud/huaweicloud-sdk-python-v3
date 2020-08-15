# coding: utf-8

import pprint
import re

import six





class ListEnvironmentVariablesV2Request:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'group_id': 'str',
        'env_id': 'str',
        'variable_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'precise_search': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group_id': 'group_id',
        'env_id': 'env_id',
        'variable_name': 'variable_name',
        'offset': 'offset',
        'limit': 'limit',
        'precise_search': 'precise_search'
    }

    def __init__(self, instance_id=None, group_id=None, env_id=None, variable_name=None, offset=0, limit=20, precise_search=None):
        """ListEnvironmentVariablesV2Request - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._group_id = None
        self._env_id = None
        self._variable_name = None
        self._offset = None
        self._limit = None
        self._precise_search = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group_id = group_id
        if env_id is not None:
            self.env_id = env_id
        if variable_name is not None:
            self.variable_name = variable_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if precise_search is not None:
            self.precise_search = precise_search

    @property
    def instance_id(self):
        """Gets the instance_id of this ListEnvironmentVariablesV2Request.


        :return: The instance_id of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListEnvironmentVariablesV2Request.


        :param instance_id: The instance_id of this ListEnvironmentVariablesV2Request.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def group_id(self):
        """Gets the group_id of this ListEnvironmentVariablesV2Request.


        :return: The group_id of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListEnvironmentVariablesV2Request.


        :param group_id: The group_id of this ListEnvironmentVariablesV2Request.
        :type: str
        """
        self._group_id = group_id

    @property
    def env_id(self):
        """Gets the env_id of this ListEnvironmentVariablesV2Request.


        :return: The env_id of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ListEnvironmentVariablesV2Request.


        :param env_id: The env_id of this ListEnvironmentVariablesV2Request.
        :type: str
        """
        self._env_id = env_id

    @property
    def variable_name(self):
        """Gets the variable_name of this ListEnvironmentVariablesV2Request.


        :return: The variable_name of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this ListEnvironmentVariablesV2Request.


        :param variable_name: The variable_name of this ListEnvironmentVariablesV2Request.
        :type: str
        """
        self._variable_name = variable_name

    @property
    def offset(self):
        """Gets the offset of this ListEnvironmentVariablesV2Request.


        :return: The offset of this ListEnvironmentVariablesV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnvironmentVariablesV2Request.


        :param offset: The offset of this ListEnvironmentVariablesV2Request.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEnvironmentVariablesV2Request.


        :return: The limit of this ListEnvironmentVariablesV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnvironmentVariablesV2Request.


        :param limit: The limit of this ListEnvironmentVariablesV2Request.
        :type: int
        """
        self._limit = limit

    @property
    def precise_search(self):
        """Gets the precise_search of this ListEnvironmentVariablesV2Request.


        :return: The precise_search of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        """Sets the precise_search of this ListEnvironmentVariablesV2Request.


        :param precise_search: The precise_search of this ListEnvironmentVariablesV2Request.
        :type: str
        """
        self._precise_search = precise_search

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
        if not isinstance(other, ListEnvironmentVariablesV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
