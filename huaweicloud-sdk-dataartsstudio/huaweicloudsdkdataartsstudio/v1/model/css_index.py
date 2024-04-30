# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CssIndex:

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
        'index_guid': 'str',
        'index_qualified_name': 'str',
        'index_doc_count': 'int',
        'index_data_size': 'float'
    }

    attribute_map = {
        'index_name': 'index_name',
        'index_guid': 'index_guid',
        'index_qualified_name': 'index_qualified_name',
        'index_doc_count': 'index_doc_count',
        'index_data_size': 'index_data_size'
    }

    def __init__(self, index_name=None, index_guid=None, index_qualified_name=None, index_doc_count=None, index_data_size=None):
        """CssIndex

        The model defined in huaweicloud sdk

        :param index_name: 索引名称
        :type index_name: str
        :param index_guid: 索引的guid
        :type index_guid: str
        :param index_qualified_name: 索引的唯一标识名称
        :type index_qualified_name: str
        :param index_doc_count: 索引中文档总数
        :type index_doc_count: int
        :param index_data_size: 索引数据量大小
        :type index_data_size: float
        """
        
        

        self._index_name = None
        self._index_guid = None
        self._index_qualified_name = None
        self._index_doc_count = None
        self._index_data_size = None
        self.discriminator = None

        if index_name is not None:
            self.index_name = index_name
        if index_guid is not None:
            self.index_guid = index_guid
        if index_qualified_name is not None:
            self.index_qualified_name = index_qualified_name
        if index_doc_count is not None:
            self.index_doc_count = index_doc_count
        if index_data_size is not None:
            self.index_data_size = index_data_size

    @property
    def index_name(self):
        """Gets the index_name of this CssIndex.

        索引名称

        :return: The index_name of this CssIndex.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """Sets the index_name of this CssIndex.

        索引名称

        :param index_name: The index_name of this CssIndex.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def index_guid(self):
        """Gets the index_guid of this CssIndex.

        索引的guid

        :return: The index_guid of this CssIndex.
        :rtype: str
        """
        return self._index_guid

    @index_guid.setter
    def index_guid(self, index_guid):
        """Sets the index_guid of this CssIndex.

        索引的guid

        :param index_guid: The index_guid of this CssIndex.
        :type index_guid: str
        """
        self._index_guid = index_guid

    @property
    def index_qualified_name(self):
        """Gets the index_qualified_name of this CssIndex.

        索引的唯一标识名称

        :return: The index_qualified_name of this CssIndex.
        :rtype: str
        """
        return self._index_qualified_name

    @index_qualified_name.setter
    def index_qualified_name(self, index_qualified_name):
        """Sets the index_qualified_name of this CssIndex.

        索引的唯一标识名称

        :param index_qualified_name: The index_qualified_name of this CssIndex.
        :type index_qualified_name: str
        """
        self._index_qualified_name = index_qualified_name

    @property
    def index_doc_count(self):
        """Gets the index_doc_count of this CssIndex.

        索引中文档总数

        :return: The index_doc_count of this CssIndex.
        :rtype: int
        """
        return self._index_doc_count

    @index_doc_count.setter
    def index_doc_count(self, index_doc_count):
        """Sets the index_doc_count of this CssIndex.

        索引中文档总数

        :param index_doc_count: The index_doc_count of this CssIndex.
        :type index_doc_count: int
        """
        self._index_doc_count = index_doc_count

    @property
    def index_data_size(self):
        """Gets the index_data_size of this CssIndex.

        索引数据量大小

        :return: The index_data_size of this CssIndex.
        :rtype: float
        """
        return self._index_data_size

    @index_data_size.setter
    def index_data_size(self, index_data_size):
        """Sets the index_data_size of this CssIndex.

        索引数据量大小

        :param index_data_size: The index_data_size of this CssIndex.
        :type index_data_size: float
        """
        self._index_data_size = index_data_size

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
        if not isinstance(other, CssIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
