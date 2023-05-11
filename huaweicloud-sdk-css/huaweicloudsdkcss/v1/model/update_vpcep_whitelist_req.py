# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpcepWhitelistReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_permissions': 'list[str]'
    }

    attribute_map = {
        'vpc_permissions': 'vpcPermissions'
    }

    def __init__(self, vpc_permissions=None):
        """UpdateVpcepWhitelistReq

        The model defined in huaweicloud sdk

        :param vpc_permissions: 白名单(用户的账号ID)。
        :type vpc_permissions: list[str]
        """
        
        

        self._vpc_permissions = None
        self.discriminator = None

        self.vpc_permissions = vpc_permissions

    @property
    def vpc_permissions(self):
        """Gets the vpc_permissions of this UpdateVpcepWhitelistReq.

        白名单(用户的账号ID)。

        :return: The vpc_permissions of this UpdateVpcepWhitelistReq.
        :rtype: list[str]
        """
        return self._vpc_permissions

    @vpc_permissions.setter
    def vpc_permissions(self, vpc_permissions):
        """Sets the vpc_permissions of this UpdateVpcepWhitelistReq.

        白名单(用户的账号ID)。

        :param vpc_permissions: The vpc_permissions of this UpdateVpcepWhitelistReq.
        :type vpc_permissions: list[str]
        """
        self._vpc_permissions = vpc_permissions

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
        if not isinstance(other, UpdateVpcepWhitelistReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
