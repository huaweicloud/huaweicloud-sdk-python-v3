# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcEipBandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'size': 'int',
        'share_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'size': 'size',
        'share_type': 'share_type',
        'name': 'name'
    }

    def __init__(self, id=None, size=None, share_type=None, name=None):
        r"""HwcEipBandwidth

        The model defined in huaweicloud sdk

        :param id: 带宽ID
        :type id: str
        :param size: 带宽大小 取值范围：默认5Mbit/s~2000Mbit/s
        :type size: int
        :param share_type: 带宽类型，标识是否是共享带宽 取值范围： PER：独享带宽 WHOLE：共享带宽 约束：其中IPv6暂不支持WHOLE类型带宽。
        :type share_type: str
        :param name: 带宽名称
        :type name: str
        """
        
        

        self._id = None
        self._size = None
        self._share_type = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if share_type is not None:
            self.share_type = share_type
        if name is not None:
            self.name = name

    @property
    def id(self):
        r"""Gets the id of this HwcEipBandwidth.

        带宽ID

        :return: The id of this HwcEipBandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HwcEipBandwidth.

        带宽ID

        :param id: The id of this HwcEipBandwidth.
        :type id: str
        """
        self._id = id

    @property
    def size(self):
        r"""Gets the size of this HwcEipBandwidth.

        带宽大小 取值范围：默认5Mbit/s~2000Mbit/s

        :return: The size of this HwcEipBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this HwcEipBandwidth.

        带宽大小 取值范围：默认5Mbit/s~2000Mbit/s

        :param size: The size of this HwcEipBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def share_type(self):
        r"""Gets the share_type of this HwcEipBandwidth.

        带宽类型，标识是否是共享带宽 取值范围： PER：独享带宽 WHOLE：共享带宽 约束：其中IPv6暂不支持WHOLE类型带宽。

        :return: The share_type of this HwcEipBandwidth.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this HwcEipBandwidth.

        带宽类型，标识是否是共享带宽 取值范围： PER：独享带宽 WHOLE：共享带宽 约束：其中IPv6暂不支持WHOLE类型带宽。

        :param share_type: The share_type of this HwcEipBandwidth.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def name(self):
        r"""Gets the name of this HwcEipBandwidth.

        带宽名称

        :return: The name of this HwcEipBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HwcEipBandwidth.

        带宽名称

        :param name: The name of this HwcEipBandwidth.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, HwcEipBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
