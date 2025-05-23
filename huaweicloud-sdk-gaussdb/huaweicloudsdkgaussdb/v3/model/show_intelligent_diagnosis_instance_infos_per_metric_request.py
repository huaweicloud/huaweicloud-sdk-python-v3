# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIntelligentDiagnosisInstanceInfosPerMetricRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'metric_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'metric_name': 'metric_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, metric_name=None, offset=None, limit=None):
        r"""ShowIntelligentDiagnosisInstanceInfosPerMetricRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param metric_name: 指标名。
        :type metric_name: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._x_language = None
        self._metric_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.metric_name = metric_name
        self.offset = offset
        self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.

        指标名。

        :return: The metric_name of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.

        指标名。

        :param metric_name: The metric_name of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def offset(self):
        r"""Gets the offset of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ShowIntelligentDiagnosisInstanceInfosPerMetricRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowIntelligentDiagnosisInstanceInfosPerMetricRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
