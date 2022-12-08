# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyBindEipRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_ip': 'str',
        'public_ip_id': 'str'
    }

    attribute_map = {
        'public_ip': 'public_ip',
        'public_ip_id': 'public_ip_id'
    }

    def __init__(self, public_ip=None, public_ip_id=None):
        """ModifyBindEipRequest

        The model defined in huaweicloud sdk

        :param public_ip: 待绑定的弹性公网IP地址。
        :type public_ip: str
        :param public_ip_id: 弹性公网IP地址对应的ID。
        :type public_ip_id: str
        """
        
        

        self._public_ip = None
        self._public_ip_id = None
        self.discriminator = None

        self.public_ip = public_ip
        self.public_ip_id = public_ip_id

    @property
    def public_ip(self):
        """Gets the public_ip of this ModifyBindEipRequest.

        待绑定的弹性公网IP地址。

        :return: The public_ip of this ModifyBindEipRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ModifyBindEipRequest.

        待绑定的弹性公网IP地址。

        :param public_ip: The public_ip of this ModifyBindEipRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def public_ip_id(self):
        """Gets the public_ip_id of this ModifyBindEipRequest.

        弹性公网IP地址对应的ID。

        :return: The public_ip_id of this ModifyBindEipRequest.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        """Sets the public_ip_id of this ModifyBindEipRequest.

        弹性公网IP地址对应的ID。

        :param public_ip_id: The public_ip_id of this ModifyBindEipRequest.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

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
        if not isinstance(other, ModifyBindEipRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
