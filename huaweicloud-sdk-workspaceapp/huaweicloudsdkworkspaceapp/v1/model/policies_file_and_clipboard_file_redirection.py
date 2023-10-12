# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesFileAndClipboardFileRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'redirection_mode': 'str',
        'options': 'FileRedirectionOptions',
        'vm_send_file_client': 'bool',
        'redirection_send_file_options': 'PoliciesFileAndClipboardFileRedirectionRedirectionSendFileOptions'
    }

    attribute_map = {
        'redirection_mode': 'redirection_mode',
        'options': 'options',
        'vm_send_file_client': 'vm_send_file_client',
        'redirection_send_file_options': 'redirection_send_file_options'
    }

    def __init__(self, redirection_mode=None, options=None, vm_send_file_client=None, redirection_send_file_options=None):
        """PoliciesFileAndClipboardFileRedirection

        The model defined in huaweicloud sdk

        :param redirection_mode: 文件重定向。取值为： DISABLED：表示禁用。（默认） READ_ONLY：表示只读。 READ_AND_WRITE：表示读写。
        :type redirection_mode: str
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptions`
        :param vm_send_file_client: 是否开启发送文件（虚机到客户端）。取值为： false：表示关闭。 true：表示开启。
        :type vm_send_file_client: bool
        :param redirection_send_file_options: 
        :type redirection_send_file_options: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboardFileRedirectionRedirectionSendFileOptions`
        """
        
        

        self._redirection_mode = None
        self._options = None
        self._vm_send_file_client = None
        self._redirection_send_file_options = None
        self.discriminator = None

        if redirection_mode is not None:
            self.redirection_mode = redirection_mode
        if options is not None:
            self.options = options
        if vm_send_file_client is not None:
            self.vm_send_file_client = vm_send_file_client
        if redirection_send_file_options is not None:
            self.redirection_send_file_options = redirection_send_file_options

    @property
    def redirection_mode(self):
        """Gets the redirection_mode of this PoliciesFileAndClipboardFileRedirection.

        文件重定向。取值为： DISABLED：表示禁用。（默认） READ_ONLY：表示只读。 READ_AND_WRITE：表示读写。

        :return: The redirection_mode of this PoliciesFileAndClipboardFileRedirection.
        :rtype: str
        """
        return self._redirection_mode

    @redirection_mode.setter
    def redirection_mode(self, redirection_mode):
        """Sets the redirection_mode of this PoliciesFileAndClipboardFileRedirection.

        文件重定向。取值为： DISABLED：表示禁用。（默认） READ_ONLY：表示只读。 READ_AND_WRITE：表示读写。

        :param redirection_mode: The redirection_mode of this PoliciesFileAndClipboardFileRedirection.
        :type redirection_mode: str
        """
        self._redirection_mode = redirection_mode

    @property
    def options(self):
        """Gets the options of this PoliciesFileAndClipboardFileRedirection.

        :return: The options of this PoliciesFileAndClipboardFileRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PoliciesFileAndClipboardFileRedirection.

        :param options: The options of this PoliciesFileAndClipboardFileRedirection.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptions`
        """
        self._options = options

    @property
    def vm_send_file_client(self):
        """Gets the vm_send_file_client of this PoliciesFileAndClipboardFileRedirection.

        是否开启发送文件（虚机到客户端）。取值为： false：表示关闭。 true：表示开启。

        :return: The vm_send_file_client of this PoliciesFileAndClipboardFileRedirection.
        :rtype: bool
        """
        return self._vm_send_file_client

    @vm_send_file_client.setter
    def vm_send_file_client(self, vm_send_file_client):
        """Sets the vm_send_file_client of this PoliciesFileAndClipboardFileRedirection.

        是否开启发送文件（虚机到客户端）。取值为： false：表示关闭。 true：表示开启。

        :param vm_send_file_client: The vm_send_file_client of this PoliciesFileAndClipboardFileRedirection.
        :type vm_send_file_client: bool
        """
        self._vm_send_file_client = vm_send_file_client

    @property
    def redirection_send_file_options(self):
        """Gets the redirection_send_file_options of this PoliciesFileAndClipboardFileRedirection.

        :return: The redirection_send_file_options of this PoliciesFileAndClipboardFileRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboardFileRedirectionRedirectionSendFileOptions`
        """
        return self._redirection_send_file_options

    @redirection_send_file_options.setter
    def redirection_send_file_options(self, redirection_send_file_options):
        """Sets the redirection_send_file_options of this PoliciesFileAndClipboardFileRedirection.

        :param redirection_send_file_options: The redirection_send_file_options of this PoliciesFileAndClipboardFileRedirection.
        :type redirection_send_file_options: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesFileAndClipboardFileRedirectionRedirectionSendFileOptions`
        """
        self._redirection_send_file_options = redirection_send_file_options

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
        if not isinstance(other, PoliciesFileAndClipboardFileRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
