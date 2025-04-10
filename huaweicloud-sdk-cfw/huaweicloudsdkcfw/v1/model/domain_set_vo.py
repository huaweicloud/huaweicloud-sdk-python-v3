# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainSetVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'name': 'str',
        'description': 'str',
        'ref_count': 'int',
        'domain_set_type': 'int',
        'config_status': 'int',
        'rules': 'list[UseRuleVO]'
    }

    attribute_map = {
        'set_id': 'set_id',
        'name': 'name',
        'description': 'description',
        'ref_count': 'ref_count',
        'domain_set_type': 'domain_set_type',
        'config_status': 'config_status',
        'rules': 'rules'
    }

    def __init__(self, set_id=None, name=None, description=None, ref_count=None, domain_set_type=None, config_status=None, rules=None):
        r"""DomainSetVo

        The model defined in huaweicloud sdk

        :param set_id: 域名组id
        :type set_id: str
        :param name: 域名组名称
        :type name: str
        :param description: 域名组描述
        :type description: str
        :param ref_count: 域名组被规则引用次数
        :type ref_count: int
        :param domain_set_type: 域名组类型，0表示应用域名组，1表示网络域名组
        :type domain_set_type: int
        :param config_status: 配置状态，-1表示未配置态，0表示配置失败，1表示配置成功，2表示配置中，3表示正常，4表示配置异常
        :type config_status: int
        :param rules: 使用规则id列表
        :type rules: list[:class:`huaweicloudsdkcfw.v1.UseRuleVO`]
        """
        
        

        self._set_id = None
        self._name = None
        self._description = None
        self._ref_count = None
        self._domain_set_type = None
        self._config_status = None
        self._rules = None
        self.discriminator = None

        if set_id is not None:
            self.set_id = set_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ref_count is not None:
            self.ref_count = ref_count
        if domain_set_type is not None:
            self.domain_set_type = domain_set_type
        if config_status is not None:
            self.config_status = config_status
        if rules is not None:
            self.rules = rules

    @property
    def set_id(self):
        r"""Gets the set_id of this DomainSetVo.

        域名组id

        :return: The set_id of this DomainSetVo.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        r"""Sets the set_id of this DomainSetVo.

        域名组id

        :param set_id: The set_id of this DomainSetVo.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def name(self):
        r"""Gets the name of this DomainSetVo.

        域名组名称

        :return: The name of this DomainSetVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DomainSetVo.

        域名组名称

        :param name: The name of this DomainSetVo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this DomainSetVo.

        域名组描述

        :return: The description of this DomainSetVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DomainSetVo.

        域名组描述

        :param description: The description of this DomainSetVo.
        :type description: str
        """
        self._description = description

    @property
    def ref_count(self):
        r"""Gets the ref_count of this DomainSetVo.

        域名组被规则引用次数

        :return: The ref_count of this DomainSetVo.
        :rtype: int
        """
        return self._ref_count

    @ref_count.setter
    def ref_count(self, ref_count):
        r"""Sets the ref_count of this DomainSetVo.

        域名组被规则引用次数

        :param ref_count: The ref_count of this DomainSetVo.
        :type ref_count: int
        """
        self._ref_count = ref_count

    @property
    def domain_set_type(self):
        r"""Gets the domain_set_type of this DomainSetVo.

        域名组类型，0表示应用域名组，1表示网络域名组

        :return: The domain_set_type of this DomainSetVo.
        :rtype: int
        """
        return self._domain_set_type

    @domain_set_type.setter
    def domain_set_type(self, domain_set_type):
        r"""Sets the domain_set_type of this DomainSetVo.

        域名组类型，0表示应用域名组，1表示网络域名组

        :param domain_set_type: The domain_set_type of this DomainSetVo.
        :type domain_set_type: int
        """
        self._domain_set_type = domain_set_type

    @property
    def config_status(self):
        r"""Gets the config_status of this DomainSetVo.

        配置状态，-1表示未配置态，0表示配置失败，1表示配置成功，2表示配置中，3表示正常，4表示配置异常

        :return: The config_status of this DomainSetVo.
        :rtype: int
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        r"""Sets the config_status of this DomainSetVo.

        配置状态，-1表示未配置态，0表示配置失败，1表示配置成功，2表示配置中，3表示正常，4表示配置异常

        :param config_status: The config_status of this DomainSetVo.
        :type config_status: int
        """
        self._config_status = config_status

    @property
    def rules(self):
        r"""Gets the rules of this DomainSetVo.

        使用规则id列表

        :return: The rules of this DomainSetVo.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.UseRuleVO`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this DomainSetVo.

        使用规则id列表

        :param rules: The rules of this DomainSetVo.
        :type rules: list[:class:`huaweicloudsdkcfw.v1.UseRuleVO`]
        """
        self._rules = rules

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
        if not isinstance(other, DomainSetVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
