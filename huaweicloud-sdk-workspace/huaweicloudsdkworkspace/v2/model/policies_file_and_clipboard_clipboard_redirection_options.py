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
        'clipboard_file_redirection_enable': 'bool'
    }

    attribute_map = {
        'rich_text_redirection_enable': 'rich_text_redirection_enable',
        'clipboard_file_redirection_enable': 'clipboard_file_redirection_enable'
    }

    def __init__(self, rich_text_redirection_enable=None, clipboard_file_redirection_enable=None):
        r"""PoliciesFileAndClipboardClipboardRedirectionOptions

        The model defined in huaweicloud sdk

        :param rich_text_redirection_enable: 是否开启剪切板富文本重定向。取值为： false：表示关闭。 true：表示开启。
        :type rich_text_redirection_enable: bool
        :param clipboard_file_redirection_enable: 是否开启剪切板文件重定向。取值为： false：表示关闭。 true：表示开启。
        :type clipboard_file_redirection_enable: bool
        """
        
        

        self._rich_text_redirection_enable = None
        self._clipboard_file_redirection_enable = None
        self.discriminator = None

        if rich_text_redirection_enable is not None:
            self.rich_text_redirection_enable = rich_text_redirection_enable
        if clipboard_file_redirection_enable is not None:
            self.clipboard_file_redirection_enable = clipboard_file_redirection_enable

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
