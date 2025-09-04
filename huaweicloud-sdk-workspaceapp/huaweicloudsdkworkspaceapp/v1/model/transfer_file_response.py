# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_url': 'str',
        'file_code': 'str',
        'file_acc_code': 'str',
        'file_system_name': 'str',
        'folder_name': 'str'
    }

    attribute_map = {
        'file_url': 'file_url',
        'file_code': 'file_code',
        'file_acc_code': 'file_acc_code',
        'file_system_name': 'file_system_name',
        'folder_name': 'folder_name'
    }

    def __init__(self, file_url=None, file_code=None, file_acc_code=None, file_system_name=None, folder_name=None):
        r"""TransferFileResponse

        The model defined in huaweicloud sdk

        :param file_url: 待流转文件url。
        :type file_url: str
        :param file_code: 文件编码。
        :type file_code: str
        :param file_acc_code: 文件提取码。
        :type file_acc_code: str
        :param file_system_name: 文件系统名称。
        :type file_system_name: str
        :param folder_name: 文件夹名称。
        :type folder_name: str
        """
        
        super(TransferFileResponse, self).__init__()

        self._file_url = None
        self._file_code = None
        self._file_acc_code = None
        self._file_system_name = None
        self._folder_name = None
        self.discriminator = None

        if file_url is not None:
            self.file_url = file_url
        if file_code is not None:
            self.file_code = file_code
        if file_acc_code is not None:
            self.file_acc_code = file_acc_code
        if file_system_name is not None:
            self.file_system_name = file_system_name
        if folder_name is not None:
            self.folder_name = folder_name

    @property
    def file_url(self):
        r"""Gets the file_url of this TransferFileResponse.

        待流转文件url。

        :return: The file_url of this TransferFileResponse.
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        r"""Sets the file_url of this TransferFileResponse.

        待流转文件url。

        :param file_url: The file_url of this TransferFileResponse.
        :type file_url: str
        """
        self._file_url = file_url

    @property
    def file_code(self):
        r"""Gets the file_code of this TransferFileResponse.

        文件编码。

        :return: The file_code of this TransferFileResponse.
        :rtype: str
        """
        return self._file_code

    @file_code.setter
    def file_code(self, file_code):
        r"""Sets the file_code of this TransferFileResponse.

        文件编码。

        :param file_code: The file_code of this TransferFileResponse.
        :type file_code: str
        """
        self._file_code = file_code

    @property
    def file_acc_code(self):
        r"""Gets the file_acc_code of this TransferFileResponse.

        文件提取码。

        :return: The file_acc_code of this TransferFileResponse.
        :rtype: str
        """
        return self._file_acc_code

    @file_acc_code.setter
    def file_acc_code(self, file_acc_code):
        r"""Sets the file_acc_code of this TransferFileResponse.

        文件提取码。

        :param file_acc_code: The file_acc_code of this TransferFileResponse.
        :type file_acc_code: str
        """
        self._file_acc_code = file_acc_code

    @property
    def file_system_name(self):
        r"""Gets the file_system_name of this TransferFileResponse.

        文件系统名称。

        :return: The file_system_name of this TransferFileResponse.
        :rtype: str
        """
        return self._file_system_name

    @file_system_name.setter
    def file_system_name(self, file_system_name):
        r"""Sets the file_system_name of this TransferFileResponse.

        文件系统名称。

        :param file_system_name: The file_system_name of this TransferFileResponse.
        :type file_system_name: str
        """
        self._file_system_name = file_system_name

    @property
    def folder_name(self):
        r"""Gets the folder_name of this TransferFileResponse.

        文件夹名称。

        :return: The folder_name of this TransferFileResponse.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        r"""Sets the folder_name of this TransferFileResponse.

        文件夹名称。

        :param folder_name: The folder_name of this TransferFileResponse.
        :type folder_name: str
        """
        self._folder_name = folder_name

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
        if not isinstance(other, TransferFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
