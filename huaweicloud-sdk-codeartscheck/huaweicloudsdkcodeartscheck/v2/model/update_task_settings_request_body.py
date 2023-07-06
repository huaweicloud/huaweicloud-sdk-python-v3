# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskSettingsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_advanced_settings': 'list[TaskAdvancedSettingsItem]'
    }

    attribute_map = {
        'task_advanced_settings': 'task_advanced_settings'
    }

    def __init__(self, task_advanced_settings=None):
        """UpdateTaskSettingsRequestBody

        The model defined in huaweicloud sdk

        :param task_advanced_settings: 高级选项参数的相关信息
        :type task_advanced_settings: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskAdvancedSettingsItem`]
        """
        
        

        self._task_advanced_settings = None
        self.discriminator = None

        self.task_advanced_settings = task_advanced_settings

    @property
    def task_advanced_settings(self):
        """Gets the task_advanced_settings of this UpdateTaskSettingsRequestBody.

        高级选项参数的相关信息

        :return: The task_advanced_settings of this UpdateTaskSettingsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskAdvancedSettingsItem`]
        """
        return self._task_advanced_settings

    @task_advanced_settings.setter
    def task_advanced_settings(self, task_advanced_settings):
        """Sets the task_advanced_settings of this UpdateTaskSettingsRequestBody.

        高级选项参数的相关信息

        :param task_advanced_settings: The task_advanced_settings of this UpdateTaskSettingsRequestBody.
        :type task_advanced_settings: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskAdvancedSettingsItem`]
        """
        self._task_advanced_settings = task_advanced_settings

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
        if not isinstance(other, UpdateTaskSettingsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
