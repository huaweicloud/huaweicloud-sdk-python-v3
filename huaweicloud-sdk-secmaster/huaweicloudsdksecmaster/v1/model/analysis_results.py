# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalysisResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datarows': 'list[list[object]]',
        'schema': 'list[AnalysisField]',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'datarows': 'datarows',
        'schema': 'schema',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, datarows=None, schema=None, size=None, total=None):
        r"""AnalysisResults

        The model defined in huaweicloud sdk

        :param datarows: 统计分析结果数据
        :type datarows: list[list[object]]
        :param schema: 统计分析结果字段类型
        :type schema: list[:class:`huaweicloudsdksecmaster.v1.AnalysisField`]
        :param size: 返回的统计分析结果条数
        :type size: int
        :param total: 统计分析结果总数
        :type total: int
        """
        
        

        self._datarows = None
        self._schema = None
        self._size = None
        self._total = None
        self.discriminator = None

        self.datarows = datarows
        self.schema = schema
        self.size = size
        self.total = total

    @property
    def datarows(self):
        r"""Gets the datarows of this AnalysisResults.

        统计分析结果数据

        :return: The datarows of this AnalysisResults.
        :rtype: list[list[object]]
        """
        return self._datarows

    @datarows.setter
    def datarows(self, datarows):
        r"""Sets the datarows of this AnalysisResults.

        统计分析结果数据

        :param datarows: The datarows of this AnalysisResults.
        :type datarows: list[list[object]]
        """
        self._datarows = datarows

    @property
    def schema(self):
        r"""Gets the schema of this AnalysisResults.

        统计分析结果字段类型

        :return: The schema of this AnalysisResults.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.AnalysisField`]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this AnalysisResults.

        统计分析结果字段类型

        :param schema: The schema of this AnalysisResults.
        :type schema: list[:class:`huaweicloudsdksecmaster.v1.AnalysisField`]
        """
        self._schema = schema

    @property
    def size(self):
        r"""Gets the size of this AnalysisResults.

        返回的统计分析结果条数

        :return: The size of this AnalysisResults.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this AnalysisResults.

        返回的统计分析结果条数

        :param size: The size of this AnalysisResults.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this AnalysisResults.

        统计分析结果总数

        :return: The total of this AnalysisResults.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this AnalysisResults.

        统计分析结果总数

        :param total: The total of this AnalysisResults.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, AnalysisResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
