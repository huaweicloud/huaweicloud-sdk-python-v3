# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportDesktopVersionListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_version': 'str',
        'os_type': 'str',
        'desktop_id': 'str',
        'desktop_name': 'str',
        'username': 'str',
        'language': 'str'
    }

    attribute_map = {
        'agent_version': 'agent_version',
        'os_type': 'os_type',
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'username': 'username',
        'language': 'language'
    }

    def __init__(self, agent_version=None, os_type=None, desktop_id=None, desktop_name=None, username=None, language=None):
        r"""ExportDesktopVersionListRequest

        The model defined in huaweicloud sdk

        :param agent_version: 桌面agent版本号（精确匹配）。
        :type agent_version: str
        :param os_type: 桌面操作系统类型。
        :type os_type: str
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param desktop_name: 桌面名称（支持模糊匹配）。
        :type desktop_name: str
        :param username: 用户名（支持模糊匹配）。
        :type username: str
        :param language: 语言。  - zh_CN：中文 - en_US：英文
        :type language: str
        """
        
        

        self._agent_version = None
        self._os_type = None
        self._desktop_id = None
        self._desktop_name = None
        self._username = None
        self._language = None
        self.discriminator = None

        self.agent_version = agent_version
        self.os_type = os_type
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if username is not None:
            self.username = username
        self.language = language

    @property
    def agent_version(self):
        r"""Gets the agent_version of this ExportDesktopVersionListRequest.

        桌面agent版本号（精确匹配）。

        :return: The agent_version of this ExportDesktopVersionListRequest.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this ExportDesktopVersionListRequest.

        桌面agent版本号（精确匹配）。

        :param agent_version: The agent_version of this ExportDesktopVersionListRequest.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def os_type(self):
        r"""Gets the os_type of this ExportDesktopVersionListRequest.

        桌面操作系统类型。

        :return: The os_type of this ExportDesktopVersionListRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ExportDesktopVersionListRequest.

        桌面操作系统类型。

        :param os_type: The os_type of this ExportDesktopVersionListRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ExportDesktopVersionListRequest.

        桌面ID。

        :return: The desktop_id of this ExportDesktopVersionListRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ExportDesktopVersionListRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this ExportDesktopVersionListRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this ExportDesktopVersionListRequest.

        桌面名称（支持模糊匹配）。

        :return: The desktop_name of this ExportDesktopVersionListRequest.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this ExportDesktopVersionListRequest.

        桌面名称（支持模糊匹配）。

        :param desktop_name: The desktop_name of this ExportDesktopVersionListRequest.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def username(self):
        r"""Gets the username of this ExportDesktopVersionListRequest.

        用户名（支持模糊匹配）。

        :return: The username of this ExportDesktopVersionListRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ExportDesktopVersionListRequest.

        用户名（支持模糊匹配）。

        :param username: The username of this ExportDesktopVersionListRequest.
        :type username: str
        """
        self._username = username

    @property
    def language(self):
        r"""Gets the language of this ExportDesktopVersionListRequest.

        语言。  - zh_CN：中文 - en_US：英文

        :return: The language of this ExportDesktopVersionListRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportDesktopVersionListRequest.

        语言。  - zh_CN：中文 - en_US：英文

        :param language: The language of this ExportDesktopVersionListRequest.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, ExportDesktopVersionListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
