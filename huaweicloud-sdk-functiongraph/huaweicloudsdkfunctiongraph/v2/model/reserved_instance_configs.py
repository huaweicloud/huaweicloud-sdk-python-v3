# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReservedInstanceConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'qualifier_type': 'str',
        'qualifier_name': 'str',
        'min_count': 'int',
        'idle_mode': 'bool',
        'tactics_config': 'TacticsConfig'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'qualifier_type': 'qualifier_type',
        'qualifier_name': 'qualifier_name',
        'min_count': 'min_count',
        'idle_mode': 'idle_mode',
        'tactics_config': 'tactics_config'
    }

    def __init__(self, function_urn=None, qualifier_type=None, qualifier_name=None, min_count=None, idle_mode=None, tactics_config=None):
        r"""ReservedInstanceConfigs

        The model defined in huaweicloud sdk

        :param function_urn: 函数URN
        :type function_urn: str
        :param qualifier_type: 限定类型, 支持version和alias
        :type qualifier_type: str
        :param qualifier_name: 限定类型对应的取值
        :type qualifier_name: str
        :param min_count: 预留实例个数
        :type min_count: int
        :param idle_mode: 是否开启闲置模式配置
        :type idle_mode: bool
        :param tactics_config: 
        :type tactics_config: :class:`huaweicloudsdkfunctiongraph.v2.TacticsConfig`
        """
        
        

        self._function_urn = None
        self._qualifier_type = None
        self._qualifier_name = None
        self._min_count = None
        self._idle_mode = None
        self._tactics_config = None
        self.discriminator = None

        if function_urn is not None:
            self.function_urn = function_urn
        if qualifier_type is not None:
            self.qualifier_type = qualifier_type
        if qualifier_name is not None:
            self.qualifier_name = qualifier_name
        if min_count is not None:
            self.min_count = min_count
        if idle_mode is not None:
            self.idle_mode = idle_mode
        if tactics_config is not None:
            self.tactics_config = tactics_config

    @property
    def function_urn(self):
        r"""Gets the function_urn of this ReservedInstanceConfigs.

        函数URN

        :return: The function_urn of this ReservedInstanceConfigs.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        r"""Sets the function_urn of this ReservedInstanceConfigs.

        函数URN

        :param function_urn: The function_urn of this ReservedInstanceConfigs.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def qualifier_type(self):
        r"""Gets the qualifier_type of this ReservedInstanceConfigs.

        限定类型, 支持version和alias

        :return: The qualifier_type of this ReservedInstanceConfigs.
        :rtype: str
        """
        return self._qualifier_type

    @qualifier_type.setter
    def qualifier_type(self, qualifier_type):
        r"""Sets the qualifier_type of this ReservedInstanceConfigs.

        限定类型, 支持version和alias

        :param qualifier_type: The qualifier_type of this ReservedInstanceConfigs.
        :type qualifier_type: str
        """
        self._qualifier_type = qualifier_type

    @property
    def qualifier_name(self):
        r"""Gets the qualifier_name of this ReservedInstanceConfigs.

        限定类型对应的取值

        :return: The qualifier_name of this ReservedInstanceConfigs.
        :rtype: str
        """
        return self._qualifier_name

    @qualifier_name.setter
    def qualifier_name(self, qualifier_name):
        r"""Sets the qualifier_name of this ReservedInstanceConfigs.

        限定类型对应的取值

        :param qualifier_name: The qualifier_name of this ReservedInstanceConfigs.
        :type qualifier_name: str
        """
        self._qualifier_name = qualifier_name

    @property
    def min_count(self):
        r"""Gets the min_count of this ReservedInstanceConfigs.

        预留实例个数

        :return: The min_count of this ReservedInstanceConfigs.
        :rtype: int
        """
        return self._min_count

    @min_count.setter
    def min_count(self, min_count):
        r"""Sets the min_count of this ReservedInstanceConfigs.

        预留实例个数

        :param min_count: The min_count of this ReservedInstanceConfigs.
        :type min_count: int
        """
        self._min_count = min_count

    @property
    def idle_mode(self):
        r"""Gets the idle_mode of this ReservedInstanceConfigs.

        是否开启闲置模式配置

        :return: The idle_mode of this ReservedInstanceConfigs.
        :rtype: bool
        """
        return self._idle_mode

    @idle_mode.setter
    def idle_mode(self, idle_mode):
        r"""Sets the idle_mode of this ReservedInstanceConfigs.

        是否开启闲置模式配置

        :param idle_mode: The idle_mode of this ReservedInstanceConfigs.
        :type idle_mode: bool
        """
        self._idle_mode = idle_mode

    @property
    def tactics_config(self):
        r"""Gets the tactics_config of this ReservedInstanceConfigs.

        :return: The tactics_config of this ReservedInstanceConfigs.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.TacticsConfig`
        """
        return self._tactics_config

    @tactics_config.setter
    def tactics_config(self, tactics_config):
        r"""Sets the tactics_config of this ReservedInstanceConfigs.

        :param tactics_config: The tactics_config of this ReservedInstanceConfigs.
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
        if not isinstance(other, ReservedInstanceConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
