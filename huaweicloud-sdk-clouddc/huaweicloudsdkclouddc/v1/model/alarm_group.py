# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label': 'str',
        'alarm_devices': 'list[AlarmDeviceInfo]',
        'sns': 'list[str]'
    }

    attribute_map = {
        'label': 'label',
        'alarm_devices': 'alarm_devices',
        'sns': 'sns'
    }

    def __init__(self, label=None, alarm_devices=None, sns=None):
        r"""AlarmGroup

        The model defined in huaweicloud sdk

        :param label: 标签
        :type label: str
        :param alarm_devices: 告警设备
        :type alarm_devices: list[:class:`huaweicloudsdkclouddc.v1.AlarmDeviceInfo`]
        :param sns: sn列表
        :type sns: list[str]
        """
        
        

        self._label = None
        self._alarm_devices = None
        self._sns = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if alarm_devices is not None:
            self.alarm_devices = alarm_devices
        if sns is not None:
            self.sns = sns

    @property
    def label(self):
        r"""Gets the label of this AlarmGroup.

        标签

        :return: The label of this AlarmGroup.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this AlarmGroup.

        标签

        :param label: The label of this AlarmGroup.
        :type label: str
        """
        self._label = label

    @property
    def alarm_devices(self):
        r"""Gets the alarm_devices of this AlarmGroup.

        告警设备

        :return: The alarm_devices of this AlarmGroup.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.AlarmDeviceInfo`]
        """
        return self._alarm_devices

    @alarm_devices.setter
    def alarm_devices(self, alarm_devices):
        r"""Sets the alarm_devices of this AlarmGroup.

        告警设备

        :param alarm_devices: The alarm_devices of this AlarmGroup.
        :type alarm_devices: list[:class:`huaweicloudsdkclouddc.v1.AlarmDeviceInfo`]
        """
        self._alarm_devices = alarm_devices

    @property
    def sns(self):
        r"""Gets the sns of this AlarmGroup.

        sn列表

        :return: The sns of this AlarmGroup.
        :rtype: list[str]
        """
        return self._sns

    @sns.setter
    def sns(self, sns):
        r"""Sets the sns of this AlarmGroup.

        sn列表

        :param sns: The sns of this AlarmGroup.
        :type sns: list[str]
        """
        self._sns = sns

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
        if not isinstance(other, AlarmGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
