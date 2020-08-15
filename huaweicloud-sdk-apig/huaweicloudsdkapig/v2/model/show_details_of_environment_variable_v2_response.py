# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowDetailsOfEnvironmentVariableV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'variable_value': 'str',
        'env_id': 'str',
        'group_id': 'str',
        'id': 'str',
        'variable_name': 'str'
    }

    attribute_map = {
        'variable_value': 'variable_value',
        'env_id': 'env_id',
        'group_id': 'group_id',
        'id': 'id',
        'variable_name': 'variable_name'
    }

    def __init__(self, variable_value=None, env_id=None, group_id=None, id=None, variable_name=None):
        """ShowDetailsOfEnvironmentVariableV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._variable_value = None
        self._env_id = None
        self._group_id = None
        self._id = None
        self._variable_name = None
        self.discriminator = None

        if variable_value is not None:
            self.variable_value = variable_value
        if env_id is not None:
            self.env_id = env_id
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if variable_name is not None:
            self.variable_name = variable_name

    @property
    def variable_value(self):
        """Gets the variable_value of this ShowDetailsOfEnvironmentVariableV2Response.

        变量值

        :return: The variable_value of this ShowDetailsOfEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._variable_value

    @variable_value.setter
    def variable_value(self, variable_value):
        """Sets the variable_value of this ShowDetailsOfEnvironmentVariableV2Response.

        变量值

        :param variable_value: The variable_value of this ShowDetailsOfEnvironmentVariableV2Response.
        :type: str
        """
        self._variable_value = variable_value

    @property
    def env_id(self):
        """Gets the env_id of this ShowDetailsOfEnvironmentVariableV2Response.

        环境编号

        :return: The env_id of this ShowDetailsOfEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ShowDetailsOfEnvironmentVariableV2Response.

        环境编号

        :param env_id: The env_id of this ShowDetailsOfEnvironmentVariableV2Response.
        :type: str
        """
        self._env_id = env_id

    @property
    def group_id(self):
        """Gets the group_id of this ShowDetailsOfEnvironmentVariableV2Response.

        API分组编号

        :return: The group_id of this ShowDetailsOfEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowDetailsOfEnvironmentVariableV2Response.

        API分组编号

        :param group_id: The group_id of this ShowDetailsOfEnvironmentVariableV2Response.
        :type: str
        """
        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this ShowDetailsOfEnvironmentVariableV2Response.

        环境变量编号

        :return: The id of this ShowDetailsOfEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDetailsOfEnvironmentVariableV2Response.

        环境变量编号

        :param id: The id of this ShowDetailsOfEnvironmentVariableV2Response.
        :type: str
        """
        self._id = id

    @property
    def variable_name(self):
        """Gets the variable_name of this ShowDetailsOfEnvironmentVariableV2Response.

        变量名

        :return: The variable_name of this ShowDetailsOfEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this ShowDetailsOfEnvironmentVariableV2Response.

        变量名

        :param variable_name: The variable_name of this ShowDetailsOfEnvironmentVariableV2Response.
        :type: str
        """
        self._variable_name = variable_name

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
        if not isinstance(other, ShowDetailsOfEnvironmentVariableV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
