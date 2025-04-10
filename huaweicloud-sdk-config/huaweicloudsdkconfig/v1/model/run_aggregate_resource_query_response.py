# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunAggregateResourceQueryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_info': 'QueryInfo',
        'results': 'list[object]'
    }

    attribute_map = {
        'query_info': 'query_info',
        'results': 'results'
    }

    def __init__(self, query_info=None, results=None):
        r"""RunAggregateResourceQueryResponse

        The model defined in huaweicloud sdk

        :param query_info: 
        :type query_info: :class:`huaweicloudsdkconfig.v1.QueryInfo`
        :param results: ResourceQL 查询结果.
        :type results: list[object]
        """
        
        super(RunAggregateResourceQueryResponse, self).__init__()

        self._query_info = None
        self._results = None
        self.discriminator = None

        if query_info is not None:
            self.query_info = query_info
        if results is not None:
            self.results = results

    @property
    def query_info(self):
        r"""Gets the query_info of this RunAggregateResourceQueryResponse.

        :return: The query_info of this RunAggregateResourceQueryResponse.
        :rtype: :class:`huaweicloudsdkconfig.v1.QueryInfo`
        """
        return self._query_info

    @query_info.setter
    def query_info(self, query_info):
        r"""Sets the query_info of this RunAggregateResourceQueryResponse.

        :param query_info: The query_info of this RunAggregateResourceQueryResponse.
        :type query_info: :class:`huaweicloudsdkconfig.v1.QueryInfo`
        """
        self._query_info = query_info

    @property
    def results(self):
        r"""Gets the results of this RunAggregateResourceQueryResponse.

        ResourceQL 查询结果.

        :return: The results of this RunAggregateResourceQueryResponse.
        :rtype: list[object]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this RunAggregateResourceQueryResponse.

        ResourceQL 查询结果.

        :param results: The results of this RunAggregateResourceQueryResponse.
        :type results: list[object]
        """
        self._results = results

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
        if not isinstance(other, RunAggregateResourceQueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
