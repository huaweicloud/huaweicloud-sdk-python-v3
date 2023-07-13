# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTransitIpRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transit_ip_id': 'str'
    }

    attribute_map = {
        'transit_ip_id': 'transit_ip_id'
    }

    def __init__(self, transit_ip_id=None):
        """ShowTransitIpRequest

        The model defined in huaweicloud sdk

        :param transit_ip_id: 中转IP的ID。
        :type transit_ip_id: str
        """
        
        

        self._transit_ip_id = None
        self.discriminator = None

        self.transit_ip_id = transit_ip_id

    @property
    def transit_ip_id(self):
        """Gets the transit_ip_id of this ShowTransitIpRequest.

        中转IP的ID。

        :return: The transit_ip_id of this ShowTransitIpRequest.
        :rtype: str
        """
        return self._transit_ip_id

    @transit_ip_id.setter
    def transit_ip_id(self, transit_ip_id):
        """Sets the transit_ip_id of this ShowTransitIpRequest.

        中转IP的ID。

        :param transit_ip_id: The transit_ip_id of this ShowTransitIpRequest.
        :type transit_ip_id: str
        """
        self._transit_ip_id = transit_ip_id

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
        if not isinstance(other, ShowTransitIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
