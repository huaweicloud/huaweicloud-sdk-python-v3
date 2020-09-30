# coding: utf-8

import pprint
import re

import six





class UpdateBandwidthOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'size': 'int',
        'charge_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, name=None, size=None, charge_mode=None):
        """UpdateBandwidthOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._size = None
        self._charge_mode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def name(self):
        """Gets the name of this UpdateBandwidthOption.

        取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线），为空表示不修改名称  功能说明：带宽名称  约束：name、size必须有一个参数有值

        :return: The name of this UpdateBandwidthOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateBandwidthOption.

        取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线），为空表示不修改名称  功能说明：带宽名称  约束：name、size必须有一个参数有值

        :param name: The name of this UpdateBandwidthOption.
        :type: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this UpdateBandwidthOption.

        取值范围：默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示），不带此参数时表示不修改大小  功能说明：带宽大小，单位Mbit/s。  约束：name、size必须有一个参数有值  如果传入的参数为小数（如 10.2）或者字符类型（如“10”），会自动强制转换为整数。  约束：name、size必须要有一个参数有值。  调整带宽时的最小单位会根据带宽范围不同存在差异:  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :return: The size of this UpdateBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UpdateBandwidthOption.

        取值范围：默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示），不带此参数时表示不修改大小  功能说明：带宽大小，单位Mbit/s。  约束：name、size必须有一个参数有值  如果传入的参数为小数（如 10.2）或者字符类型（如“10”），会自动强制转换为整数。  约束：name、size必须要有一个参数有值。  调整带宽时的最小单位会根据带宽范围不同存在差异:  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :param size: The size of this UpdateBandwidthOption.
        :type: int
        """
        self._size = size

    @property
    def charge_mode(self):
        """Gets the charge_mode of this UpdateBandwidthOption.

        功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :return: The charge_mode of this UpdateBandwidthOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this UpdateBandwidthOption.

        功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :param charge_mode: The charge_mode of this UpdateBandwidthOption.
        :type: str
        """
        self._charge_mode = charge_mode

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
