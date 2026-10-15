# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataFilterRulesResultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'query_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'query_id': 'query_id',
        'x_language': 'X-Language'
    }

    def __init__(self, job_id=None, query_id=None, x_language=None):
        r"""ShowDataFilterRulesResultRequest

        The model defined in huaweicloud sdk

        :param job_id: 数据迁移任务ID，用于指定要查询过滤规则的目标任务。
        :type job_id: str
        :param query_id: 查询数据过滤规则结果请求ID，用于关联之前提交的查询过滤校验请求。
        :type query_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._job_id = None
        self._query_id = None
        self._x_language = None
        self.discriminator = None

        self.job_id = job_id
        if query_id is not None:
            self.query_id = query_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowDataFilterRulesResultRequest.

        数据迁移任务ID，用于指定要查询过滤规则的目标任务。

        :return: The job_id of this ShowDataFilterRulesResultRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowDataFilterRulesResultRequest.

        数据迁移任务ID，用于指定要查询过滤规则的目标任务。

        :param job_id: The job_id of this ShowDataFilterRulesResultRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def query_id(self):
        r"""Gets the query_id of this ShowDataFilterRulesResultRequest.

        查询数据过滤规则结果请求ID，用于关联之前提交的查询过滤校验请求。

        :return: The query_id of this ShowDataFilterRulesResultRequest.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this ShowDataFilterRulesResultRequest.

        查询数据过滤规则结果请求ID，用于关联之前提交的查询过滤校验请求。

        :param query_id: The query_id of this ShowDataFilterRulesResultRequest.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowDataFilterRulesResultRequest.

        请求语言类型。

        :return: The x_language of this ShowDataFilterRulesResultRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowDataFilterRulesResultRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowDataFilterRulesResultRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowDataFilterRulesResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
