# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicipBandwidthInfo:

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
        'charge_mode': 'str',
        'name': 'str',
        'billing_info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'size': 'size',
        'share_type': 'share_type',
        'charge_mode': 'charge_mode',
        'name': 'name',
        'billing_info': 'billing_info'
    }

    def __init__(self, id=None, size=None, share_type=None, charge_mode=None, name=None, billing_info=None):
        r"""PublicipBandwidthInfo

        The model defined in huaweicloud sdk

        :param id: 带宽ID
        :type id: str
        :param size: 功能描述：带宽大小 取值范围：默认5Mbit/s~2000Mbit/s
        :type size: int
        :param share_type: 功能说明：带宽类型,标识是否是共享带宽 取值范围：PER，WHOLE。   PER：独享带宽   WHOLE：共享带宽 约束：其中IPv6暂不支持WHOLE类型带宽。
        :type share_type: str
        :param charge_mode: 功能说明：按流量计费还是按带宽计费 取值范围： bandwidth：按带宽计费 traffic：按流量计费 95peak_plus：按增强型95计费
        :type charge_mode: str
        :param name: 功能说明：带宽名称 取值范围：1-64个字符,支持数字、字母、中文、_(下划线)、-(中划线)、.(点)
        :type name: str
        :param billing_info: 功能说明：账单信息。如果billinginfo不为空，说明是包周期的带宽
        :type billing_info: str
        """
        
        

        self._id = None
        self._size = None
        self._share_type = None
        self._charge_mode = None
        self._name = None
        self._billing_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if share_type is not None:
            self.share_type = share_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if name is not None:
            self.name = name
        if billing_info is not None:
            self.billing_info = billing_info

    @property
    def id(self):
        r"""Gets the id of this PublicipBandwidthInfo.

        带宽ID

        :return: The id of this PublicipBandwidthInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublicipBandwidthInfo.

        带宽ID

        :param id: The id of this PublicipBandwidthInfo.
        :type id: str
        """
        self._id = id

    @property
    def size(self):
        r"""Gets the size of this PublicipBandwidthInfo.

        功能描述：带宽大小 取值范围：默认5Mbit/s~2000Mbit/s

        :return: The size of this PublicipBandwidthInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this PublicipBandwidthInfo.

        功能描述：带宽大小 取值范围：默认5Mbit/s~2000Mbit/s

        :param size: The size of this PublicipBandwidthInfo.
        :type size: int
        """
        self._size = size

    @property
    def share_type(self):
        r"""Gets the share_type of this PublicipBandwidthInfo.

        功能说明：带宽类型,标识是否是共享带宽 取值范围：PER，WHOLE。   PER：独享带宽   WHOLE：共享带宽 约束：其中IPv6暂不支持WHOLE类型带宽。

        :return: The share_type of this PublicipBandwidthInfo.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this PublicipBandwidthInfo.

        功能说明：带宽类型,标识是否是共享带宽 取值范围：PER，WHOLE。   PER：独享带宽   WHOLE：共享带宽 约束：其中IPv6暂不支持WHOLE类型带宽。

        :param share_type: The share_type of this PublicipBandwidthInfo.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this PublicipBandwidthInfo.

        功能说明：按流量计费还是按带宽计费 取值范围： bandwidth：按带宽计费 traffic：按流量计费 95peak_plus：按增强型95计费

        :return: The charge_mode of this PublicipBandwidthInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this PublicipBandwidthInfo.

        功能说明：按流量计费还是按带宽计费 取值范围： bandwidth：按带宽计费 traffic：按流量计费 95peak_plus：按增强型95计费

        :param charge_mode: The charge_mode of this PublicipBandwidthInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def name(self):
        r"""Gets the name of this PublicipBandwidthInfo.

        功能说明：带宽名称 取值范围：1-64个字符,支持数字、字母、中文、_(下划线)、-(中划线)、.(点)

        :return: The name of this PublicipBandwidthInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PublicipBandwidthInfo.

        功能说明：带宽名称 取值范围：1-64个字符,支持数字、字母、中文、_(下划线)、-(中划线)、.(点)

        :param name: The name of this PublicipBandwidthInfo.
        :type name: str
        """
        self._name = name

    @property
    def billing_info(self):
        r"""Gets the billing_info of this PublicipBandwidthInfo.

        功能说明：账单信息。如果billinginfo不为空，说明是包周期的带宽

        :return: The billing_info of this PublicipBandwidthInfo.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this PublicipBandwidthInfo.

        功能说明：账单信息。如果billinginfo不为空，说明是包周期的带宽

        :param billing_info: The billing_info of this PublicipBandwidthInfo.
        :type billing_info: str
        """
        self._billing_info = billing_info

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
        if not isinstance(other, PublicipBandwidthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
