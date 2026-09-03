# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddFullSqlTasksRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_reqs': 'list[QueryReq]'
    }

    attribute_map = {
        'query_reqs': 'query_reqs'
    }

    def __init__(self, query_reqs=None):
        r"""BatchAddFullSqlTasksRequestBody

        The model defined in huaweicloud sdk

        :param query_reqs: SQL解析任务列表
        :type query_reqs: list[:class:`huaweicloudsdkdas.v3.QueryReq`]
        """
        
        

        self._query_reqs = None
        self.discriminator = None

        self.query_reqs = query_reqs

    @property
    def query_reqs(self):
        r"""Gets the query_reqs of this BatchAddFullSqlTasksRequestBody.

        SQL解析任务列表

        :return: The query_reqs of this BatchAddFullSqlTasksRequestBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.QueryReq`]
        """
        return self._query_reqs

    @query_reqs.setter
    def query_reqs(self, query_reqs):
        r"""Sets the query_reqs of this BatchAddFullSqlTasksRequestBody.

        SQL解析任务列表

        :param query_reqs: The query_reqs of this BatchAddFullSqlTasksRequestBody.
        :type query_reqs: list[:class:`huaweicloudsdkdas.v3.QueryReq`]
        """
        self._query_reqs = query_reqs

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
        if not isinstance(other, BatchAddFullSqlTasksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
