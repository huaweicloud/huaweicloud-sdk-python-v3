# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RankRiskRuleNew:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'new_rank': 'int'
    }

    attribute_map = {
        'id': 'id',
        'new_rank': 'new_rank'
    }

    def __init__(self, id=None, new_rank=None):
        r"""RankRiskRuleNew

        The model defined in huaweicloud sdk

        :param id: 规则ID
        :type id: str
        :param new_rank: 优先级序号，从1开始越小优先级越高
        :type new_rank: int
        """
        
        

        self._id = None
        self._new_rank = None
        self.discriminator = None

        self.id = id
        self.new_rank = new_rank

    @property
    def id(self):
        r"""Gets the id of this RankRiskRuleNew.

        规则ID

        :return: The id of this RankRiskRuleNew.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RankRiskRuleNew.

        规则ID

        :param id: The id of this RankRiskRuleNew.
        :type id: str
        """
        self._id = id

    @property
    def new_rank(self):
        r"""Gets the new_rank of this RankRiskRuleNew.

        优先级序号，从1开始越小优先级越高

        :return: The new_rank of this RankRiskRuleNew.
        :rtype: int
        """
        return self._new_rank

    @new_rank.setter
    def new_rank(self, new_rank):
        r"""Sets the new_rank of this RankRiskRuleNew.

        优先级序号，从1开始越小优先级越高

        :param new_rank: The new_rank of this RankRiskRuleNew.
        :type new_rank: int
        """
        self._new_rank = new_rank

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
        if not isinstance(other, RankRiskRuleNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
