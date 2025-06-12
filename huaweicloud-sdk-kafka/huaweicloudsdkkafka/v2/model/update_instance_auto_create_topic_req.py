# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceAutoCreateTopicReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_auto_topic': 'bool'
    }

    attribute_map = {
        'enable_auto_topic': 'enable_auto_topic'
    }

    def __init__(self, enable_auto_topic=None):
        r"""UpdateInstanceAutoCreateTopicReq

        The model defined in huaweicloud sdk

        :param enable_auto_topic: 是否开启自动创建Topic功能。
        :type enable_auto_topic: bool
        """
        
        

        self._enable_auto_topic = None
        self.discriminator = None

        self.enable_auto_topic = enable_auto_topic

    @property
    def enable_auto_topic(self):
        r"""Gets the enable_auto_topic of this UpdateInstanceAutoCreateTopicReq.

        是否开启自动创建Topic功能。

        :return: The enable_auto_topic of this UpdateInstanceAutoCreateTopicReq.
        :rtype: bool
        """
        return self._enable_auto_topic

    @enable_auto_topic.setter
    def enable_auto_topic(self, enable_auto_topic):
        r"""Sets the enable_auto_topic of this UpdateInstanceAutoCreateTopicReq.

        是否开启自动创建Topic功能。

        :param enable_auto_topic: The enable_auto_topic of this UpdateInstanceAutoCreateTopicReq.
        :type enable_auto_topic: bool
        """
        self._enable_auto_topic = enable_auto_topic

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
        if not isinstance(other, UpdateInstanceAutoCreateTopicReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
