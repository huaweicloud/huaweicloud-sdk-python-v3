# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddRuleAclDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'type': 'int',
        'rules': 'list[AddRuleAclDtoRules]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'type': 'type',
        'rules': 'rules'
    }

    def __init__(self, object_id=None, type=None, rules=None):
        r"""AddRuleAclDto

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得
        :type object_id: str
        :param type: 规则类型，0：互联网边界规则，1：vpc间规则，2：nat规则，当type取0时，规则源和目的地址需要为公网ip或域名，vpc间规则需要源和目的地址为私有ip，nat规则需要源地址为私网ip，目的地址为公网ip或域名。
        :type type: int
        :param rules: 添加规则请求规则列表
        :type rules: list[:class:`huaweicloudsdkcfw.v1.AddRuleAclDtoRules`]
        """
        
        

        self._object_id = None
        self._type = None
        self._rules = None
        self.discriminator = None

        self.object_id = object_id
        self.type = type
        self.rules = rules

    @property
    def object_id(self):
        r"""Gets the object_id of this AddRuleAclDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :return: The object_id of this AddRuleAclDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this AddRuleAclDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :param object_id: The object_id of this AddRuleAclDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def type(self):
        r"""Gets the type of this AddRuleAclDto.

        规则类型，0：互联网边界规则，1：vpc间规则，2：nat规则，当type取0时，规则源和目的地址需要为公网ip或域名，vpc间规则需要源和目的地址为私有ip，nat规则需要源地址为私网ip，目的地址为公网ip或域名。

        :return: The type of this AddRuleAclDto.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddRuleAclDto.

        规则类型，0：互联网边界规则，1：vpc间规则，2：nat规则，当type取0时，规则源和目的地址需要为公网ip或域名，vpc间规则需要源和目的地址为私有ip，nat规则需要源地址为私网ip，目的地址为公网ip或域名。

        :param type: The type of this AddRuleAclDto.
        :type type: int
        """
        self._type = type

    @property
    def rules(self):
        r"""Gets the rules of this AddRuleAclDto.

        添加规则请求规则列表

        :return: The rules of this AddRuleAclDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AddRuleAclDtoRules`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this AddRuleAclDto.

        添加规则请求规则列表

        :param rules: The rules of this AddRuleAclDto.
        :type rules: list[:class:`huaweicloudsdkcfw.v1.AddRuleAclDtoRules`]
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
        if not isinstance(other, AddRuleAclDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
