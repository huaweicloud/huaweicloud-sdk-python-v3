# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSpecsPriceFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        r"""ResourceSpecsPriceFilter

        The model defined in huaweicloud sdk

        :param key: 过滤条件的key值，必填，支持RESOURCE_SPEC：资源规格编码、CHARGING_MODE：计费模式
        :type key: str
        :param value: 过滤条件的value值，必填，不支持模糊查询。当key&#x3D;CHARGING_MODE时，此处取值如下：PERIOD：包年/包月、ON_DEMAND：按需、ONE_TIME：一次性、ON_DEMAND_PKG：按需套餐包
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this ResourceSpecsPriceFilter.

        过滤条件的key值，必填，支持RESOURCE_SPEC：资源规格编码、CHARGING_MODE：计费模式

        :return: The key of this ResourceSpecsPriceFilter.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ResourceSpecsPriceFilter.

        过滤条件的key值，必填，支持RESOURCE_SPEC：资源规格编码、CHARGING_MODE：计费模式

        :param key: The key of this ResourceSpecsPriceFilter.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this ResourceSpecsPriceFilter.

        过滤条件的value值，必填，不支持模糊查询。当key=CHARGING_MODE时，此处取值如下：PERIOD：包年/包月、ON_DEMAND：按需、ONE_TIME：一次性、ON_DEMAND_PKG：按需套餐包

        :return: The value of this ResourceSpecsPriceFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ResourceSpecsPriceFilter.

        过滤条件的value值，必填，不支持模糊查询。当key=CHARGING_MODE时，此处取值如下：PERIOD：包年/包月、ON_DEMAND：按需、ONE_TIME：一次性、ON_DEMAND_PKG：按需套餐包

        :param value: The value of this ResourceSpecsPriceFilter.
        :type value: str
        """
        self._value = value

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceSpecsPriceFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
