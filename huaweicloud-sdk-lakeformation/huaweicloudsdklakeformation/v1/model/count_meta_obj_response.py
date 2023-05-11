# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountMetaObjResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'functions_count': 'int',
        'catalogs_count': 'int',
        'databases_count': 'int',
        'tables_count': 'int',
        'partitions_count': 'int',
        'indexes_count': 'int'
    }

    attribute_map = {
        'total_count': 'total_count',
        'functions_count': 'functions_count',
        'catalogs_count': 'catalogs_count',
        'databases_count': 'databases_count',
        'tables_count': 'tables_count',
        'partitions_count': 'partitions_count',
        'indexes_count': 'indexes_count'
    }

    def __init__(self, total_count=None, functions_count=None, catalogs_count=None, databases_count=None, tables_count=None, partitions_count=None, indexes_count=None):
        """CountMetaObjResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数量
        :type total_count: int
        :param functions_count: 函数数量
        :type functions_count: int
        :param catalogs_count: 目录数量
        :type catalogs_count: int
        :param databases_count: 数据库数量
        :type databases_count: int
        :param tables_count: 表数量
        :type tables_count: int
        :param partitions_count: 分区数量
        :type partitions_count: int
        :param indexes_count: 索引数量
        :type indexes_count: int
        """
        
        super(CountMetaObjResponse, self).__init__()

        self._total_count = None
        self._functions_count = None
        self._catalogs_count = None
        self._databases_count = None
        self._tables_count = None
        self._partitions_count = None
        self._indexes_count = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if functions_count is not None:
            self.functions_count = functions_count
        if catalogs_count is not None:
            self.catalogs_count = catalogs_count
        if databases_count is not None:
            self.databases_count = databases_count
        if tables_count is not None:
            self.tables_count = tables_count
        if partitions_count is not None:
            self.partitions_count = partitions_count
        if indexes_count is not None:
            self.indexes_count = indexes_count

    @property
    def total_count(self):
        """Gets the total_count of this CountMetaObjResponse.

        总数量

        :return: The total_count of this CountMetaObjResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this CountMetaObjResponse.

        总数量

        :param total_count: The total_count of this CountMetaObjResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def functions_count(self):
        """Gets the functions_count of this CountMetaObjResponse.

        函数数量

        :return: The functions_count of this CountMetaObjResponse.
        :rtype: int
        """
        return self._functions_count

    @functions_count.setter
    def functions_count(self, functions_count):
        """Sets the functions_count of this CountMetaObjResponse.

        函数数量

        :param functions_count: The functions_count of this CountMetaObjResponse.
        :type functions_count: int
        """
        self._functions_count = functions_count

    @property
    def catalogs_count(self):
        """Gets the catalogs_count of this CountMetaObjResponse.

        目录数量

        :return: The catalogs_count of this CountMetaObjResponse.
        :rtype: int
        """
        return self._catalogs_count

    @catalogs_count.setter
    def catalogs_count(self, catalogs_count):
        """Sets the catalogs_count of this CountMetaObjResponse.

        目录数量

        :param catalogs_count: The catalogs_count of this CountMetaObjResponse.
        :type catalogs_count: int
        """
        self._catalogs_count = catalogs_count

    @property
    def databases_count(self):
        """Gets the databases_count of this CountMetaObjResponse.

        数据库数量

        :return: The databases_count of this CountMetaObjResponse.
        :rtype: int
        """
        return self._databases_count

    @databases_count.setter
    def databases_count(self, databases_count):
        """Sets the databases_count of this CountMetaObjResponse.

        数据库数量

        :param databases_count: The databases_count of this CountMetaObjResponse.
        :type databases_count: int
        """
        self._databases_count = databases_count

    @property
    def tables_count(self):
        """Gets the tables_count of this CountMetaObjResponse.

        表数量

        :return: The tables_count of this CountMetaObjResponse.
        :rtype: int
        """
        return self._tables_count

    @tables_count.setter
    def tables_count(self, tables_count):
        """Sets the tables_count of this CountMetaObjResponse.

        表数量

        :param tables_count: The tables_count of this CountMetaObjResponse.
        :type tables_count: int
        """
        self._tables_count = tables_count

    @property
    def partitions_count(self):
        """Gets the partitions_count of this CountMetaObjResponse.

        分区数量

        :return: The partitions_count of this CountMetaObjResponse.
        :rtype: int
        """
        return self._partitions_count

    @partitions_count.setter
    def partitions_count(self, partitions_count):
        """Sets the partitions_count of this CountMetaObjResponse.

        分区数量

        :param partitions_count: The partitions_count of this CountMetaObjResponse.
        :type partitions_count: int
        """
        self._partitions_count = partitions_count

    @property
    def indexes_count(self):
        """Gets the indexes_count of this CountMetaObjResponse.

        索引数量

        :return: The indexes_count of this CountMetaObjResponse.
        :rtype: int
        """
        return self._indexes_count

    @indexes_count.setter
    def indexes_count(self, indexes_count):
        """Sets the indexes_count of this CountMetaObjResponse.

        索引数量

        :param indexes_count: The indexes_count of this CountMetaObjResponse.
        :type indexes_count: int
        """
        self._indexes_count = indexes_count

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
        if not isinstance(other, CountMetaObjResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
