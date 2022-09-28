# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDatabaseDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'files': 'list[str]',
        'delimiter': 'str',
        'skip_lines': 'int'
    }

    attribute_map = {
        'files': 'files',
        'delimiter': 'delimiter',
        'skip_lines': 'skip_lines'
    }

    def __init__(self, files=None, delimiter=None, skip_lines=None):
        """ImportDatabaseDataReq

        The model defined in huaweicloud sdk

        :param files: 导入文件l路径列表
        :type files: list[str]
        :param delimiter: 分隔符，常见分隔符为, ;
        :type delimiter: str
        :param skip_lines: 跳过的header行数
        :type skip_lines: int
        """
        
        

        self._files = None
        self._delimiter = None
        self._skip_lines = None
        self.discriminator = None

        self.files = files
        self.delimiter = delimiter
        self.skip_lines = skip_lines

    @property
    def files(self):
        """Gets the files of this ImportDatabaseDataReq.

        导入文件l路径列表

        :return: The files of this ImportDatabaseDataReq.
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ImportDatabaseDataReq.

        导入文件l路径列表

        :param files: The files of this ImportDatabaseDataReq.
        :type files: list[str]
        """
        self._files = files

    @property
    def delimiter(self):
        """Gets the delimiter of this ImportDatabaseDataReq.

        分隔符，常见分隔符为, ;

        :return: The delimiter of this ImportDatabaseDataReq.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this ImportDatabaseDataReq.

        分隔符，常见分隔符为, ;

        :param delimiter: The delimiter of this ImportDatabaseDataReq.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def skip_lines(self):
        """Gets the skip_lines of this ImportDatabaseDataReq.

        跳过的header行数

        :return: The skip_lines of this ImportDatabaseDataReq.
        :rtype: int
        """
        return self._skip_lines

    @skip_lines.setter
    def skip_lines(self, skip_lines):
        """Sets the skip_lines of this ImportDatabaseDataReq.

        跳过的header行数

        :param skip_lines: The skip_lines of this ImportDatabaseDataReq.
        :type skip_lines: int
        """
        self._skip_lines = skip_lines

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
        if not isinstance(other, ImportDatabaseDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
