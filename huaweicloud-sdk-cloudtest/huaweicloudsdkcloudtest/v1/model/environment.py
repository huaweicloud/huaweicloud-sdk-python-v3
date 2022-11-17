# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Environment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'environment_id': 'str',
        'environment_name': 'str',
        'environment_description': 'str',
        'is_default': 'bool'
    }

    attribute_map = {
        'environment_id': 'environment_id',
        'environment_name': 'environment_name',
        'environment_description': 'environment_description',
        'is_default': 'is_default'
    }

    def __init__(self, environment_id=None, environment_name=None, environment_description=None, is_default=None):
        """Environment

        The model defined in huaweicloud sdk

        :param environment_id: 环境分组id
        :type environment_id: str
        :param environment_name: 环境分组名
        :type environment_name: str
        :param environment_description: 环境分组描述
        :type environment_description: str
        :param is_default: 是否是默认环境
        :type is_default: bool
        """
        
        

        self._environment_id = None
        self._environment_name = None
        self._environment_description = None
        self._is_default = None
        self.discriminator = None

        if environment_id is not None:
            self.environment_id = environment_id
        if environment_name is not None:
            self.environment_name = environment_name
        if environment_description is not None:
            self.environment_description = environment_description
        if is_default is not None:
            self.is_default = is_default

    @property
    def environment_id(self):
        """Gets the environment_id of this Environment.

        环境分组id

        :return: The environment_id of this Environment.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this Environment.

        环境分组id

        :param environment_id: The environment_id of this Environment.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def environment_name(self):
        """Gets the environment_name of this Environment.

        环境分组名

        :return: The environment_name of this Environment.
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this Environment.

        环境分组名

        :param environment_name: The environment_name of this Environment.
        :type environment_name: str
        """
        self._environment_name = environment_name

    @property
    def environment_description(self):
        """Gets the environment_description of this Environment.

        环境分组描述

        :return: The environment_description of this Environment.
        :rtype: str
        """
        return self._environment_description

    @environment_description.setter
    def environment_description(self, environment_description):
        """Sets the environment_description of this Environment.

        环境分组描述

        :param environment_description: The environment_description of this Environment.
        :type environment_description: str
        """
        self._environment_description = environment_description

    @property
    def is_default(self):
        """Gets the is_default of this Environment.

        是否是默认环境

        :return: The is_default of this Environment.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this Environment.

        是否是默认环境

        :param is_default: The is_default of this Environment.
        :type is_default: bool
        """
        self._is_default = is_default

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Environment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
