# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogicalClusterPlanActions:

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
        'type': 'str',
        'strategy': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'strategy': 'strategy'
    }

    def __init__(self, id=None, type=None, strategy=None):
        r"""UpdateLogicalClusterPlanActions

        The model defined in huaweicloud sdk

        :param id: 更新逻辑集群增删行动ID
        :type id: str
        :param type: 更新逻辑集群增删计划行动类型，取值范围为(create|delete)
        :type type: str
        :param strategy: 更新逻辑集群增删计划行为Cron策略表达式
        :type strategy: str
        """
        
        

        self._id = None
        self._type = None
        self._strategy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if strategy is not None:
            self.strategy = strategy

    @property
    def id(self):
        r"""Gets the id of this UpdateLogicalClusterPlanActions.

        更新逻辑集群增删行动ID

        :return: The id of this UpdateLogicalClusterPlanActions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateLogicalClusterPlanActions.

        更新逻辑集群增删行动ID

        :param id: The id of this UpdateLogicalClusterPlanActions.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this UpdateLogicalClusterPlanActions.

        更新逻辑集群增删计划行动类型，取值范围为(create|delete)

        :return: The type of this UpdateLogicalClusterPlanActions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateLogicalClusterPlanActions.

        更新逻辑集群增删计划行动类型，取值范围为(create|delete)

        :param type: The type of this UpdateLogicalClusterPlanActions.
        :type type: str
        """
        self._type = type

    @property
    def strategy(self):
        r"""Gets the strategy of this UpdateLogicalClusterPlanActions.

        更新逻辑集群增删计划行为Cron策略表达式

        :return: The strategy of this UpdateLogicalClusterPlanActions.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this UpdateLogicalClusterPlanActions.

        更新逻辑集群增删计划行为Cron策略表达式

        :param strategy: The strategy of this UpdateLogicalClusterPlanActions.
        :type strategy: str
        """
        self._strategy = strategy

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
        if not isinstance(other, UpdateLogicalClusterPlanActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
