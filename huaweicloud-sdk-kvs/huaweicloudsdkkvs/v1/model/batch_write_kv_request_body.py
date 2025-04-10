# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchWriteKvRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_opers': 'list[TableBatch]'
    }

    attribute_map = {
        'table_opers': 'table_opers'
    }

    def __init__(self, table_opers=None):
        r"""BatchWriteKvRequestBody

        The model defined in huaweicloud sdk

        :param table_opers: 行操作数组，可以是多个表的操作。
        :type table_opers: list[:class:`huaweicloudsdkkvs.v1.TableBatch`]
        """
        
        

        self._table_opers = None
        self.discriminator = None

        self.table_opers = table_opers

    @property
    def table_opers(self):
        r"""Gets the table_opers of this BatchWriteKvRequestBody.

        行操作数组，可以是多个表的操作。

        :return: The table_opers of this BatchWriteKvRequestBody.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.TableBatch`]
        """
        return self._table_opers

    @table_opers.setter
    def table_opers(self, table_opers):
        r"""Sets the table_opers of this BatchWriteKvRequestBody.

        行操作数组，可以是多个表的操作。

        :param table_opers: The table_opers of this BatchWriteKvRequestBody.
        :type table_opers: list[:class:`huaweicloudsdkkvs.v1.TableBatch`]
        """
        self._table_opers = table_opers

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
        if not isinstance(other, BatchWriteKvRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
