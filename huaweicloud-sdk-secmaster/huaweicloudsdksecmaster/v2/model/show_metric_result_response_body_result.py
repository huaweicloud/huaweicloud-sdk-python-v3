# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetricResultResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'labels': 'list[str]',
        'datarows': 'list[list[object]]',
        'effective_column': 'str'
    }

    attribute_map = {
        'labels': 'labels',
        'datarows': 'datarows',
        'effective_column': 'effective_column'
    }

    def __init__(self, labels=None, datarows=None, effective_column=None):
        r"""ShowMetricResultResponseBodyResult

        The model defined in huaweicloud sdk

        :param labels: 指标查询结果表格标题
        :type labels: list[str]
        :param datarows: 指标查询结果内容表格
        :type datarows: list[list[object]]
        :param effective_column: 生效的列, 当有该参数时，使用指定列作为指标数据结果
        :type effective_column: str
        """
        
        

        self._labels = None
        self._datarows = None
        self._effective_column = None
        self.discriminator = None

        self.labels = labels
        self.datarows = datarows
        if effective_column is not None:
            self.effective_column = effective_column

    @property
    def labels(self):
        r"""Gets the labels of this ShowMetricResultResponseBodyResult.

        指标查询结果表格标题

        :return: The labels of this ShowMetricResultResponseBodyResult.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ShowMetricResultResponseBodyResult.

        指标查询结果表格标题

        :param labels: The labels of this ShowMetricResultResponseBodyResult.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def datarows(self):
        r"""Gets the datarows of this ShowMetricResultResponseBodyResult.

        指标查询结果内容表格

        :return: The datarows of this ShowMetricResultResponseBodyResult.
        :rtype: list[list[object]]
        """
        return self._datarows

    @datarows.setter
    def datarows(self, datarows):
        r"""Sets the datarows of this ShowMetricResultResponseBodyResult.

        指标查询结果内容表格

        :param datarows: The datarows of this ShowMetricResultResponseBodyResult.
        :type datarows: list[list[object]]
        """
        self._datarows = datarows

    @property
    def effective_column(self):
        r"""Gets the effective_column of this ShowMetricResultResponseBodyResult.

        生效的列, 当有该参数时，使用指定列作为指标数据结果

        :return: The effective_column of this ShowMetricResultResponseBodyResult.
        :rtype: str
        """
        return self._effective_column

    @effective_column.setter
    def effective_column(self, effective_column):
        r"""Sets the effective_column of this ShowMetricResultResponseBodyResult.

        生效的列, 当有该参数时，使用指定列作为指标数据结果

        :param effective_column: The effective_column of this ShowMetricResultResponseBodyResult.
        :type effective_column: str
        """
        self._effective_column = effective_column

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
        if not isinstance(other, ShowMetricResultResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
