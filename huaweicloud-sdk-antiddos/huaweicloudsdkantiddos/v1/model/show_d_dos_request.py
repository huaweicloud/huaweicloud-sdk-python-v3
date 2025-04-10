# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDDosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'floating_ip_id': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'floating_ip_id': 'floating_ip_id',
        'ip': 'ip'
    }

    def __init__(self, floating_ip_id=None, ip=None):
        r"""ShowDDosRequest

        The model defined in huaweicloud sdk

        :param floating_ip_id: 用户EIP对应的ID
        :type floating_ip_id: str
        :param ip: 用户EIP
        :type ip: str
        """
        
        

        self._floating_ip_id = None
        self._ip = None
        self.discriminator = None

        self.floating_ip_id = floating_ip_id
        if ip is not None:
            self.ip = ip

    @property
    def floating_ip_id(self):
        r"""Gets the floating_ip_id of this ShowDDosRequest.

        用户EIP对应的ID

        :return: The floating_ip_id of this ShowDDosRequest.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        r"""Sets the floating_ip_id of this ShowDDosRequest.

        用户EIP对应的ID

        :param floating_ip_id: The floating_ip_id of this ShowDDosRequest.
        :type floating_ip_id: str
        """
        self._floating_ip_id = floating_ip_id

    @property
    def ip(self):
        r"""Gets the ip of this ShowDDosRequest.

        用户EIP

        :return: The ip of this ShowDDosRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ShowDDosRequest.

        用户EIP

        :param ip: The ip of this ShowDDosRequest.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, ShowDDosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
