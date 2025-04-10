# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployStrategyGrayRelease:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'replica_surge_mode': 'str',
        'deployment_mode': 'int',
        'first_batch_weight': 'int',
        'rule_match_mode': 'str',
        'rules': 'list[DeployStrategyGrayReleaseRules]',
        'first_batch_replica': 'int',
        'remaining_batch': 'int'
    }

    attribute_map = {
        'type': 'type',
        'replica_surge_mode': 'replica_surge_mode',
        'deployment_mode': 'deployment_mode',
        'first_batch_weight': 'first_batch_weight',
        'rule_match_mode': 'rule_match_mode',
        'rules': 'rules',
        'first_batch_replica': 'first_batch_replica',
        'remaining_batch': 'remaining_batch'
    }

    def __init__(self, type=None, replica_surge_mode=None, deployment_mode=None, first_batch_weight=None, rule_match_mode=None, rules=None, first_batch_replica=None, remaining_batch=None):
        r"""DeployStrategyGrayRelease

        The model defined in huaweicloud sdk

        :param type: 灰度策略:WEIGHT为基于流量比例，CONTENT为基于内容
        :type type: str
        :param replica_surge_mode: 灰度实例新增模式:MIRROR为蓝绿，EXTRA为金丝雀（先增后减），NOSURGE为金丝雀（先减后增）
        :type replica_surge_mode: str
        :param deployment_mode: 类型1（使用应用网关、微服务引擎）、类型3（注册到微服务中心）、类型4（对接ELB独享型）、类型6（对接ELB共享型）
        :type deployment_mode: int
        :param first_batch_weight: 灰度流量比例(type为WEIGHT时配置)
        :type first_batch_weight: int
        :param rule_match_mode: all满足所有条件，any满足任意条件(type为CONTENT时配置)
        :type rule_match_mode: str
        :param rules: 灰度匹配规则(type为CONTENT时配置)
        :type rules: list[:class:`huaweicloudsdkservicestage.v3.DeployStrategyGrayReleaseRules`]
        :param first_batch_replica: 首批灰度实例数量(replica_surge_mode为金丝雀类型时需要配置)
        :type first_batch_replica: int
        :param remaining_batch: 剩余实例部署批次(replica_surge_mode为金丝雀类型时需要配置)
        :type remaining_batch: int
        """
        
        

        self._type = None
        self._replica_surge_mode = None
        self._deployment_mode = None
        self._first_batch_weight = None
        self._rule_match_mode = None
        self._rules = None
        self._first_batch_replica = None
        self._remaining_batch = None
        self.discriminator = None

        self.type = type
        self.replica_surge_mode = replica_surge_mode
        self.deployment_mode = deployment_mode
        if first_batch_weight is not None:
            self.first_batch_weight = first_batch_weight
        if rule_match_mode is not None:
            self.rule_match_mode = rule_match_mode
        if rules is not None:
            self.rules = rules
        if first_batch_replica is not None:
            self.first_batch_replica = first_batch_replica
        if remaining_batch is not None:
            self.remaining_batch = remaining_batch

    @property
    def type(self):
        r"""Gets the type of this DeployStrategyGrayRelease.

        灰度策略:WEIGHT为基于流量比例，CONTENT为基于内容

        :return: The type of this DeployStrategyGrayRelease.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeployStrategyGrayRelease.

        灰度策略:WEIGHT为基于流量比例，CONTENT为基于内容

        :param type: The type of this DeployStrategyGrayRelease.
        :type type: str
        """
        self._type = type

    @property
    def replica_surge_mode(self):
        r"""Gets the replica_surge_mode of this DeployStrategyGrayRelease.

        灰度实例新增模式:MIRROR为蓝绿，EXTRA为金丝雀（先增后减），NOSURGE为金丝雀（先减后增）

        :return: The replica_surge_mode of this DeployStrategyGrayRelease.
        :rtype: str
        """
        return self._replica_surge_mode

    @replica_surge_mode.setter
    def replica_surge_mode(self, replica_surge_mode):
        r"""Sets the replica_surge_mode of this DeployStrategyGrayRelease.

        灰度实例新增模式:MIRROR为蓝绿，EXTRA为金丝雀（先增后减），NOSURGE为金丝雀（先减后增）

        :param replica_surge_mode: The replica_surge_mode of this DeployStrategyGrayRelease.
        :type replica_surge_mode: str
        """
        self._replica_surge_mode = replica_surge_mode

    @property
    def deployment_mode(self):
        r"""Gets the deployment_mode of this DeployStrategyGrayRelease.

        类型1（使用应用网关、微服务引擎）、类型3（注册到微服务中心）、类型4（对接ELB独享型）、类型6（对接ELB共享型）

        :return: The deployment_mode of this DeployStrategyGrayRelease.
        :rtype: int
        """
        return self._deployment_mode

    @deployment_mode.setter
    def deployment_mode(self, deployment_mode):
        r"""Sets the deployment_mode of this DeployStrategyGrayRelease.

        类型1（使用应用网关、微服务引擎）、类型3（注册到微服务中心）、类型4（对接ELB独享型）、类型6（对接ELB共享型）

        :param deployment_mode: The deployment_mode of this DeployStrategyGrayRelease.
        :type deployment_mode: int
        """
        self._deployment_mode = deployment_mode

    @property
    def first_batch_weight(self):
        r"""Gets the first_batch_weight of this DeployStrategyGrayRelease.

        灰度流量比例(type为WEIGHT时配置)

        :return: The first_batch_weight of this DeployStrategyGrayRelease.
        :rtype: int
        """
        return self._first_batch_weight

    @first_batch_weight.setter
    def first_batch_weight(self, first_batch_weight):
        r"""Sets the first_batch_weight of this DeployStrategyGrayRelease.

        灰度流量比例(type为WEIGHT时配置)

        :param first_batch_weight: The first_batch_weight of this DeployStrategyGrayRelease.
        :type first_batch_weight: int
        """
        self._first_batch_weight = first_batch_weight

    @property
    def rule_match_mode(self):
        r"""Gets the rule_match_mode of this DeployStrategyGrayRelease.

        all满足所有条件，any满足任意条件(type为CONTENT时配置)

        :return: The rule_match_mode of this DeployStrategyGrayRelease.
        :rtype: str
        """
        return self._rule_match_mode

    @rule_match_mode.setter
    def rule_match_mode(self, rule_match_mode):
        r"""Sets the rule_match_mode of this DeployStrategyGrayRelease.

        all满足所有条件，any满足任意条件(type为CONTENT时配置)

        :param rule_match_mode: The rule_match_mode of this DeployStrategyGrayRelease.
        :type rule_match_mode: str
        """
        self._rule_match_mode = rule_match_mode

    @property
    def rules(self):
        r"""Gets the rules of this DeployStrategyGrayRelease.

        灰度匹配规则(type为CONTENT时配置)

        :return: The rules of this DeployStrategyGrayRelease.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.DeployStrategyGrayReleaseRules`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this DeployStrategyGrayRelease.

        灰度匹配规则(type为CONTENT时配置)

        :param rules: The rules of this DeployStrategyGrayRelease.
        :type rules: list[:class:`huaweicloudsdkservicestage.v3.DeployStrategyGrayReleaseRules`]
        """
        self._rules = rules

    @property
    def first_batch_replica(self):
        r"""Gets the first_batch_replica of this DeployStrategyGrayRelease.

        首批灰度实例数量(replica_surge_mode为金丝雀类型时需要配置)

        :return: The first_batch_replica of this DeployStrategyGrayRelease.
        :rtype: int
        """
        return self._first_batch_replica

    @first_batch_replica.setter
    def first_batch_replica(self, first_batch_replica):
        r"""Sets the first_batch_replica of this DeployStrategyGrayRelease.

        首批灰度实例数量(replica_surge_mode为金丝雀类型时需要配置)

        :param first_batch_replica: The first_batch_replica of this DeployStrategyGrayRelease.
        :type first_batch_replica: int
        """
        self._first_batch_replica = first_batch_replica

    @property
    def remaining_batch(self):
        r"""Gets the remaining_batch of this DeployStrategyGrayRelease.

        剩余实例部署批次(replica_surge_mode为金丝雀类型时需要配置)

        :return: The remaining_batch of this DeployStrategyGrayRelease.
        :rtype: int
        """
        return self._remaining_batch

    @remaining_batch.setter
    def remaining_batch(self, remaining_batch):
        r"""Sets the remaining_batch of this DeployStrategyGrayRelease.

        剩余实例部署批次(replica_surge_mode为金丝雀类型时需要配置)

        :param remaining_batch: The remaining_batch of this DeployStrategyGrayRelease.
        :type remaining_batch: int
        """
        self._remaining_batch = remaining_batch

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
        if not isinstance(other, DeployStrategyGrayRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
