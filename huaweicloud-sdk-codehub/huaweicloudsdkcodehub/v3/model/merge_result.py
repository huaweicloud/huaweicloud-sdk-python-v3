# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'closed': 'float',
        'merge_requests': 'list[MergeRequestsItem]',
        'merged': 'float',
        'opened': 'float',
        'total': 'float'
    }

    attribute_map = {
        'closed': 'closed',
        'merge_requests': 'merge_requests',
        'merged': 'merged',
        'opened': 'opened',
        'total': 'total'
    }

    def __init__(self, closed=None, merge_requests=None, merged=None, opened=None, total=None):
        """MergeResult

        The model defined in huaweicloud sdk

        :param closed: 已关闭合并请求数
        :type closed: float
        :param merge_requests: 合并请求详情
        :type merge_requests: list[:class:`huaweicloudsdkcodehub.v3.MergeRequestsItem`]
        :param merged: 已合并合并请求数数
        :type merged: float
        :param opened: 开启中合并请求数
        :type opened: float
        :param total: 合并请求总数
        :type total: float
        """
        
        

        self._closed = None
        self._merge_requests = None
        self._merged = None
        self._opened = None
        self._total = None
        self.discriminator = None

        if closed is not None:
            self.closed = closed
        if merge_requests is not None:
            self.merge_requests = merge_requests
        if merged is not None:
            self.merged = merged
        if opened is not None:
            self.opened = opened
        if total is not None:
            self.total = total

    @property
    def closed(self):
        """Gets the closed of this MergeResult.

        已关闭合并请求数

        :return: The closed of this MergeResult.
        :rtype: float
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this MergeResult.

        已关闭合并请求数

        :param closed: The closed of this MergeResult.
        :type closed: float
        """
        self._closed = closed

    @property
    def merge_requests(self):
        """Gets the merge_requests of this MergeResult.

        合并请求详情

        :return: The merge_requests of this MergeResult.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.MergeRequestsItem`]
        """
        return self._merge_requests

    @merge_requests.setter
    def merge_requests(self, merge_requests):
        """Sets the merge_requests of this MergeResult.

        合并请求详情

        :param merge_requests: The merge_requests of this MergeResult.
        :type merge_requests: list[:class:`huaweicloudsdkcodehub.v3.MergeRequestsItem`]
        """
        self._merge_requests = merge_requests

    @property
    def merged(self):
        """Gets the merged of this MergeResult.

        已合并合并请求数数

        :return: The merged of this MergeResult.
        :rtype: float
        """
        return self._merged

    @merged.setter
    def merged(self, merged):
        """Sets the merged of this MergeResult.

        已合并合并请求数数

        :param merged: The merged of this MergeResult.
        :type merged: float
        """
        self._merged = merged

    @property
    def opened(self):
        """Gets the opened of this MergeResult.

        开启中合并请求数

        :return: The opened of this MergeResult.
        :rtype: float
        """
        return self._opened

    @opened.setter
    def opened(self, opened):
        """Sets the opened of this MergeResult.

        开启中合并请求数

        :param opened: The opened of this MergeResult.
        :type opened: float
        """
        self._opened = opened

    @property
    def total(self):
        """Gets the total of this MergeResult.

        合并请求总数

        :return: The total of this MergeResult.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this MergeResult.

        合并请求总数

        :param total: The total of this MergeResult.
        :type total: float
        """
        self._total = total

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
        if not isinstance(other, MergeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
