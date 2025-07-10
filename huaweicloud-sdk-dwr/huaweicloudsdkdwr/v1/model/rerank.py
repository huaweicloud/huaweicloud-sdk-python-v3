# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rerank:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'strategy': 'str',
        'params': 'dict(str, object)'
    }

    attribute_map = {
        'strategy': 'strategy',
        'params': 'params'
    }

    def __init__(self, strategy=None, params=None):
        r"""Rerank

        The model defined in huaweicloud sdk

        :param strategy: **参数解释：** 重排序的策略名称。 **约束限制：** 不涉及 **取值范围：** &#x60;[\&quot;weighted\&quot;, \&quot;rrf\&quot;]&#x60; 默认取值: \&quot;rrf\&quot;
        :type strategy: str
        :param params: **参数解释：** rerank策略的算法参数。 可以设置的参数： - k：平滑值。（仅对rrf策略生效） - weights：各个向量搜索结果的权值。（仅对weighted策略生效，且当策略为weighted时该参数必填） 重排序的策略名称。 **约束限制：** 不涉及。 **取值范围：** - weights：[0, 1] - k：(0, 16384) **默认取值：** - k：60
        :type params: dict(str, object)
        """
        
        

        self._strategy = None
        self._params = None
        self.discriminator = None

        self.strategy = strategy
        if params is not None:
            self.params = params

    @property
    def strategy(self):
        r"""Gets the strategy of this Rerank.

        **参数解释：** 重排序的策略名称。 **约束限制：** 不涉及 **取值范围：** `[\"weighted\", \"rrf\"]` 默认取值: \"rrf\"

        :return: The strategy of this Rerank.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this Rerank.

        **参数解释：** 重排序的策略名称。 **约束限制：** 不涉及 **取值范围：** `[\"weighted\", \"rrf\"]` 默认取值: \"rrf\"

        :param strategy: The strategy of this Rerank.
        :type strategy: str
        """
        self._strategy = strategy

    @property
    def params(self):
        r"""Gets the params of this Rerank.

        **参数解释：** rerank策略的算法参数。 可以设置的参数： - k：平滑值。（仅对rrf策略生效） - weights：各个向量搜索结果的权值。（仅对weighted策略生效，且当策略为weighted时该参数必填） 重排序的策略名称。 **约束限制：** 不涉及。 **取值范围：** - weights：[0, 1] - k：(0, 16384) **默认取值：** - k：60

        :return: The params of this Rerank.
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this Rerank.

        **参数解释：** rerank策略的算法参数。 可以设置的参数： - k：平滑值。（仅对rrf策略生效） - weights：各个向量搜索结果的权值。（仅对weighted策略生效，且当策略为weighted时该参数必填） 重排序的策略名称。 **约束限制：** 不涉及。 **取值范围：** - weights：[0, 1] - k：(0, 16384) **默认取值：** - k：60

        :param params: The params of this Rerank.
        :type params: dict(str, object)
        """
        self._params = params

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
        if not isinstance(other, Rerank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
