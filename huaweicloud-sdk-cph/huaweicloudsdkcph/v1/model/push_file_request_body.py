# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PushFileRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command': 'str',
        'content': 'str',
        'phone_ids': 'list[str]',
        'server_ids': 'list[str]'
    }

    attribute_map = {
        'command': 'command',
        'content': 'content',
        'phone_ids': 'phone_ids',
        'server_ids': 'server_ids'
    }

    def __init__(self, command=None, content=None, phone_ids=None, server_ids=None):
        r"""PushFileRequestBody

        The model defined in huaweicloud sdk

        :param command: 推送文件固定填写push。
        :type command: str
        :param content: 推送的文件只支持tar文件类型，指定OBS桶中的tar文件。 最大长度为1024字节，只支持大小写字母、数字、下划线（_）、点（.）、斜线（/）、冒号（:）、中划线（-）。文件格式：obs://obs-bucket-name/obs-file-path/file.tar，文件路径与OBS桶对象路径对应。
        :type content: str
        :param phone_ids: 云手机ID列表。 server_ids参数不存在时必选，同时存在只处理phone_ids。
        :type phone_ids: list[str]
        :param server_ids: 云手机服务器ID列表。 phone_ids参数不存在时必选，同时存在只处理phone_ids。
        :type server_ids: list[str]
        """
        
        

        self._command = None
        self._content = None
        self._phone_ids = None
        self._server_ids = None
        self.discriminator = None

        self.command = command
        self.content = content
        if phone_ids is not None:
            self.phone_ids = phone_ids
        if server_ids is not None:
            self.server_ids = server_ids

    @property
    def command(self):
        r"""Gets the command of this PushFileRequestBody.

        推送文件固定填写push。

        :return: The command of this PushFileRequestBody.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this PushFileRequestBody.

        推送文件固定填写push。

        :param command: The command of this PushFileRequestBody.
        :type command: str
        """
        self._command = command

    @property
    def content(self):
        r"""Gets the content of this PushFileRequestBody.

        推送的文件只支持tar文件类型，指定OBS桶中的tar文件。 最大长度为1024字节，只支持大小写字母、数字、下划线（_）、点（.）、斜线（/）、冒号（:）、中划线（-）。文件格式：obs://obs-bucket-name/obs-file-path/file.tar，文件路径与OBS桶对象路径对应。

        :return: The content of this PushFileRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this PushFileRequestBody.

        推送的文件只支持tar文件类型，指定OBS桶中的tar文件。 最大长度为1024字节，只支持大小写字母、数字、下划线（_）、点（.）、斜线（/）、冒号（:）、中划线（-）。文件格式：obs://obs-bucket-name/obs-file-path/file.tar，文件路径与OBS桶对象路径对应。

        :param content: The content of this PushFileRequestBody.
        :type content: str
        """
        self._content = content

    @property
    def phone_ids(self):
        r"""Gets the phone_ids of this PushFileRequestBody.

        云手机ID列表。 server_ids参数不存在时必选，同时存在只处理phone_ids。

        :return: The phone_ids of this PushFileRequestBody.
        :rtype: list[str]
        """
        return self._phone_ids

    @phone_ids.setter
    def phone_ids(self, phone_ids):
        r"""Sets the phone_ids of this PushFileRequestBody.

        云手机ID列表。 server_ids参数不存在时必选，同时存在只处理phone_ids。

        :param phone_ids: The phone_ids of this PushFileRequestBody.
        :type phone_ids: list[str]
        """
        self._phone_ids = phone_ids

    @property
    def server_ids(self):
        r"""Gets the server_ids of this PushFileRequestBody.

        云手机服务器ID列表。 phone_ids参数不存在时必选，同时存在只处理phone_ids。

        :return: The server_ids of this PushFileRequestBody.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        r"""Sets the server_ids of this PushFileRequestBody.

        云手机服务器ID列表。 phone_ids参数不存在时必选，同时存在只处理phone_ids。

        :param server_ids: The server_ids of this PushFileRequestBody.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

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
        if not isinstance(other, PushFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
