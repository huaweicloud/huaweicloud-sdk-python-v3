# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index_name': 'str',
        'field_name': 'str',
        'build_progress': 'float',
        'indexed_rows': 'int',
        'total_rows': 'int'
    }

    attribute_map = {
        'index_name': 'index_name',
        'field_name': 'field_name',
        'build_progress': 'build_progress',
        'indexed_rows': 'indexed_rows',
        'total_rows': 'total_rows'
    }

    def __init__(self, index_name=None, field_name=None, build_progress=None, indexed_rows=None, total_rows=None):
        r"""BuildProgress

        The model defined in huaweicloud sdk

        :param index_name: 索引名
        :type index_name: str
        :param field_name: 索引对应的列
        :type field_name: str
        :param build_progress: 构建索引的进度，进度值为[0,1]
        :type build_progress: float
        :param indexed_rows: 已完成索引的数据量
        :type indexed_rows: int
        :param total_rows: 需要索引的数据量
        :type total_rows: int
        """
        
        

        self._index_name = None
        self._field_name = None
        self._build_progress = None
        self._indexed_rows = None
        self._total_rows = None
        self.discriminator = None

        if index_name is not None:
            self.index_name = index_name
        if field_name is not None:
            self.field_name = field_name
        if build_progress is not None:
            self.build_progress = build_progress
        if indexed_rows is not None:
            self.indexed_rows = indexed_rows
        if total_rows is not None:
            self.total_rows = total_rows

    @property
    def index_name(self):
        r"""Gets the index_name of this BuildProgress.

        索引名

        :return: The index_name of this BuildProgress.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        r"""Sets the index_name of this BuildProgress.

        索引名

        :param index_name: The index_name of this BuildProgress.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def field_name(self):
        r"""Gets the field_name of this BuildProgress.

        索引对应的列

        :return: The field_name of this BuildProgress.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this BuildProgress.

        索引对应的列

        :param field_name: The field_name of this BuildProgress.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def build_progress(self):
        r"""Gets the build_progress of this BuildProgress.

        构建索引的进度，进度值为[0,1]

        :return: The build_progress of this BuildProgress.
        :rtype: float
        """
        return self._build_progress

    @build_progress.setter
    def build_progress(self, build_progress):
        r"""Sets the build_progress of this BuildProgress.

        构建索引的进度，进度值为[0,1]

        :param build_progress: The build_progress of this BuildProgress.
        :type build_progress: float
        """
        self._build_progress = build_progress

    @property
    def indexed_rows(self):
        r"""Gets the indexed_rows of this BuildProgress.

        已完成索引的数据量

        :return: The indexed_rows of this BuildProgress.
        :rtype: int
        """
        return self._indexed_rows

    @indexed_rows.setter
    def indexed_rows(self, indexed_rows):
        r"""Sets the indexed_rows of this BuildProgress.

        已完成索引的数据量

        :param indexed_rows: The indexed_rows of this BuildProgress.
        :type indexed_rows: int
        """
        self._indexed_rows = indexed_rows

    @property
    def total_rows(self):
        r"""Gets the total_rows of this BuildProgress.

        需要索引的数据量

        :return: The total_rows of this BuildProgress.
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        r"""Sets the total_rows of this BuildProgress.

        需要索引的数据量

        :param total_rows: The total_rows of this BuildProgress.
        :type total_rows: int
        """
        self._total_rows = total_rows

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
        if not isinstance(other, BuildProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
