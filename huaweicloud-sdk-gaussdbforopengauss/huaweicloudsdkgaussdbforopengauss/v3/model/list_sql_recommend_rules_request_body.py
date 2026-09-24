# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlRecommendRulesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recommend_type': 'str',
        'recommend_count': 'int',
        'use_ops_tunnel': 'bool'
    }

    attribute_map = {
        'recommend_type': 'recommend_type',
        'recommend_count': 'recommend_count',
        'use_ops_tunnel': 'use_ops_tunnel'
    }

    def __init__(self, recommend_type=None, recommend_count=None, use_ops_tunnel=None):
        r"""ListSqlRecommendRulesRequestBody

        The model defined in huaweicloud sdk

        :param recommend_type: **参数解释**: 推荐类型。 **约束限制**: 不涉及。 **取值范围**: - all：全部 - exec_count：执行次数 - avg_exec_time：平均执行时间 - max_exec_time：最大执行时间  **默认取值**: all
        :type recommend_type: str
        :param recommend_count: **参数解释**: 推荐规则返回条数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type recommend_count: int
        :param use_ops_tunnel: **参数解释**: 是否使用紧急通道。 **约束限制**: 不涉及。 **取值范围**: - true：开启紧急通道 - false：关闭紧急通道  **默认取值**: false
        :type use_ops_tunnel: bool
        """
        
        

        self._recommend_type = None
        self._recommend_count = None
        self._use_ops_tunnel = None
        self.discriminator = None

        if recommend_type is not None:
            self.recommend_type = recommend_type
        if recommend_count is not None:
            self.recommend_count = recommend_count
        if use_ops_tunnel is not None:
            self.use_ops_tunnel = use_ops_tunnel

    @property
    def recommend_type(self):
        r"""Gets the recommend_type of this ListSqlRecommendRulesRequestBody.

        **参数解释**: 推荐类型。 **约束限制**: 不涉及。 **取值范围**: - all：全部 - exec_count：执行次数 - avg_exec_time：平均执行时间 - max_exec_time：最大执行时间  **默认取值**: all

        :return: The recommend_type of this ListSqlRecommendRulesRequestBody.
        :rtype: str
        """
        return self._recommend_type

    @recommend_type.setter
    def recommend_type(self, recommend_type):
        r"""Sets the recommend_type of this ListSqlRecommendRulesRequestBody.

        **参数解释**: 推荐类型。 **约束限制**: 不涉及。 **取值范围**: - all：全部 - exec_count：执行次数 - avg_exec_time：平均执行时间 - max_exec_time：最大执行时间  **默认取值**: all

        :param recommend_type: The recommend_type of this ListSqlRecommendRulesRequestBody.
        :type recommend_type: str
        """
        self._recommend_type = recommend_type

    @property
    def recommend_count(self):
        r"""Gets the recommend_count of this ListSqlRecommendRulesRequestBody.

        **参数解释**: 推荐规则返回条数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The recommend_count of this ListSqlRecommendRulesRequestBody.
        :rtype: int
        """
        return self._recommend_count

    @recommend_count.setter
    def recommend_count(self, recommend_count):
        r"""Sets the recommend_count of this ListSqlRecommendRulesRequestBody.

        **参数解释**: 推荐规则返回条数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param recommend_count: The recommend_count of this ListSqlRecommendRulesRequestBody.
        :type recommend_count: int
        """
        self._recommend_count = recommend_count

    @property
    def use_ops_tunnel(self):
        r"""Gets the use_ops_tunnel of this ListSqlRecommendRulesRequestBody.

        **参数解释**: 是否使用紧急通道。 **约束限制**: 不涉及。 **取值范围**: - true：开启紧急通道 - false：关闭紧急通道  **默认取值**: false

        :return: The use_ops_tunnel of this ListSqlRecommendRulesRequestBody.
        :rtype: bool
        """
        return self._use_ops_tunnel

    @use_ops_tunnel.setter
    def use_ops_tunnel(self, use_ops_tunnel):
        r"""Sets the use_ops_tunnel of this ListSqlRecommendRulesRequestBody.

        **参数解释**: 是否使用紧急通道。 **约束限制**: 不涉及。 **取值范围**: - true：开启紧急通道 - false：关闭紧急通道  **默认取值**: false

        :param use_ops_tunnel: The use_ops_tunnel of this ListSqlRecommendRulesRequestBody.
        :type use_ops_tunnel: bool
        """
        self._use_ops_tunnel = use_ops_tunnel

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
        if not isinstance(other, ListSqlRecommendRulesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
