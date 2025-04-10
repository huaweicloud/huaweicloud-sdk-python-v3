# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesFileAndClipboardClipboardRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rich_text_redirection_enable': 'bool',
        'rich_text_clipboard_redirection': 'str',
        'clipboard_file_redirection_enable': 'bool',
        'file_clipboard_redirection': 'str',
        'clipboard_length_limit_cts_enable': 'bool',
        'clipboard_length_limit_cts': 'int',
        'clipboard_length_limit_stc_enable': 'bool',
        'clipboard_length_limit_stc': 'int'
    }

    attribute_map = {
        'rich_text_redirection_enable': 'rich_text_redirection_enable',
        'rich_text_clipboard_redirection': 'rich_text_clipboard_redirection',
        'clipboard_file_redirection_enable': 'clipboard_file_redirection_enable',
        'file_clipboard_redirection': 'file_clipboard_redirection',
        'clipboard_length_limit_cts_enable': 'clipboard_length_limit_cts_enable',
        'clipboard_length_limit_cts': 'clipboard_length_limit_cts',
        'clipboard_length_limit_stc_enable': 'clipboard_length_limit_stc_enable',
        'clipboard_length_limit_stc': 'clipboard_length_limit_stc'
    }

    def __init__(self, rich_text_redirection_enable=None, rich_text_clipboard_redirection=None, clipboard_file_redirection_enable=None, file_clipboard_redirection=None, clipboard_length_limit_cts_enable=None, clipboard_length_limit_cts=None, clipboard_length_limit_stc_enable=None, clipboard_length_limit_stc=None):
        r"""PoliciesFileAndClipboardClipboardRedirectionOptions

        The model defined in huaweicloud sdk

        :param rich_text_redirection_enable: 是否开启剪切板富文本重定向。取值为： false：表示关闭。 true：表示开启。
        :type rich_text_redirection_enable: bool
        :param rich_text_clipboard_redirection: 剪切板富文本重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。
        :type rich_text_clipboard_redirection: str
        :param clipboard_file_redirection_enable: 是否开启剪切板文件重定向。取值为： false：表示关闭。 true：表示开启。
        :type clipboard_file_redirection_enable: bool
        :param file_clipboard_redirection: 剪切板文件重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。
        :type file_clipboard_redirection: str
        :param clipboard_length_limit_cts_enable: 本地到虚拟机长度限制开关。取值为： false: 标识关闭。 ture: 标识开启。
        :type clipboard_length_limit_cts_enable: bool
        :param clipboard_length_limit_cts: 本地到虚拟机长度限制。
        :type clipboard_length_limit_cts: int
        :param clipboard_length_limit_stc_enable: 虚拟机到本地到长度限制开关。取值为： false: 标识关闭。 ture: 标识开启。
        :type clipboard_length_limit_stc_enable: bool
        :param clipboard_length_limit_stc: 虚拟机到本地长度限制。
        :type clipboard_length_limit_stc: int
        """
        
        

        self._rich_text_redirection_enable = None
        self._rich_text_clipboard_redirection = None
        self._clipboard_file_redirection_enable = None
        self._file_clipboard_redirection = None
        self._clipboard_length_limit_cts_enable = None
        self._clipboard_length_limit_cts = None
        self._clipboard_length_limit_stc_enable = None
        self._clipboard_length_limit_stc = None
        self.discriminator = None

        if rich_text_redirection_enable is not None:
            self.rich_text_redirection_enable = rich_text_redirection_enable
        if rich_text_clipboard_redirection is not None:
            self.rich_text_clipboard_redirection = rich_text_clipboard_redirection
        if clipboard_file_redirection_enable is not None:
            self.clipboard_file_redirection_enable = clipboard_file_redirection_enable
        if file_clipboard_redirection is not None:
            self.file_clipboard_redirection = file_clipboard_redirection
        if clipboard_length_limit_cts_enable is not None:
            self.clipboard_length_limit_cts_enable = clipboard_length_limit_cts_enable
        if clipboard_length_limit_cts is not None:
            self.clipboard_length_limit_cts = clipboard_length_limit_cts
        if clipboard_length_limit_stc_enable is not None:
            self.clipboard_length_limit_stc_enable = clipboard_length_limit_stc_enable
        if clipboard_length_limit_stc is not None:
            self.clipboard_length_limit_stc = clipboard_length_limit_stc

    @property
    def rich_text_redirection_enable(self):
        r"""Gets the rich_text_redirection_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        是否开启剪切板富文本重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The rich_text_redirection_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :rtype: bool
        """
        return self._rich_text_redirection_enable

    @rich_text_redirection_enable.setter
    def rich_text_redirection_enable(self, rich_text_redirection_enable):
        r"""Sets the rich_text_redirection_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        是否开启剪切板富文本重定向。取值为： false：表示关闭。 true：表示开启。

        :param rich_text_redirection_enable: The rich_text_redirection_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :type rich_text_redirection_enable: bool
        """
        self._rich_text_redirection_enable = rich_text_redirection_enable

    @property
    def rich_text_clipboard_redirection(self):
        r"""Gets the rich_text_clipboard_redirection of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        剪切板富文本重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。

        :return: The rich_text_clipboard_redirection of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :rtype: str
        """
        return self._rich_text_clipboard_redirection

    @rich_text_clipboard_redirection.setter
    def rich_text_clipboard_redirection(self, rich_text_clipboard_redirection):
        r"""Sets the rich_text_clipboard_redirection of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        剪切板富文本重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。

        :param rich_text_clipboard_redirection: The rich_text_clipboard_redirection of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :type rich_text_clipboard_redirection: str
        """
        self._rich_text_clipboard_redirection = rich_text_clipboard_redirection

    @property
    def clipboard_file_redirection_enable(self):
        r"""Gets the clipboard_file_redirection_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        是否开启剪切板文件重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The clipboard_file_redirection_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :rtype: bool
        """
        return self._clipboard_file_redirection_enable

    @clipboard_file_redirection_enable.setter
    def clipboard_file_redirection_enable(self, clipboard_file_redirection_enable):
        r"""Sets the clipboard_file_redirection_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        是否开启剪切板文件重定向。取值为： false：表示关闭。 true：表示开启。

        :param clipboard_file_redirection_enable: The clipboard_file_redirection_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :type clipboard_file_redirection_enable: bool
        """
        self._clipboard_file_redirection_enable = clipboard_file_redirection_enable

    @property
    def file_clipboard_redirection(self):
        r"""Gets the file_clipboard_redirection of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        剪切板文件重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。

        :return: The file_clipboard_redirection of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :rtype: str
        """
        return self._file_clipboard_redirection

    @file_clipboard_redirection.setter
    def file_clipboard_redirection(self, file_clipboard_redirection):
        r"""Sets the file_clipboard_redirection of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        剪切板文件重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。

        :param file_clipboard_redirection: The file_clipboard_redirection of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :type file_clipboard_redirection: str
        """
        self._file_clipboard_redirection = file_clipboard_redirection

    @property
    def clipboard_length_limit_cts_enable(self):
        r"""Gets the clipboard_length_limit_cts_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        本地到虚拟机长度限制开关。取值为： false: 标识关闭。 ture: 标识开启。

        :return: The clipboard_length_limit_cts_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :rtype: bool
        """
        return self._clipboard_length_limit_cts_enable

    @clipboard_length_limit_cts_enable.setter
    def clipboard_length_limit_cts_enable(self, clipboard_length_limit_cts_enable):
        r"""Sets the clipboard_length_limit_cts_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        本地到虚拟机长度限制开关。取值为： false: 标识关闭。 ture: 标识开启。

        :param clipboard_length_limit_cts_enable: The clipboard_length_limit_cts_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :type clipboard_length_limit_cts_enable: bool
        """
        self._clipboard_length_limit_cts_enable = clipboard_length_limit_cts_enable

    @property
    def clipboard_length_limit_cts(self):
        r"""Gets the clipboard_length_limit_cts of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        本地到虚拟机长度限制。

        :return: The clipboard_length_limit_cts of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :rtype: int
        """
        return self._clipboard_length_limit_cts

    @clipboard_length_limit_cts.setter
    def clipboard_length_limit_cts(self, clipboard_length_limit_cts):
        r"""Sets the clipboard_length_limit_cts of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        本地到虚拟机长度限制。

        :param clipboard_length_limit_cts: The clipboard_length_limit_cts of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :type clipboard_length_limit_cts: int
        """
        self._clipboard_length_limit_cts = clipboard_length_limit_cts

    @property
    def clipboard_length_limit_stc_enable(self):
        r"""Gets the clipboard_length_limit_stc_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        虚拟机到本地到长度限制开关。取值为： false: 标识关闭。 ture: 标识开启。

        :return: The clipboard_length_limit_stc_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :rtype: bool
        """
        return self._clipboard_length_limit_stc_enable

    @clipboard_length_limit_stc_enable.setter
    def clipboard_length_limit_stc_enable(self, clipboard_length_limit_stc_enable):
        r"""Sets the clipboard_length_limit_stc_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        虚拟机到本地到长度限制开关。取值为： false: 标识关闭。 ture: 标识开启。

        :param clipboard_length_limit_stc_enable: The clipboard_length_limit_stc_enable of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :type clipboard_length_limit_stc_enable: bool
        """
        self._clipboard_length_limit_stc_enable = clipboard_length_limit_stc_enable

    @property
    def clipboard_length_limit_stc(self):
        r"""Gets the clipboard_length_limit_stc of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        虚拟机到本地长度限制。

        :return: The clipboard_length_limit_stc of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :rtype: int
        """
        return self._clipboard_length_limit_stc

    @clipboard_length_limit_stc.setter
    def clipboard_length_limit_stc(self, clipboard_length_limit_stc):
        r"""Sets the clipboard_length_limit_stc of this PoliciesFileAndClipboardClipboardRedirectionOptions.

        虚拟机到本地长度限制。

        :param clipboard_length_limit_stc: The clipboard_length_limit_stc of this PoliciesFileAndClipboardClipboardRedirectionOptions.
        :type clipboard_length_limit_stc: int
        """
        self._clipboard_length_limit_stc = clipboard_length_limit_stc

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
        if not isinstance(other, PoliciesFileAndClipboardClipboardRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
