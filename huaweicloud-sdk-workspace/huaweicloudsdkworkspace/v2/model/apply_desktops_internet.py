# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyDesktopsInternet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'eip_type': 'str',
        'eip_charge_mode': 'str',
        'bandwidth_size': 'int',
        'count': 'int'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'eip_type': 'eip_type',
        'eip_charge_mode': 'eip_charge_mode',
        'bandwidth_size': 'bandwidth_size',
        'count': 'count'
    }

    def __init__(self, desktop_ids=None, eip_type=None, eip_charge_mode=None, bandwidth_size=None, count=None):
        r"""ApplyDesktopsInternet

        The model defined in huaweicloud sdk

        :param desktop_ids: 需要开通上网功能的桌面id列表。
        :type desktop_ids: list[str]
        :param eip_type: 支持的类型请参考EIP服务支持的类型。可通过调用如下链接的接口查询，https://support.huaweicloud.com/api-eip/ShowPublicIpType.html。
        :type eip_type: str
        :param eip_charge_mode: eip带宽计费模式 - TRAFFIC：按流量计费。 - BANDWIDTH：按带宽计费。
        :type eip_charge_mode: str
        :param bandwidth_size: 带宽大小，单位Mbit/s。默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。
        :type bandwidth_size: int
        :param count: 需要购买EIP的数量，当desktop_ids为空时需要填，兼容单独购买EIP场景。
        :type count: int
        """
        
        

        self._desktop_ids = None
        self._eip_type = None
        self._eip_charge_mode = None
        self._bandwidth_size = None
        self._count = None
        self.discriminator = None

        if desktop_ids is not None:
            self.desktop_ids = desktop_ids
        self.eip_type = eip_type
        self.eip_charge_mode = eip_charge_mode
        self.bandwidth_size = bandwidth_size
        if count is not None:
            self.count = count

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this ApplyDesktopsInternet.

        需要开通上网功能的桌面id列表。

        :return: The desktop_ids of this ApplyDesktopsInternet.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this ApplyDesktopsInternet.

        需要开通上网功能的桌面id列表。

        :param desktop_ids: The desktop_ids of this ApplyDesktopsInternet.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def eip_type(self):
        r"""Gets the eip_type of this ApplyDesktopsInternet.

        支持的类型请参考EIP服务支持的类型。可通过调用如下链接的接口查询，https://support.huaweicloud.com/api-eip/ShowPublicIpType.html。

        :return: The eip_type of this ApplyDesktopsInternet.
        :rtype: str
        """
        return self._eip_type

    @eip_type.setter
    def eip_type(self, eip_type):
        r"""Sets the eip_type of this ApplyDesktopsInternet.

        支持的类型请参考EIP服务支持的类型。可通过调用如下链接的接口查询，https://support.huaweicloud.com/api-eip/ShowPublicIpType.html。

        :param eip_type: The eip_type of this ApplyDesktopsInternet.
        :type eip_type: str
        """
        self._eip_type = eip_type

    @property
    def eip_charge_mode(self):
        r"""Gets the eip_charge_mode of this ApplyDesktopsInternet.

        eip带宽计费模式 - TRAFFIC：按流量计费。 - BANDWIDTH：按带宽计费。

        :return: The eip_charge_mode of this ApplyDesktopsInternet.
        :rtype: str
        """
        return self._eip_charge_mode

    @eip_charge_mode.setter
    def eip_charge_mode(self, eip_charge_mode):
        r"""Sets the eip_charge_mode of this ApplyDesktopsInternet.

        eip带宽计费模式 - TRAFFIC：按流量计费。 - BANDWIDTH：按带宽计费。

        :param eip_charge_mode: The eip_charge_mode of this ApplyDesktopsInternet.
        :type eip_charge_mode: str
        """
        self._eip_charge_mode = eip_charge_mode

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this ApplyDesktopsInternet.

        带宽大小，单位Mbit/s。默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :return: The bandwidth_size of this ApplyDesktopsInternet.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this ApplyDesktopsInternet.

        带宽大小，单位Mbit/s。默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :param bandwidth_size: The bandwidth_size of this ApplyDesktopsInternet.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def count(self):
        r"""Gets the count of this ApplyDesktopsInternet.

        需要购买EIP的数量，当desktop_ids为空时需要填，兼容单独购买EIP场景。

        :return: The count of this ApplyDesktopsInternet.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ApplyDesktopsInternet.

        需要购买EIP的数量，当desktop_ids为空时需要填，兼容单独购买EIP场景。

        :param count: The count of this ApplyDesktopsInternet.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ApplyDesktopsInternet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
