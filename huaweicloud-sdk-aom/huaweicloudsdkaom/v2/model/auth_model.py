# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'bool',
        'role_name': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'role_name': 'role_name'
    }

    def __init__(self, status=None, role_name=None):
        """AuthModel

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: bool
        :param role_name: 角色列表
        :type role_name: list[str]
        """
        
        

        self._status = None
        self._role_name = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if role_name is not None:
            self.role_name = role_name

    @property
    def status(self):
        """Gets the status of this AuthModel.

        状态

        :return: The status of this AuthModel.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuthModel.

        状态

        :param status: The status of this AuthModel.
        :type status: bool
        """
        self._status = status

    @property
    def role_name(self):
        """Gets the role_name of this AuthModel.

        角色列表

        :return: The role_name of this AuthModel.
        :rtype: list[str]
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this AuthModel.

        角色列表

        :param role_name: The role_name of this AuthModel.
        :type role_name: list[str]
        """
        self._role_name = role_name

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
        if not isinstance(other, AuthModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
