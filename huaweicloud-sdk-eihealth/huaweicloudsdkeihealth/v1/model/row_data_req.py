# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RowDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_values': 'list[ColumnValueDto]'
    }

    attribute_map = {
        'column_values': 'column_values'
    }

    def __init__(self, column_values=None):
        """RowDataReq

        The model defined in huaweicloud sdk

        :param column_values: 列及对应值列表
        :type column_values: list[:class:`huaweicloudsdkeihealth.v1.ColumnValueDto`]
        """
        
        

        self._column_values = None
        self.discriminator = None

        self.column_values = column_values

    @property
    def column_values(self):
        """Gets the column_values of this RowDataReq.

        列及对应值列表

        :return: The column_values of this RowDataReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ColumnValueDto`]
        """
        return self._column_values

    @column_values.setter
    def column_values(self, column_values):
        """Sets the column_values of this RowDataReq.

        列及对应值列表

        :param column_values: The column_values of this RowDataReq.
        :type column_values: list[:class:`huaweicloudsdkeihealth.v1.ColumnValueDto`]
        """
        self._column_values = column_values

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
        if not isinstance(other, RowDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
