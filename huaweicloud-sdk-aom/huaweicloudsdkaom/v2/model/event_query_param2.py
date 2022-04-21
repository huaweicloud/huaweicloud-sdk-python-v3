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

        :param time_range: 查询时间范围。 格式：开始时间UTC毫秒.结束时间UTC毫秒.时间范围分钟数。开始和结束时间为-1时，表示最近N分钟，N为时间范围分钟取值。查询时间段，如最近五分钟可以表示为-1.-1.5，固定的时间范围（2017-08-01 08:00:00到2017-08-02 08:00:00）可以表示为1501545600000.1501632000000.1440。
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

        查询时间范围。 格式：开始时间UTC毫秒.结束时间UTC毫秒.时间范围分钟数。开始和结束时间为-1时，表示最近N分钟，N为时间范围分钟取值。查询时间段，如最近五分钟可以表示为-1.-1.5，固定的时间范围（2017-08-01 08:00:00到2017-08-02 08:00:00）可以表示为1501545600000.1501632000000.1440。

        :return: The time_range of this EventQueryParam2.
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this EventQueryParam2.

        查询时间范围。 格式：开始时间UTC毫秒.结束时间UTC毫秒.时间范围分钟数。开始和结束时间为-1时，表示最近N分钟，N为时间范围分钟取值。查询时间段，如最近五分钟可以表示为-1.-1.5，固定的时间范围（2017-08-01 08:00:00到2017-08-02 08:00:00）可以表示为1501545600000.1501632000000.1440。

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
