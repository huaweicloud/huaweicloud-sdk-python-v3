# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Counter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bytes_written': 'int',
        'total_files': 'int',
        'rows_read': 'int',
        'bytes_read': 'int',
        'rows_written': 'int',
        'files_written': 'int',
        'files_read': 'int',
        'total_size': 'int',
        'files_skipped': 'int',
        'rows_written_skipped': 'int'
    }

    attribute_map = {
        'bytes_written': 'BYTES_WRITTEN',
        'total_files': 'TOTAL_FILES',
        'rows_read': 'ROWS_READ',
        'bytes_read': 'BYTES_READ',
        'rows_written': 'ROWS_WRITTEN',
        'files_written': 'FILES_WRITTEN',
        'files_read': 'FILES_READ',
        'total_size': 'TOTAL_SIZE',
        'files_skipped': 'FILES_SKIPPED',
        'rows_written_skipped': 'ROWS_WRITTEN_SKIPPED'
    }

    def __init__(self, bytes_written=None, total_files=None, rows_read=None, bytes_read=None, rows_written=None, files_written=None, files_read=None, total_size=None, files_skipped=None, rows_written_skipped=None):
        """Counter

        The model defined in huaweicloud sdk

        :param bytes_written: 写入的字节数
        :type bytes_written: int
        :param total_files: 总文件数
        :type total_files: int
        :param rows_read: 读取的行数
        :type rows_read: int
        :param bytes_read: 读取的字节数
        :type bytes_read: int
        :param rows_written: 写入的行数
        :type rows_written: int
        :param files_written: 写入的文件数
        :type files_written: int
        :param files_read: 读取的文件数
        :type files_read: int
        :param total_size: 总字节数
        :type total_size: int
        :param files_skipped: 跳过的文件数
        :type files_skipped: int
        :param rows_written_skipped: 跳过的行数
        :type rows_written_skipped: int
        """
        
        

        self._bytes_written = None
        self._total_files = None
        self._rows_read = None
        self._bytes_read = None
        self._rows_written = None
        self._files_written = None
        self._files_read = None
        self._total_size = None
        self._files_skipped = None
        self._rows_written_skipped = None
        self.discriminator = None

        if bytes_written is not None:
            self.bytes_written = bytes_written
        if total_files is not None:
            self.total_files = total_files
        if rows_read is not None:
            self.rows_read = rows_read
        if bytes_read is not None:
            self.bytes_read = bytes_read
        if rows_written is not None:
            self.rows_written = rows_written
        if files_written is not None:
            self.files_written = files_written
        if files_read is not None:
            self.files_read = files_read
        if total_size is not None:
            self.total_size = total_size
        if files_skipped is not None:
            self.files_skipped = files_skipped
        if rows_written_skipped is not None:
            self.rows_written_skipped = rows_written_skipped

    @property
    def bytes_written(self):
        """Gets the bytes_written of this Counter.

        写入的字节数

        :return: The bytes_written of this Counter.
        :rtype: int
        """
        return self._bytes_written

    @bytes_written.setter
    def bytes_written(self, bytes_written):
        """Sets the bytes_written of this Counter.

        写入的字节数

        :param bytes_written: The bytes_written of this Counter.
        :type bytes_written: int
        """
        self._bytes_written = bytes_written

    @property
    def total_files(self):
        """Gets the total_files of this Counter.

        总文件数

        :return: The total_files of this Counter.
        :rtype: int
        """
        return self._total_files

    @total_files.setter
    def total_files(self, total_files):
        """Sets the total_files of this Counter.

        总文件数

        :param total_files: The total_files of this Counter.
        :type total_files: int
        """
        self._total_files = total_files

    @property
    def rows_read(self):
        """Gets the rows_read of this Counter.

        读取的行数

        :return: The rows_read of this Counter.
        :rtype: int
        """
        return self._rows_read

    @rows_read.setter
    def rows_read(self, rows_read):
        """Sets the rows_read of this Counter.

        读取的行数

        :param rows_read: The rows_read of this Counter.
        :type rows_read: int
        """
        self._rows_read = rows_read

    @property
    def bytes_read(self):
        """Gets the bytes_read of this Counter.

        读取的字节数

        :return: The bytes_read of this Counter.
        :rtype: int
        """
        return self._bytes_read

    @bytes_read.setter
    def bytes_read(self, bytes_read):
        """Sets the bytes_read of this Counter.

        读取的字节数

        :param bytes_read: The bytes_read of this Counter.
        :type bytes_read: int
        """
        self._bytes_read = bytes_read

    @property
    def rows_written(self):
        """Gets the rows_written of this Counter.

        写入的行数

        :return: The rows_written of this Counter.
        :rtype: int
        """
        return self._rows_written

    @rows_written.setter
    def rows_written(self, rows_written):
        """Sets the rows_written of this Counter.

        写入的行数

        :param rows_written: The rows_written of this Counter.
        :type rows_written: int
        """
        self._rows_written = rows_written

    @property
    def files_written(self):
        """Gets the files_written of this Counter.

        写入的文件数

        :return: The files_written of this Counter.
        :rtype: int
        """
        return self._files_written

    @files_written.setter
    def files_written(self, files_written):
        """Sets the files_written of this Counter.

        写入的文件数

        :param files_written: The files_written of this Counter.
        :type files_written: int
        """
        self._files_written = files_written

    @property
    def files_read(self):
        """Gets the files_read of this Counter.

        读取的文件数

        :return: The files_read of this Counter.
        :rtype: int
        """
        return self._files_read

    @files_read.setter
    def files_read(self, files_read):
        """Sets the files_read of this Counter.

        读取的文件数

        :param files_read: The files_read of this Counter.
        :type files_read: int
        """
        self._files_read = files_read

    @property
    def total_size(self):
        """Gets the total_size of this Counter.

        总字节数

        :return: The total_size of this Counter.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this Counter.

        总字节数

        :param total_size: The total_size of this Counter.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def files_skipped(self):
        """Gets the files_skipped of this Counter.

        跳过的文件数

        :return: The files_skipped of this Counter.
        :rtype: int
        """
        return self._files_skipped

    @files_skipped.setter
    def files_skipped(self, files_skipped):
        """Sets the files_skipped of this Counter.

        跳过的文件数

        :param files_skipped: The files_skipped of this Counter.
        :type files_skipped: int
        """
        self._files_skipped = files_skipped

    @property
    def rows_written_skipped(self):
        """Gets the rows_written_skipped of this Counter.

        跳过的行数

        :return: The rows_written_skipped of this Counter.
        :rtype: int
        """
        return self._rows_written_skipped

    @rows_written_skipped.setter
    def rows_written_skipped(self, rows_written_skipped):
        """Sets the rows_written_skipped of this Counter.

        跳过的行数

        :param rows_written_skipped: The rows_written_skipped of this Counter.
        :type rows_written_skipped: int
        """
        self._rows_written_skipped = rows_written_skipped

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
        if not isinstance(other, Counter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
