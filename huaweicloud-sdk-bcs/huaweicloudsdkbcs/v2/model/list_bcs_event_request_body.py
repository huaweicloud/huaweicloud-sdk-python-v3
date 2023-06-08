# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBcsEventRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_range': 'str',
        'step': 'int',
        'search': 'str',
        'metadata_relation': 'list[EventMetadataRelation]',
        'sort': 'EventResultSort'
    }

    attribute_map = {
        'time_range': 'time_range',
        'step': 'step',
        'search': 'search',
        'metadata_relation': 'metadata_relation',
        'sort': 'sort'
    }

    def __init__(self, time_range=None, step=None, search=None, metadata_relation=None, sort=None):
        """ListBcsEventRequestBody

        The model defined in huaweicloud sdk

        :param time_range: timeRange用于指标查询时间范围，主要用于解决客户端时间和服务端时间不一致情况下，查询最近N分钟的数据。另可用于精确查询某一段时间的数据。
        :type time_range: str
        :param step: 统计步长。毫秒数
        :type step: int
        :param search: 模糊查询匹配字段，可以为空
        :type search: str
        :param metadata_relation: 查询条件组合，可以为空
        :type metadata_relation: list[:class:`huaweicloudsdkbcs.v2.EventMetadataRelation`]
        :param sort: 
        :type sort: :class:`huaweicloudsdkbcs.v2.EventResultSort`
        """
        
        

        self._time_range = None
        self._step = None
        self._search = None
        self._metadata_relation = None
        self._sort = None
        self.discriminator = None

        self.time_range = time_range
        self.step = step
        if search is not None:
            self.search = search
        if metadata_relation is not None:
            self.metadata_relation = metadata_relation
        if sort is not None:
            self.sort = sort

    @property
    def time_range(self):
        """Gets the time_range of this ListBcsEventRequestBody.

        timeRange用于指标查询时间范围，主要用于解决客户端时间和服务端时间不一致情况下，查询最近N分钟的数据。另可用于精确查询某一段时间的数据。

        :return: The time_range of this ListBcsEventRequestBody.
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this ListBcsEventRequestBody.

        timeRange用于指标查询时间范围，主要用于解决客户端时间和服务端时间不一致情况下，查询最近N分钟的数据。另可用于精确查询某一段时间的数据。

        :param time_range: The time_range of this ListBcsEventRequestBody.
        :type time_range: str
        """
        self._time_range = time_range

    @property
    def step(self):
        """Gets the step of this ListBcsEventRequestBody.

        统计步长。毫秒数

        :return: The step of this ListBcsEventRequestBody.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this ListBcsEventRequestBody.

        统计步长。毫秒数

        :param step: The step of this ListBcsEventRequestBody.
        :type step: int
        """
        self._step = step

    @property
    def search(self):
        """Gets the search of this ListBcsEventRequestBody.

        模糊查询匹配字段，可以为空

        :return: The search of this ListBcsEventRequestBody.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListBcsEventRequestBody.

        模糊查询匹配字段，可以为空

        :param search: The search of this ListBcsEventRequestBody.
        :type search: str
        """
        self._search = search

    @property
    def metadata_relation(self):
        """Gets the metadata_relation of this ListBcsEventRequestBody.

        查询条件组合，可以为空

        :return: The metadata_relation of this ListBcsEventRequestBody.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.EventMetadataRelation`]
        """
        return self._metadata_relation

    @metadata_relation.setter
    def metadata_relation(self, metadata_relation):
        """Sets the metadata_relation of this ListBcsEventRequestBody.

        查询条件组合，可以为空

        :param metadata_relation: The metadata_relation of this ListBcsEventRequestBody.
        :type metadata_relation: list[:class:`huaweicloudsdkbcs.v2.EventMetadataRelation`]
        """
        self._metadata_relation = metadata_relation

    @property
    def sort(self):
        """Gets the sort of this ListBcsEventRequestBody.

        :return: The sort of this ListBcsEventRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.EventResultSort`
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListBcsEventRequestBody.

        :param sort: The sort of this ListBcsEventRequestBody.
        :type sort: :class:`huaweicloudsdkbcs.v2.EventResultSort`
        """
        self._sort = sort

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
        if not isinstance(other, ListBcsEventRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
