# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalConnectionBandwidthQuotas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota': 'int',
        'used': 'int',
        'type': 'str'
    }

    attribute_map = {
        'quota': 'quota',
        'used': 'used',
        'type': 'type'
    }

    def __init__(self, quota=None, used=None, type=None):
        """GlobalConnectionBandwidthQuotas

        The model defined in huaweicloud sdk

        :param quota: 配额大小。
        :type quota: int
        :param used: 已使用值。
        :type used: int
        :param type: 配额类型。 gcb.size：全域互联带宽大小 gcb.count：全域互联带宽数量 
        :type type: str
        """
        
        

        self._quota = None
        self._used = None
        self._type = None
        self.discriminator = None

        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used
        if type is not None:
            self.type = type

    @property
    def quota(self):
        """Gets the quota of this GlobalConnectionBandwidthQuotas.

        配额大小。

        :return: The quota of this GlobalConnectionBandwidthQuotas.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this GlobalConnectionBandwidthQuotas.

        配额大小。

        :param quota: The quota of this GlobalConnectionBandwidthQuotas.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        """Gets the used of this GlobalConnectionBandwidthQuotas.

        已使用值。

        :return: The used of this GlobalConnectionBandwidthQuotas.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this GlobalConnectionBandwidthQuotas.

        已使用值。

        :param used: The used of this GlobalConnectionBandwidthQuotas.
        :type used: int
        """
        self._used = used

    @property
    def type(self):
        """Gets the type of this GlobalConnectionBandwidthQuotas.

        配额类型。 gcb.size：全域互联带宽大小 gcb.count：全域互联带宽数量 

        :return: The type of this GlobalConnectionBandwidthQuotas.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GlobalConnectionBandwidthQuotas.

        配额类型。 gcb.size：全域互联带宽大小 gcb.count：全域互联带宽数量 

        :param type: The type of this GlobalConnectionBandwidthQuotas.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, GlobalConnectionBandwidthQuotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
