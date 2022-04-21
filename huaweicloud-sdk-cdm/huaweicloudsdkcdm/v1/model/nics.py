# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Nics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'security_group_id': 'str',
        'net_id': 'str'
    }

    attribute_map = {
        'security_group_id': 'securityGroupId',
        'net_id': 'net-id'
    }

    def __init__(self, security_group_id=None, net_id=None):
        """Nics

        The model defined in huaweicloud sdk

        :param security_group_id: 安全组ID
        :type security_group_id: str
        :param net_id: 子网ID
        :type net_id: str
        """
        
        

        self._security_group_id = None
        self._net_id = None
        self.discriminator = None

        self.security_group_id = security_group_id
        self.net_id = net_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this Nics.

        安全组ID

        :return: The security_group_id of this Nics.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this Nics.

        安全组ID

        :param security_group_id: The security_group_id of this Nics.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def net_id(self):
        """Gets the net_id of this Nics.

        子网ID

        :return: The net_id of this Nics.
        :rtype: str
        """
        return self._net_id

    @net_id.setter
    def net_id(self, net_id):
        """Sets the net_id of this Nics.

        子网ID

        :param net_id: The net_id of this Nics.
        :type net_id: str
        """
        self._net_id = net_id

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
        if not isinstance(other, Nics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
