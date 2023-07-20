# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportImportFileResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_size': 'str',
        'previous_select': 'str'
    }

    attribute_map = {
        'file_size': 'file_size',
        'previous_select': 'previous_select'
    }

    def __init__(self, file_size=None, previous_select=None):
        """SupportImportFileResult

        The model defined in huaweicloud sdk

        :param file_size: 文件导入阈值。
        :type file_size: str
        :param previous_select: 上一次选择对象的方式。
        :type previous_select: str
        """
        
        

        self._file_size = None
        self._previous_select = None
        self.discriminator = None

        if file_size is not None:
            self.file_size = file_size
        if previous_select is not None:
            self.previous_select = previous_select

    @property
    def file_size(self):
        """Gets the file_size of this SupportImportFileResult.

        文件导入阈值。

        :return: The file_size of this SupportImportFileResult.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this SupportImportFileResult.

        文件导入阈值。

        :param file_size: The file_size of this SupportImportFileResult.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def previous_select(self):
        """Gets the previous_select of this SupportImportFileResult.

        上一次选择对象的方式。

        :return: The previous_select of this SupportImportFileResult.
        :rtype: str
        """
        return self._previous_select

    @previous_select.setter
    def previous_select(self, previous_select):
        """Sets the previous_select of this SupportImportFileResult.

        上一次选择对象的方式。

        :param previous_select: The previous_select of this SupportImportFileResult.
        :type previous_select: str
        """
        self._previous_select = previous_select

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
        if not isinstance(other, SupportImportFileResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
