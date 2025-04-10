# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportMetricNameListSupportMetricNames:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'list[str]',
        'metric_name': 'str',
        'unit': 'str',
        'description': 'str'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'metric_name': 'metric_name',
        'unit': 'unit',
        'description': 'description'
    }

    def __init__(self, datastore_type=None, metric_name=None, unit=None, description=None):
        r"""SupportMetricNameListSupportMetricNames

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型
        :type datastore_type: list[str]
        :param metric_name: 指标名称
        :type metric_name: str
        :param unit: 单位
        :type unit: str
        :param description: 描述
        :type description: str
        """
        
        

        self._datastore_type = None
        self._metric_name = None
        self._unit = None
        self._description = None
        self.discriminator = None

        if datastore_type is not None:
            self.datastore_type = datastore_type
        if metric_name is not None:
            self.metric_name = metric_name
        if unit is not None:
            self.unit = unit
        if description is not None:
            self.description = description

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this SupportMetricNameListSupportMetricNames.

        数据库类型

        :return: The datastore_type of this SupportMetricNameListSupportMetricNames.
        :rtype: list[str]
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this SupportMetricNameListSupportMetricNames.

        数据库类型

        :param datastore_type: The datastore_type of this SupportMetricNameListSupportMetricNames.
        :type datastore_type: list[str]
        """
        self._datastore_type = datastore_type

    @property
    def metric_name(self):
        r"""Gets the metric_name of this SupportMetricNameListSupportMetricNames.

        指标名称

        :return: The metric_name of this SupportMetricNameListSupportMetricNames.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this SupportMetricNameListSupportMetricNames.

        指标名称

        :param metric_name: The metric_name of this SupportMetricNameListSupportMetricNames.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def unit(self):
        r"""Gets the unit of this SupportMetricNameListSupportMetricNames.

        单位

        :return: The unit of this SupportMetricNameListSupportMetricNames.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this SupportMetricNameListSupportMetricNames.

        单位

        :param unit: The unit of this SupportMetricNameListSupportMetricNames.
        :type unit: str
        """
        self._unit = unit

    @property
    def description(self):
        r"""Gets the description of this SupportMetricNameListSupportMetricNames.

        描述

        :return: The description of this SupportMetricNameListSupportMetricNames.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SupportMetricNameListSupportMetricNames.

        描述

        :param description: The description of this SupportMetricNameListSupportMetricNames.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, SupportMetricNameListSupportMetricNames):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
