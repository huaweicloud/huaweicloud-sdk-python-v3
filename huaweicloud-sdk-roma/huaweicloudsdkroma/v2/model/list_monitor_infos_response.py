# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMonitorInfosResponse(SdkResponse):

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
        'entities': 'list[TaskMonitorInfo]'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'entities': 'entities'
    }

    def __init__(self, total=None, size=None, entities=None):
        r"""ListMonitorInfosResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param size: 当前页监控信息数量
        :type size: int
        :param entities: 任务监控信息当前页元素
        :type entities: list[:class:`huaweicloudsdkroma.v2.TaskMonitorInfo`]
        """
        
        super(ListMonitorInfosResponse, self).__init__()

        self._total = None
        self._size = None
        self._entities = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if entities is not None:
            self.entities = entities

    @property
    def total(self):
        r"""Gets the total of this ListMonitorInfosResponse.

        总数

        :return: The total of this ListMonitorInfosResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListMonitorInfosResponse.

        总数

        :param total: The total of this ListMonitorInfosResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ListMonitorInfosResponse.

        当前页监控信息数量

        :return: The size of this ListMonitorInfosResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListMonitorInfosResponse.

        当前页监控信息数量

        :param size: The size of this ListMonitorInfosResponse.
        :type size: int
        """
        self._size = size

    @property
    def entities(self):
        r"""Gets the entities of this ListMonitorInfosResponse.

        任务监控信息当前页元素

        :return: The entities of this ListMonitorInfosResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.TaskMonitorInfo`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this ListMonitorInfosResponse.

        任务监控信息当前页元素

        :param entities: The entities of this ListMonitorInfosResponse.
        :type entities: list[:class:`huaweicloudsdkroma.v2.TaskMonitorInfo`]
        """
        self._entities = entities

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
        if not isinstance(other, ListMonitorInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
