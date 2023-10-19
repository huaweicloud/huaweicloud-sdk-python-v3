# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBandwidthPackage:

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
        'description': 'str',
        'bandwidth': 'int',
        'billing_mode': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'bandwidth': 'bandwidth',
        'billing_mode': 'billing_mode'
    }

    def __init__(self, name=None, description=None, bandwidth=None, billing_mode=None):
        """UpdateBandwidthPackage

        The model defined in huaweicloud sdk

        :param name: 实例名字。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param bandwidth: 带宽包实例中的带宽值。
        :type bandwidth: int
        :param billing_mode: 带宽包实例在大陆站或国际站的计费方式： - 5：大陆站按95方式计费 - 6：国际站按95方式计费
        :type billing_mode: int
        """
        
        

        self._name = None
        self._description = None
        self._bandwidth = None
        self._billing_mode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if billing_mode is not None:
            self.billing_mode = billing_mode

    @property
    def name(self):
        """Gets the name of this UpdateBandwidthPackage.

        实例名字。

        :return: The name of this UpdateBandwidthPackage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateBandwidthPackage.

        实例名字。

        :param name: The name of this UpdateBandwidthPackage.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateBandwidthPackage.

        实例描述。不支持 <>。

        :return: The description of this UpdateBandwidthPackage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateBandwidthPackage.

        实例描述。不支持 <>。

        :param description: The description of this UpdateBandwidthPackage.
        :type description: str
        """
        self._description = description

    @property
    def bandwidth(self):
        """Gets the bandwidth of this UpdateBandwidthPackage.

        带宽包实例中的带宽值。

        :return: The bandwidth of this UpdateBandwidthPackage.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this UpdateBandwidthPackage.

        带宽包实例中的带宽值。

        :param bandwidth: The bandwidth of this UpdateBandwidthPackage.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def billing_mode(self):
        """Gets the billing_mode of this UpdateBandwidthPackage.

        带宽包实例在大陆站或国际站的计费方式： - 5：大陆站按95方式计费 - 6：国际站按95方式计费

        :return: The billing_mode of this UpdateBandwidthPackage.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this UpdateBandwidthPackage.

        带宽包实例在大陆站或国际站的计费方式： - 5：大陆站按95方式计费 - 6：国际站按95方式计费

        :param billing_mode: The billing_mode of this UpdateBandwidthPackage.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

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
        if not isinstance(other, UpdateBandwidthPackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
