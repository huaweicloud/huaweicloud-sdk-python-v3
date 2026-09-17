# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRiskTrendRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        '_from': 'int',
        'to': 'int',
        'metric_code': 'str'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        '_from': 'from',
        'to': 'to',
        'metric_code': 'metric_code'
    }

    def __init__(self, engine_type=None, _from=None, to=None, metric_code=None):
        r"""ShowRiskTrendRequest

        The model defined in huaweicloud sdk

        :param engine_type: 数据库类型
        :type engine_type: str
        :param _from: 开始时间（Unix timestamp，毫秒）
        :type _from: int
        :param to: 结束时间（Unix timestamp，毫秒）
        :type to: int
        :param metric_code: 指标码
        :type metric_code: str
        """
        
        

        self._engine_type = None
        self.__from = None
        self._to = None
        self._metric_code = None
        self.discriminator = None

        self.engine_type = engine_type
        self._from = _from
        self.to = to
        self.metric_code = metric_code

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowRiskTrendRequest.

        数据库类型

        :return: The engine_type of this ShowRiskTrendRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowRiskTrendRequest.

        数据库类型

        :param engine_type: The engine_type of this ShowRiskTrendRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def _from(self):
        r"""Gets the _from of this ShowRiskTrendRequest.

        开始时间（Unix timestamp，毫秒）

        :return: The _from of this ShowRiskTrendRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowRiskTrendRequest.

        开始时间（Unix timestamp，毫秒）

        :param _from: The _from of this ShowRiskTrendRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ShowRiskTrendRequest.

        结束时间（Unix timestamp，毫秒）

        :return: The to of this ShowRiskTrendRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ShowRiskTrendRequest.

        结束时间（Unix timestamp，毫秒）

        :param to: The to of this ShowRiskTrendRequest.
        :type to: int
        """
        self._to = to

    @property
    def metric_code(self):
        r"""Gets the metric_code of this ShowRiskTrendRequest.

        指标码

        :return: The metric_code of this ShowRiskTrendRequest.
        :rtype: str
        """
        return self._metric_code

    @metric_code.setter
    def metric_code(self, metric_code):
        r"""Sets the metric_code of this ShowRiskTrendRequest.

        指标码

        :param metric_code: The metric_code of this ShowRiskTrendRequest.
        :type metric_code: str
        """
        self._metric_code = metric_code

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
        if not isinstance(other, ShowRiskTrendRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
