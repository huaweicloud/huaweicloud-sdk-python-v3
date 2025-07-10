# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesFileAndClipboard:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_redirection': 'PoliciesFileAndClipboardFileRedirection',
        'clip_length_limit_flag_c2s': 'bool',
        'clip_length_limit_c2s': 'int',
        'clip_length_limit_flag_s2c': 'bool',
        'clip_length_limit_s2c': 'int',
        'fd_mobile_client_redir_enable': 'bool',
        'clipboard_redirection': 'str',
        'clipboard_redirection_options': 'PoliciesFileAndClipboardClipboardRedirectionOptions'
    }

    attribute_map = {
        'file_redirection': 'file_redirection',
        'clip_length_limit_flag_c2s': 'clip_length_limit_flag_c2s',
        'clip_length_limit_c2s': 'clip_length_limit_c2s',
        'clip_length_limit_flag_s2c': 'clip_length_limit_flag_s2c',
        'clip_length_limit_s2c': 'clip_length_limit_s2c',
        'fd_mobile_client_redir_enable': 'fd_mobile_client_redir_enable',
        'clipboard_redirection': 'clipboard_redirection',
        'clipboard_redirection_options': 'clipboard_redirection_options'
    }

    def __init__(self, file_redirection=None, clip_length_limit_flag_c2s=None, clip_length_limit_c2s=None, clip_length_limit_flag_s2c=None, clip_length_limit_s2c=None, fd_mobile_client_redir_enable=None, clipboard_redirection=None, clipboard_redirection_options=None):
        r"""PoliciesFileAndClipboard

        The model defined in huaweicloud sdk

        :param file_redirection: 
        :type file_redirection: :class:`huaweicloudsdkworkspace.v2.PoliciesFileAndClipboardFileRedirection`
        :param clip_length_limit_flag_c2s: 剪切板长度表示。
        :type clip_length_limit_flag_c2s: bool
        :param clip_length_limit_c2s: 剪切板客户端长度。
        :type clip_length_limit_c2s: int
        :param clip_length_limit_flag_s2c: 剪切板长度表示。
        :type clip_length_limit_flag_s2c: bool
        :param clip_length_limit_s2c: 剪切板客户端长度。
        :type clip_length_limit_s2c: int
        :param fd_mobile_client_redir_enable: 移动客户端文件重定向：取值为： false：表示关闭。 true：表示开启。
        :type fd_mobile_client_redir_enable: bool
        :param clipboard_redirection: 剪切板重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。
        :type clipboard_redirection: str
        :param clipboard_redirection_options: 
        :type clipboard_redirection_options: :class:`huaweicloudsdkworkspace.v2.PoliciesFileAndClipboardClipboardRedirectionOptions`
        """
        
        

        self._file_redirection = None
        self._clip_length_limit_flag_c2s = None
        self._clip_length_limit_c2s = None
        self._clip_length_limit_flag_s2c = None
        self._clip_length_limit_s2c = None
        self._fd_mobile_client_redir_enable = None
        self._clipboard_redirection = None
        self._clipboard_redirection_options = None
        self.discriminator = None

        if file_redirection is not None:
            self.file_redirection = file_redirection
        if clip_length_limit_flag_c2s is not None:
            self.clip_length_limit_flag_c2s = clip_length_limit_flag_c2s
        if clip_length_limit_c2s is not None:
            self.clip_length_limit_c2s = clip_length_limit_c2s
        if clip_length_limit_flag_s2c is not None:
            self.clip_length_limit_flag_s2c = clip_length_limit_flag_s2c
        if clip_length_limit_s2c is not None:
            self.clip_length_limit_s2c = clip_length_limit_s2c
        if fd_mobile_client_redir_enable is not None:
            self.fd_mobile_client_redir_enable = fd_mobile_client_redir_enable
        if clipboard_redirection is not None:
            self.clipboard_redirection = clipboard_redirection
        if clipboard_redirection_options is not None:
            self.clipboard_redirection_options = clipboard_redirection_options

    @property
    def file_redirection(self):
        r"""Gets the file_redirection of this PoliciesFileAndClipboard.

        :return: The file_redirection of this PoliciesFileAndClipboard.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesFileAndClipboardFileRedirection`
        """
        return self._file_redirection

    @file_redirection.setter
    def file_redirection(self, file_redirection):
        r"""Sets the file_redirection of this PoliciesFileAndClipboard.

        :param file_redirection: The file_redirection of this PoliciesFileAndClipboard.
        :type file_redirection: :class:`huaweicloudsdkworkspace.v2.PoliciesFileAndClipboardFileRedirection`
        """
        self._file_redirection = file_redirection

    @property
    def clip_length_limit_flag_c2s(self):
        r"""Gets the clip_length_limit_flag_c2s of this PoliciesFileAndClipboard.

        剪切板长度表示。

        :return: The clip_length_limit_flag_c2s of this PoliciesFileAndClipboard.
        :rtype: bool
        """
        return self._clip_length_limit_flag_c2s

    @clip_length_limit_flag_c2s.setter
    def clip_length_limit_flag_c2s(self, clip_length_limit_flag_c2s):
        r"""Sets the clip_length_limit_flag_c2s of this PoliciesFileAndClipboard.

        剪切板长度表示。

        :param clip_length_limit_flag_c2s: The clip_length_limit_flag_c2s of this PoliciesFileAndClipboard.
        :type clip_length_limit_flag_c2s: bool
        """
        self._clip_length_limit_flag_c2s = clip_length_limit_flag_c2s

    @property
    def clip_length_limit_c2s(self):
        r"""Gets the clip_length_limit_c2s of this PoliciesFileAndClipboard.

        剪切板客户端长度。

        :return: The clip_length_limit_c2s of this PoliciesFileAndClipboard.
        :rtype: int
        """
        return self._clip_length_limit_c2s

    @clip_length_limit_c2s.setter
    def clip_length_limit_c2s(self, clip_length_limit_c2s):
        r"""Sets the clip_length_limit_c2s of this PoliciesFileAndClipboard.

        剪切板客户端长度。

        :param clip_length_limit_c2s: The clip_length_limit_c2s of this PoliciesFileAndClipboard.
        :type clip_length_limit_c2s: int
        """
        self._clip_length_limit_c2s = clip_length_limit_c2s

    @property
    def clip_length_limit_flag_s2c(self):
        r"""Gets the clip_length_limit_flag_s2c of this PoliciesFileAndClipboard.

        剪切板长度表示。

        :return: The clip_length_limit_flag_s2c of this PoliciesFileAndClipboard.
        :rtype: bool
        """
        return self._clip_length_limit_flag_s2c

    @clip_length_limit_flag_s2c.setter
    def clip_length_limit_flag_s2c(self, clip_length_limit_flag_s2c):
        r"""Sets the clip_length_limit_flag_s2c of this PoliciesFileAndClipboard.

        剪切板长度表示。

        :param clip_length_limit_flag_s2c: The clip_length_limit_flag_s2c of this PoliciesFileAndClipboard.
        :type clip_length_limit_flag_s2c: bool
        """
        self._clip_length_limit_flag_s2c = clip_length_limit_flag_s2c

    @property
    def clip_length_limit_s2c(self):
        r"""Gets the clip_length_limit_s2c of this PoliciesFileAndClipboard.

        剪切板客户端长度。

        :return: The clip_length_limit_s2c of this PoliciesFileAndClipboard.
        :rtype: int
        """
        return self._clip_length_limit_s2c

    @clip_length_limit_s2c.setter
    def clip_length_limit_s2c(self, clip_length_limit_s2c):
        r"""Sets the clip_length_limit_s2c of this PoliciesFileAndClipboard.

        剪切板客户端长度。

        :param clip_length_limit_s2c: The clip_length_limit_s2c of this PoliciesFileAndClipboard.
        :type clip_length_limit_s2c: int
        """
        self._clip_length_limit_s2c = clip_length_limit_s2c

    @property
    def fd_mobile_client_redir_enable(self):
        r"""Gets the fd_mobile_client_redir_enable of this PoliciesFileAndClipboard.

        移动客户端文件重定向：取值为： false：表示关闭。 true：表示开启。

        :return: The fd_mobile_client_redir_enable of this PoliciesFileAndClipboard.
        :rtype: bool
        """
        return self._fd_mobile_client_redir_enable

    @fd_mobile_client_redir_enable.setter
    def fd_mobile_client_redir_enable(self, fd_mobile_client_redir_enable):
        r"""Sets the fd_mobile_client_redir_enable of this PoliciesFileAndClipboard.

        移动客户端文件重定向：取值为： false：表示关闭。 true：表示开启。

        :param fd_mobile_client_redir_enable: The fd_mobile_client_redir_enable of this PoliciesFileAndClipboard.
        :type fd_mobile_client_redir_enable: bool
        """
        self._fd_mobile_client_redir_enable = fd_mobile_client_redir_enable

    @property
    def clipboard_redirection(self):
        r"""Gets the clipboard_redirection of this PoliciesFileAndClipboard.

        剪切板重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。

        :return: The clipboard_redirection of this PoliciesFileAndClipboard.
        :rtype: str
        """
        return self._clipboard_redirection

    @clipboard_redirection.setter
    def clipboard_redirection(self, clipboard_redirection):
        r"""Sets the clipboard_redirection of this PoliciesFileAndClipboard.

        剪切板重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。

        :param clipboard_redirection: The clipboard_redirection of this PoliciesFileAndClipboard.
        :type clipboard_redirection: str
        """
        self._clipboard_redirection = clipboard_redirection

    @property
    def clipboard_redirection_options(self):
        r"""Gets the clipboard_redirection_options of this PoliciesFileAndClipboard.

        :return: The clipboard_redirection_options of this PoliciesFileAndClipboard.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesFileAndClipboardClipboardRedirectionOptions`
        """
        return self._clipboard_redirection_options

    @clipboard_redirection_options.setter
    def clipboard_redirection_options(self, clipboard_redirection_options):
        r"""Sets the clipboard_redirection_options of this PoliciesFileAndClipboard.

        :param clipboard_redirection_options: The clipboard_redirection_options of this PoliciesFileAndClipboard.
        :type clipboard_redirection_options: :class:`huaweicloudsdkworkspace.v2.PoliciesFileAndClipboardClipboardRedirectionOptions`
        """
        self._clipboard_redirection_options = clipboard_redirection_options

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
        if not isinstance(other, PoliciesFileAndClipboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
