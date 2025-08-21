# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'amount': 'int',
        'remarks': 'str'
    }

    attribute_map = {
        'type': 'type',
        'amount': 'amount',
        'remarks': 'remarks'
    }

    def __init__(self, type=None, amount=None, remarks=None):
        r"""AssetInfo

        The model defined in huaweicloud sdk

        :param type: 资产类型；服务器设备/网络设备/配件/耗材/其他
        :type type: str
        :param amount: 数量
        :type amount: int
        :param remarks: 备注
        :type remarks: str
        """
        
        

        self._type = None
        self._amount = None
        self._remarks = None
        self.discriminator = None

        self.type = type
        self.amount = amount
        if remarks is not None:
            self.remarks = remarks

    @property
    def type(self):
        r"""Gets the type of this AssetInfo.

        资产类型；服务器设备/网络设备/配件/耗材/其他

        :return: The type of this AssetInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AssetInfo.

        资产类型；服务器设备/网络设备/配件/耗材/其他

        :param type: The type of this AssetInfo.
        :type type: str
        """
        self._type = type

    @property
    def amount(self):
        r"""Gets the amount of this AssetInfo.

        数量

        :return: The amount of this AssetInfo.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this AssetInfo.

        数量

        :param amount: The amount of this AssetInfo.
        :type amount: int
        """
        self._amount = amount

    @property
    def remarks(self):
        r"""Gets the remarks of this AssetInfo.

        备注

        :return: The remarks of this AssetInfo.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this AssetInfo.

        备注

        :param remarks: The remarks of this AssetInfo.
        :type remarks: str
        """
        self._remarks = remarks

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
        if not isinstance(other, AssetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
