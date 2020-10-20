# coding: utf-8

import pprint
import re

import six





class CreateLoadBalancerBandwidthOption:


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
        'charge_mode': 'str',
        'share_type': 'str',
        'billing_info': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'charge_mode': 'charge_mode',
        'share_type': 'share_type',
        'billing_info': 'billing_info'
    }

    def __init__(self, name=None, size=None, charge_mode=None, share_type=None, billing_info=None):
        """CreateLoadBalancerBandwidthOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._size = None
        self._charge_mode = None
        self._share_type = None
        self._billing_info = None
        self.discriminator = None

        self.name = name
        self.size = size
        self.charge_mode = charge_mode
        self.share_type = share_type
        if billing_info is not None:
            self.billing_info = billing_info

    @property
    def name(self):
        """Gets the name of this CreateLoadBalancerBandwidthOption.

        带宽名称

        :return: The name of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLoadBalancerBandwidthOption.

        带宽名称

        :param name: The name of this CreateLoadBalancerBandwidthOption.
        :type: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this CreateLoadBalancerBandwidthOption.

        带宽大小 取值范围:默认1Mbit/s~2000Mbit/s(具体范围以各区域配置为准,请参见控制台对应页面显示)。 约束:share_type是PER,该参数必须带,如果share_type是WHOLE并且id有值,该参数会忽略。 注意:调整带宽时的最小单位会根据带宽范围不同存在差异。 小于等于300Mbit/s:默认最小单位为1Mbit/s。 300Mbit/s~1000Mbit/s:默认最小单位为50Mbit/s。 大于1000Mbit/s:默认最小单位为500Mbit/s。

        :return: The size of this CreateLoadBalancerBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateLoadBalancerBandwidthOption.

        带宽大小 取值范围:默认1Mbit/s~2000Mbit/s(具体范围以各区域配置为准,请参见控制台对应页面显示)。 约束:share_type是PER,该参数必须带,如果share_type是WHOLE并且id有值,该参数会忽略。 注意:调整带宽时的最小单位会根据带宽范围不同存在差异。 小于等于300Mbit/s:默认最小单位为1Mbit/s。 300Mbit/s~1000Mbit/s:默认最小单位为50Mbit/s。 大于1000Mbit/s:默认最小单位为500Mbit/s。

        :param size: The size of this CreateLoadBalancerBandwidthOption.
        :type: int
        """
        self._size = size

    @property
    def charge_mode(self):
        """Gets the charge_mode of this CreateLoadBalancerBandwidthOption.

        按流量计费还是按带宽计费。 其中IPv6国外默认是bandwidth,国内默认是traffic。取值为traffic,表示流量计费

        :return: The charge_mode of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this CreateLoadBalancerBandwidthOption.

        按流量计费还是按带宽计费。 其中IPv6国外默认是bandwidth,国内默认是traffic。取值为traffic,表示流量计费

        :param charge_mode: The charge_mode of this CreateLoadBalancerBandwidthOption.
        :type: str
        """
        self._charge_mode = charge_mode

    @property
    def share_type(self):
        """Gets the share_type of this CreateLoadBalancerBandwidthOption.

        有效值：PER,WHOLE 约束:其中IPv6暂不支持WHOLE类型带宽,该字段为WHOLE时,必须指定带宽ID。

        :return: The share_type of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this CreateLoadBalancerBandwidthOption.

        有效值：PER,WHOLE 约束:其中IPv6暂不支持WHOLE类型带宽,该字段为WHOLE时,必须指定带宽ID。

        :param share_type: The share_type of this CreateLoadBalancerBandwidthOption.
        :type: str
        """
        self._share_type = share_type

    @property
    def billing_info(self):
        """Gets the billing_info of this CreateLoadBalancerBandwidthOption.

        预留资源账单信息，默认为空表示按需计费， 非空为包周期。admin权限才能更新此字段

        :return: The billing_info of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this CreateLoadBalancerBandwidthOption.

        预留资源账单信息，默认为空表示按需计费， 非空为包周期。admin权限才能更新此字段

        :param billing_info: The billing_info of this CreateLoadBalancerBandwidthOption.
        :type: str
        """
        self._billing_info = billing_info

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
        if not isinstance(other, CreateLoadBalancerBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
