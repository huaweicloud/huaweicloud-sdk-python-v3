# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServersByHostIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, host_id=None, sort_field=None, sort_type=None, limit=None, offset=None):
        r"""ListServersByHostIdRequest

        The model defined in huaweicloud sdk

        :param host_id: 云办公主机id。
        :type host_id: str
        :param sort_field: 排序字段名称，需要结合sort_type字段一起使用。 - vcpu CPU核数 - memory 内存大小
        :type sort_field: str
        :param sort_type: 排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。
        :type sort_type: str
        :param limit: 每页显示的数量。
        :type limit: int
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        """
        
        

        self._host_id = None
        self._sort_field = None
        self._sort_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.host_id = host_id
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def host_id(self):
        r"""Gets the host_id of this ListServersByHostIdRequest.

        云办公主机id。

        :return: The host_id of this ListServersByHostIdRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListServersByHostIdRequest.

        云办公主机id。

        :param host_id: The host_id of this ListServersByHostIdRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListServersByHostIdRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - vcpu CPU核数 - memory 内存大小

        :return: The sort_field of this ListServersByHostIdRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListServersByHostIdRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - vcpu CPU核数 - memory 内存大小

        :param sort_field: The sort_field of this ListServersByHostIdRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this ListServersByHostIdRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :return: The sort_type of this ListServersByHostIdRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this ListServersByHostIdRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :param sort_type: The sort_type of this ListServersByHostIdRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def limit(self):
        r"""Gets the limit of this ListServersByHostIdRequest.

        每页显示的数量。

        :return: The limit of this ListServersByHostIdRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListServersByHostIdRequest.

        每页显示的数量。

        :param limit: The limit of this ListServersByHostIdRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListServersByHostIdRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListServersByHostIdRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListServersByHostIdRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListServersByHostIdRequest.
        :type offset: int
        """
        self._offset = offset

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListServersByHostIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
