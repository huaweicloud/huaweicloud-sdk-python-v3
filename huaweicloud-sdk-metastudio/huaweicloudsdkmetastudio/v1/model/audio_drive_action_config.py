# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioDriveActionConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_tag': 'str',
        'action_name': 'str',
        'action_start_time': 'float'
    }

    attribute_map = {
        'action_tag': 'action_tag',
        'action_name': 'action_name',
        'action_start_time': 'action_start_time'
    }

    def __init__(self, action_tag=None, action_name=None, action_start_time=None):
        r"""AudioDriveActionConfig

        The model defined in huaweicloud sdk

        :param action_tag: 动作标签
        :type action_tag: str
        :param action_name: 动作名称
        :type action_name: str
        :param action_start_time: 动作开始时间
        :type action_start_time: float
        """
        
        

        self._action_tag = None
        self._action_name = None
        self._action_start_time = None
        self.discriminator = None

        self.action_tag = action_tag
        if action_name is not None:
            self.action_name = action_name
        self.action_start_time = action_start_time

    @property
    def action_tag(self):
        r"""Gets the action_tag of this AudioDriveActionConfig.

        动作标签

        :return: The action_tag of this AudioDriveActionConfig.
        :rtype: str
        """
        return self._action_tag

    @action_tag.setter
    def action_tag(self, action_tag):
        r"""Sets the action_tag of this AudioDriveActionConfig.

        动作标签

        :param action_tag: The action_tag of this AudioDriveActionConfig.
        :type action_tag: str
        """
        self._action_tag = action_tag

    @property
    def action_name(self):
        r"""Gets the action_name of this AudioDriveActionConfig.

        动作名称

        :return: The action_name of this AudioDriveActionConfig.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this AudioDriveActionConfig.

        动作名称

        :param action_name: The action_name of this AudioDriveActionConfig.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def action_start_time(self):
        r"""Gets the action_start_time of this AudioDriveActionConfig.

        动作开始时间

        :return: The action_start_time of this AudioDriveActionConfig.
        :rtype: float
        """
        return self._action_start_time

    @action_start_time.setter
    def action_start_time(self, action_start_time):
        r"""Sets the action_start_time of this AudioDriveActionConfig.

        动作开始时间

        :param action_start_time: The action_start_time of this AudioDriveActionConfig.
        :type action_start_time: float
        """
        self._action_start_time = action_start_time

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
        if not isinstance(other, AudioDriveActionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
