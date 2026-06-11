# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesFolderRedirectionV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'folder_redirection_v2_status': 'int',
        'options': 'FolderRedirectionV2Options'
    }

    attribute_map = {
        'folder_redirection_v2_status': 'folder_redirection_v2_status',
        'options': 'options'
    }

    def __init__(self, folder_redirection_v2_status=None, options=None):
        r"""PoliciesFolderRedirectionV2

        The model defined in huaweicloud sdk

        :param folder_redirection_v2_status: 配置文件夹重定向状态： 0: 关闭 1: 已启用
        :type folder_redirection_v2_status: int
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.FolderRedirectionV2Options`
        """
        
        

        self._folder_redirection_v2_status = None
        self._options = None
        self.discriminator = None

        if folder_redirection_v2_status is not None:
            self.folder_redirection_v2_status = folder_redirection_v2_status
        if options is not None:
            self.options = options

    @property
    def folder_redirection_v2_status(self):
        r"""Gets the folder_redirection_v2_status of this PoliciesFolderRedirectionV2.

        配置文件夹重定向状态： 0: 关闭 1: 已启用

        :return: The folder_redirection_v2_status of this PoliciesFolderRedirectionV2.
        :rtype: int
        """
        return self._folder_redirection_v2_status

    @folder_redirection_v2_status.setter
    def folder_redirection_v2_status(self, folder_redirection_v2_status):
        r"""Sets the folder_redirection_v2_status of this PoliciesFolderRedirectionV2.

        配置文件夹重定向状态： 0: 关闭 1: 已启用

        :param folder_redirection_v2_status: The folder_redirection_v2_status of this PoliciesFolderRedirectionV2.
        :type folder_redirection_v2_status: int
        """
        self._folder_redirection_v2_status = folder_redirection_v2_status

    @property
    def options(self):
        r"""Gets the options of this PoliciesFolderRedirectionV2.

        :return: The options of this PoliciesFolderRedirectionV2.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.FolderRedirectionV2Options`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesFolderRedirectionV2.

        :param options: The options of this PoliciesFolderRedirectionV2.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.FolderRedirectionV2Options`
        """
        self._options = options

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
        if not isinstance(other, PoliciesFolderRedirectionV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
