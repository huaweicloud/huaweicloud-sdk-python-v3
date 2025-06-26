# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrendQueryDataResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_time': 'int',
        'indicator_name': 'str',
        'object_id': 'str',
        'unit': 'str',
        'sub_object_id': 'str',
        'data_points': 'list[TrendQueryData]'
    }

    attribute_map = {
        'query_time': 'query_time',
        'indicator_name': 'indicator_name',
        'object_id': 'object_id',
        'unit': 'unit',
        'sub_object_id': 'sub_object_id',
        'data_points': 'data_points'
    }

    def __init__(self, query_time=None, indicator_name=None, object_id=None, unit=None, sub_object_id=None, data_points=None):
        r"""TrendQueryDataResp

        The model defined in huaweicloud sdk

        :param query_time: **参数解释**： 查询时间。 **取值范围**： 不涉及。
        :type query_time: int
        :param indicator_name: **参数解释**： 监控指标名称。 **取值范围**： 不涉及。
        :type indicator_name: str
        :param object_id: **参数解释**： 监控对象ID。 **取值范围**： 不涉及。
        :type object_id: str
        :param unit: **参数解释**： 单位。 **取值范围**： 不涉及。
        :type unit: str
        :param sub_object_id: **参数解释**： 次级监控ID。 **取值范围**： 不涉及。
        :type sub_object_id: str
        :param data_points: **参数解释**： 节点数据。 **取值范围**： 不涉及。
        :type data_points: list[:class:`huaweicloudsdkdws.v2.TrendQueryData`]
        """
        
        

        self._query_time = None
        self._indicator_name = None
        self._object_id = None
        self._unit = None
        self._sub_object_id = None
        self._data_points = None
        self.discriminator = None

        if query_time is not None:
            self.query_time = query_time
        if indicator_name is not None:
            self.indicator_name = indicator_name
        if object_id is not None:
            self.object_id = object_id
        if unit is not None:
            self.unit = unit
        if sub_object_id is not None:
            self.sub_object_id = sub_object_id
        if data_points is not None:
            self.data_points = data_points

    @property
    def query_time(self):
        r"""Gets the query_time of this TrendQueryDataResp.

        **参数解释**： 查询时间。 **取值范围**： 不涉及。

        :return: The query_time of this TrendQueryDataResp.
        :rtype: int
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        r"""Sets the query_time of this TrendQueryDataResp.

        **参数解释**： 查询时间。 **取值范围**： 不涉及。

        :param query_time: The query_time of this TrendQueryDataResp.
        :type query_time: int
        """
        self._query_time = query_time

    @property
    def indicator_name(self):
        r"""Gets the indicator_name of this TrendQueryDataResp.

        **参数解释**： 监控指标名称。 **取值范围**： 不涉及。

        :return: The indicator_name of this TrendQueryDataResp.
        :rtype: str
        """
        return self._indicator_name

    @indicator_name.setter
    def indicator_name(self, indicator_name):
        r"""Sets the indicator_name of this TrendQueryDataResp.

        **参数解释**： 监控指标名称。 **取值范围**： 不涉及。

        :param indicator_name: The indicator_name of this TrendQueryDataResp.
        :type indicator_name: str
        """
        self._indicator_name = indicator_name

    @property
    def object_id(self):
        r"""Gets the object_id of this TrendQueryDataResp.

        **参数解释**： 监控对象ID。 **取值范围**： 不涉及。

        :return: The object_id of this TrendQueryDataResp.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this TrendQueryDataResp.

        **参数解释**： 监控对象ID。 **取值范围**： 不涉及。

        :param object_id: The object_id of this TrendQueryDataResp.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def unit(self):
        r"""Gets the unit of this TrendQueryDataResp.

        **参数解释**： 单位。 **取值范围**： 不涉及。

        :return: The unit of this TrendQueryDataResp.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this TrendQueryDataResp.

        **参数解释**： 单位。 **取值范围**： 不涉及。

        :param unit: The unit of this TrendQueryDataResp.
        :type unit: str
        """
        self._unit = unit

    @property
    def sub_object_id(self):
        r"""Gets the sub_object_id of this TrendQueryDataResp.

        **参数解释**： 次级监控ID。 **取值范围**： 不涉及。

        :return: The sub_object_id of this TrendQueryDataResp.
        :rtype: str
        """
        return self._sub_object_id

    @sub_object_id.setter
    def sub_object_id(self, sub_object_id):
        r"""Sets the sub_object_id of this TrendQueryDataResp.

        **参数解释**： 次级监控ID。 **取值范围**： 不涉及。

        :param sub_object_id: The sub_object_id of this TrendQueryDataResp.
        :type sub_object_id: str
        """
        self._sub_object_id = sub_object_id

    @property
    def data_points(self):
        r"""Gets the data_points of this TrendQueryDataResp.

        **参数解释**： 节点数据。 **取值范围**： 不涉及。

        :return: The data_points of this TrendQueryDataResp.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TrendQueryData`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        r"""Sets the data_points of this TrendQueryDataResp.

        **参数解释**： 节点数据。 **取值范围**： 不涉及。

        :param data_points: The data_points of this TrendQueryDataResp.
        :type data_points: list[:class:`huaweicloudsdkdws.v2.TrendQueryData`]
        """
        self._data_points = data_points

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
        if not isinstance(other, TrendQueryDataResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
