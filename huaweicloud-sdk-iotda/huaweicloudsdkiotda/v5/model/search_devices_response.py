# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchDevicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'devices': 'list[SearchDevice]',
        'count': 'int'
    }

    attribute_map = {
        'devices': 'devices',
        'count': 'count'
    }

    def __init__(self, devices=None, count=None):
        r"""SearchDevicesResponse

        The model defined in huaweicloud sdk

        :param devices: 搜索设备结果列表。
        :type devices: list[:class:`huaweicloudsdkiotda.v5.SearchDevice`]
        :param count: 满足查询条件的记录总数(只有条件为select count(*)/count(1)时单独返回)。
        :type count: int
        """
        
        super(SearchDevicesResponse, self).__init__()

        self._devices = None
        self._count = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        if count is not None:
            self.count = count

    @property
    def devices(self):
        r"""Gets the devices of this SearchDevicesResponse.

        搜索设备结果列表。

        :return: The devices of this SearchDevicesResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.SearchDevice`]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        r"""Sets the devices of this SearchDevicesResponse.

        搜索设备结果列表。

        :param devices: The devices of this SearchDevicesResponse.
        :type devices: list[:class:`huaweicloudsdkiotda.v5.SearchDevice`]
        """
        self._devices = devices

    @property
    def count(self):
        r"""Gets the count of this SearchDevicesResponse.

        满足查询条件的记录总数(只有条件为select count(*)/count(1)时单独返回)。

        :return: The count of this SearchDevicesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this SearchDevicesResponse.

        满足查询条件的记录总数(只有条件为select count(*)/count(1)时单独返回)。

        :param count: The count of this SearchDevicesResponse.
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
        if not isinstance(other, SearchDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
