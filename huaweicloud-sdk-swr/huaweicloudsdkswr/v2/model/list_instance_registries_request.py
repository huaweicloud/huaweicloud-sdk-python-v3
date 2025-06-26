# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceRegistriesRequest:

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
        'order_column': 'str',
        'order_type': 'str',
        'name': 'str',
        'type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'order_column': 'order_column',
        'order_type': 'order_type',
        'name': 'name',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, order_column=None, order_type=None, name=None, type=None, offset=None, limit=None):
        r"""ListInstanceRegistriesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param order_column: 排序字段，支持created_at、updated_at、name，默认为created_at
        :type order_column: str
        :param order_type: 排序方式，支持desc、asc，默认desc; 注意：order_type需要与order_column配合使用
        :type order_type: str
        :param name: 名称，模糊查询
        :type name: str
        :param type: 仓库类型
        :type type: str
        :param offset: 起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type offset: int
        :param limit: 返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type limit: int
        """
        
        

        self._instance_id = None
        self._order_column = None
        self._order_type = None
        self._name = None
        self._type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if order_column is not None:
            self.order_column = order_column
        if order_type is not None:
            self.order_type = order_type
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceRegistriesRequest.

        企业仓库实例ID

        :return: The instance_id of this ListInstanceRegistriesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceRegistriesRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListInstanceRegistriesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def order_column(self):
        r"""Gets the order_column of this ListInstanceRegistriesRequest.

        排序字段，支持created_at、updated_at、name，默认为created_at

        :return: The order_column of this ListInstanceRegistriesRequest.
        :rtype: str
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        r"""Sets the order_column of this ListInstanceRegistriesRequest.

        排序字段，支持created_at、updated_at、name，默认为created_at

        :param order_column: The order_column of this ListInstanceRegistriesRequest.
        :type order_column: str
        """
        self._order_column = order_column

    @property
    def order_type(self):
        r"""Gets the order_type of this ListInstanceRegistriesRequest.

        排序方式，支持desc、asc，默认desc; 注意：order_type需要与order_column配合使用

        :return: The order_type of this ListInstanceRegistriesRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        r"""Sets the order_type of this ListInstanceRegistriesRequest.

        排序方式，支持desc、asc，默认desc; 注意：order_type需要与order_column配合使用

        :param order_type: The order_type of this ListInstanceRegistriesRequest.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def name(self):
        r"""Gets the name of this ListInstanceRegistriesRequest.

        名称，模糊查询

        :return: The name of this ListInstanceRegistriesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstanceRegistriesRequest.

        名称，模糊查询

        :param name: The name of this ListInstanceRegistriesRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ListInstanceRegistriesRequest.

        仓库类型

        :return: The type of this ListInstanceRegistriesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListInstanceRegistriesRequest.

        仓库类型

        :param type: The type of this ListInstanceRegistriesRequest.
        :type type: str
        """
        self._type = type

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceRegistriesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The offset of this ListInstanceRegistriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceRegistriesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param offset: The offset of this ListInstanceRegistriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceRegistriesRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The limit of this ListInstanceRegistriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceRegistriesRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param limit: The limit of this ListInstanceRegistriesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListInstanceRegistriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
