# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInternetBandwidthRequestBodyInternetBandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'size': 'int',
        'charge_mode': 'str',
        'ingress_size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'size': 'size',
        'charge_mode': 'charge_mode',
        'ingress_size': 'ingress_size'
    }

    def __init__(self, name=None, description=None, size=None, charge_mode=None, ingress_size=None):
        r"""UpdateInternetBandwidthRequestBodyInternetBandwidth

        The model defined in huaweicloud sdk

        :param name: - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。
        :type description: str
        :param size: 全域公网带宽大小（出云方向）
        :type size: int
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param ingress_size: 全域公网带宽大小（入云方向）
        :type ingress_size: int
        """
        
        

        self._name = None
        self._description = None
        self._size = None
        self._charge_mode = None
        self._ingress_size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if size is not None:
            self.size = size
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if ingress_size is not None:
            self.ingress_size = ingress_size

    @property
    def name(self):
        r"""Gets the name of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :return: The description of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :param description: The description of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :type description: str
        """
        self._description = description

    @property
    def size(self):
        r"""Gets the size of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽大小（出云方向）

        :return: The size of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽大小（出云方向）

        :param size: The size of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        计费模式

        :return: The charge_mode of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        计费模式

        :param charge_mode: The charge_mode of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def ingress_size(self):
        r"""Gets the ingress_size of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽大小（入云方向）

        :return: The ingress_size of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: int
        """
        return self._ingress_size

    @ingress_size.setter
    def ingress_size(self, ingress_size):
        r"""Sets the ingress_size of this UpdateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽大小（入云方向）

        :param ingress_size: The ingress_size of this UpdateInternetBandwidthRequestBodyInternetBandwidth.
        :type ingress_size: int
        """
        self._ingress_size = ingress_size

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
        if not isinstance(other, UpdateInternetBandwidthRequestBodyInternetBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
