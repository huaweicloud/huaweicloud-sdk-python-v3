# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRiskScoreResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'int',
        'risk_num': 'int',
        'risk_server_num': 'int'
    }

    attribute_map = {
        'score': 'score',
        'risk_num': 'risk_num',
        'risk_server_num': 'risk_server_num'
    }

    def __init__(self, score=None, risk_num=None, risk_server_num=None):
        r"""ShowRiskScoreResponse

        The model defined in huaweicloud sdk

        :param score: 安全评分
        :type score: int
        :param risk_num: 安全风险个数
        :type risk_num: int
        :param risk_server_num: 安全风险主机个数
        :type risk_server_num: int
        """
        
        super(ShowRiskScoreResponse, self).__init__()

        self._score = None
        self._risk_num = None
        self._risk_server_num = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if risk_num is not None:
            self.risk_num = risk_num
        if risk_server_num is not None:
            self.risk_server_num = risk_server_num

    @property
    def score(self):
        r"""Gets the score of this ShowRiskScoreResponse.

        安全评分

        :return: The score of this ShowRiskScoreResponse.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this ShowRiskScoreResponse.

        安全评分

        :param score: The score of this ShowRiskScoreResponse.
        :type score: int
        """
        self._score = score

    @property
    def risk_num(self):
        r"""Gets the risk_num of this ShowRiskScoreResponse.

        安全风险个数

        :return: The risk_num of this ShowRiskScoreResponse.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this ShowRiskScoreResponse.

        安全风险个数

        :param risk_num: The risk_num of this ShowRiskScoreResponse.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def risk_server_num(self):
        r"""Gets the risk_server_num of this ShowRiskScoreResponse.

        安全风险主机个数

        :return: The risk_server_num of this ShowRiskScoreResponse.
        :rtype: int
        """
        return self._risk_server_num

    @risk_server_num.setter
    def risk_server_num(self, risk_server_num):
        r"""Sets the risk_server_num of this ShowRiskScoreResponse.

        安全风险主机个数

        :param risk_server_num: The risk_server_num of this ShowRiskScoreResponse.
        :type risk_server_num: int
        """
        self._risk_server_num = risk_server_num

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
        if not isinstance(other, ShowRiskScoreResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
