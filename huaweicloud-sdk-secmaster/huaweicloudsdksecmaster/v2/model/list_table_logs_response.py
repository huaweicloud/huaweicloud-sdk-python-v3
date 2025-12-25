# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema': 'list[SearchQueryField]',
        'datarows': 'list[list[object]]',
        'total': 'int',
        'size': 'int',
        'results': 'list[SearchQueryResult]'
    }

    attribute_map = {
        'schema': 'schema',
        'datarows': 'datarows',
        'total': 'total',
        'size': 'size',
        'results': 'results'
    }

    def __init__(self, schema=None, datarows=None, total=None, size=None, results=None):
        r"""ListTableLogsResponse

        The model defined in huaweicloud sdk

        :param schema: 查询结果 schema
        :type schema: list[:class:`huaweicloudsdksecmaster.v2.SearchQueryField`]
        :param datarows: 查询结果行
        :type datarows: list[list[object]]
        :param total: Total count of results
        :type total: int
        :param size: Returned count of results
        :type size: int
        :param results: Results in JSON format
        :type results: list[:class:`huaweicloudsdksecmaster.v2.SearchQueryResult`]
        """
        
        super().__init__()

        self._schema = None
        self._datarows = None
        self._total = None
        self._size = None
        self._results = None
        self.discriminator = None

        if schema is not None:
            self.schema = schema
        if datarows is not None:
            self.datarows = datarows
        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if results is not None:
            self.results = results

    @property
    def schema(self):
        r"""Gets the schema of this ListTableLogsResponse.

        查询结果 schema

        :return: The schema of this ListTableLogsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.SearchQueryField`]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ListTableLogsResponse.

        查询结果 schema

        :param schema: The schema of this ListTableLogsResponse.
        :type schema: list[:class:`huaweicloudsdksecmaster.v2.SearchQueryField`]
        """
        self._schema = schema

    @property
    def datarows(self):
        r"""Gets the datarows of this ListTableLogsResponse.

        查询结果行

        :return: The datarows of this ListTableLogsResponse.
        :rtype: list[list[object]]
        """
        return self._datarows

    @datarows.setter
    def datarows(self, datarows):
        r"""Sets the datarows of this ListTableLogsResponse.

        查询结果行

        :param datarows: The datarows of this ListTableLogsResponse.
        :type datarows: list[list[object]]
        """
        self._datarows = datarows

    @property
    def total(self):
        r"""Gets the total of this ListTableLogsResponse.

        Total count of results

        :return: The total of this ListTableLogsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTableLogsResponse.

        Total count of results

        :param total: The total of this ListTableLogsResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ListTableLogsResponse.

        Returned count of results

        :return: The size of this ListTableLogsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListTableLogsResponse.

        Returned count of results

        :param size: The size of this ListTableLogsResponse.
        :type size: int
        """
        self._size = size

    @property
    def results(self):
        r"""Gets the results of this ListTableLogsResponse.

        Results in JSON format

        :return: The results of this ListTableLogsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.SearchQueryResult`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this ListTableLogsResponse.

        Results in JSON format

        :param results: The results of this ListTableLogsResponse.
        :type results: list[:class:`huaweicloudsdksecmaster.v2.SearchQueryResult`]
        """
        self._results = results

    def to_dict(self):
        import warnings
        warnings.warn("ListTableLogsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTableLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
