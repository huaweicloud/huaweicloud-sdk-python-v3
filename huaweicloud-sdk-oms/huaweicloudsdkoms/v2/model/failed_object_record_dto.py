# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedObjectRecordDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'bool',
        'list_file_key': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'result': 'result',
        'list_file_key': 'list_file_key',
        'error_code': 'error_code'
    }

    def __init__(self, result=None, list_file_key=None, error_code=None):
        r"""FailedObjectRecordDto

        The model defined in huaweicloud sdk

        :param result: 是否支持失败对象重传。
        :type result: bool
        :param list_file_key: 失败对象列表文件路径。
        :type list_file_key: str
        :param error_code: 失败对象列表上传失败的错误码。
        :type error_code: str
        """
        
        

        self._result = None
        self._list_file_key = None
        self._error_code = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if list_file_key is not None:
            self.list_file_key = list_file_key
        if error_code is not None:
            self.error_code = error_code

    @property
    def result(self):
        r"""Gets the result of this FailedObjectRecordDto.

        是否支持失败对象重传。

        :return: The result of this FailedObjectRecordDto.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this FailedObjectRecordDto.

        是否支持失败对象重传。

        :param result: The result of this FailedObjectRecordDto.
        :type result: bool
        """
        self._result = result

    @property
    def list_file_key(self):
        r"""Gets the list_file_key of this FailedObjectRecordDto.

        失败对象列表文件路径。

        :return: The list_file_key of this FailedObjectRecordDto.
        :rtype: str
        """
        return self._list_file_key

    @list_file_key.setter
    def list_file_key(self, list_file_key):
        r"""Sets the list_file_key of this FailedObjectRecordDto.

        失败对象列表文件路径。

        :param list_file_key: The list_file_key of this FailedObjectRecordDto.
        :type list_file_key: str
        """
        self._list_file_key = list_file_key

    @property
    def error_code(self):
        r"""Gets the error_code of this FailedObjectRecordDto.

        失败对象列表上传失败的错误码。

        :return: The error_code of this FailedObjectRecordDto.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this FailedObjectRecordDto.

        失败对象列表上传失败的错误码。

        :param error_code: The error_code of this FailedObjectRecordDto.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, FailedObjectRecordDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
