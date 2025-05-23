# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetHostPrivilegeRequestV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'hosts': 'list[str]'
    }

    attribute_map = {
        'user_name': 'user_name',
        'hosts': 'hosts'
    }

    def __init__(self, user_name=None, hosts=None):
        r"""SetHostPrivilegeRequestV3

        The model defined in huaweicloud sdk

        :param user_name: 数据库用户名
        :type user_name: str
        :param hosts: host信息
        :type hosts: list[str]
        """
        
        

        self._user_name = None
        self._hosts = None
        self.discriminator = None

        self.user_name = user_name
        self.hosts = hosts

    @property
    def user_name(self):
        r"""Gets the user_name of this SetHostPrivilegeRequestV3.

        数据库用户名

        :return: The user_name of this SetHostPrivilegeRequestV3.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SetHostPrivilegeRequestV3.

        数据库用户名

        :param user_name: The user_name of this SetHostPrivilegeRequestV3.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def hosts(self):
        r"""Gets the hosts of this SetHostPrivilegeRequestV3.

        host信息

        :return: The hosts of this SetHostPrivilegeRequestV3.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this SetHostPrivilegeRequestV3.

        host信息

        :param hosts: The hosts of this SetHostPrivilegeRequestV3.
        :type hosts: list[str]
        """
        self._hosts = hosts

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
        if not isinstance(other, SetHostPrivilegeRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
