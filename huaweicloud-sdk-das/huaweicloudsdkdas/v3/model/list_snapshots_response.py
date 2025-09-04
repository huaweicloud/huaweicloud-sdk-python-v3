# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[QuerySnapshotsRespItems]',
        'count': 'int'
    }

    attribute_map = {
        'items': 'items',
        'count': 'count'
    }

    def __init__(self, items=None, count=None):
        r"""ListSnapshotsResponse

        The model defined in huaweicloud sdk

        :param items: 具体的snapshot
        :type items: list[:class:`huaweicloudsdkdas.v3.QuerySnapshotsRespItems`]
        :param count: snapshot的数量
        :type count: int
        """
        
        super(ListSnapshotsResponse, self).__init__()

        self._items = None
        self._count = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if count is not None:
            self.count = count

    @property
    def items(self):
        r"""Gets the items of this ListSnapshotsResponse.

        具体的snapshot

        :return: The items of this ListSnapshotsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.QuerySnapshotsRespItems`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListSnapshotsResponse.

        具体的snapshot

        :param items: The items of this ListSnapshotsResponse.
        :type items: list[:class:`huaweicloudsdkdas.v3.QuerySnapshotsRespItems`]
        """
        self._items = items

    @property
    def count(self):
        r"""Gets the count of this ListSnapshotsResponse.

        snapshot的数量

        :return: The count of this ListSnapshotsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSnapshotsResponse.

        snapshot的数量

        :param count: The count of this ListSnapshotsResponse.
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
        if not isinstance(other, ListSnapshotsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
