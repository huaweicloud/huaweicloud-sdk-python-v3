# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNamespaceRepositoriesRequest:

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
        'namespace_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'order_column': 'order_column',
        'order_type': 'order_type',
        'namespace_name': 'namespace_name'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, order_column=None, order_type=None, namespace_name=None):
        r"""ListNamespaceRepositoriesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param offset: 起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type offset: int
        :param limit: 返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type limit: int
        :param order_column: 排序字段，支持created_at、updated_at，默认为created_at
        :type order_column: str
        :param order_type: 排序方式，支持desc、asc，默认desc;order_column和order_type参数需要配套使用
        :type order_type: str
        :param namespace_name: 所属命名空间名称
        :type namespace_name: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._order_column = None
        self._order_type = None
        self._namespace_name = None
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
        self.namespace_name = namespace_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListNamespaceRepositoriesRequest.

        企业仓库实例ID

        :return: The instance_id of this ListNamespaceRepositoriesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListNamespaceRepositoriesRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListNamespaceRepositoriesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListNamespaceRepositoriesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The offset of this ListNamespaceRepositoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNamespaceRepositoriesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param offset: The offset of this ListNamespaceRepositoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListNamespaceRepositoriesRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The limit of this ListNamespaceRepositoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNamespaceRepositoriesRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param limit: The limit of this ListNamespaceRepositoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_column(self):
        r"""Gets the order_column of this ListNamespaceRepositoriesRequest.

        排序字段，支持created_at、updated_at，默认为created_at

        :return: The order_column of this ListNamespaceRepositoriesRequest.
        :rtype: str
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        r"""Sets the order_column of this ListNamespaceRepositoriesRequest.

        排序字段，支持created_at、updated_at，默认为created_at

        :param order_column: The order_column of this ListNamespaceRepositoriesRequest.
        :type order_column: str
        """
        self._order_column = order_column

    @property
    def order_type(self):
        r"""Gets the order_type of this ListNamespaceRepositoriesRequest.

        排序方式，支持desc、asc，默认desc;order_column和order_type参数需要配套使用

        :return: The order_type of this ListNamespaceRepositoriesRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        r"""Sets the order_type of this ListNamespaceRepositoriesRequest.

        排序方式，支持desc、asc，默认desc;order_column和order_type参数需要配套使用

        :param order_type: The order_type of this ListNamespaceRepositoriesRequest.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ListNamespaceRepositoriesRequest.

        所属命名空间名称

        :return: The namespace_name of this ListNamespaceRepositoriesRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ListNamespaceRepositoriesRequest.

        所属命名空间名称

        :param namespace_name: The namespace_name of this ListNamespaceRepositoriesRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

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
        if not isinstance(other, ListNamespaceRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
