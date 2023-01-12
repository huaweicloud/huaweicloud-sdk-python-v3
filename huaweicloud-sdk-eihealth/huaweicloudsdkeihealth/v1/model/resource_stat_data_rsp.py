# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceStatDataRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statistic': 'str',
        'unit': 'str',
        'metric_name': 'str',
        'resource_id': 'str',
        'device_id': 'str'
    }

    attribute_map = {
        'statistic': 'statistic',
        'unit': 'unit',
        'metric_name': 'metric_name',
        'resource_id': 'resource_id',
        'device_id': 'device_id'
    }

    def __init__(self, statistic=None, unit=None, metric_name=None, resource_id=None, device_id=None):
        """ResourceStatDataRsp

        The model defined in huaweicloud sdk

        :param statistic: 统计值
        :type statistic: str
        :param unit: 数据单位
        :type unit: str
        :param metric_name: 监控指标名称
        :type metric_name: str
        :param resource_id: 监控资源id
        :type resource_id: str
        :param device_id: 显卡id
        :type device_id: str
        """
        
        

        self._statistic = None
        self._unit = None
        self._metric_name = None
        self._resource_id = None
        self._device_id = None
        self.discriminator = None

        if statistic is not None:
            self.statistic = statistic
        if unit is not None:
            self.unit = unit
        if metric_name is not None:
            self.metric_name = metric_name
        if resource_id is not None:
            self.resource_id = resource_id
        if device_id is not None:
            self.device_id = device_id

    @property
    def statistic(self):
        """Gets the statistic of this ResourceStatDataRsp.

        统计值

        :return: The statistic of this ResourceStatDataRsp.
        :rtype: str
        """
        return self._statistic

    @statistic.setter
    def statistic(self, statistic):
        """Sets the statistic of this ResourceStatDataRsp.

        统计值

        :param statistic: The statistic of this ResourceStatDataRsp.
        :type statistic: str
        """
        self._statistic = statistic

    @property
    def unit(self):
        """Gets the unit of this ResourceStatDataRsp.

        数据单位

        :return: The unit of this ResourceStatDataRsp.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ResourceStatDataRsp.

        数据单位

        :param unit: The unit of this ResourceStatDataRsp.
        :type unit: str
        """
        self._unit = unit

    @property
    def metric_name(self):
        """Gets the metric_name of this ResourceStatDataRsp.

        监控指标名称

        :return: The metric_name of this ResourceStatDataRsp.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ResourceStatDataRsp.

        监控指标名称

        :param metric_name: The metric_name of this ResourceStatDataRsp.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourceStatDataRsp.

        监控资源id

        :return: The resource_id of this ResourceStatDataRsp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourceStatDataRsp.

        监控资源id

        :param resource_id: The resource_id of this ResourceStatDataRsp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def device_id(self):
        """Gets the device_id of this ResourceStatDataRsp.

        显卡id

        :return: The device_id of this ResourceStatDataRsp.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ResourceStatDataRsp.

        显卡id

        :param device_id: The device_id of this ResourceStatDataRsp.
        :type device_id: str
        """
        self._device_id = device_id

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
        if not isinstance(other, ResourceStatDataRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
