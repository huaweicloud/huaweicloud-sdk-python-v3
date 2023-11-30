# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudtableSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'row_key': 'list[RowKey]',
        'columns': 'list[Column]'
    }

    attribute_map = {
        'row_key': 'row_key',
        'columns': 'columns'
    }

    def __init__(self, row_key=None, columns=None):
        """CloudtableSchema

        The model defined in huaweicloud sdk

        :param row_key: CloudTable集群HBase数据rowkey的Schema配置，用于将通道内的JSON数据生成HBase数据的rowkey。  取值范围：1～64。
        :type row_key: list[:class:`huaweicloudsdkdis.v2.RowKey`]
        :param columns: CloudTable集群HBase数据列的Schema配置，用于将通道内的JSON数据生成HBase数据的列。  取值范围：1～4096。
        :type columns: list[:class:`huaweicloudsdkdis.v2.Column`]
        """
        
        

        self._row_key = None
        self._columns = None
        self.discriminator = None

        self.row_key = row_key
        self.columns = columns

    @property
    def row_key(self):
        """Gets the row_key of this CloudtableSchema.

        CloudTable集群HBase数据rowkey的Schema配置，用于将通道内的JSON数据生成HBase数据的rowkey。  取值范围：1～64。

        :return: The row_key of this CloudtableSchema.
        :rtype: list[:class:`huaweicloudsdkdis.v2.RowKey`]
        """
        return self._row_key

    @row_key.setter
    def row_key(self, row_key):
        """Sets the row_key of this CloudtableSchema.

        CloudTable集群HBase数据rowkey的Schema配置，用于将通道内的JSON数据生成HBase数据的rowkey。  取值范围：1～64。

        :param row_key: The row_key of this CloudtableSchema.
        :type row_key: list[:class:`huaweicloudsdkdis.v2.RowKey`]
        """
        self._row_key = row_key

    @property
    def columns(self):
        """Gets the columns of this CloudtableSchema.

        CloudTable集群HBase数据列的Schema配置，用于将通道内的JSON数据生成HBase数据的列。  取值范围：1～4096。

        :return: The columns of this CloudtableSchema.
        :rtype: list[:class:`huaweicloudsdkdis.v2.Column`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this CloudtableSchema.

        CloudTable集群HBase数据列的Schema配置，用于将通道内的JSON数据生成HBase数据的列。  取值范围：1～4096。

        :param columns: The columns of this CloudtableSchema.
        :type columns: list[:class:`huaweicloudsdkdis.v2.Column`]
        """
        self._columns = columns

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
        if not isinstance(other, CloudtableSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
