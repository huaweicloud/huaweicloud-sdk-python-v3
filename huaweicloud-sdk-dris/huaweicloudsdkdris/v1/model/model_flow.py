# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelFlow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vehicle_class': 'int',
        'flow': 'int',
        'average_speed': 'float'
    }

    attribute_map = {
        'vehicle_class': 'vehicle_class',
        'flow': 'flow',
        'average_speed': 'average_speed'
    }

    def __init__(self, vehicle_class=None, flow=None, average_speed=None):
        r"""ModelFlow

        The model defined in huaweicloud sdk

        :param vehicle_class: **参数说明**：车辆类型。参考[车辆基本类型](https://support.huaweicloud.com/api-v2x/v2x_04_0162.html)。
        :type vehicle_class: int
        :param flow: **参数说明**：统计周期内的车辆数。
        :type flow: int
        :param average_speed: **参数说明**：车辆平均速度，单位km/h。
        :type average_speed: float
        """
        
        

        self._vehicle_class = None
        self._flow = None
        self._average_speed = None
        self.discriminator = None

        if vehicle_class is not None:
            self.vehicle_class = vehicle_class
        if flow is not None:
            self.flow = flow
        if average_speed is not None:
            self.average_speed = average_speed

    @property
    def vehicle_class(self):
        r"""Gets the vehicle_class of this ModelFlow.

        **参数说明**：车辆类型。参考[车辆基本类型](https://support.huaweicloud.com/api-v2x/v2x_04_0162.html)。

        :return: The vehicle_class of this ModelFlow.
        :rtype: int
        """
        return self._vehicle_class

    @vehicle_class.setter
    def vehicle_class(self, vehicle_class):
        r"""Sets the vehicle_class of this ModelFlow.

        **参数说明**：车辆类型。参考[车辆基本类型](https://support.huaweicloud.com/api-v2x/v2x_04_0162.html)。

        :param vehicle_class: The vehicle_class of this ModelFlow.
        :type vehicle_class: int
        """
        self._vehicle_class = vehicle_class

    @property
    def flow(self):
        r"""Gets the flow of this ModelFlow.

        **参数说明**：统计周期内的车辆数。

        :return: The flow of this ModelFlow.
        :rtype: int
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        r"""Sets the flow of this ModelFlow.

        **参数说明**：统计周期内的车辆数。

        :param flow: The flow of this ModelFlow.
        :type flow: int
        """
        self._flow = flow

    @property
    def average_speed(self):
        r"""Gets the average_speed of this ModelFlow.

        **参数说明**：车辆平均速度，单位km/h。

        :return: The average_speed of this ModelFlow.
        :rtype: float
        """
        return self._average_speed

    @average_speed.setter
    def average_speed(self, average_speed):
        r"""Sets the average_speed of this ModelFlow.

        **参数说明**：车辆平均速度，单位km/h。

        :param average_speed: The average_speed of this ModelFlow.
        :type average_speed: float
        """
        self._average_speed = average_speed

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
        if not isinstance(other, ModelFlow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
