# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsistencyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dir_check': 'str',
        'num_total_files': 'int',
        'num_different_files': 'int',
        'num_target_miss_files': 'int',
        'num_target_more_files': 'int'
    }

    attribute_map = {
        'dir_check': 'dir_check',
        'num_total_files': 'num_total_files',
        'num_different_files': 'num_different_files',
        'num_target_miss_files': 'num_target_miss_files',
        'num_target_more_files': 'num_target_more_files'
    }

    def __init__(self, dir_check=None, num_total_files=None, num_different_files=None, num_target_miss_files=None, num_target_more_files=None):
        r"""ConsistencyResult

        The model defined in huaweicloud sdk

        :param dir_check: 校验目录
        :type dir_check: str
        :param num_total_files: 文件总数
        :type num_total_files: int
        :param num_different_files: 差异文件数量
        :type num_different_files: int
        :param num_target_miss_files: 目的端缺少文件数量
        :type num_target_miss_files: int
        :param num_target_more_files: 目的端多余文件数量
        :type num_target_more_files: int
        """
        
        

        self._dir_check = None
        self._num_total_files = None
        self._num_different_files = None
        self._num_target_miss_files = None
        self._num_target_more_files = None
        self.discriminator = None

        self.dir_check = dir_check
        self.num_total_files = num_total_files
        self.num_different_files = num_different_files
        self.num_target_miss_files = num_target_miss_files
        self.num_target_more_files = num_target_more_files

    @property
    def dir_check(self):
        r"""Gets the dir_check of this ConsistencyResult.

        校验目录

        :return: The dir_check of this ConsistencyResult.
        :rtype: str
        """
        return self._dir_check

    @dir_check.setter
    def dir_check(self, dir_check):
        r"""Sets the dir_check of this ConsistencyResult.

        校验目录

        :param dir_check: The dir_check of this ConsistencyResult.
        :type dir_check: str
        """
        self._dir_check = dir_check

    @property
    def num_total_files(self):
        r"""Gets the num_total_files of this ConsistencyResult.

        文件总数

        :return: The num_total_files of this ConsistencyResult.
        :rtype: int
        """
        return self._num_total_files

    @num_total_files.setter
    def num_total_files(self, num_total_files):
        r"""Sets the num_total_files of this ConsistencyResult.

        文件总数

        :param num_total_files: The num_total_files of this ConsistencyResult.
        :type num_total_files: int
        """
        self._num_total_files = num_total_files

    @property
    def num_different_files(self):
        r"""Gets the num_different_files of this ConsistencyResult.

        差异文件数量

        :return: The num_different_files of this ConsistencyResult.
        :rtype: int
        """
        return self._num_different_files

    @num_different_files.setter
    def num_different_files(self, num_different_files):
        r"""Sets the num_different_files of this ConsistencyResult.

        差异文件数量

        :param num_different_files: The num_different_files of this ConsistencyResult.
        :type num_different_files: int
        """
        self._num_different_files = num_different_files

    @property
    def num_target_miss_files(self):
        r"""Gets the num_target_miss_files of this ConsistencyResult.

        目的端缺少文件数量

        :return: The num_target_miss_files of this ConsistencyResult.
        :rtype: int
        """
        return self._num_target_miss_files

    @num_target_miss_files.setter
    def num_target_miss_files(self, num_target_miss_files):
        r"""Sets the num_target_miss_files of this ConsistencyResult.

        目的端缺少文件数量

        :param num_target_miss_files: The num_target_miss_files of this ConsistencyResult.
        :type num_target_miss_files: int
        """
        self._num_target_miss_files = num_target_miss_files

    @property
    def num_target_more_files(self):
        r"""Gets the num_target_more_files of this ConsistencyResult.

        目的端多余文件数量

        :return: The num_target_more_files of this ConsistencyResult.
        :rtype: int
        """
        return self._num_target_more_files

    @num_target_more_files.setter
    def num_target_more_files(self, num_target_more_files):
        r"""Sets the num_target_more_files of this ConsistencyResult.

        目的端多余文件数量

        :param num_target_more_files: The num_target_more_files of this ConsistencyResult.
        :type num_target_more_files: int
        """
        self._num_target_more_files = num_target_more_files

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
        if not isinstance(other, ConsistencyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
