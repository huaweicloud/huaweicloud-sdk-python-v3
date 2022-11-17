# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFunctionReservedInstancesCountRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'idle_mode': 'bool',
        'tactics_config': 'TacticsConfig'
    }

    attribute_map = {
        'count': 'count',
        'idle_mode': 'idle_mode',
        'tactics_config': 'tactics_config'
    }

    def __init__(self, count=None, idle_mode=None, tactics_config=None):
        """UpdateFunctionReservedInstancesCountRequestBody

        The model defined in huaweicloud sdk

        :param count: 预留实例个数
        :type count: int
        :param idle_mode: 是否开启闲置模式配置
        :type idle_mode: bool
        :param tactics_config: 
        :type tactics_config: :class:`huaweicloudsdkfunctiongraph.v2.TacticsConfig`
        """
        
        

        self._count = None
        self._idle_mode = None
        self._tactics_config = None
        self.discriminator = None

        self.count = count
        if idle_mode is not None:
            self.idle_mode = idle_mode
        if tactics_config is not None:
            self.tactics_config = tactics_config

    @property
    def count(self):
        """Gets the count of this UpdateFunctionReservedInstancesCountRequestBody.

        预留实例个数

        :return: The count of this UpdateFunctionReservedInstancesCountRequestBody.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this UpdateFunctionReservedInstancesCountRequestBody.

        预留实例个数

        :param count: The count of this UpdateFunctionReservedInstancesCountRequestBody.
        :type count: int
        """
        self._count = count

    @property
    def idle_mode(self):
        """Gets the idle_mode of this UpdateFunctionReservedInstancesCountRequestBody.

        是否开启闲置模式配置

        :return: The idle_mode of this UpdateFunctionReservedInstancesCountRequestBody.
        :rtype: bool
        """
        return self._idle_mode

    @idle_mode.setter
    def idle_mode(self, idle_mode):
        """Sets the idle_mode of this UpdateFunctionReservedInstancesCountRequestBody.

        是否开启闲置模式配置

        :param idle_mode: The idle_mode of this UpdateFunctionReservedInstancesCountRequestBody.
        :type idle_mode: bool
        """
        self._idle_mode = idle_mode

    @property
    def tactics_config(self):
        """Gets the tactics_config of this UpdateFunctionReservedInstancesCountRequestBody.

        :return: The tactics_config of this UpdateFunctionReservedInstancesCountRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.TacticsConfig`
        """
        return self._tactics_config

    @tactics_config.setter
    def tactics_config(self, tactics_config):
        """Sets the tactics_config of this UpdateFunctionReservedInstancesCountRequestBody.

        :param tactics_config: The tactics_config of this UpdateFunctionReservedInstancesCountRequestBody.
        :type tactics_config: :class:`huaweicloudsdkfunctiongraph.v2.TacticsConfig`
        """
        self._tactics_config = tactics_config

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
        if not isinstance(other, UpdateFunctionReservedInstancesCountRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
