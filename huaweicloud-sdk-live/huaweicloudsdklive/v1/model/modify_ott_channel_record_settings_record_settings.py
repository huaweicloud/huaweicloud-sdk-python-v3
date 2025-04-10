# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyOttChannelRecordSettingsRecordSettings:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rollingbuffer_duration': 'int'
    }

    attribute_map = {
        'rollingbuffer_duration': 'rollingbuffer_duration'
    }

    def __init__(self, rollingbuffer_duration=None):
        r"""ModifyOttChannelRecordSettingsRecordSettings

        The model defined in huaweicloud sdk

        :param rollingbuffer_duration: 最大回看录制时长。在此时间段内会连续不断的录制，为必选项  单位：秒。取值为“0”时，表示不支持录制；最大支持录制14天。
        :type rollingbuffer_duration: int
        """
        
        

        self._rollingbuffer_duration = None
        self.discriminator = None

        if rollingbuffer_duration is not None:
            self.rollingbuffer_duration = rollingbuffer_duration

    @property
    def rollingbuffer_duration(self):
        r"""Gets the rollingbuffer_duration of this ModifyOttChannelRecordSettingsRecordSettings.

        最大回看录制时长。在此时间段内会连续不断的录制，为必选项  单位：秒。取值为“0”时，表示不支持录制；最大支持录制14天。

        :return: The rollingbuffer_duration of this ModifyOttChannelRecordSettingsRecordSettings.
        :rtype: int
        """
        return self._rollingbuffer_duration

    @rollingbuffer_duration.setter
    def rollingbuffer_duration(self, rollingbuffer_duration):
        r"""Sets the rollingbuffer_duration of this ModifyOttChannelRecordSettingsRecordSettings.

        最大回看录制时长。在此时间段内会连续不断的录制，为必选项  单位：秒。取值为“0”时，表示不支持录制；最大支持录制14天。

        :param rollingbuffer_duration: The rollingbuffer_duration of this ModifyOttChannelRecordSettingsRecordSettings.
        :type rollingbuffer_duration: int
        """
        self._rollingbuffer_duration = rollingbuffer_duration

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
        if not isinstance(other, ModifyOttChannelRecordSettingsRecordSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
