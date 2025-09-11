# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseRiskStatisticsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_id': 'str',
        'db_ip': 'str',
        'db_name': 'str',
        'high_risk': 'int',
        'instance_id': 'str',
        'instance_name': 'str',
        'low_risk': 'int',
        'medium_risk': 'int',
        'risk_rule': 'list[RiskRuleStatistic]',
        'total_risk': 'int'
    }

    attribute_map = {
        'db_id': 'db_id',
        'db_ip': 'db_ip',
        'db_name': 'db_name',
        'high_risk': 'high_risk',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'low_risk': 'low_risk',
        'medium_risk': 'medium_risk',
        'risk_rule': 'risk_rule',
        'total_risk': 'total_risk'
    }

    def __init__(self, db_id=None, db_ip=None, db_name=None, high_risk=None, instance_id=None, instance_name=None, low_risk=None, medium_risk=None, risk_rule=None, total_risk=None):
        r"""DatabaseRiskStatisticsDto

        The model defined in huaweicloud sdk

        :param db_id: 数据库ID
        :type db_id: str
        :param db_ip: 数据库IP
        :type db_ip: str
        :param db_name: 数据库名称
        :type db_name: str
        :param high_risk: 高风险总量
        :type high_risk: int
        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param low_risk: 低风险总量
        :type low_risk: int
        :param medium_risk: 中风险总量
        :type medium_risk: int
        :param risk_rule: 风险规则统计
        :type risk_rule: list[:class:`huaweicloudsdkdbss.v1.RiskRuleStatistic`]
        :param total_risk: 总风险数量
        :type total_risk: int
        """
        
        

        self._db_id = None
        self._db_ip = None
        self._db_name = None
        self._high_risk = None
        self._instance_id = None
        self._instance_name = None
        self._low_risk = None
        self._medium_risk = None
        self._risk_rule = None
        self._total_risk = None
        self.discriminator = None

        if db_id is not None:
            self.db_id = db_id
        if db_ip is not None:
            self.db_ip = db_ip
        if db_name is not None:
            self.db_name = db_name
        if high_risk is not None:
            self.high_risk = high_risk
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if low_risk is not None:
            self.low_risk = low_risk
        if medium_risk is not None:
            self.medium_risk = medium_risk
        if risk_rule is not None:
            self.risk_rule = risk_rule
        if total_risk is not None:
            self.total_risk = total_risk

    @property
    def db_id(self):
        r"""Gets the db_id of this DatabaseRiskStatisticsDto.

        数据库ID

        :return: The db_id of this DatabaseRiskStatisticsDto.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this DatabaseRiskStatisticsDto.

        数据库ID

        :param db_id: The db_id of this DatabaseRiskStatisticsDto.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def db_ip(self):
        r"""Gets the db_ip of this DatabaseRiskStatisticsDto.

        数据库IP

        :return: The db_ip of this DatabaseRiskStatisticsDto.
        :rtype: str
        """
        return self._db_ip

    @db_ip.setter
    def db_ip(self, db_ip):
        r"""Sets the db_ip of this DatabaseRiskStatisticsDto.

        数据库IP

        :param db_ip: The db_ip of this DatabaseRiskStatisticsDto.
        :type db_ip: str
        """
        self._db_ip = db_ip

    @property
    def db_name(self):
        r"""Gets the db_name of this DatabaseRiskStatisticsDto.

        数据库名称

        :return: The db_name of this DatabaseRiskStatisticsDto.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this DatabaseRiskStatisticsDto.

        数据库名称

        :param db_name: The db_name of this DatabaseRiskStatisticsDto.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def high_risk(self):
        r"""Gets the high_risk of this DatabaseRiskStatisticsDto.

        高风险总量

        :return: The high_risk of this DatabaseRiskStatisticsDto.
        :rtype: int
        """
        return self._high_risk

    @high_risk.setter
    def high_risk(self, high_risk):
        r"""Sets the high_risk of this DatabaseRiskStatisticsDto.

        高风险总量

        :param high_risk: The high_risk of this DatabaseRiskStatisticsDto.
        :type high_risk: int
        """
        self._high_risk = high_risk

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DatabaseRiskStatisticsDto.

        实例ID

        :return: The instance_id of this DatabaseRiskStatisticsDto.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DatabaseRiskStatisticsDto.

        实例ID

        :param instance_id: The instance_id of this DatabaseRiskStatisticsDto.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DatabaseRiskStatisticsDto.

        实例名称

        :return: The instance_name of this DatabaseRiskStatisticsDto.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DatabaseRiskStatisticsDto.

        实例名称

        :param instance_name: The instance_name of this DatabaseRiskStatisticsDto.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def low_risk(self):
        r"""Gets the low_risk of this DatabaseRiskStatisticsDto.

        低风险总量

        :return: The low_risk of this DatabaseRiskStatisticsDto.
        :rtype: int
        """
        return self._low_risk

    @low_risk.setter
    def low_risk(self, low_risk):
        r"""Sets the low_risk of this DatabaseRiskStatisticsDto.

        低风险总量

        :param low_risk: The low_risk of this DatabaseRiskStatisticsDto.
        :type low_risk: int
        """
        self._low_risk = low_risk

    @property
    def medium_risk(self):
        r"""Gets the medium_risk of this DatabaseRiskStatisticsDto.

        中风险总量

        :return: The medium_risk of this DatabaseRiskStatisticsDto.
        :rtype: int
        """
        return self._medium_risk

    @medium_risk.setter
    def medium_risk(self, medium_risk):
        r"""Sets the medium_risk of this DatabaseRiskStatisticsDto.

        中风险总量

        :param medium_risk: The medium_risk of this DatabaseRiskStatisticsDto.
        :type medium_risk: int
        """
        self._medium_risk = medium_risk

    @property
    def risk_rule(self):
        r"""Gets the risk_rule of this DatabaseRiskStatisticsDto.

        风险规则统计

        :return: The risk_rule of this DatabaseRiskStatisticsDto.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.RiskRuleStatistic`]
        """
        return self._risk_rule

    @risk_rule.setter
    def risk_rule(self, risk_rule):
        r"""Sets the risk_rule of this DatabaseRiskStatisticsDto.

        风险规则统计

        :param risk_rule: The risk_rule of this DatabaseRiskStatisticsDto.
        :type risk_rule: list[:class:`huaweicloudsdkdbss.v1.RiskRuleStatistic`]
        """
        self._risk_rule = risk_rule

    @property
    def total_risk(self):
        r"""Gets the total_risk of this DatabaseRiskStatisticsDto.

        总风险数量

        :return: The total_risk of this DatabaseRiskStatisticsDto.
        :rtype: int
        """
        return self._total_risk

    @total_risk.setter
    def total_risk(self, total_risk):
        r"""Sets the total_risk of this DatabaseRiskStatisticsDto.

        总风险数量

        :param total_risk: The total_risk of this DatabaseRiskStatisticsDto.
        :type total_risk: int
        """
        self._total_risk = total_risk

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
        if not isinstance(other, DatabaseRiskStatisticsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
