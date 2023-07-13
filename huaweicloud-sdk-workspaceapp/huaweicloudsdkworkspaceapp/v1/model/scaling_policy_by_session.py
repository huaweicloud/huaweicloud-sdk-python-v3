# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingPolicyBySession:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_usage_threshold': 'int',
        'shrink_after_session_idle_minutes': 'int'
    }

    attribute_map = {
        'session_usage_threshold': 'session_usage_threshold',
        'shrink_after_session_idle_minutes': 'shrink_after_session_idle_minutes'
    }

    def __init__(self, session_usage_threshold=None, shrink_after_session_idle_minutes=None):
        """ScalingPolicyBySession

        The model defined in huaweicloud sdk

        :param session_usage_threshold: 分组的总会话使用率(达到改阈值后扩容)
        :type session_usage_threshold: int
        :param shrink_after_session_idle_minutes: 给定时间内无会话连接的的实例进行释放
        :type shrink_after_session_idle_minutes: int
        """
        
        

        self._session_usage_threshold = None
        self._shrink_after_session_idle_minutes = None
        self.discriminator = None

        self.session_usage_threshold = session_usage_threshold
        self.shrink_after_session_idle_minutes = shrink_after_session_idle_minutes

    @property
    def session_usage_threshold(self):
        """Gets the session_usage_threshold of this ScalingPolicyBySession.

        分组的总会话使用率(达到改阈值后扩容)

        :return: The session_usage_threshold of this ScalingPolicyBySession.
        :rtype: int
        """
        return self._session_usage_threshold

    @session_usage_threshold.setter
    def session_usage_threshold(self, session_usage_threshold):
        """Sets the session_usage_threshold of this ScalingPolicyBySession.

        分组的总会话使用率(达到改阈值后扩容)

        :param session_usage_threshold: The session_usage_threshold of this ScalingPolicyBySession.
        :type session_usage_threshold: int
        """
        self._session_usage_threshold = session_usage_threshold

    @property
    def shrink_after_session_idle_minutes(self):
        """Gets the shrink_after_session_idle_minutes of this ScalingPolicyBySession.

        给定时间内无会话连接的的实例进行释放

        :return: The shrink_after_session_idle_minutes of this ScalingPolicyBySession.
        :rtype: int
        """
        return self._shrink_after_session_idle_minutes

    @shrink_after_session_idle_minutes.setter
    def shrink_after_session_idle_minutes(self, shrink_after_session_idle_minutes):
        """Sets the shrink_after_session_idle_minutes of this ScalingPolicyBySession.

        给定时间内无会话连接的的实例进行释放

        :param shrink_after_session_idle_minutes: The shrink_after_session_idle_minutes of this ScalingPolicyBySession.
        :type shrink_after_session_idle_minutes: int
        """
        self._shrink_after_session_idle_minutes = shrink_after_session_idle_minutes

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
        if not isinstance(other, ScalingPolicyBySession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
