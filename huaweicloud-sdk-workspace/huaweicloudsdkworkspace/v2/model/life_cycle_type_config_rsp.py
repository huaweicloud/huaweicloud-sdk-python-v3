# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LifeCycleTypeConfigRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_wait_time': 'int',
        'default_wait_time': 'int',
        'min_exec_time': 'int',
        'default_exec_time': 'int',
        'support_exec_time': 'bool',
        'actions': 'list[ActionConfig]'
    }

    attribute_map = {
        'min_wait_time': 'min_wait_time',
        'default_wait_time': 'default_wait_time',
        'min_exec_time': 'min_exec_time',
        'default_exec_time': 'default_exec_time',
        'support_exec_time': 'support_exec_time',
        'actions': 'actions'
    }

    def __init__(self, min_wait_time=None, default_wait_time=None, min_exec_time=None, default_exec_time=None, support_exec_time=None, actions=None):
        r"""LifeCycleTypeConfigRsp

        The model defined in huaweicloud sdk

        :param min_wait_time: 最小等待时长，单位分钟。
        :type min_wait_time: int
        :param default_wait_time: 默认等待时长，单位分钟。
        :type default_wait_time: int
        :param min_exec_time: 最小执行周期，单位分钟。
        :type min_exec_time: int
        :param default_exec_time: 默认执行周期，单位分钟。
        :type default_exec_time: int
        :param support_exec_time: 是否支持执行周期。
        :type support_exec_time: bool
        :param actions: 可执行的动作列表。
        :type actions: list[:class:`huaweicloudsdkworkspace.v2.ActionConfig`]
        """
        
        

        self._min_wait_time = None
        self._default_wait_time = None
        self._min_exec_time = None
        self._default_exec_time = None
        self._support_exec_time = None
        self._actions = None
        self.discriminator = None

        if min_wait_time is not None:
            self.min_wait_time = min_wait_time
        if default_wait_time is not None:
            self.default_wait_time = default_wait_time
        if min_exec_time is not None:
            self.min_exec_time = min_exec_time
        if default_exec_time is not None:
            self.default_exec_time = default_exec_time
        if support_exec_time is not None:
            self.support_exec_time = support_exec_time
        if actions is not None:
            self.actions = actions

    @property
    def min_wait_time(self):
        r"""Gets the min_wait_time of this LifeCycleTypeConfigRsp.

        最小等待时长，单位分钟。

        :return: The min_wait_time of this LifeCycleTypeConfigRsp.
        :rtype: int
        """
        return self._min_wait_time

    @min_wait_time.setter
    def min_wait_time(self, min_wait_time):
        r"""Sets the min_wait_time of this LifeCycleTypeConfigRsp.

        最小等待时长，单位分钟。

        :param min_wait_time: The min_wait_time of this LifeCycleTypeConfigRsp.
        :type min_wait_time: int
        """
        self._min_wait_time = min_wait_time

    @property
    def default_wait_time(self):
        r"""Gets the default_wait_time of this LifeCycleTypeConfigRsp.

        默认等待时长，单位分钟。

        :return: The default_wait_time of this LifeCycleTypeConfigRsp.
        :rtype: int
        """
        return self._default_wait_time

    @default_wait_time.setter
    def default_wait_time(self, default_wait_time):
        r"""Sets the default_wait_time of this LifeCycleTypeConfigRsp.

        默认等待时长，单位分钟。

        :param default_wait_time: The default_wait_time of this LifeCycleTypeConfigRsp.
        :type default_wait_time: int
        """
        self._default_wait_time = default_wait_time

    @property
    def min_exec_time(self):
        r"""Gets the min_exec_time of this LifeCycleTypeConfigRsp.

        最小执行周期，单位分钟。

        :return: The min_exec_time of this LifeCycleTypeConfigRsp.
        :rtype: int
        """
        return self._min_exec_time

    @min_exec_time.setter
    def min_exec_time(self, min_exec_time):
        r"""Sets the min_exec_time of this LifeCycleTypeConfigRsp.

        最小执行周期，单位分钟。

        :param min_exec_time: The min_exec_time of this LifeCycleTypeConfigRsp.
        :type min_exec_time: int
        """
        self._min_exec_time = min_exec_time

    @property
    def default_exec_time(self):
        r"""Gets the default_exec_time of this LifeCycleTypeConfigRsp.

        默认执行周期，单位分钟。

        :return: The default_exec_time of this LifeCycleTypeConfigRsp.
        :rtype: int
        """
        return self._default_exec_time

    @default_exec_time.setter
    def default_exec_time(self, default_exec_time):
        r"""Sets the default_exec_time of this LifeCycleTypeConfigRsp.

        默认执行周期，单位分钟。

        :param default_exec_time: The default_exec_time of this LifeCycleTypeConfigRsp.
        :type default_exec_time: int
        """
        self._default_exec_time = default_exec_time

    @property
    def support_exec_time(self):
        r"""Gets the support_exec_time of this LifeCycleTypeConfigRsp.

        是否支持执行周期。

        :return: The support_exec_time of this LifeCycleTypeConfigRsp.
        :rtype: bool
        """
        return self._support_exec_time

    @support_exec_time.setter
    def support_exec_time(self, support_exec_time):
        r"""Sets the support_exec_time of this LifeCycleTypeConfigRsp.

        是否支持执行周期。

        :param support_exec_time: The support_exec_time of this LifeCycleTypeConfigRsp.
        :type support_exec_time: bool
        """
        self._support_exec_time = support_exec_time

    @property
    def actions(self):
        r"""Gets the actions of this LifeCycleTypeConfigRsp.

        可执行的动作列表。

        :return: The actions of this LifeCycleTypeConfigRsp.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ActionConfig`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this LifeCycleTypeConfigRsp.

        可执行的动作列表。

        :param actions: The actions of this LifeCycleTypeConfigRsp.
        :type actions: list[:class:`huaweicloudsdkworkspace.v2.ActionConfig`]
        """
        self._actions = actions

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LifeCycleTypeConfigRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
