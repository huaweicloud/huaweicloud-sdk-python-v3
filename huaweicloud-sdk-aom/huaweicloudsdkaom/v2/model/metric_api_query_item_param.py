# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricAPIQueryItemParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inventory_id': 'str',
        'metric_items': 'list[QueryMetricItemOptionParam]'
    }

    attribute_map = {
        'inventory_id': 'inventoryId',
        'metric_items': 'metricItems'
    }

    def __init__(self, inventory_id=None, metric_items=None):
        """MetricAPIQueryItemParam

        The model defined in huaweicloud sdk

        :param inventory_id: 资源编号，格式为resType_resId。其中resType部分的枚举值为：host，application，instance， container，process，network，storage， volume。当URI参数中的type取值为“inventory”时，通过该参数查询关联的指标，不再使用metricItems数组中的信息。
        :type inventory_id: str
        :param metric_items: 当URI参数中的type取值不为“inventory”时，就通过该数组传递的参数信息进行指标查询。
        :type metric_items: list[:class:`huaweicloudsdkaom.v2.QueryMetricItemOptionParam`]
        """
        
        

        self._inventory_id = None
        self._metric_items = None
        self.discriminator = None

        if inventory_id is not None:
            self.inventory_id = inventory_id
        if metric_items is not None:
            self.metric_items = metric_items

    @property
    def inventory_id(self):
        """Gets the inventory_id of this MetricAPIQueryItemParam.

        资源编号，格式为resType_resId。其中resType部分的枚举值为：host，application，instance， container，process，network，storage， volume。当URI参数中的type取值为“inventory”时，通过该参数查询关联的指标，不再使用metricItems数组中的信息。

        :return: The inventory_id of this MetricAPIQueryItemParam.
        :rtype: str
        """
        return self._inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        """Sets the inventory_id of this MetricAPIQueryItemParam.

        资源编号，格式为resType_resId。其中resType部分的枚举值为：host，application，instance， container，process，network，storage， volume。当URI参数中的type取值为“inventory”时，通过该参数查询关联的指标，不再使用metricItems数组中的信息。

        :param inventory_id: The inventory_id of this MetricAPIQueryItemParam.
        :type inventory_id: str
        """
        self._inventory_id = inventory_id

    @property
    def metric_items(self):
        """Gets the metric_items of this MetricAPIQueryItemParam.

        当URI参数中的type取值不为“inventory”时，就通过该数组传递的参数信息进行指标查询。

        :return: The metric_items of this MetricAPIQueryItemParam.
        :rtype: list[:class:`huaweicloudsdkaom.v2.QueryMetricItemOptionParam`]
        """
        return self._metric_items

    @metric_items.setter
    def metric_items(self, metric_items):
        """Sets the metric_items of this MetricAPIQueryItemParam.

        当URI参数中的type取值不为“inventory”时，就通过该数组传递的参数信息进行指标查询。

        :param metric_items: The metric_items of this MetricAPIQueryItemParam.
        :type metric_items: list[:class:`huaweicloudsdkaom.v2.QueryMetricItemOptionParam`]
        """
        self._metric_items = metric_items

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
        if not isinstance(other, MetricAPIQueryItemParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
