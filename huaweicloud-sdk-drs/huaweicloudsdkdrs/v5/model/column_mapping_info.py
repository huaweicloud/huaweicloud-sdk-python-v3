# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnMappingInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'column_info_lists': 'list[ColumnInfo]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'column_info_lists': 'column_info_lists'
    }

    def __init__(self, object_id=None, column_info_lists=None):
        r"""ColumnMappingInfo

        The model defined in huaweicloud sdk

        :param object_id: 对象id
        :type object_id: str
        :param column_info_lists: 列信息
        :type column_info_lists: list[:class:`huaweicloudsdkdrs.v5.ColumnInfo`]
        """
        
        

        self._object_id = None
        self._column_info_lists = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if column_info_lists is not None:
            self.column_info_lists = column_info_lists

    @property
    def object_id(self):
        r"""Gets the object_id of this ColumnMappingInfo.

        对象id

        :return: The object_id of this ColumnMappingInfo.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ColumnMappingInfo.

        对象id

        :param object_id: The object_id of this ColumnMappingInfo.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def column_info_lists(self):
        r"""Gets the column_info_lists of this ColumnMappingInfo.

        列信息

        :return: The column_info_lists of this ColumnMappingInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ColumnInfo`]
        """
        return self._column_info_lists

    @column_info_lists.setter
    def column_info_lists(self, column_info_lists):
        r"""Sets the column_info_lists of this ColumnMappingInfo.

        列信息

        :param column_info_lists: The column_info_lists of this ColumnMappingInfo.
        :type column_info_lists: list[:class:`huaweicloudsdkdrs.v5.ColumnInfo`]
        """
        self._column_info_lists = column_info_lists

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
        if not isinstance(other, ColumnMappingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
