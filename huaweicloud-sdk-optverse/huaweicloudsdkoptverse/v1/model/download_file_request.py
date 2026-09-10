# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_need_content': 'bool',
        'chat_id': 'str',
        'filename': 'str'
    }

    attribute_map = {
        'x_need_content': 'X-Need-Content',
        'chat_id': 'chat_id',
        'filename': 'filename'
    }

    def __init__(self, x_need_content=None, chat_id=None, filename=None):
        r"""DownloadFileRequest

        The model defined in huaweicloud sdk

        :param x_need_content: **参数解释**：   返回文件内容。   **约束限制**：   不涉及 **取值范围**：   * true：返回文件内容 * false：不返回文件内容 **默认取值**：   false 
        :type x_need_content: bool
        :param chat_id: **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type chat_id: str
        :param filename: **参数解释**： 问答ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type filename: str
        """
        
        

        self._x_need_content = None
        self._chat_id = None
        self._filename = None
        self.discriminator = None

        if x_need_content is not None:
            self.x_need_content = x_need_content
        self.chat_id = chat_id
        self.filename = filename

    @property
    def x_need_content(self):
        r"""Gets the x_need_content of this DownloadFileRequest.

        **参数解释**：   返回文件内容。   **约束限制**：   不涉及 **取值范围**：   * true：返回文件内容 * false：不返回文件内容 **默认取值**：   false 

        :return: The x_need_content of this DownloadFileRequest.
        :rtype: bool
        """
        return self._x_need_content

    @x_need_content.setter
    def x_need_content(self, x_need_content):
        r"""Sets the x_need_content of this DownloadFileRequest.

        **参数解释**：   返回文件内容。   **约束限制**：   不涉及 **取值范围**：   * true：返回文件内容 * false：不返回文件内容 **默认取值**：   false 

        :param x_need_content: The x_need_content of this DownloadFileRequest.
        :type x_need_content: bool
        """
        self._x_need_content = x_need_content

    @property
    def chat_id(self):
        r"""Gets the chat_id of this DownloadFileRequest.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The chat_id of this DownloadFileRequest.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        r"""Sets the chat_id of this DownloadFileRequest.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param chat_id: The chat_id of this DownloadFileRequest.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def filename(self):
        r"""Gets the filename of this DownloadFileRequest.

        **参数解释**： 问答ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The filename of this DownloadFileRequest.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        r"""Sets the filename of this DownloadFileRequest.

        **参数解释**： 问答ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param filename: The filename of this DownloadFileRequest.
        :type filename: str
        """
        self._filename = filename

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DownloadFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
