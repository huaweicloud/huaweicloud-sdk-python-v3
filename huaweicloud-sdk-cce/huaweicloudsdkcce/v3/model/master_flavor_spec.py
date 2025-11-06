# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasterFlavorSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'azs': 'list[str]',
        'az_fault_domains': 'dict(str, list[str])'
    }

    attribute_map = {
        'name': 'name',
        'azs': 'azs',
        'az_fault_domains': 'azFaultDomains'
    }

    def __init__(self, name=None, azs=None, az_fault_domains=None):
        r"""MasterFlavorSpec

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 控制节点规格 **取值范围**： 不涉及
        :type name: str
        :param azs: **参数解释**： 控制节点支持的可用区
        :type azs: list[str]
        :param az_fault_domains: **参数解释**： 控制节点所在可用区支持的故障域
        :type az_fault_domains: dict(str, list[str])
        """
        
        

        self._name = None
        self._azs = None
        self._az_fault_domains = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if azs is not None:
            self.azs = azs
        if az_fault_domains is not None:
            self.az_fault_domains = az_fault_domains

    @property
    def name(self):
        r"""Gets the name of this MasterFlavorSpec.

        **参数解释**： 控制节点规格 **取值范围**： 不涉及

        :return: The name of this MasterFlavorSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MasterFlavorSpec.

        **参数解释**： 控制节点规格 **取值范围**： 不涉及

        :param name: The name of this MasterFlavorSpec.
        :type name: str
        """
        self._name = name

    @property
    def azs(self):
        r"""Gets the azs of this MasterFlavorSpec.

        **参数解释**： 控制节点支持的可用区

        :return: The azs of this MasterFlavorSpec.
        :rtype: list[str]
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        r"""Sets the azs of this MasterFlavorSpec.

        **参数解释**： 控制节点支持的可用区

        :param azs: The azs of this MasterFlavorSpec.
        :type azs: list[str]
        """
        self._azs = azs

    @property
    def az_fault_domains(self):
        r"""Gets the az_fault_domains of this MasterFlavorSpec.

        **参数解释**： 控制节点所在可用区支持的故障域

        :return: The az_fault_domains of this MasterFlavorSpec.
        :rtype: dict(str, list[str])
        """
        return self._az_fault_domains

    @az_fault_domains.setter
    def az_fault_domains(self, az_fault_domains):
        r"""Sets the az_fault_domains of this MasterFlavorSpec.

        **参数解释**： 控制节点所在可用区支持的故障域

        :param az_fault_domains: The az_fault_domains of this MasterFlavorSpec.
        :type az_fault_domains: dict(str, list[str])
        """
        self._az_fault_domains = az_fault_domains

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
        if not isinstance(other, MasterFlavorSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
