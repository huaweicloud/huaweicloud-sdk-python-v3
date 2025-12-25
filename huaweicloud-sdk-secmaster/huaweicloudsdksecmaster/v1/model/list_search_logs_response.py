# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSearchLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'analysis_results': 'AnalysisResults',
        'count': 'int',
        'results': 'list[SearchResult]'
    }

    attribute_map = {
        'analysis_results': 'analysis_results',
        'count': 'count',
        'results': 'results'
    }

    def __init__(self, analysis_results=None, count=None, results=None):
        r"""ListSearchLogsResponse

        The model defined in huaweicloud sdk

        :param analysis_results: 
        :type analysis_results: :class:`huaweicloudsdksecmaster.v1.AnalysisResults`
        :param count: 查询结果的条数
        :type count: int
        :param results: 返回的查询结果
        :type results: list[:class:`huaweicloudsdksecmaster.v1.SearchResult`]
        """
        
        super().__init__()

        self._analysis_results = None
        self._count = None
        self._results = None
        self.discriminator = None

        if analysis_results is not None:
            self.analysis_results = analysis_results
        if count is not None:
            self.count = count
        if results is not None:
            self.results = results

    @property
    def analysis_results(self):
        r"""Gets the analysis_results of this ListSearchLogsResponse.

        :return: The analysis_results of this ListSearchLogsResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.AnalysisResults`
        """
        return self._analysis_results

    @analysis_results.setter
    def analysis_results(self, analysis_results):
        r"""Sets the analysis_results of this ListSearchLogsResponse.

        :param analysis_results: The analysis_results of this ListSearchLogsResponse.
        :type analysis_results: :class:`huaweicloudsdksecmaster.v1.AnalysisResults`
        """
        self._analysis_results = analysis_results

    @property
    def count(self):
        r"""Gets the count of this ListSearchLogsResponse.

        查询结果的条数

        :return: The count of this ListSearchLogsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSearchLogsResponse.

        查询结果的条数

        :param count: The count of this ListSearchLogsResponse.
        :type count: int
        """
        self._count = count

    @property
    def results(self):
        r"""Gets the results of this ListSearchLogsResponse.

        返回的查询结果

        :return: The results of this ListSearchLogsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.SearchResult`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this ListSearchLogsResponse.

        返回的查询结果

        :param results: The results of this ListSearchLogsResponse.
        :type results: list[:class:`huaweicloudsdksecmaster.v1.SearchResult`]
        """
        self._results = results

    def to_dict(self):
        import warnings
        warnings.warn("ListSearchLogsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSearchLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
