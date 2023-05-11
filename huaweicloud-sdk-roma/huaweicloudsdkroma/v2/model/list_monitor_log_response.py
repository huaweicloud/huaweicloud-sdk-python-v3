# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMonitorLogResponse(SdkResponse):

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
        'entities': 'list[TaskMonitorLog]'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'entities': 'entities'
    }

    def __init__(self, total=None, size=None, entities=None):
        """ListMonitorLogResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param size: 当前页日志数量
        :type size: int
        :param entities: 任务监控日志当前页元素
        :type entities: list[:class:`huaweicloudsdkroma.v2.TaskMonitorLog`]
        """
        
        super(ListMonitorLogResponse, self).__init__()

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
        """Gets the total of this ListMonitorLogResponse.

        总数

        :return: The total of this ListMonitorLogResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListMonitorLogResponse.

        总数

        :param total: The total of this ListMonitorLogResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        """Gets the size of this ListMonitorLogResponse.

        当前页日志数量

        :return: The size of this ListMonitorLogResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListMonitorLogResponse.

        当前页日志数量

        :param size: The size of this ListMonitorLogResponse.
        :type size: int
        """
        self._size = size

    @property
    def entities(self):
        """Gets the entities of this ListMonitorLogResponse.

        任务监控日志当前页元素

        :return: The entities of this ListMonitorLogResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.TaskMonitorLog`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ListMonitorLogResponse.

        任务监控日志当前页元素

        :param entities: The entities of this ListMonitorLogResponse.
        :type entities: list[:class:`huaweicloudsdkroma.v2.TaskMonitorLog`]
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
        if not isinstance(other, ListMonitorLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
