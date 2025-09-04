# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferFilePreReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'file_name': 'str',
        'file_code': 'str',
        'file_acc_code': 'str',
        'file_system_name': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'file_name': 'file_name',
        'file_code': 'file_code',
        'file_acc_code': 'file_acc_code',
        'file_system_name': 'file_system_name'
    }

    def __init__(self, user_name=None, file_name=None, file_code=None, file_acc_code=None, file_system_name=None):
        r"""TransferFilePreReq

        The model defined in huaweicloud sdk

        :param user_name: 分享者或接收者的用户标识。
        :type user_name: str
        :param file_name: 待流转的文件名称，不包含完整路径。
        :type file_name: str
        :param file_code: 文件编码。
        :type file_code: str
        :param file_acc_code: 文件提取码。
        :type file_acc_code: str
        :param file_system_name: 文件系统名称。
        :type file_system_name: str
        """
        
        

        self._user_name = None
        self._file_name = None
        self._file_code = None
        self._file_acc_code = None
        self._file_system_name = None
        self.discriminator = None

        self.user_name = user_name
        self.file_name = file_name
        self.file_code = file_code
        self.file_acc_code = file_acc_code
        if file_system_name is not None:
            self.file_system_name = file_system_name

    @property
    def user_name(self):
        r"""Gets the user_name of this TransferFilePreReq.

        分享者或接收者的用户标识。

        :return: The user_name of this TransferFilePreReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this TransferFilePreReq.

        分享者或接收者的用户标识。

        :param user_name: The user_name of this TransferFilePreReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def file_name(self):
        r"""Gets the file_name of this TransferFilePreReq.

        待流转的文件名称，不包含完整路径。

        :return: The file_name of this TransferFilePreReq.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this TransferFilePreReq.

        待流转的文件名称，不包含完整路径。

        :param file_name: The file_name of this TransferFilePreReq.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_code(self):
        r"""Gets the file_code of this TransferFilePreReq.

        文件编码。

        :return: The file_code of this TransferFilePreReq.
        :rtype: str
        """
        return self._file_code

    @file_code.setter
    def file_code(self, file_code):
        r"""Sets the file_code of this TransferFilePreReq.

        文件编码。

        :param file_code: The file_code of this TransferFilePreReq.
        :type file_code: str
        """
        self._file_code = file_code

    @property
    def file_acc_code(self):
        r"""Gets the file_acc_code of this TransferFilePreReq.

        文件提取码。

        :return: The file_acc_code of this TransferFilePreReq.
        :rtype: str
        """
        return self._file_acc_code

    @file_acc_code.setter
    def file_acc_code(self, file_acc_code):
        r"""Sets the file_acc_code of this TransferFilePreReq.

        文件提取码。

        :param file_acc_code: The file_acc_code of this TransferFilePreReq.
        :type file_acc_code: str
        """
        self._file_acc_code = file_acc_code

    @property
    def file_system_name(self):
        r"""Gets the file_system_name of this TransferFilePreReq.

        文件系统名称。

        :return: The file_system_name of this TransferFilePreReq.
        :rtype: str
        """
        return self._file_system_name

    @file_system_name.setter
    def file_system_name(self, file_system_name):
        r"""Sets the file_system_name of this TransferFilePreReq.

        文件系统名称。

        :param file_system_name: The file_system_name of this TransferFilePreReq.
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
        if not isinstance(other, TransferFilePreReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
