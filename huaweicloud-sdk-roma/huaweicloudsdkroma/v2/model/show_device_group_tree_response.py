# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeviceGroupTreeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'items': 'list[GroupTreeResponse]'
    }

    attribute_map = {
        'size': 'size',
        'items': 'items'
    }

    def __init__(self, size=None, items=None):
        r"""ShowDeviceGroupTreeResponse

        The model defined in huaweicloud sdk

        :param size: 本次返回数量
        :type size: int
        :param items: 设备分组信息
        :type items: list[:class:`huaweicloudsdkroma.v2.GroupTreeResponse`]
        """
        
        super(ShowDeviceGroupTreeResponse, self).__init__()

        self._size = None
        self._items = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if items is not None:
            self.items = items

    @property
    def size(self):
        r"""Gets the size of this ShowDeviceGroupTreeResponse.

        本次返回数量

        :return: The size of this ShowDeviceGroupTreeResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowDeviceGroupTreeResponse.

        本次返回数量

        :param size: The size of this ShowDeviceGroupTreeResponse.
        :type size: int
        """
        self._size = size

    @property
    def items(self):
        r"""Gets the items of this ShowDeviceGroupTreeResponse.

        设备分组信息

        :return: The items of this ShowDeviceGroupTreeResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.GroupTreeResponse`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ShowDeviceGroupTreeResponse.

        设备分组信息

        :param items: The items of this ShowDeviceGroupTreeResponse.
        :type items: list[:class:`huaweicloudsdkroma.v2.GroupTreeResponse`]
        """
        self._items = items

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
        if not isinstance(other, ShowDeviceGroupTreeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
