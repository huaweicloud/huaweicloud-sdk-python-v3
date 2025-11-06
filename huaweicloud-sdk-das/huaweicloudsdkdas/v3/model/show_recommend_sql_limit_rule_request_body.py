# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecommendSqlLimitRuleRequestBody:

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
        'rds_recommendation_type': 'str',
        'taurus_recommendation_type': 'str',
        'recommend_count': 'int',
        'node_id': 'str'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'rds_recommendation_type': 'rds_recommendation_type',
        'taurus_recommendation_type': 'taurus_recommendation_type',
        'recommend_count': 'recommend_count',
        'node_id': 'node_id'
    }

    def __init__(self, engine_type=None, rds_recommendation_type=None, taurus_recommendation_type=None, recommend_count=None, node_id=None):
        r"""ShowRecommendSqlLimitRuleRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 引擎类型，目前只支持mysql或者taurus
        :type engine_type: str
        :param rds_recommendation_type: 如果是rds类型， 那么可以选择&#39;count&#39;, &#39;average_time&#39;, &#39;max_time&#39;, &#39;all&#39;这几种类型
        :type rds_recommendation_type: str
        :param taurus_recommendation_type: 如果选择了taurus类型，那么可以选择&#39;count&#39;, &#39;avg_time&#39;
        :type taurus_recommendation_type: str
        :param recommend_count: 推荐数量
        :type recommend_count: int
        :param node_id: 如果选择了taurus， 那么需要制定node id
        :type node_id: str
        """
        
        

        self._engine_type = None
        self._rds_recommendation_type = None
        self._taurus_recommendation_type = None
        self._recommend_count = None
        self._node_id = None
        self.discriminator = None

        if engine_type is not None:
            self.engine_type = engine_type
        if rds_recommendation_type is not None:
            self.rds_recommendation_type = rds_recommendation_type
        if taurus_recommendation_type is not None:
            self.taurus_recommendation_type = taurus_recommendation_type
        if recommend_count is not None:
            self.recommend_count = recommend_count
        if node_id is not None:
            self.node_id = node_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowRecommendSqlLimitRuleRequestBody.

        引擎类型，目前只支持mysql或者taurus

        :return: The engine_type of this ShowRecommendSqlLimitRuleRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowRecommendSqlLimitRuleRequestBody.

        引擎类型，目前只支持mysql或者taurus

        :param engine_type: The engine_type of this ShowRecommendSqlLimitRuleRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def rds_recommendation_type(self):
        r"""Gets the rds_recommendation_type of this ShowRecommendSqlLimitRuleRequestBody.

        如果是rds类型， 那么可以选择'count', 'average_time', 'max_time', 'all'这几种类型

        :return: The rds_recommendation_type of this ShowRecommendSqlLimitRuleRequestBody.
        :rtype: str
        """
        return self._rds_recommendation_type

    @rds_recommendation_type.setter
    def rds_recommendation_type(self, rds_recommendation_type):
        r"""Sets the rds_recommendation_type of this ShowRecommendSqlLimitRuleRequestBody.

        如果是rds类型， 那么可以选择'count', 'average_time', 'max_time', 'all'这几种类型

        :param rds_recommendation_type: The rds_recommendation_type of this ShowRecommendSqlLimitRuleRequestBody.
        :type rds_recommendation_type: str
        """
        self._rds_recommendation_type = rds_recommendation_type

    @property
    def taurus_recommendation_type(self):
        r"""Gets the taurus_recommendation_type of this ShowRecommendSqlLimitRuleRequestBody.

        如果选择了taurus类型，那么可以选择'count', 'avg_time'

        :return: The taurus_recommendation_type of this ShowRecommendSqlLimitRuleRequestBody.
        :rtype: str
        """
        return self._taurus_recommendation_type

    @taurus_recommendation_type.setter
    def taurus_recommendation_type(self, taurus_recommendation_type):
        r"""Sets the taurus_recommendation_type of this ShowRecommendSqlLimitRuleRequestBody.

        如果选择了taurus类型，那么可以选择'count', 'avg_time'

        :param taurus_recommendation_type: The taurus_recommendation_type of this ShowRecommendSqlLimitRuleRequestBody.
        :type taurus_recommendation_type: str
        """
        self._taurus_recommendation_type = taurus_recommendation_type

    @property
    def recommend_count(self):
        r"""Gets the recommend_count of this ShowRecommendSqlLimitRuleRequestBody.

        推荐数量

        :return: The recommend_count of this ShowRecommendSqlLimitRuleRequestBody.
        :rtype: int
        """
        return self._recommend_count

    @recommend_count.setter
    def recommend_count(self, recommend_count):
        r"""Sets the recommend_count of this ShowRecommendSqlLimitRuleRequestBody.

        推荐数量

        :param recommend_count: The recommend_count of this ShowRecommendSqlLimitRuleRequestBody.
        :type recommend_count: int
        """
        self._recommend_count = recommend_count

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowRecommendSqlLimitRuleRequestBody.

        如果选择了taurus， 那么需要制定node id

        :return: The node_id of this ShowRecommendSqlLimitRuleRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowRecommendSqlLimitRuleRequestBody.

        如果选择了taurus， 那么需要制定node id

        :param node_id: The node_id of this ShowRecommendSqlLimitRuleRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, ShowRecommendSqlLimitRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
