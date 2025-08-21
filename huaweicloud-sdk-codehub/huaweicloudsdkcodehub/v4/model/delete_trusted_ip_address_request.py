# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTrustedIpAddressRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'ip_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'ip_id': 'ip_id'
    }

    def __init__(self, id=None, ip_id=None):
        r"""DeleteTrustedIpAddressRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 仓库id，代码仓首页，Repository ID后的数字Id。
        :type id: int
        :param ip_id: **参数解释：** ip白名单id。
        :type ip_id: int
        """
        
        

        self._id = None
        self._ip_id = None
        self.discriminator = None

        self.id = id
        self.ip_id = ip_id

    @property
    def id(self):
        r"""Gets the id of this DeleteTrustedIpAddressRequest.

        **参数解释：** 仓库id，代码仓首页，Repository ID后的数字Id。

        :return: The id of this DeleteTrustedIpAddressRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteTrustedIpAddressRequest.

        **参数解释：** 仓库id，代码仓首页，Repository ID后的数字Id。

        :param id: The id of this DeleteTrustedIpAddressRequest.
        :type id: int
        """
        self._id = id

    @property
    def ip_id(self):
        r"""Gets the ip_id of this DeleteTrustedIpAddressRequest.

        **参数解释：** ip白名单id。

        :return: The ip_id of this DeleteTrustedIpAddressRequest.
        :rtype: int
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        r"""Sets the ip_id of this DeleteTrustedIpAddressRequest.

        **参数解释：** ip白名单id。

        :param ip_id: The ip_id of this DeleteTrustedIpAddressRequest.
        :type ip_id: int
        """
        self._ip_id = ip_id

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
        if not isinstance(other, DeleteTrustedIpAddressRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
