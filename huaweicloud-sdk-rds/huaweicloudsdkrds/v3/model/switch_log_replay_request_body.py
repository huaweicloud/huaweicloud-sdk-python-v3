# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchLogReplayRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pause_log_replay': 'str'
    }

    attribute_map = {
        'pause_log_replay': 'pause_log_replay'
    }

    def __init__(self, pause_log_replay=None):
        r"""SwitchLogReplayRequestBody

        The model defined in huaweicloud sdk

        :param pause_log_replay: “true”表示中止回放，“false”表示恢复回放，其他情况表示不做操作
        :type pause_log_replay: str
        """
        
        

        self._pause_log_replay = None
        self.discriminator = None

        self.pause_log_replay = pause_log_replay

    @property
    def pause_log_replay(self):
        r"""Gets the pause_log_replay of this SwitchLogReplayRequestBody.

        “true”表示中止回放，“false”表示恢复回放，其他情况表示不做操作

        :return: The pause_log_replay of this SwitchLogReplayRequestBody.
        :rtype: str
        """
        return self._pause_log_replay

    @pause_log_replay.setter
    def pause_log_replay(self, pause_log_replay):
        r"""Sets the pause_log_replay of this SwitchLogReplayRequestBody.

        “true”表示中止回放，“false”表示恢复回放，其他情况表示不做操作

        :param pause_log_replay: The pause_log_replay of this SwitchLogReplayRequestBody.
        :type pause_log_replay: str
        """
        self._pause_log_replay = pause_log_replay

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
        if not isinstance(other, SwitchLogReplayRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
