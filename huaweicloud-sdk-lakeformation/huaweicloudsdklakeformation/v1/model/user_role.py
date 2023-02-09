# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserRole:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'principal_type': 'str',
        'principal_name': 'str',
        'principal_source': 'str'
    }

    attribute_map = {
        'principal_type': 'principal_type',
        'principal_name': 'principal_name',
        'principal_source': 'principal_source'
    }

    def __init__(self, principal_type=None, principal_name=None, principal_source=None):
        """UserRole

        The model defined in huaweicloud sdk

        :param principal_type: 主体类型 USER用户 GROUP组
        :type principal_type: str
        :param principal_name: 主体名称
        :type principal_name: str
        :param principal_source: 主体来源 IAM云用户 SAML联邦 LDAP ld用户 LOCAL 本地用户 OTHER 其它
        :type principal_source: str
        """
        
        

        self._principal_type = None
        self._principal_name = None
        self._principal_source = None
        self.discriminator = None

        self.principal_type = principal_type
        self.principal_name = principal_name
        self.principal_source = principal_source

    @property
    def principal_type(self):
        """Gets the principal_type of this UserRole.

        主体类型 USER用户 GROUP组

        :return: The principal_type of this UserRole.
        :rtype: str
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        """Sets the principal_type of this UserRole.

        主体类型 USER用户 GROUP组

        :param principal_type: The principal_type of this UserRole.
        :type principal_type: str
        """
        self._principal_type = principal_type

    @property
    def principal_name(self):
        """Gets the principal_name of this UserRole.

        主体名称

        :return: The principal_name of this UserRole.
        :rtype: str
        """
        return self._principal_name

    @principal_name.setter
    def principal_name(self, principal_name):
        """Sets the principal_name of this UserRole.

        主体名称

        :param principal_name: The principal_name of this UserRole.
        :type principal_name: str
        """
        self._principal_name = principal_name

    @property
    def principal_source(self):
        """Gets the principal_source of this UserRole.

        主体来源 IAM云用户 SAML联邦 LDAP ld用户 LOCAL 本地用户 OTHER 其它

        :return: The principal_source of this UserRole.
        :rtype: str
        """
        return self._principal_source

    @principal_source.setter
    def principal_source(self, principal_source):
        """Sets the principal_source of this UserRole.

        主体来源 IAM云用户 SAML联邦 LDAP ld用户 LOCAL 本地用户 OTHER 其它

        :param principal_source: The principal_source of this UserRole.
        :type principal_source: str
        """
        self._principal_source = principal_source

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
        if not isinstance(other, UserRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
