# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportGraphReqPaginate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'row_count_per_file': 'int',
        'num_thread': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'row_count_per_file': 'row_count_per_file',
        'num_thread': 'num_thread'
    }

    def __init__(self, enable=None, row_count_per_file=None, num_thread=None):
        r"""ExportGraphReqPaginate

        The model defined in huaweicloud sdk

        :param enable: 是否开启分页，默认为true，不需要开启分页时，需显示声明为false。
        :type enable: bool
        :param row_count_per_file: 按页导出时，每个文件最大行数，默认10000000。
        :type row_count_per_file: int
        :param num_thread: 按页导出时，并行线程数，默认为8。
        :type num_thread: int
        """
        
        

        self._enable = None
        self._row_count_per_file = None
        self._num_thread = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if row_count_per_file is not None:
            self.row_count_per_file = row_count_per_file
        if num_thread is not None:
            self.num_thread = num_thread

    @property
    def enable(self):
        r"""Gets the enable of this ExportGraphReqPaginate.

        是否开启分页，默认为true，不需要开启分页时，需显示声明为false。

        :return: The enable of this ExportGraphReqPaginate.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ExportGraphReqPaginate.

        是否开启分页，默认为true，不需要开启分页时，需显示声明为false。

        :param enable: The enable of this ExportGraphReqPaginate.
        :type enable: bool
        """
        self._enable = enable

    @property
    def row_count_per_file(self):
        r"""Gets the row_count_per_file of this ExportGraphReqPaginate.

        按页导出时，每个文件最大行数，默认10000000。

        :return: The row_count_per_file of this ExportGraphReqPaginate.
        :rtype: int
        """
        return self._row_count_per_file

    @row_count_per_file.setter
    def row_count_per_file(self, row_count_per_file):
        r"""Sets the row_count_per_file of this ExportGraphReqPaginate.

        按页导出时，每个文件最大行数，默认10000000。

        :param row_count_per_file: The row_count_per_file of this ExportGraphReqPaginate.
        :type row_count_per_file: int
        """
        self._row_count_per_file = row_count_per_file

    @property
    def num_thread(self):
        r"""Gets the num_thread of this ExportGraphReqPaginate.

        按页导出时，并行线程数，默认为8。

        :return: The num_thread of this ExportGraphReqPaginate.
        :rtype: int
        """
        return self._num_thread

    @num_thread.setter
    def num_thread(self, num_thread):
        r"""Sets the num_thread of this ExportGraphReqPaginate.

        按页导出时，并行线程数，默认为8。

        :param num_thread: The num_thread of this ExportGraphReqPaginate.
        :type num_thread: int
        """
        self._num_thread = num_thread

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
        if not isinstance(other, ExportGraphReqPaginate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
