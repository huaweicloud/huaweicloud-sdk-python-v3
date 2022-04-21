# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionSmnForwarding:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region_name': 'str',
        'project_id': 'str',
        'theme_name': 'str',
        'topic_urn': 'str',
        'message_content': 'str',
        'message_title': 'str'
    }

    attribute_map = {
        'region_name': 'region_name',
        'project_id': 'project_id',
        'theme_name': 'theme_name',
        'topic_urn': 'topic_urn',
        'message_content': 'message_content',
        'message_title': 'message_title'
    }

    def __init__(self, region_name=None, project_id=None, theme_name=None, topic_urn=None, message_content=None, message_title=None):
        """ActionSmnForwarding

        The model defined in huaweicloud sdk

        :param region_name: **参数说明**：SMN服务对应的region区域。
        :type region_name: str
        :param project_id: **参数说明**：SMN服务对应的projectId信息。
        :type project_id: str
        :param theme_name: **参数说明**：SMN服务对应的主题名称。
        :type theme_name: str
        :param topic_urn: **参数说明**：SMN服务对应的topic的主题URN。
        :type topic_urn: str
        :param message_content: **参数说明**：短信或邮件的内容。。
        :type message_content: str
        :param message_title: **参数说明**：短信或邮件的主题。。
        :type message_title: str
        """
        
        

        self._region_name = None
        self._project_id = None
        self._theme_name = None
        self._topic_urn = None
        self._message_content = None
        self._message_title = None
        self.discriminator = None

        self.region_name = region_name
        self.project_id = project_id
        self.theme_name = theme_name
        self.topic_urn = topic_urn
        self.message_content = message_content
        self.message_title = message_title

    @property
    def region_name(self):
        """Gets the region_name of this ActionSmnForwarding.

        **参数说明**：SMN服务对应的region区域。

        :return: The region_name of this ActionSmnForwarding.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ActionSmnForwarding.

        **参数说明**：SMN服务对应的region区域。

        :param region_name: The region_name of this ActionSmnForwarding.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        """Gets the project_id of this ActionSmnForwarding.

        **参数说明**：SMN服务对应的projectId信息。

        :return: The project_id of this ActionSmnForwarding.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ActionSmnForwarding.

        **参数说明**：SMN服务对应的projectId信息。

        :param project_id: The project_id of this ActionSmnForwarding.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def theme_name(self):
        """Gets the theme_name of this ActionSmnForwarding.

        **参数说明**：SMN服务对应的主题名称。

        :return: The theme_name of this ActionSmnForwarding.
        :rtype: str
        """
        return self._theme_name

    @theme_name.setter
    def theme_name(self, theme_name):
        """Sets the theme_name of this ActionSmnForwarding.

        **参数说明**：SMN服务对应的主题名称。

        :param theme_name: The theme_name of this ActionSmnForwarding.
        :type theme_name: str
        """
        self._theme_name = theme_name

    @property
    def topic_urn(self):
        """Gets the topic_urn of this ActionSmnForwarding.

        **参数说明**：SMN服务对应的topic的主题URN。

        :return: The topic_urn of this ActionSmnForwarding.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this ActionSmnForwarding.

        **参数说明**：SMN服务对应的topic的主题URN。

        :param topic_urn: The topic_urn of this ActionSmnForwarding.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def message_content(self):
        """Gets the message_content of this ActionSmnForwarding.

        **参数说明**：短信或邮件的内容。。

        :return: The message_content of this ActionSmnForwarding.
        :rtype: str
        """
        return self._message_content

    @message_content.setter
    def message_content(self, message_content):
        """Sets the message_content of this ActionSmnForwarding.

        **参数说明**：短信或邮件的内容。。

        :param message_content: The message_content of this ActionSmnForwarding.
        :type message_content: str
        """
        self._message_content = message_content

    @property
    def message_title(self):
        """Gets the message_title of this ActionSmnForwarding.

        **参数说明**：短信或邮件的主题。。

        :return: The message_title of this ActionSmnForwarding.
        :rtype: str
        """
        return self._message_title

    @message_title.setter
    def message_title(self, message_title):
        """Sets the message_title of this ActionSmnForwarding.

        **参数说明**：短信或邮件的主题。。

        :param message_title: The message_title of this ActionSmnForwarding.
        :type message_title: str
        """
        self._message_title = message_title

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
        if not isinstance(other, ActionSmnForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
