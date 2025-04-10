# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerTableResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_count': 'int',
        'table_list': 'list[SmartDocumentRecognizerTableBlock]'
    }

    attribute_map = {
        'table_count': 'table_count',
        'table_list': 'table_list'
    }

    def __init__(self, table_count=None, table_list=None):
        r"""SmartDocumentRecognizerTableResult

        The model defined in huaweicloud sdk

        :param table_count: 模型识别到的表格数量。 
        :type table_count: int
        :param table_list: 表格识别结果列表。 
        :type table_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableBlock`]
        """
        
        

        self._table_count = None
        self._table_list = None
        self.discriminator = None

        if table_count is not None:
            self.table_count = table_count
        if table_list is not None:
            self.table_list = table_list

    @property
    def table_count(self):
        r"""Gets the table_count of this SmartDocumentRecognizerTableResult.

        模型识别到的表格数量。 

        :return: The table_count of this SmartDocumentRecognizerTableResult.
        :rtype: int
        """
        return self._table_count

    @table_count.setter
    def table_count(self, table_count):
        r"""Sets the table_count of this SmartDocumentRecognizerTableResult.

        模型识别到的表格数量。 

        :param table_count: The table_count of this SmartDocumentRecognizerTableResult.
        :type table_count: int
        """
        self._table_count = table_count

    @property
    def table_list(self):
        r"""Gets the table_list of this SmartDocumentRecognizerTableResult.

        表格识别结果列表。 

        :return: The table_list of this SmartDocumentRecognizerTableResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableBlock`]
        """
        return self._table_list

    @table_list.setter
    def table_list(self, table_list):
        r"""Sets the table_list of this SmartDocumentRecognizerTableResult.

        表格识别结果列表。 

        :param table_list: The table_list of this SmartDocumentRecognizerTableResult.
        :type table_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableBlock`]
        """
        self._table_list = table_list

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
        if not isinstance(other, SmartDocumentRecognizerTableResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
