# coding: utf-8

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
        'trigger_conditions': 'list[str]',
        'message_template_name': 'str'
    }

    attribute_map = {
        'language': 'language',
        'topic_urn': 'topic_urn',
        'trigger_conditions': 'trigger_conditions',
        'message_template_name': 'message_template_name'
    }

    def __init__(self, language=None, topic_urn=None, trigger_conditions=None, message_template_name=None):
        r"""SmnConfig

        The model defined in huaweicloud sdk

        :param language: 当前用户所使用的管理控制台的语言。  可以选择zh-cn或者en-us。
        :type language: str
        :param topic_urn: 迁移任务所绑定的SMN消息主题的urn号。
        :type topic_urn: str
        :param trigger_conditions: SMN消息的触发条件，取决于迁移任务状态。  迁移任务状态的取值范围为SUCCESS或者FAILURE。  - FAILURE表示任务失败后发送SMN消息。 - SUCCESS表示任务成功后发送SMN消息。
        :type trigger_conditions: list[str]
        :param message_template_name: 如果设置此值，则表示用模板方式发送smn信息。 模板示例: {  “Task_Status”: \&quot;\&quot;,     \&quot;Task_Name\&quot; : \&quot;\&quot;,     \&quot;Start_Time\&quot;: \&quot;\&quot;,     \&quot;Total_Time_Used\&quot;: \&quot;\&quot;,     \&quot;Transferred_Data\&quot;: \&quot;\&quot;,     \&quot;Average_Speed\&quot;: \&quot;\&quot;,     \&quot;Source_Bucket\&quot;: \&quot;\&quot;,     \&quot;Destination_Bucket\&quot;: \&quot;\&quot;,     \&quot;List_File_Bucket\&quot;: \&quot;\&quot;,     \&quot;List_File_Key\&quot;: \&quot;\&quot;,     \&quot;Success_object_list_path\&quot;: \&quot;\&quot;,     \&quot;Skip_object_list_path\&quot;: \&quot;\&quot;,     \&quot;Failed_object_list_path\&quot;: \&quot;\&quot; }
        :type message_template_name: str
        """
        
        

        self._language = None
        self._topic_urn = None
        self._trigger_conditions = None
        self._message_template_name = None
        self.discriminator = None

        if language is not None:
            self.language = language
        self.topic_urn = topic_urn
        self.trigger_conditions = trigger_conditions
        if message_template_name is not None:
            self.message_template_name = message_template_name

    @property
    def language(self):
        r"""Gets the language of this SmnConfig.

        当前用户所使用的管理控制台的语言。  可以选择zh-cn或者en-us。

        :return: The language of this SmnConfig.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this SmnConfig.

        当前用户所使用的管理控制台的语言。  可以选择zh-cn或者en-us。

        :param language: The language of this SmnConfig.
        :type language: str
        """
        self._language = language

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this SmnConfig.

        迁移任务所绑定的SMN消息主题的urn号。

        :return: The topic_urn of this SmnConfig.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this SmnConfig.

        迁移任务所绑定的SMN消息主题的urn号。

        :param topic_urn: The topic_urn of this SmnConfig.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def trigger_conditions(self):
        r"""Gets the trigger_conditions of this SmnConfig.

        SMN消息的触发条件，取决于迁移任务状态。  迁移任务状态的取值范围为SUCCESS或者FAILURE。  - FAILURE表示任务失败后发送SMN消息。 - SUCCESS表示任务成功后发送SMN消息。

        :return: The trigger_conditions of this SmnConfig.
        :rtype: list[str]
        """
        return self._trigger_conditions

    @trigger_conditions.setter
    def trigger_conditions(self, trigger_conditions):
        r"""Sets the trigger_conditions of this SmnConfig.

        SMN消息的触发条件，取决于迁移任务状态。  迁移任务状态的取值范围为SUCCESS或者FAILURE。  - FAILURE表示任务失败后发送SMN消息。 - SUCCESS表示任务成功后发送SMN消息。

        :param trigger_conditions: The trigger_conditions of this SmnConfig.
        :type trigger_conditions: list[str]
        """
        self._trigger_conditions = trigger_conditions

    @property
    def message_template_name(self):
        r"""Gets the message_template_name of this SmnConfig.

        如果设置此值，则表示用模板方式发送smn信息。 模板示例: {  “Task_Status”: \"\",     \"Task_Name\" : \"\",     \"Start_Time\": \"\",     \"Total_Time_Used\": \"\",     \"Transferred_Data\": \"\",     \"Average_Speed\": \"\",     \"Source_Bucket\": \"\",     \"Destination_Bucket\": \"\",     \"List_File_Bucket\": \"\",     \"List_File_Key\": \"\",     \"Success_object_list_path\": \"\",     \"Skip_object_list_path\": \"\",     \"Failed_object_list_path\": \"\" }

        :return: The message_template_name of this SmnConfig.
        :rtype: str
        """
        return self._message_template_name

    @message_template_name.setter
    def message_template_name(self, message_template_name):
        r"""Sets the message_template_name of this SmnConfig.

        如果设置此值，则表示用模板方式发送smn信息。 模板示例: {  “Task_Status”: \"\",     \"Task_Name\" : \"\",     \"Start_Time\": \"\",     \"Total_Time_Used\": \"\",     \"Transferred_Data\": \"\",     \"Average_Speed\": \"\",     \"Source_Bucket\": \"\",     \"Destination_Bucket\": \"\",     \"List_File_Bucket\": \"\",     \"List_File_Key\": \"\",     \"Success_object_list_path\": \"\",     \"Skip_object_list_path\": \"\",     \"Failed_object_list_path\": \"\" }

        :param message_template_name: The message_template_name of this SmnConfig.
        :type message_template_name: str
        """
        self._message_template_name = message_template_name

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
