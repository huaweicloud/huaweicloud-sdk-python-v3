# coding: utf-8

import pprint
import re

import six





class CreateSharedBandwidthOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'name': 'str',
        'size': 'int',
        'charge_mode': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'size': 'size',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, enterprise_project_id='0', name=None, size=None, charge_mode=None):
        """CreateSharedBandwidthOption - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._name = None
        self._size = None
        self._charge_mode = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.name = name
        self.size = size
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateSharedBandwidthOption.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建共享带宽时，给共享带宽绑定企业项目ID。

        :return: The enterprise_project_id of this CreateSharedBandwidthOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateSharedBandwidthOption.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建共享带宽时，给共享带宽绑定企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateSharedBandwidthOption.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CreateSharedBandwidthOption.

        取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  功能说明：带宽名称

        :return: The name of this CreateSharedBandwidthOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSharedBandwidthOption.

        取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  功能说明：带宽名称

        :param name: The name of this CreateSharedBandwidthOption.
        :type: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this CreateSharedBandwidthOption.

        功能说明：带宽大小。共享带宽的大小有最小值限制，默认为5M，可能因局点不同而不同。  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。  如果传入的参数为小数（如 10.2）或者字符类型（如“10”），会自动强制转换为整数。  调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :return: The size of this CreateSharedBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateSharedBandwidthOption.

        功能说明：带宽大小。共享带宽的大小有最小值限制，默认为5M，可能因局点不同而不同。  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。  如果传入的参数为小数（如 10.2）或者字符类型（如“10”），会自动强制转换为整数。  调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :param size: The size of this CreateSharedBandwidthOption.
        :type: int
        """
        self._size = size

    @property
    def charge_mode(self):
        """Gets the charge_mode of this CreateSharedBandwidthOption.

        功能说明：按带宽计费还是按增强型95计费。  取值范围：bandwidth，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :return: The charge_mode of this CreateSharedBandwidthOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this CreateSharedBandwidthOption.

        功能说明：按带宽计费还是按增强型95计费。  取值范围：bandwidth，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :param charge_mode: The charge_mode of this CreateSharedBandwidthOption.
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
        if not isinstance(other, CreateSharedBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
