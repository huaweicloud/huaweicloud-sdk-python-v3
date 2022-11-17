# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePublicIpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_id': 'str'
    }

    attribute_map = {
        'port_id': 'port_id'
    }

    def __init__(self, port_id=None):
        """UpdatePublicIpOption

        The model defined in huaweicloud sdk

        :param port_id: vip对应的port的ID可为空。当为空的时候，代表解绑原有eip的关系。不为空时，代表绑定eip和vip。
        :type port_id: str
        """
        
        

        self._port_id = None
        self.discriminator = None

        self.port_id = port_id

    @property
    def port_id(self):
        """Gets the port_id of this UpdatePublicIpOption.

        vip对应的port的ID可为空。当为空的时候，代表解绑原有eip的关系。不为空时，代表绑定eip和vip。

        :return: The port_id of this UpdatePublicIpOption.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this UpdatePublicIpOption.

        vip对应的port的ID可为空。当为空的时候，代表解绑原有eip的关系。不为空时，代表绑定eip和vip。

        :param port_id: The port_id of this UpdatePublicIpOption.
        :type port_id: str
        """
        self._port_id = port_id

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
        if not isinstance(other, UpdatePublicIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
