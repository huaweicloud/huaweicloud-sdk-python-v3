# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'items': 'list[InstanceInfo]'
    }

    attribute_map = {
        'count': 'count',
        'items': 'items'
    }

    def __init__(self, count=None, items=None):
        r"""ListInstanceResponse

        The model defined in huaweicloud sdk

        :param count: 实例总数
        :type count: int
        :param items: 实例
        :type items: list[:class:`huaweicloudsdkaad.v1.InstanceInfo`]
        """
        
        super(ListInstanceResponse, self).__init__()

        self._count = None
        self._items = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if items is not None:
            self.items = items

    @property
    def count(self):
        r"""Gets the count of this ListInstanceResponse.

        实例总数

        :return: The count of this ListInstanceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListInstanceResponse.

        实例总数

        :param count: The count of this ListInstanceResponse.
        :type count: int
        """
        self._count = count

    @property
    def items(self):
        r"""Gets the items of this ListInstanceResponse.

        实例

        :return: The items of this ListInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v1.InstanceInfo`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListInstanceResponse.

        实例

        :param items: The items of this ListInstanceResponse.
        :type items: list[:class:`huaweicloudsdkaad.v1.InstanceInfo`]
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
        if not isinstance(other, ListInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
