# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoScalingSwitchStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_switch': 'str',
        'flavor_switch': 'str',
        'read_only_switch': 'str'
    }

    attribute_map = {
        'scaling_switch': 'scaling_switch',
        'flavor_switch': 'flavor_switch',
        'read_only_switch': 'read_only_switch'
    }

    def __init__(self, scaling_switch=None, flavor_switch=None, read_only_switch=None):
        """AutoScalingSwitchStatus

        The model defined in huaweicloud sdk

        :param scaling_switch: 自动变配开关状态。  取值：  - ON：开启。 - OFF：关闭。
        :type scaling_switch: str
        :param flavor_switch: 扩缩规格开关状态。  取值：  - ON：开启。 - OFF：关闭。
        :type flavor_switch: str
        :param read_only_switch: 增删只读节点开关状态。  取值：  - ON：开启。 - OFF：关闭。
        :type read_only_switch: str
        """
        
        

        self._scaling_switch = None
        self._flavor_switch = None
        self._read_only_switch = None
        self.discriminator = None

        if scaling_switch is not None:
            self.scaling_switch = scaling_switch
        if flavor_switch is not None:
            self.flavor_switch = flavor_switch
        if read_only_switch is not None:
            self.read_only_switch = read_only_switch

    @property
    def scaling_switch(self):
        """Gets the scaling_switch of this AutoScalingSwitchStatus.

        自动变配开关状态。  取值：  - ON：开启。 - OFF：关闭。

        :return: The scaling_switch of this AutoScalingSwitchStatus.
        :rtype: str
        """
        return self._scaling_switch

    @scaling_switch.setter
    def scaling_switch(self, scaling_switch):
        """Sets the scaling_switch of this AutoScalingSwitchStatus.

        自动变配开关状态。  取值：  - ON：开启。 - OFF：关闭。

        :param scaling_switch: The scaling_switch of this AutoScalingSwitchStatus.
        :type scaling_switch: str
        """
        self._scaling_switch = scaling_switch

    @property
    def flavor_switch(self):
        """Gets the flavor_switch of this AutoScalingSwitchStatus.

        扩缩规格开关状态。  取值：  - ON：开启。 - OFF：关闭。

        :return: The flavor_switch of this AutoScalingSwitchStatus.
        :rtype: str
        """
        return self._flavor_switch

    @flavor_switch.setter
    def flavor_switch(self, flavor_switch):
        """Sets the flavor_switch of this AutoScalingSwitchStatus.

        扩缩规格开关状态。  取值：  - ON：开启。 - OFF：关闭。

        :param flavor_switch: The flavor_switch of this AutoScalingSwitchStatus.
        :type flavor_switch: str
        """
        self._flavor_switch = flavor_switch

    @property
    def read_only_switch(self):
        """Gets the read_only_switch of this AutoScalingSwitchStatus.

        增删只读节点开关状态。  取值：  - ON：开启。 - OFF：关闭。

        :return: The read_only_switch of this AutoScalingSwitchStatus.
        :rtype: str
        """
        return self._read_only_switch

    @read_only_switch.setter
    def read_only_switch(self, read_only_switch):
        """Sets the read_only_switch of this AutoScalingSwitchStatus.

        增删只读节点开关状态。  取值：  - ON：开启。 - OFF：关闭。

        :param read_only_switch: The read_only_switch of this AutoScalingSwitchStatus.
        :type read_only_switch: str
        """
        self._read_only_switch = read_only_switch

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
        if not isinstance(other, AutoScalingSwitchStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
