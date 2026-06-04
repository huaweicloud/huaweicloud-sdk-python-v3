# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IcebergSortField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_id': 'int',
        'transform': 'str',
        'direction': 'str',
        'null_order': 'str'
    }

    attribute_map = {
        'source_id': 'source_id',
        'transform': 'transform',
        'direction': 'direction',
        'null_order': 'null_order'
    }

    def __init__(self, source_id=None, transform=None, direction=None, null_order=None):
        r"""IcebergSortField

        The model defined in huaweicloud sdk

        :param source_id: 源字段的id。
        :type source_id: int
        :param transform: 转换函数。
        :type transform: str
        :param direction: 排序方向。
        :type direction: str
        :param null_order: null值的排序。
        :type null_order: str
        """
        
        

        self._source_id = None
        self._transform = None
        self._direction = None
        self._null_order = None
        self.discriminator = None

        self.source_id = source_id
        self.transform = transform
        self.direction = direction
        self.null_order = null_order

    @property
    def source_id(self):
        r"""Gets the source_id of this IcebergSortField.

        源字段的id。

        :return: The source_id of this IcebergSortField.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this IcebergSortField.

        源字段的id。

        :param source_id: The source_id of this IcebergSortField.
        :type source_id: int
        """
        self._source_id = source_id

    @property
    def transform(self):
        r"""Gets the transform of this IcebergSortField.

        转换函数。

        :return: The transform of this IcebergSortField.
        :rtype: str
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        r"""Sets the transform of this IcebergSortField.

        转换函数。

        :param transform: The transform of this IcebergSortField.
        :type transform: str
        """
        self._transform = transform

    @property
    def direction(self):
        r"""Gets the direction of this IcebergSortField.

        排序方向。

        :return: The direction of this IcebergSortField.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this IcebergSortField.

        排序方向。

        :param direction: The direction of this IcebergSortField.
        :type direction: str
        """
        self._direction = direction

    @property
    def null_order(self):
        r"""Gets the null_order of this IcebergSortField.

        null值的排序。

        :return: The null_order of this IcebergSortField.
        :rtype: str
        """
        return self._null_order

    @null_order.setter
    def null_order(self, null_order):
        r"""Sets the null_order of this IcebergSortField.

        null值的排序。

        :param null_order: The null_order of this IcebergSortField.
        :type null_order: str
        """
        self._null_order = null_order

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
        if not isinstance(other, IcebergSortField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
