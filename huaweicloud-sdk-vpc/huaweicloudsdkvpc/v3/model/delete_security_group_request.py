# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSecurityGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_group_id': 'str'
    }

    attribute_map = {
        'security_group_id': 'security_group_id'
    }

    def __init__(self, security_group_id=None):
        r"""DeleteSecurityGroupRequest

        The model defined in huaweicloud sdk

        :param security_group_id: 安全组资源ID
        :type security_group_id: str
        """
        
        

        self._security_group_id = None
        self.discriminator = None

        self.security_group_id = security_group_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this DeleteSecurityGroupRequest.

        安全组资源ID

        :return: The security_group_id of this DeleteSecurityGroupRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this DeleteSecurityGroupRequest.

        安全组资源ID

        :param security_group_id: The security_group_id of this DeleteSecurityGroupRequest.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

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
        if not isinstance(other, DeleteSecurityGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
