# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateNotice:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_channel': 'str',
        'enable': 'str',
        'groups': 'list[AlertGroup]',
        'operate_types': 'list[str]'
    }

    attribute_map = {
        'alert_channel': 'alert_channel',
        'enable': 'enable',
        'groups': 'groups',
        'operate_types': 'operateTypes'
    }

    def __init__(self, alert_channel=None, enable=None, groups=None, operate_types=None):
        r"""OperateNotice

        The model defined in huaweicloud sdk

        :param alert_channel: 发送告警渠道
        :type alert_channel: str
        :param enable: 操作通知 0 关闭 1开启
        :type enable: str
        :param groups: 通知组列表
        :type groups: list[:class:`huaweicloudsdkcloudtest.v1.AlertGroup`]
        :param operate_types: 通知类型列表
        :type operate_types: list[str]
        """
        
        

        self._alert_channel = None
        self._enable = None
        self._groups = None
        self._operate_types = None
        self.discriminator = None

        if alert_channel is not None:
            self.alert_channel = alert_channel
        if enable is not None:
            self.enable = enable
        if groups is not None:
            self.groups = groups
        if operate_types is not None:
            self.operate_types = operate_types

    @property
    def alert_channel(self):
        r"""Gets the alert_channel of this OperateNotice.

        发送告警渠道

        :return: The alert_channel of this OperateNotice.
        :rtype: str
        """
        return self._alert_channel

    @alert_channel.setter
    def alert_channel(self, alert_channel):
        r"""Sets the alert_channel of this OperateNotice.

        发送告警渠道

        :param alert_channel: The alert_channel of this OperateNotice.
        :type alert_channel: str
        """
        self._alert_channel = alert_channel

    @property
    def enable(self):
        r"""Gets the enable of this OperateNotice.

        操作通知 0 关闭 1开启

        :return: The enable of this OperateNotice.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this OperateNotice.

        操作通知 0 关闭 1开启

        :param enable: The enable of this OperateNotice.
        :type enable: str
        """
        self._enable = enable

    @property
    def groups(self):
        r"""Gets the groups of this OperateNotice.

        通知组列表

        :return: The groups of this OperateNotice.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AlertGroup`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this OperateNotice.

        通知组列表

        :param groups: The groups of this OperateNotice.
        :type groups: list[:class:`huaweicloudsdkcloudtest.v1.AlertGroup`]
        """
        self._groups = groups

    @property
    def operate_types(self):
        r"""Gets the operate_types of this OperateNotice.

        通知类型列表

        :return: The operate_types of this OperateNotice.
        :rtype: list[str]
        """
        return self._operate_types

    @operate_types.setter
    def operate_types(self, operate_types):
        r"""Sets the operate_types of this OperateNotice.

        通知类型列表

        :param operate_types: The operate_types of this OperateNotice.
        :type operate_types: list[str]
        """
        self._operate_types = operate_types

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
        if not isinstance(other, OperateNotice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
