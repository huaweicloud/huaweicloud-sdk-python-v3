# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulnDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vulnerability_id': 'str',
        'description': 'str',
        'rule_ids': 'list[str]',
        'create_time': 'int'
    }

    attribute_map = {
        'vulnerability_id': 'vulnerability_id',
        'description': 'description',
        'rule_ids': 'rule_ids',
        'create_time': 'create_time'
    }

    def __init__(self, vulnerability_id=None, description=None, rule_ids=None, create_time=None):
        r"""VulnDto

        The model defined in huaweicloud sdk

        :param vulnerability_id: 漏洞编号
        :type vulnerability_id: str
        :param description: 漏洞描述
        :type description: str
        :param rule_ids: 可防护的规则ID列表
        :type rule_ids: list[str]
        :param create_time: 漏洞情报创建时间
        :type create_time: int
        """
        
        

        self._vulnerability_id = None
        self._description = None
        self._rule_ids = None
        self._create_time = None
        self.discriminator = None

        if vulnerability_id is not None:
            self.vulnerability_id = vulnerability_id
        if description is not None:
            self.description = description
        if rule_ids is not None:
            self.rule_ids = rule_ids
        if create_time is not None:
            self.create_time = create_time

    @property
    def vulnerability_id(self):
        r"""Gets the vulnerability_id of this VulnDto.

        漏洞编号

        :return: The vulnerability_id of this VulnDto.
        :rtype: str
        """
        return self._vulnerability_id

    @vulnerability_id.setter
    def vulnerability_id(self, vulnerability_id):
        r"""Sets the vulnerability_id of this VulnDto.

        漏洞编号

        :param vulnerability_id: The vulnerability_id of this VulnDto.
        :type vulnerability_id: str
        """
        self._vulnerability_id = vulnerability_id

    @property
    def description(self):
        r"""Gets the description of this VulnDto.

        漏洞描述

        :return: The description of this VulnDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VulnDto.

        漏洞描述

        :param description: The description of this VulnDto.
        :type description: str
        """
        self._description = description

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this VulnDto.

        可防护的规则ID列表

        :return: The rule_ids of this VulnDto.
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this VulnDto.

        可防护的规则ID列表

        :param rule_ids: The rule_ids of this VulnDto.
        :type rule_ids: list[str]
        """
        self._rule_ids = rule_ids

    @property
    def create_time(self):
        r"""Gets the create_time of this VulnDto.

        漏洞情报创建时间

        :return: The create_time of this VulnDto.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this VulnDto.

        漏洞情报创建时间

        :param create_time: The create_time of this VulnDto.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, VulnDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
