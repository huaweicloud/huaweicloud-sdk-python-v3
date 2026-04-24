# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExtraColumnsResponse(SdkResponse):

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
        'column_process_objects': 'list[ColumnProcessObjects]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'column_process_objects': 'column_process_objects'
    }

    def __init__(self, total_count=None, column_process_objects=None):
        r"""ListExtraColumnsResponse

        The model defined in huaweicloud sdk

        :param total_count: 列表中的项目总数，与分页无关。
        :type total_count: int
        :param column_process_objects: 列加工对象
        :type column_process_objects: list[:class:`huaweicloudsdkdrs.v5.ColumnProcessObjects`]
        """
        
        super().__init__()

        self._total_count = None
        self._column_process_objects = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if column_process_objects is not None:
            self.column_process_objects = column_process_objects

    @property
    def total_count(self):
        r"""Gets the total_count of this ListExtraColumnsResponse.

        列表中的项目总数，与分页无关。

        :return: The total_count of this ListExtraColumnsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListExtraColumnsResponse.

        列表中的项目总数，与分页无关。

        :param total_count: The total_count of this ListExtraColumnsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def column_process_objects(self):
        r"""Gets the column_process_objects of this ListExtraColumnsResponse.

        列加工对象

        :return: The column_process_objects of this ListExtraColumnsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ColumnProcessObjects`]
        """
        return self._column_process_objects

    @column_process_objects.setter
    def column_process_objects(self, column_process_objects):
        r"""Sets the column_process_objects of this ListExtraColumnsResponse.

        列加工对象

        :param column_process_objects: The column_process_objects of this ListExtraColumnsResponse.
        :type column_process_objects: list[:class:`huaweicloudsdkdrs.v5.ColumnProcessObjects`]
        """
        self._column_process_objects = column_process_objects

    def to_dict(self):
        import warnings
        warnings.warn("ListExtraColumnsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListExtraColumnsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
