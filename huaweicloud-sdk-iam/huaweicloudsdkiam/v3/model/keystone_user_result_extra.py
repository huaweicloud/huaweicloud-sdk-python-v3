# coding: utf-8

import pprint
import re

import six





class KeystoneUserResultExtra:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'pwd_status': 'bool',
        'last_project_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'pwd_status': 'pwd_status',
        'last_project_id': 'last_project_id'
    }

    def __init__(self, description=None, pwd_status=None, last_project_id=None):
        """KeystoneUserResultExtra - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._pwd_status = None
        self._last_project_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if pwd_status is not None:
            self.pwd_status = pwd_status
        if last_project_id is not None:
            self.last_project_id = last_project_id

    @property
    def description(self):
        """Gets the description of this KeystoneUserResultExtra.

        IAM用户描述信息。

        :return: The description of this KeystoneUserResultExtra.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeystoneUserResultExtra.

        IAM用户描述信息。

        :param description: The description of this KeystoneUserResultExtra.
        :type: str
        """
        self._description = description

    @property
    def pwd_status(self):
        """Gets the pwd_status of this KeystoneUserResultExtra.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :return: The pwd_status of this KeystoneUserResultExtra.
        :rtype: bool
        """
        return self._pwd_status

    @pwd_status.setter
    def pwd_status(self, pwd_status):
        """Sets the pwd_status of this KeystoneUserResultExtra.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :param pwd_status: The pwd_status of this KeystoneUserResultExtra.
        :type: bool
        """
        self._pwd_status = pwd_status

    @property
    def last_project_id(self):
        """Gets the last_project_id of this KeystoneUserResultExtra.

        IAM用户退出系统前，在控制台最后访问的项目ID。

        :return: The last_project_id of this KeystoneUserResultExtra.
        :rtype: str
        """
        return self._last_project_id

    @last_project_id.setter
    def last_project_id(self, last_project_id):
        """Sets the last_project_id of this KeystoneUserResultExtra.

        IAM用户退出系统前，在控制台最后访问的项目ID。

        :param last_project_id: The last_project_id of this KeystoneUserResultExtra.
        :type: str
        """
        self._last_project_id = last_project_id

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
        if not isinstance(other, KeystoneUserResultExtra):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
