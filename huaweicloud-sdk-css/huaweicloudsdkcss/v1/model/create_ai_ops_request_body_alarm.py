# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAiOpsRequestBodyAlarm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'level': 'str',
        'smn_topic': 'str'
    }

    attribute_map = {
        'level': 'level',
        'smn_topic': 'smn_topic'
    }

    def __init__(self, level=None, smn_topic=None):
        """CreateAiOpsRequestBodyAlarm

        The model defined in huaweicloud sdk

        :param level: SMN告警消息敏感度。 - high：高风险。 - medium：中风险。 - suggestion：建议。 - norisk：无风险。
        :type level: str
        :param smn_topic: SMN主题名称。
        :type smn_topic: str
        """
        
        

        self._level = None
        self._smn_topic = None
        self.discriminator = None

        self.level = level
        self.smn_topic = smn_topic

    @property
    def level(self):
        """Gets the level of this CreateAiOpsRequestBodyAlarm.

        SMN告警消息敏感度。 - high：高风险。 - medium：中风险。 - suggestion：建议。 - norisk：无风险。

        :return: The level of this CreateAiOpsRequestBodyAlarm.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this CreateAiOpsRequestBodyAlarm.

        SMN告警消息敏感度。 - high：高风险。 - medium：中风险。 - suggestion：建议。 - norisk：无风险。

        :param level: The level of this CreateAiOpsRequestBodyAlarm.
        :type level: str
        """
        self._level = level

    @property
    def smn_topic(self):
        """Gets the smn_topic of this CreateAiOpsRequestBodyAlarm.

        SMN主题名称。

        :return: The smn_topic of this CreateAiOpsRequestBodyAlarm.
        :rtype: str
        """
        return self._smn_topic

    @smn_topic.setter
    def smn_topic(self, smn_topic):
        """Sets the smn_topic of this CreateAiOpsRequestBodyAlarm.

        SMN主题名称。

        :param smn_topic: The smn_topic of this CreateAiOpsRequestBodyAlarm.
        :type smn_topic: str
        """
        self._smn_topic = smn_topic

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
        if not isinstance(other, CreateAiOpsRequestBodyAlarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
