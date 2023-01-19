# coding: utf-8

import re
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
        """TrendQueryDataResp

        The model defined in huaweicloud sdk

        :param query_time: 查询时间。
        :type query_time: int
        :param indicator_name: 监控指标名称。
        :type indicator_name: str
        :param object_id: 监控对象id。
        :type object_id: str
        :param unit: 单位。
        :type unit: str
        :param sub_object_id: 次级监控id。
        :type sub_object_id: str
        :param data_points: 节点数据。
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
        """Gets the query_time of this TrendQueryDataResp.

        查询时间。

        :return: The query_time of this TrendQueryDataResp.
        :rtype: int
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        """Sets the query_time of this TrendQueryDataResp.

        查询时间。

        :param query_time: The query_time of this TrendQueryDataResp.
        :type query_time: int
        """
        self._query_time = query_time

    @property
    def indicator_name(self):
        """Gets the indicator_name of this TrendQueryDataResp.

        监控指标名称。

        :return: The indicator_name of this TrendQueryDataResp.
        :rtype: str
        """
        return self._indicator_name

    @indicator_name.setter
    def indicator_name(self, indicator_name):
        """Sets the indicator_name of this TrendQueryDataResp.

        监控指标名称。

        :param indicator_name: The indicator_name of this TrendQueryDataResp.
        :type indicator_name: str
        """
        self._indicator_name = indicator_name

    @property
    def object_id(self):
        """Gets the object_id of this TrendQueryDataResp.

        监控对象id。

        :return: The object_id of this TrendQueryDataResp.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this TrendQueryDataResp.

        监控对象id。

        :param object_id: The object_id of this TrendQueryDataResp.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def unit(self):
        """Gets the unit of this TrendQueryDataResp.

        单位。

        :return: The unit of this TrendQueryDataResp.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TrendQueryDataResp.

        单位。

        :param unit: The unit of this TrendQueryDataResp.
        :type unit: str
        """
        self._unit = unit

    @property
    def sub_object_id(self):
        """Gets the sub_object_id of this TrendQueryDataResp.

        次级监控id。

        :return: The sub_object_id of this TrendQueryDataResp.
        :rtype: str
        """
        return self._sub_object_id

    @sub_object_id.setter
    def sub_object_id(self, sub_object_id):
        """Sets the sub_object_id of this TrendQueryDataResp.

        次级监控id。

        :param sub_object_id: The sub_object_id of this TrendQueryDataResp.
        :type sub_object_id: str
        """
        self._sub_object_id = sub_object_id

    @property
    def data_points(self):
        """Gets the data_points of this TrendQueryDataResp.

        节点数据。

        :return: The data_points of this TrendQueryDataResp.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TrendQueryData`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this TrendQueryDataResp.

        节点数据。

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
