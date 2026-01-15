# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowColumnInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_map_infos': 'list[ColumnMappingInfo]',
        'object_with_column_infos': 'list[ObjectWithColumnInfo]'
    }

    attribute_map = {
        'column_map_infos': 'column_map_infos',
        'object_with_column_infos': 'object_with_column_infos'
    }

    def __init__(self, column_map_infos=None, object_with_column_infos=None):
        r"""ShowColumnInfosResponse

        The model defined in huaweicloud sdk

        :param column_map_infos: 列映射信息
        :type column_map_infos: list[:class:`huaweicloudsdkdrs.v5.ColumnMappingInfo`]
        :param object_with_column_infos: 和列信息相关的对象
        :type object_with_column_infos: list[:class:`huaweicloudsdkdrs.v5.ObjectWithColumnInfo`]
        """
        
        super().__init__()

        self._column_map_infos = None
        self._object_with_column_infos = None
        self.discriminator = None

        if column_map_infos is not None:
            self.column_map_infos = column_map_infos
        if object_with_column_infos is not None:
            self.object_with_column_infos = object_with_column_infos

    @property
    def column_map_infos(self):
        r"""Gets the column_map_infos of this ShowColumnInfosResponse.

        列映射信息

        :return: The column_map_infos of this ShowColumnInfosResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ColumnMappingInfo`]
        """
        return self._column_map_infos

    @column_map_infos.setter
    def column_map_infos(self, column_map_infos):
        r"""Sets the column_map_infos of this ShowColumnInfosResponse.

        列映射信息

        :param column_map_infos: The column_map_infos of this ShowColumnInfosResponse.
        :type column_map_infos: list[:class:`huaweicloudsdkdrs.v5.ColumnMappingInfo`]
        """
        self._column_map_infos = column_map_infos

    @property
    def object_with_column_infos(self):
        r"""Gets the object_with_column_infos of this ShowColumnInfosResponse.

        和列信息相关的对象

        :return: The object_with_column_infos of this ShowColumnInfosResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ObjectWithColumnInfo`]
        """
        return self._object_with_column_infos

    @object_with_column_infos.setter
    def object_with_column_infos(self, object_with_column_infos):
        r"""Sets the object_with_column_infos of this ShowColumnInfosResponse.

        和列信息相关的对象

        :param object_with_column_infos: The object_with_column_infos of this ShowColumnInfosResponse.
        :type object_with_column_infos: list[:class:`huaweicloudsdkdrs.v5.ObjectWithColumnInfo`]
        """
        self._object_with_column_infos = object_with_column_infos

    def to_dict(self):
        import warnings
        warnings.warn("ShowColumnInfosResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowColumnInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
