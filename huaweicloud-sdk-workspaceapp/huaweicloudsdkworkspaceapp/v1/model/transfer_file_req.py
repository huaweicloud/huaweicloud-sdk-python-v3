# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferFileReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transfer_type': 'int',
        'user_name': 'str',
        'file_url': 'str',
        'file_code': 'str',
        'file_acc_code': 'str',
        'target_file_url': 'str',
        'file_system_name': 'str'
    }

    attribute_map = {
        'transfer_type': 'transfer_type',
        'user_name': 'user_name',
        'file_url': 'file_url',
        'file_code': 'file_code',
        'file_acc_code': 'file_acc_code',
        'target_file_url': 'target_file_url',
        'file_system_name': 'file_system_name'
    }

    def __init__(self, transfer_type=None, user_name=None, file_url=None, file_code=None, file_acc_code=None, target_file_url=None, file_system_name=None):
        r"""TransferFileReq

        The model defined in huaweicloud sdk

        :param transfer_type: 操作方式, 0:个人-&gt;共享, 1:共享-&gt;个人。
        :type transfer_type: int
        :param user_name: 分享者或接收者的用户标识。
        :type user_name: str
        :param file_url: 待流转文件url。
        :type file_url: str
        :param file_code: 文件编码(仅接收文件使用，从分享返回体获取)。
        :type file_code: str
        :param file_acc_code: 文件提取码(仅接收文件使用，从分享返回体获取)。
        :type file_acc_code: str
        :param target_file_url: 目标文件url。
        :type target_file_url: str
        :param file_system_name: 文件系统名称。
        :type file_system_name: str
        """
        
        

        self._transfer_type = None
        self._user_name = None
        self._file_url = None
        self._file_code = None
        self._file_acc_code = None
        self._target_file_url = None
        self._file_system_name = None
        self.discriminator = None

        self.transfer_type = transfer_type
        self.user_name = user_name
        self.file_url = file_url
        if file_code is not None:
            self.file_code = file_code
        if file_acc_code is not None:
            self.file_acc_code = file_acc_code
        if target_file_url is not None:
            self.target_file_url = target_file_url
        if file_system_name is not None:
            self.file_system_name = file_system_name

    @property
    def transfer_type(self):
        r"""Gets the transfer_type of this TransferFileReq.

        操作方式, 0:个人->共享, 1:共享->个人。

        :return: The transfer_type of this TransferFileReq.
        :rtype: int
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        r"""Sets the transfer_type of this TransferFileReq.

        操作方式, 0:个人->共享, 1:共享->个人。

        :param transfer_type: The transfer_type of this TransferFileReq.
        :type transfer_type: int
        """
        self._transfer_type = transfer_type

    @property
    def user_name(self):
        r"""Gets the user_name of this TransferFileReq.

        分享者或接收者的用户标识。

        :return: The user_name of this TransferFileReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this TransferFileReq.

        分享者或接收者的用户标识。

        :param user_name: The user_name of this TransferFileReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def file_url(self):
        r"""Gets the file_url of this TransferFileReq.

        待流转文件url。

        :return: The file_url of this TransferFileReq.
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        r"""Sets the file_url of this TransferFileReq.

        待流转文件url。

        :param file_url: The file_url of this TransferFileReq.
        :type file_url: str
        """
        self._file_url = file_url

    @property
    def file_code(self):
        r"""Gets the file_code of this TransferFileReq.

        文件编码(仅接收文件使用，从分享返回体获取)。

        :return: The file_code of this TransferFileReq.
        :rtype: str
        """
        return self._file_code

    @file_code.setter
    def file_code(self, file_code):
        r"""Sets the file_code of this TransferFileReq.

        文件编码(仅接收文件使用，从分享返回体获取)。

        :param file_code: The file_code of this TransferFileReq.
        :type file_code: str
        """
        self._file_code = file_code

    @property
    def file_acc_code(self):
        r"""Gets the file_acc_code of this TransferFileReq.

        文件提取码(仅接收文件使用，从分享返回体获取)。

        :return: The file_acc_code of this TransferFileReq.
        :rtype: str
        """
        return self._file_acc_code

    @file_acc_code.setter
    def file_acc_code(self, file_acc_code):
        r"""Sets the file_acc_code of this TransferFileReq.

        文件提取码(仅接收文件使用，从分享返回体获取)。

        :param file_acc_code: The file_acc_code of this TransferFileReq.
        :type file_acc_code: str
        """
        self._file_acc_code = file_acc_code

    @property
    def target_file_url(self):
        r"""Gets the target_file_url of this TransferFileReq.

        目标文件url。

        :return: The target_file_url of this TransferFileReq.
        :rtype: str
        """
        return self._target_file_url

    @target_file_url.setter
    def target_file_url(self, target_file_url):
        r"""Sets the target_file_url of this TransferFileReq.

        目标文件url。

        :param target_file_url: The target_file_url of this TransferFileReq.
        :type target_file_url: str
        """
        self._target_file_url = target_file_url

    @property
    def file_system_name(self):
        r"""Gets the file_system_name of this TransferFileReq.

        文件系统名称。

        :return: The file_system_name of this TransferFileReq.
        :rtype: str
        """
        return self._file_system_name

    @file_system_name.setter
    def file_system_name(self, file_system_name):
        r"""Sets the file_system_name of this TransferFileReq.

        文件系统名称。

        :param file_system_name: The file_system_name of this TransferFileReq.
        :type file_system_name: str
        """
        self._file_system_name = file_system_name

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
        if not isinstance(other, TransferFileReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
