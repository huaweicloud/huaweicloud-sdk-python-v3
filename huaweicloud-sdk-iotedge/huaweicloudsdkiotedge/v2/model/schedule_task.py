# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_ids': 'list[str]',
        'action': 'str',
        'paras': 'object'
    }

    attribute_map = {
        'device_ids': 'device_ids',
        'action': 'action',
        'paras': 'paras'
    }

    def __init__(self, device_ids=None, action=None, paras=None):
        """ScheduleTask

        The model defined in huaweicloud sdk

        :param device_ids: 设备id数组
        :type device_ids: list[str]
        :param action: 任务执行的动作，当前支持SetProperties
        :type action: str
        :param paras: 对应action的参数
        :type paras: object
        """
        
        

        self._device_ids = None
        self._action = None
        self._paras = None
        self.discriminator = None

        self.device_ids = device_ids
        self.action = action
        self.paras = paras

    @property
    def device_ids(self):
        """Gets the device_ids of this ScheduleTask.

        设备id数组

        :return: The device_ids of this ScheduleTask.
        :rtype: list[str]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this ScheduleTask.

        设备id数组

        :param device_ids: The device_ids of this ScheduleTask.
        :type device_ids: list[str]
        """
        self._device_ids = device_ids

    @property
    def action(self):
        """Gets the action of this ScheduleTask.

        任务执行的动作，当前支持SetProperties

        :return: The action of this ScheduleTask.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ScheduleTask.

        任务执行的动作，当前支持SetProperties

        :param action: The action of this ScheduleTask.
        :type action: str
        """
        self._action = action

    @property
    def paras(self):
        """Gets the paras of this ScheduleTask.

        对应action的参数

        :return: The paras of this ScheduleTask.
        :rtype: object
        """
        return self._paras

    @paras.setter
    def paras(self, paras):
        """Sets the paras of this ScheduleTask.

        对应action的参数

        :param paras: The paras of this ScheduleTask.
        :type paras: object
        """
        self._paras = paras

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
        if not isinstance(other, ScheduleTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
