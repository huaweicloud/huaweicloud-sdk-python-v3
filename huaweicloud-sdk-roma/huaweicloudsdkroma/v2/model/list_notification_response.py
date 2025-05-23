# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'size': 'int',
        'items': 'list[NotificationResponseBody]'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'items': 'items'
    }

    def __init__(self, total=None, size=None, items=None):
        r"""ListNotificationResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param size: 本次返回数量
        :type size: int
        :param items: 订阅管理列表
        :type items: list[:class:`huaweicloudsdkroma.v2.NotificationResponseBody`]
        """
        
        super(ListNotificationResponse, self).__init__()

        self._total = None
        self._size = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if items is not None:
            self.items = items

    @property
    def total(self):
        r"""Gets the total of this ListNotificationResponse.

        总数

        :return: The total of this ListNotificationResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListNotificationResponse.

        总数

        :param total: The total of this ListNotificationResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ListNotificationResponse.

        本次返回数量

        :return: The size of this ListNotificationResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListNotificationResponse.

        本次返回数量

        :param size: The size of this ListNotificationResponse.
        :type size: int
        """
        self._size = size

    @property
    def items(self):
        r"""Gets the items of this ListNotificationResponse.

        订阅管理列表

        :return: The items of this ListNotificationResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.NotificationResponseBody`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListNotificationResponse.

        订阅管理列表

        :param items: The items of this ListNotificationResponse.
        :type items: list[:class:`huaweicloudsdkroma.v2.NotificationResponseBody`]
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
        if not isinstance(other, ListNotificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
