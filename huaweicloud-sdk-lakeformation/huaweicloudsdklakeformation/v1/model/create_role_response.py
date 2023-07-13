# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRoleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_name': 'str',
        'description': 'str',
        'principal_source': 'str'
    }

    attribute_map = {
        'role_name': 'role_name',
        'description': 'description',
        'principal_source': 'principal_source'
    }

    def __init__(self, role_name=None, description=None, principal_source=None):
        """CreateRoleResponse

        The model defined in huaweicloud sdk

        :param role_name: role名字
        :type role_name: str
        :param description: 描述信息
        :type description: str
        :param principal_source: 主体来源 IAM云用户 SAML联邦 LDAP ld用户 LOCAL 本地用户 OTHER 其它
        :type principal_source: str
        """
        
        super(CreateRoleResponse, self).__init__()

        self._role_name = None
        self._description = None
        self._principal_source = None
        self.discriminator = None

        if role_name is not None:
            self.role_name = role_name
        if description is not None:
            self.description = description
        if principal_source is not None:
            self.principal_source = principal_source

    @property
    def role_name(self):
        """Gets the role_name of this CreateRoleResponse.

        role名字

        :return: The role_name of this CreateRoleResponse.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this CreateRoleResponse.

        role名字

        :param role_name: The role_name of this CreateRoleResponse.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def description(self):
        """Gets the description of this CreateRoleResponse.

        描述信息

        :return: The description of this CreateRoleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRoleResponse.

        描述信息

        :param description: The description of this CreateRoleResponse.
        :type description: str
        """
        self._description = description

    @property
    def principal_source(self):
        """Gets the principal_source of this CreateRoleResponse.

        主体来源 IAM云用户 SAML联邦 LDAP ld用户 LOCAL 本地用户 OTHER 其它

        :return: The principal_source of this CreateRoleResponse.
        :rtype: str
        """
        return self._principal_source

    @principal_source.setter
    def principal_source(self, principal_source):
        """Sets the principal_source of this CreateRoleResponse.

        主体来源 IAM云用户 SAML联邦 LDAP ld用户 LOCAL 本地用户 OTHER 其它

        :param principal_source: The principal_source of this CreateRoleResponse.
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
        if not isinstance(other, CreateRoleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
