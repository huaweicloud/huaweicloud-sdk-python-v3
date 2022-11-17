# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RolesOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_db_name': 'str',
        'role_name': 'str'
    }

    attribute_map = {
        'role_db_name': 'role_db_name',
        'role_name': 'role_name'
    }

    def __init__(self, role_db_name=None, role_name=None):
        """RolesOption

        The model defined in huaweicloud sdk

        :param role_db_name: 被继承角色所在数据库名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。
        :type role_db_name: str
        :param role_name: 被继承角色的名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。
        :type role_name: str
        """
        
        

        self._role_db_name = None
        self._role_name = None
        self.discriminator = None

        self.role_db_name = role_db_name
        self.role_name = role_name

    @property
    def role_db_name(self):
        """Gets the role_db_name of this RolesOption.

        被继承角色所在数据库名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :return: The role_db_name of this RolesOption.
        :rtype: str
        """
        return self._role_db_name

    @role_db_name.setter
    def role_db_name(self, role_db_name):
        """Sets the role_db_name of this RolesOption.

        被继承角色所在数据库名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :param role_db_name: The role_db_name of this RolesOption.
        :type role_db_name: str
        """
        self._role_db_name = role_db_name

    @property
    def role_name(self):
        """Gets the role_name of this RolesOption.

        被继承角色的名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :return: The role_name of this RolesOption.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this RolesOption.

        被继承角色的名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :param role_name: The role_name of this RolesOption.
        :type role_name: str
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
        if not isinstance(other, RolesOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
