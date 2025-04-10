# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasourceOrderPara:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'field': 'str',
        'optional': 'bool',
        'sort': 'str',
        'order': 'int',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'field': 'field',
        'optional': 'optional',
        'sort': 'sort',
        'order': 'order',
        'description': 'description'
    }

    def __init__(self, name=None, field=None, optional=None, sort=None, order=None, description=None):
        r"""DatasourceOrderPara

        The model defined in huaweicloud sdk

        :param name: 排序参数名称
        :type name: str
        :param field: 对应的参数字段
        :type field: str
        :param optional: 是否可选
        :type optional: bool
        :param sort: 排序方式
        :type sort: str
        :param order: 排序参数顺序
        :type order: int
        :param description: 排序参数描述信息。
        :type description: str
        """
        
        

        self._name = None
        self._field = None
        self._optional = None
        self._sort = None
        self._order = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if field is not None:
            self.field = field
        if optional is not None:
            self.optional = optional
        if sort is not None:
            self.sort = sort
        if order is not None:
            self.order = order
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this DatasourceOrderPara.

        排序参数名称

        :return: The name of this DatasourceOrderPara.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DatasourceOrderPara.

        排序参数名称

        :param name: The name of this DatasourceOrderPara.
        :type name: str
        """
        self._name = name

    @property
    def field(self):
        r"""Gets the field of this DatasourceOrderPara.

        对应的参数字段

        :return: The field of this DatasourceOrderPara.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this DatasourceOrderPara.

        对应的参数字段

        :param field: The field of this DatasourceOrderPara.
        :type field: str
        """
        self._field = field

    @property
    def optional(self):
        r"""Gets the optional of this DatasourceOrderPara.

        是否可选

        :return: The optional of this DatasourceOrderPara.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        r"""Sets the optional of this DatasourceOrderPara.

        是否可选

        :param optional: The optional of this DatasourceOrderPara.
        :type optional: bool
        """
        self._optional = optional

    @property
    def sort(self):
        r"""Gets the sort of this DatasourceOrderPara.

        排序方式

        :return: The sort of this DatasourceOrderPara.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this DatasourceOrderPara.

        排序方式

        :param sort: The sort of this DatasourceOrderPara.
        :type sort: str
        """
        self._sort = sort

    @property
    def order(self):
        r"""Gets the order of this DatasourceOrderPara.

        排序参数顺序

        :return: The order of this DatasourceOrderPara.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this DatasourceOrderPara.

        排序参数顺序

        :param order: The order of this DatasourceOrderPara.
        :type order: int
        """
        self._order = order

    @property
    def description(self):
        r"""Gets the description of this DatasourceOrderPara.

        排序参数描述信息。

        :return: The description of this DatasourceOrderPara.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DatasourceOrderPara.

        排序参数描述信息。

        :param description: The description of this DatasourceOrderPara.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, DatasourceOrderPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
