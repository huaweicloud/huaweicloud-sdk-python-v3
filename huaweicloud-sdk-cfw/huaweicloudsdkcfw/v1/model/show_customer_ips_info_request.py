# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomerIpsInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ips_cfw_id': 'str',
        'object_id': 'str',
        'fw_instance_id': 'str'
    }

    attribute_map = {
        'ips_cfw_id': 'ips_cfw_id',
        'object_id': 'object_id',
        'fw_instance_id': 'fw_instance_id'
    }

    def __init__(self, ips_cfw_id=None, object_id=None, fw_instance_id=None):
        r"""ShowCustomerIpsInfoRequest

        The model defined in huaweicloud sdk

        :param ips_cfw_id: **参数解释**： cfw侧自定义IPS规则id **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type ips_cfw_id: str
        :param object_id: **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type object_id: str
        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        """
        
        

        self._ips_cfw_id = None
        self._object_id = None
        self._fw_instance_id = None
        self.discriminator = None

        self.ips_cfw_id = ips_cfw_id
        self.object_id = object_id
        self.fw_instance_id = fw_instance_id

    @property
    def ips_cfw_id(self):
        r"""Gets the ips_cfw_id of this ShowCustomerIpsInfoRequest.

        **参数解释**： cfw侧自定义IPS规则id **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The ips_cfw_id of this ShowCustomerIpsInfoRequest.
        :rtype: str
        """
        return self._ips_cfw_id

    @ips_cfw_id.setter
    def ips_cfw_id(self, ips_cfw_id):
        r"""Sets the ips_cfw_id of this ShowCustomerIpsInfoRequest.

        **参数解释**： cfw侧自定义IPS规则id **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param ips_cfw_id: The ips_cfw_id of this ShowCustomerIpsInfoRequest.
        :type ips_cfw_id: str
        """
        self._ips_cfw_id = ips_cfw_id

    @property
    def object_id(self):
        r"""Gets the object_id of this ShowCustomerIpsInfoRequest.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The object_id of this ShowCustomerIpsInfoRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ShowCustomerIpsInfoRequest.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param object_id: The object_id of this ShowCustomerIpsInfoRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ShowCustomerIpsInfoRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ShowCustomerIpsInfoRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ShowCustomerIpsInfoRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ShowCustomerIpsInfoRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

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
        if not isinstance(other, ShowCustomerIpsInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
