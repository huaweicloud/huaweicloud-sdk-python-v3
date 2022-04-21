# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'topic_urn': 'str',
        'trigger_conditions': 'list[str]'
    }

    attribute_map = {
        'language': 'language',
        'topic_urn': 'topic_urn',
        'trigger_conditions': 'trigger_conditions'
    }

    def __init__(self, language=None, topic_urn=None, trigger_conditions=None):
        """SmnConfig

        The model defined in huaweicloud sdk

        :param language: 当前用户所使用的管理控制台的语言。  可以选择zh-cn或者en-us。
        :type language: str
        :param topic_urn: 迁移任务所绑定的SMN消息主题的urn号。
        :type topic_urn: str
        :param trigger_conditions:   SMN消息的触发条件，取决于迁移任务状态。  迁移任务状态的取值范围为SUCCESS或者FAILURE。  - FAILURE表示任务失败后发送SMN消息。 - SUCCESS表示任务成功后发送SMN消息。
        :type trigger_conditions: list[str]
        """
        
        

        self._language = None
        self._topic_urn = None
        self._trigger_conditions = None
        self.discriminator = None

        if language is not None:
            self.language = language
        self.topic_urn = topic_urn
        self.trigger_conditions = trigger_conditions

    @property
    def language(self):
        """Gets the language of this SmnConfig.

        当前用户所使用的管理控制台的语言。  可以选择zh-cn或者en-us。

        :return: The language of this SmnConfig.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SmnConfig.

        当前用户所使用的管理控制台的语言。  可以选择zh-cn或者en-us。

        :param language: The language of this SmnConfig.
        :type language: str
        """
        self._language = language

    @property
    def topic_urn(self):
        """Gets the topic_urn of this SmnConfig.

        迁移任务所绑定的SMN消息主题的urn号。

        :return: The topic_urn of this SmnConfig.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this SmnConfig.

        迁移任务所绑定的SMN消息主题的urn号。

        :param topic_urn: The topic_urn of this SmnConfig.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def trigger_conditions(self):
        """Gets the trigger_conditions of this SmnConfig.

          SMN消息的触发条件，取决于迁移任务状态。  迁移任务状态的取值范围为SUCCESS或者FAILURE。  - FAILURE表示任务失败后发送SMN消息。 - SUCCESS表示任务成功后发送SMN消息。

        :return: The trigger_conditions of this SmnConfig.
        :rtype: list[str]
        """
        return self._trigger_conditions

    @trigger_conditions.setter
    def trigger_conditions(self, trigger_conditions):
        """Sets the trigger_conditions of this SmnConfig.

          SMN消息的触发条件，取决于迁移任务状态。  迁移任务状态的取值范围为SUCCESS或者FAILURE。  - FAILURE表示任务失败后发送SMN消息。 - SUCCESS表示任务成功后发送SMN消息。

        :param trigger_conditions: The trigger_conditions of this SmnConfig.
        :type trigger_conditions: list[str]
        """
        self._trigger_conditions = trigger_conditions

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
        if not isinstance(other, SmnConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
