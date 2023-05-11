# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportFunctionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'func_name': 'str',
        'file_name': 'str',
        'file_type': 'str',
        'file_code': 'str',
        'package': 'str'
    }

    attribute_map = {
        'func_name': 'func_name',
        'file_name': 'file_name',
        'file_type': 'file_type',
        'file_code': 'file_code',
        'package': 'package'
    }

    def __init__(self, func_name=None, file_name=None, file_type=None, file_code=None, package=None):
        """ImportFunctionRequestBody

        The model defined in huaweicloud sdk

        :param func_name: 函数名
        :type func_name: str
        :param file_name: 文件名
        :type file_name: str
        :param file_type: 文件类型
        :type file_type: str
        :param file_code: 函数代码。代码必须要进行base64编码
        :type file_code: str
        :param package: 应用名称，默认为default
        :type package: str
        """
        
        

        self._func_name = None
        self._file_name = None
        self._file_type = None
        self._file_code = None
        self._package = None
        self.discriminator = None

        self.func_name = func_name
        self.file_name = file_name
        self.file_type = file_type
        self.file_code = file_code
        if package is not None:
            self.package = package

    @property
    def func_name(self):
        """Gets the func_name of this ImportFunctionRequestBody.

        函数名

        :return: The func_name of this ImportFunctionRequestBody.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        """Sets the func_name of this ImportFunctionRequestBody.

        函数名

        :param func_name: The func_name of this ImportFunctionRequestBody.
        :type func_name: str
        """
        self._func_name = func_name

    @property
    def file_name(self):
        """Gets the file_name of this ImportFunctionRequestBody.

        文件名

        :return: The file_name of this ImportFunctionRequestBody.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ImportFunctionRequestBody.

        文件名

        :param file_name: The file_name of this ImportFunctionRequestBody.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        """Gets the file_type of this ImportFunctionRequestBody.

        文件类型

        :return: The file_type of this ImportFunctionRequestBody.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ImportFunctionRequestBody.

        文件类型

        :param file_type: The file_type of this ImportFunctionRequestBody.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def file_code(self):
        """Gets the file_code of this ImportFunctionRequestBody.

        函数代码。代码必须要进行base64编码

        :return: The file_code of this ImportFunctionRequestBody.
        :rtype: str
        """
        return self._file_code

    @file_code.setter
    def file_code(self, file_code):
        """Sets the file_code of this ImportFunctionRequestBody.

        函数代码。代码必须要进行base64编码

        :param file_code: The file_code of this ImportFunctionRequestBody.
        :type file_code: str
        """
        self._file_code = file_code

    @property
    def package(self):
        """Gets the package of this ImportFunctionRequestBody.

        应用名称，默认为default

        :return: The package of this ImportFunctionRequestBody.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this ImportFunctionRequestBody.

        应用名称，默认为default

        :param package: The package of this ImportFunctionRequestBody.
        :type package: str
        """
        self._package = package

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
        if not isinstance(other, ImportFunctionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
