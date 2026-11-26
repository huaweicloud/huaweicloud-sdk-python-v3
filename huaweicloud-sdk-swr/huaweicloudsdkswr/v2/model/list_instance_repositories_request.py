# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceRepositoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'order_column': 'str',
        'order_type': 'str',
        'namespace_id': 'int',
        'name': 'str',
        'with_tag': 'bool',
        'tags': 'str',
        'namespace_ids': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'order_column': 'order_column',
        'order_type': 'order_type',
        'namespace_id': 'namespace_id',
        'name': 'name',
        'with_tag': 'with_tag',
        'tags': 'tags',
        'namespace_ids': 'namespace_ids'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, order_column=None, order_type=None, namespace_id=None, name=None, with_tag=None, tags=None, namespace_ids=None):
        r"""ListInstanceRepositoriesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param offset: 起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type offset: int
        :param limit: 返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type limit: int
        :param order_column: 排序字段，支持created_at、updated_at，默认为created_at
        :type order_column: str
        :param order_type: 排序方式，支持desc、asc，默认desc
        :type order_type: str
        :param namespace_id: 所属命名空间ID
        :type namespace_id: int
        :param name: 根据仓库名称或命名空间名称进行模糊查询
        :type name: str
        :param with_tag: 是否返回仓库的标签
        :type with_tag: bool
        :param tags: 根据标签过滤，多个标签以英文逗号隔开，最多支持20个标签同时过滤查询。格式为key1&#x3D;value1,key2&#x3D;value2。如果标签的key/value值中有特殊字符&#x3D;，请先把 &#x3D; 替换成 %3D 再进行请求。注意：使用curl命令请求，需要把 &#x3D; 替换成 %253D(即 %3D 的 %25 被编码为 %25)再次请求。
        :type tags: str
        :param namespace_ids: 支持按多个所属命名空间ID过滤，多个ID之间用英文逗号分隔。注意：namespace_id与namespace_ids不支持同时传参。
        :type namespace_ids: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._order_column = None
        self._order_type = None
        self._namespace_id = None
        self._name = None
        self._with_tag = None
        self._tags = None
        self._namespace_ids = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_column is not None:
            self.order_column = order_column
        if order_type is not None:
            self.order_type = order_type
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if name is not None:
            self.name = name
        if with_tag is not None:
            self.with_tag = with_tag
        if tags is not None:
            self.tags = tags
        if namespace_ids is not None:
            self.namespace_ids = namespace_ids

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceRepositoriesRequest.

        企业仓库实例ID

        :return: The instance_id of this ListInstanceRepositoriesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceRepositoriesRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListInstanceRepositoriesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceRepositoriesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The offset of this ListInstanceRepositoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceRepositoriesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param offset: The offset of this ListInstanceRepositoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceRepositoriesRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The limit of this ListInstanceRepositoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceRepositoriesRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param limit: The limit of this ListInstanceRepositoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_column(self):
        r"""Gets the order_column of this ListInstanceRepositoriesRequest.

        排序字段，支持created_at、updated_at，默认为created_at

        :return: The order_column of this ListInstanceRepositoriesRequest.
        :rtype: str
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        r"""Sets the order_column of this ListInstanceRepositoriesRequest.

        排序字段，支持created_at、updated_at，默认为created_at

        :param order_column: The order_column of this ListInstanceRepositoriesRequest.
        :type order_column: str
        """
        self._order_column = order_column

    @property
    def order_type(self):
        r"""Gets the order_type of this ListInstanceRepositoriesRequest.

        排序方式，支持desc、asc，默认desc

        :return: The order_type of this ListInstanceRepositoriesRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        r"""Sets the order_type of this ListInstanceRepositoriesRequest.

        排序方式，支持desc、asc，默认desc

        :param order_type: The order_type of this ListInstanceRepositoriesRequest.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this ListInstanceRepositoriesRequest.

        所属命名空间ID

        :return: The namespace_id of this ListInstanceRepositoriesRequest.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this ListInstanceRepositoriesRequest.

        所属命名空间ID

        :param namespace_id: The namespace_id of this ListInstanceRepositoriesRequest.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def name(self):
        r"""Gets the name of this ListInstanceRepositoriesRequest.

        根据仓库名称或命名空间名称进行模糊查询

        :return: The name of this ListInstanceRepositoriesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstanceRepositoriesRequest.

        根据仓库名称或命名空间名称进行模糊查询

        :param name: The name of this ListInstanceRepositoriesRequest.
        :type name: str
        """
        self._name = name

    @property
    def with_tag(self):
        r"""Gets the with_tag of this ListInstanceRepositoriesRequest.

        是否返回仓库的标签

        :return: The with_tag of this ListInstanceRepositoriesRequest.
        :rtype: bool
        """
        return self._with_tag

    @with_tag.setter
    def with_tag(self, with_tag):
        r"""Sets the with_tag of this ListInstanceRepositoriesRequest.

        是否返回仓库的标签

        :param with_tag: The with_tag of this ListInstanceRepositoriesRequest.
        :type with_tag: bool
        """
        self._with_tag = with_tag

    @property
    def tags(self):
        r"""Gets the tags of this ListInstanceRepositoriesRequest.

        根据标签过滤，多个标签以英文逗号隔开，最多支持20个标签同时过滤查询。格式为key1=value1,key2=value2。如果标签的key/value值中有特殊字符=，请先把 = 替换成 %3D 再进行请求。注意：使用curl命令请求，需要把 = 替换成 %253D(即 %3D 的 %25 被编码为 %25)再次请求。

        :return: The tags of this ListInstanceRepositoriesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListInstanceRepositoriesRequest.

        根据标签过滤，多个标签以英文逗号隔开，最多支持20个标签同时过滤查询。格式为key1=value1,key2=value2。如果标签的key/value值中有特殊字符=，请先把 = 替换成 %3D 再进行请求。注意：使用curl命令请求，需要把 = 替换成 %253D(即 %3D 的 %25 被编码为 %25)再次请求。

        :param tags: The tags of this ListInstanceRepositoriesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def namespace_ids(self):
        r"""Gets the namespace_ids of this ListInstanceRepositoriesRequest.

        支持按多个所属命名空间ID过滤，多个ID之间用英文逗号分隔。注意：namespace_id与namespace_ids不支持同时传参。

        :return: The namespace_ids of this ListInstanceRepositoriesRequest.
        :rtype: str
        """
        return self._namespace_ids

    @namespace_ids.setter
    def namespace_ids(self, namespace_ids):
        r"""Sets the namespace_ids of this ListInstanceRepositoriesRequest.

        支持按多个所属命名空间ID过滤，多个ID之间用英文逗号分隔。注意：namespace_id与namespace_ids不支持同时传参。

        :param namespace_ids: The namespace_ids of this ListInstanceRepositoriesRequest.
        :type namespace_ids: str
        """
        self._namespace_ids = namespace_ids

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
        if not isinstance(other, ListInstanceRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
