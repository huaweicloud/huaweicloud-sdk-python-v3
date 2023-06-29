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
        'bypass_in_remote_app_enable': 'bool',
        'file_redirection': 'PoliciesFileAndClipboardFileRedirection',
        'fd_mobile_client_redir_enable': 'bool',
        'clipboard_redirection': 'str',
        'clipboard_redirection_options': 'PoliciesFileAndClipboardClipboardRedirectionOptions'
    }

    attribute_map = {
        'bypass_in_remote_app_enable': 'bypass_in_remote_app_enable',
        'file_redirection': 'file_redirection',
        'fd_mobile_client_redir_enable': 'fd_mobile_client_redir_enable',
        'clipboard_redirection': 'clipboard_redirection',
        'clipboard_redirection_options': 'clipboard_redirection_options'
    }

    def __init__(self, bypass_in_remote_app_enable=None, file_redirection=None, fd_mobile_client_redir_enable=None, clipboard_redirection=None, clipboard_redirection_options=None):
        """PoliciesFileAndClipboard

        The model defined in huaweicloud sdk

        :param bypass_in_remote_app_enable: 应用聚合场景下是否双向放通：取值为： false：表示不放通。 true：表示放通。
        :type bypass_in_remote_app_enable: bool
        :param file_redirection: 
        :type file_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboardFileRedirection`
        :param fd_mobile_client_redir_enable: 移动客户端文件重定向：取值为： false：表示关闭。 true：表示开启。
        :type fd_mobile_client_redir_enable: bool
        :param clipboard_redirection: 剪切板重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。
        :type clipboard_redirection: str
        :param clipboard_redirection_options: 
        :type clipboard_redirection_options: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboardClipboardRedirectionOptions`
        """
        
        

        self._bypass_in_remote_app_enable = None
        self._file_redirection = None
        self._fd_mobile_client_redir_enable = None
        self._clipboard_redirection = None
        self._clipboard_redirection_options = None
        self.discriminator = None

        if bypass_in_remote_app_enable is not None:
            self.bypass_in_remote_app_enable = bypass_in_remote_app_enable
        if file_redirection is not None:
            self.file_redirection = file_redirection
        if fd_mobile_client_redir_enable is not None:
            self.fd_mobile_client_redir_enable = fd_mobile_client_redir_enable
        if clipboard_redirection is not None:
            self.clipboard_redirection = clipboard_redirection
        if clipboard_redirection_options is not None:
            self.clipboard_redirection_options = clipboard_redirection_options

    @property
    def bypass_in_remote_app_enable(self):
        """Gets the bypass_in_remote_app_enable of this PoliciesFileAndClipboard.

        应用聚合场景下是否双向放通：取值为： false：表示不放通。 true：表示放通。

        :return: The bypass_in_remote_app_enable of this PoliciesFileAndClipboard.
        :rtype: bool
        """
        return self._bypass_in_remote_app_enable

    @bypass_in_remote_app_enable.setter
    def bypass_in_remote_app_enable(self, bypass_in_remote_app_enable):
        """Sets the bypass_in_remote_app_enable of this PoliciesFileAndClipboard.

        应用聚合场景下是否双向放通：取值为： false：表示不放通。 true：表示放通。

        :param bypass_in_remote_app_enable: The bypass_in_remote_app_enable of this PoliciesFileAndClipboard.
        :type bypass_in_remote_app_enable: bool
        """
        self._bypass_in_remote_app_enable = bypass_in_remote_app_enable

    @property
    def file_redirection(self):
        """Gets the file_redirection of this PoliciesFileAndClipboard.

        :return: The file_redirection of this PoliciesFileAndClipboard.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboardFileRedirection`
        """
        return self._file_redirection

    @file_redirection.setter
    def file_redirection(self, file_redirection):
        """Sets the file_redirection of this PoliciesFileAndClipboard.

        :param file_redirection: The file_redirection of this PoliciesFileAndClipboard.
        :type file_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboardFileRedirection`
        """
        self._file_redirection = file_redirection

    @property
    def fd_mobile_client_redir_enable(self):
        """Gets the fd_mobile_client_redir_enable of this PoliciesFileAndClipboard.

        移动客户端文件重定向：取值为： false：表示关闭。 true：表示开启。

        :return: The fd_mobile_client_redir_enable of this PoliciesFileAndClipboard.
        :rtype: bool
        """
        return self._fd_mobile_client_redir_enable

    @fd_mobile_client_redir_enable.setter
    def fd_mobile_client_redir_enable(self, fd_mobile_client_redir_enable):
        """Sets the fd_mobile_client_redir_enable of this PoliciesFileAndClipboard.

        移动客户端文件重定向：取值为： false：表示关闭。 true：表示开启。

        :param fd_mobile_client_redir_enable: The fd_mobile_client_redir_enable of this PoliciesFileAndClipboard.
        :type fd_mobile_client_redir_enable: bool
        """
        self._fd_mobile_client_redir_enable = fd_mobile_client_redir_enable

    @property
    def clipboard_redirection(self):
        """Gets the clipboard_redirection of this PoliciesFileAndClipboard.

        剪切板重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。

        :return: The clipboard_redirection of this PoliciesFileAndClipboard.
        :rtype: str
        """
        return self._clipboard_redirection

    @clipboard_redirection.setter
    def clipboard_redirection(self, clipboard_redirection):
        """Sets the clipboard_redirection of this PoliciesFileAndClipboard.

        剪切板重定向。取值为： DISABLED：表示禁用。（默认） SERVER_TO_CLIENT_ENABLED：表示开启服务端到客户端。 CLIENT_TO_SERVER_ENABLED：表示开启客户端到服务端。 TWO_WAY_ENABLED：表示开启双向。

        :param clipboard_redirection: The clipboard_redirection of this PoliciesFileAndClipboard.
        :type clipboard_redirection: str
        """
        self._clipboard_redirection = clipboard_redirection

    @property
    def clipboard_redirection_options(self):
        """Gets the clipboard_redirection_options of this PoliciesFileAndClipboard.

        :return: The clipboard_redirection_options of this PoliciesFileAndClipboard.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboardClipboardRedirectionOptions`
        """
        return self._clipboard_redirection_options

    @clipboard_redirection_options.setter
    def clipboard_redirection_options(self, clipboard_redirection_options):
        """Sets the clipboard_redirection_options of this PoliciesFileAndClipboard.

        :param clipboard_redirection_options: The clipboard_redirection_options of this PoliciesFileAndClipboard.
        :type clipboard_redirection_options: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboardClipboardRedirectionOptions`
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
