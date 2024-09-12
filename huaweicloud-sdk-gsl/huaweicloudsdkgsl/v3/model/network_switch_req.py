# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkSwitchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cid': 'str',
        'carrier_type': 'int'
    }

    attribute_map = {
        'cid': 'cid',
        'carrier_type': 'carrier_type'
    }

    def __init__(self, cid=None, carrier_type=None):
        """NetworkSwitchReq

        The model defined in huaweicloud sdk

        :param cid: 容器ID
        :type cid: str
        :param carrier_type: 切换的目标网络
        :type carrier_type: int
        """
        
        

        self._cid = None
        self._carrier_type = None
        self.discriminator = None

        if cid is not None:
            self.cid = cid
        self.carrier_type = carrier_type

    @property
    def cid(self):
        """Gets the cid of this NetworkSwitchReq.

        容器ID

        :return: The cid of this NetworkSwitchReq.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this NetworkSwitchReq.

        容器ID

        :param cid: The cid of this NetworkSwitchReq.
        :type cid: str
        """
        self._cid = cid

    @property
    def carrier_type(self):
        """Gets the carrier_type of this NetworkSwitchReq.

        切换的目标网络

        :return: The carrier_type of this NetworkSwitchReq.
        :rtype: int
        """
        return self._carrier_type

    @carrier_type.setter
    def carrier_type(self, carrier_type):
        """Sets the carrier_type of this NetworkSwitchReq.

        切换的目标网络

        :param carrier_type: The carrier_type of this NetworkSwitchReq.
        :type carrier_type: int
        """
        self._carrier_type = carrier_type

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
        if not isinstance(other, NetworkSwitchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
