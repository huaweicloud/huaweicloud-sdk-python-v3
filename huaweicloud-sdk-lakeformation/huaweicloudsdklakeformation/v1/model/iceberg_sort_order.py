# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IcebergSortOrder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'int',
        'fields': 'list[IcebergSortField]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'fields': 'fields'
    }

    def __init__(self, order_id=None, fields=None):
        r"""IcebergSortOrder

        The model defined in huaweicloud sdk

        :param order_id: 排序规范的id
        :type order_id: int
        :param fields: IcebergSortField的数组
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.IcebergSortField`]
        """
        
        

        self._order_id = None
        self._fields = None
        self.discriminator = None

        self.order_id = order_id
        self.fields = fields

    @property
    def order_id(self):
        r"""Gets the order_id of this IcebergSortOrder.

        排序规范的id

        :return: The order_id of this IcebergSortOrder.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this IcebergSortOrder.

        排序规范的id

        :param order_id: The order_id of this IcebergSortOrder.
        :type order_id: int
        """
        self._order_id = order_id

    @property
    def fields(self):
        r"""Gets the fields of this IcebergSortOrder.

        IcebergSortField的数组

        :return: The fields of this IcebergSortOrder.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.IcebergSortField`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this IcebergSortOrder.

        IcebergSortField的数组

        :param fields: The fields of this IcebergSortOrder.
        :type fields: list[:class:`huaweicloudsdklakeformation.v1.IcebergSortField`]
        """
        self._fields = fields

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
        if not isinstance(other, IcebergSortOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
