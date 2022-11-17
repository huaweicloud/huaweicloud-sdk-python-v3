# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppAclCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_acl_type': 'str',
        'app_acl_values': 'list[str]'
    }

    attribute_map = {
        'app_acl_type': 'app_acl_type',
        'app_acl_values': 'app_acl_values'
    }

    def __init__(self, app_acl_type=None, app_acl_values=None):
        """AppAclCreate

        The model defined in huaweicloud sdk

        :param app_acl_type: 类型 -  PERMIT (白名单类型) -  DENY (黑名单类型)
        :type app_acl_type: str
        :param app_acl_values: ACL策略值，支持IP、IP范围和CIDR方式。IP范围以英文中划线分隔。
        :type app_acl_values: list[str]
        """
        
        

        self._app_acl_type = None
        self._app_acl_values = None
        self.discriminator = None

        self.app_acl_type = app_acl_type
        self.app_acl_values = app_acl_values

    @property
    def app_acl_type(self):
        """Gets the app_acl_type of this AppAclCreate.

        类型 -  PERMIT (白名单类型) -  DENY (黑名单类型)

        :return: The app_acl_type of this AppAclCreate.
        :rtype: str
        """
        return self._app_acl_type

    @app_acl_type.setter
    def app_acl_type(self, app_acl_type):
        """Sets the app_acl_type of this AppAclCreate.

        类型 -  PERMIT (白名单类型) -  DENY (黑名单类型)

        :param app_acl_type: The app_acl_type of this AppAclCreate.
        :type app_acl_type: str
        """
        self._app_acl_type = app_acl_type

    @property
    def app_acl_values(self):
        """Gets the app_acl_values of this AppAclCreate.

        ACL策略值，支持IP、IP范围和CIDR方式。IP范围以英文中划线分隔。

        :return: The app_acl_values of this AppAclCreate.
        :rtype: list[str]
        """
        return self._app_acl_values

    @app_acl_values.setter
    def app_acl_values(self, app_acl_values):
        """Sets the app_acl_values of this AppAclCreate.

        ACL策略值，支持IP、IP范围和CIDR方式。IP范围以英文中划线分隔。

        :param app_acl_values: The app_acl_values of this AppAclCreate.
        :type app_acl_values: list[str]
        """
        self._app_acl_values = app_acl_values

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
        if not isinstance(other, AppAclCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
