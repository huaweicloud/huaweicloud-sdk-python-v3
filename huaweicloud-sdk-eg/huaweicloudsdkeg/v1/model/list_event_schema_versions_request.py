# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventSchemaVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort': 'str',
        'version': 'str'
    }

    attribute_map = {
        'schema_id': 'schema_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'version': 'version'
    }

    def __init__(self, schema_id=None, offset=None, limit=None, sort=None, version=None):
        r"""ListEventSchemaVersionsRequest

        The model defined in huaweicloud sdk

        :param schema_id: 指定查询的事件模型ID
        :type schema_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量不能小于0
        :type offset: int
        :param limit: 每页显示的条目数量，不能小于1或大于1000
        :type limit: int
        :param sort: 指定查询排序
        :type sort: str
        :param version: 指定查询的事件模型版本号
        :type version: str
        """
        
        

        self._schema_id = None
        self._offset = None
        self._limit = None
        self._sort = None
        self._version = None
        self.discriminator = None

        self.schema_id = schema_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort
        if version is not None:
            self.version = version

    @property
    def schema_id(self):
        r"""Gets the schema_id of this ListEventSchemaVersionsRequest.

        指定查询的事件模型ID

        :return: The schema_id of this ListEventSchemaVersionsRequest.
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        r"""Sets the schema_id of this ListEventSchemaVersionsRequest.

        指定查询的事件模型ID

        :param schema_id: The schema_id of this ListEventSchemaVersionsRequest.
        :type schema_id: str
        """
        self._schema_id = schema_id

    @property
    def offset(self):
        r"""Gets the offset of this ListEventSchemaVersionsRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :return: The offset of this ListEventSchemaVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEventSchemaVersionsRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :param offset: The offset of this ListEventSchemaVersionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEventSchemaVersionsRequest.

        每页显示的条目数量，不能小于1或大于1000

        :return: The limit of this ListEventSchemaVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEventSchemaVersionsRequest.

        每页显示的条目数量，不能小于1或大于1000

        :param limit: The limit of this ListEventSchemaVersionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort(self):
        r"""Gets the sort of this ListEventSchemaVersionsRequest.

        指定查询排序

        :return: The sort of this ListEventSchemaVersionsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListEventSchemaVersionsRequest.

        指定查询排序

        :param sort: The sort of this ListEventSchemaVersionsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def version(self):
        r"""Gets the version of this ListEventSchemaVersionsRequest.

        指定查询的事件模型版本号

        :return: The version of this ListEventSchemaVersionsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListEventSchemaVersionsRequest.

        指定查询的事件模型版本号

        :param version: The version of this ListEventSchemaVersionsRequest.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ListEventSchemaVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
