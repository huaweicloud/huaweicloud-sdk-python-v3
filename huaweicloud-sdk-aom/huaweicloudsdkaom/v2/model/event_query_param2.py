# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventQueryParam2:

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
        'sort': 'EventQueryParam2Sort',
        'metadata_relation': 'list[RelationModel]'
    }

    attribute_map = {
        'time_range': 'time_range',
        'step': 'step',
        'search': 'search',
        'sort': 'sort',
        'metadata_relation': 'metadata_relation'
    }

    def __init__(self, time_range=None, step=None, search=None, sort=None, metadata_relation=None):
        """EventQueryParam2

        The model defined in huaweicloud sdk

        :param time_range: timeRange用于指标查询时间范围，主要用于解决客户端时间和服务端时间不一致情况下，查询最近N分钟的数据。另可用于精确查询某一段时间的数据。  如：  - -1.-1.60(表示最近60分钟)，不管当前客户端是什么时间，都以服务端时间为准查询最近60分钟。 - 1650852000000.1650852300000.5(表示北京时间2022-04-25 10:00:00至2022-04-25 10:05:00指定的5分钟)  格式：  startTimeInMillis.endTimeInMillis.durationInMinutes  参数解释：  - startTimeInMillis: 查询的开始时间，格式为UTC毫秒，如果指定为-1，服务端将按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如-1.1650852300000.5，则相当于1650852000000.1650852300000.5 - endTimeInMillis: 查询的结束时间，格式为UTC毫秒，如果指定为-1，服务端将按(startTimeInMillis + durationInMinutes * 60 * 1000)计算结束时间，如果计算出的结束时间大于当前系统时间，则使用当前系统时间。如1650852000000.-1.5，则相当于1650852000000.1650852300000.5 - durationInMinutes：查询时间的跨度分钟数。 取值范围大于0并且大于等于(endTimeInMillis - startTimeInMillis) / (60 * 1000) - 1。当开始时间与结束时间都设置为-1时，系统会将结束时间设置为当前时间UTC毫秒值，并按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如：-1.-1.60(表示最近60分钟)  约束：  单次请求中，查询时长与周期需要满足以下条件: durationInMinutes * 60 / period &lt;&#x3D; 1440
        :type time_range: str
        :param step: 统计步长。毫秒数，例如一分钟则填写为60000。
        :type step: int
        :param search: 模糊查询匹配字段，可以为空。如果值不为空，可以模糊匹配。metadata字段为必选字段。
        :type search: str
        :param sort: 
        :type sort: :class:`huaweicloudsdkaom.v2.EventQueryParam2Sort`
        :param metadata_relation: 查询条件组合，可以为空。
        :type metadata_relation: list[:class:`huaweicloudsdkaom.v2.RelationModel`]
        """
        
        

        self._time_range = None
        self._step = None
        self._search = None
        self._sort = None
        self._metadata_relation = None
        self.discriminator = None

        self.time_range = time_range
        if step is not None:
            self.step = step
        if search is not None:
            self.search = search
        if sort is not None:
            self.sort = sort
        if metadata_relation is not None:
            self.metadata_relation = metadata_relation

    @property
    def time_range(self):
        """Gets the time_range of this EventQueryParam2.

        timeRange用于指标查询时间范围，主要用于解决客户端时间和服务端时间不一致情况下，查询最近N分钟的数据。另可用于精确查询某一段时间的数据。  如：  - -1.-1.60(表示最近60分钟)，不管当前客户端是什么时间，都以服务端时间为准查询最近60分钟。 - 1650852000000.1650852300000.5(表示北京时间2022-04-25 10:00:00至2022-04-25 10:05:00指定的5分钟)  格式：  startTimeInMillis.endTimeInMillis.durationInMinutes  参数解释：  - startTimeInMillis: 查询的开始时间，格式为UTC毫秒，如果指定为-1，服务端将按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如-1.1650852300000.5，则相当于1650852000000.1650852300000.5 - endTimeInMillis: 查询的结束时间，格式为UTC毫秒，如果指定为-1，服务端将按(startTimeInMillis + durationInMinutes * 60 * 1000)计算结束时间，如果计算出的结束时间大于当前系统时间，则使用当前系统时间。如1650852000000.-1.5，则相当于1650852000000.1650852300000.5 - durationInMinutes：查询时间的跨度分钟数。 取值范围大于0并且大于等于(endTimeInMillis - startTimeInMillis) / (60 * 1000) - 1。当开始时间与结束时间都设置为-1时，系统会将结束时间设置为当前时间UTC毫秒值，并按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如：-1.-1.60(表示最近60分钟)  约束：  单次请求中，查询时长与周期需要满足以下条件: durationInMinutes * 60 / period <= 1440

        :return: The time_range of this EventQueryParam2.
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this EventQueryParam2.

        timeRange用于指标查询时间范围，主要用于解决客户端时间和服务端时间不一致情况下，查询最近N分钟的数据。另可用于精确查询某一段时间的数据。  如：  - -1.-1.60(表示最近60分钟)，不管当前客户端是什么时间，都以服务端时间为准查询最近60分钟。 - 1650852000000.1650852300000.5(表示北京时间2022-04-25 10:00:00至2022-04-25 10:05:00指定的5分钟)  格式：  startTimeInMillis.endTimeInMillis.durationInMinutes  参数解释：  - startTimeInMillis: 查询的开始时间，格式为UTC毫秒，如果指定为-1，服务端将按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如-1.1650852300000.5，则相当于1650852000000.1650852300000.5 - endTimeInMillis: 查询的结束时间，格式为UTC毫秒，如果指定为-1，服务端将按(startTimeInMillis + durationInMinutes * 60 * 1000)计算结束时间，如果计算出的结束时间大于当前系统时间，则使用当前系统时间。如1650852000000.-1.5，则相当于1650852000000.1650852300000.5 - durationInMinutes：查询时间的跨度分钟数。 取值范围大于0并且大于等于(endTimeInMillis - startTimeInMillis) / (60 * 1000) - 1。当开始时间与结束时间都设置为-1时，系统会将结束时间设置为当前时间UTC毫秒值，并按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如：-1.-1.60(表示最近60分钟)  约束：  单次请求中，查询时长与周期需要满足以下条件: durationInMinutes * 60 / period <= 1440

        :param time_range: The time_range of this EventQueryParam2.
        :type time_range: str
        """
        self._time_range = time_range

    @property
    def step(self):
        """Gets the step of this EventQueryParam2.

        统计步长。毫秒数，例如一分钟则填写为60000。

        :return: The step of this EventQueryParam2.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this EventQueryParam2.

        统计步长。毫秒数，例如一分钟则填写为60000。

        :param step: The step of this EventQueryParam2.
        :type step: int
        """
        self._step = step

    @property
    def search(self):
        """Gets the search of this EventQueryParam2.

        模糊查询匹配字段，可以为空。如果值不为空，可以模糊匹配。metadata字段为必选字段。

        :return: The search of this EventQueryParam2.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this EventQueryParam2.

        模糊查询匹配字段，可以为空。如果值不为空，可以模糊匹配。metadata字段为必选字段。

        :param search: The search of this EventQueryParam2.
        :type search: str
        """
        self._search = search

    @property
    def sort(self):
        """Gets the sort of this EventQueryParam2.

        :return: The sort of this EventQueryParam2.
        :rtype: :class:`huaweicloudsdkaom.v2.EventQueryParam2Sort`
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this EventQueryParam2.

        :param sort: The sort of this EventQueryParam2.
        :type sort: :class:`huaweicloudsdkaom.v2.EventQueryParam2Sort`
        """
        self._sort = sort

    @property
    def metadata_relation(self):
        """Gets the metadata_relation of this EventQueryParam2.

        查询条件组合，可以为空。

        :return: The metadata_relation of this EventQueryParam2.
        :rtype: list[:class:`huaweicloudsdkaom.v2.RelationModel`]
        """
        return self._metadata_relation

    @metadata_relation.setter
    def metadata_relation(self, metadata_relation):
        """Sets the metadata_relation of this EventQueryParam2.

        查询条件组合，可以为空。

        :param metadata_relation: The metadata_relation of this EventQueryParam2.
        :type metadata_relation: list[:class:`huaweicloudsdkaom.v2.RelationModel`]
        """
        self._metadata_relation = metadata_relation

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
        if not isinstance(other, EventQueryParam2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
