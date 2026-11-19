# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeFlavorItemDetail:

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
        'spec_code': 'str',
        'iaas_code': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'supported_ipv6': 'bool',
        'az_status': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'spec_code': 'spec_code',
        'iaas_code': 'iaas_code',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'supported_ipv6': 'supported_ipv6',
        'az_status': 'az_status'
    }

    def __init__(self, id=None, spec_code=None, iaas_code=None, vcpus=None, ram=None, supported_ipv6=None, az_status=None):
        r"""ComputeFlavorItemDetail

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 规格ID。 **取值范围**: 不涉及。
        :type id: str
        :param spec_code: **参数解释**: 规格编码。 **取值范围**: 不涉及。
        :type spec_code: str
        :param iaas_code: **参数解释**: IaaS规格编码。 **取值范围**: 不涉及。
        :type iaas_code: str
        :param vcpus: **参数解释**: CPU核数。 **取值范围**: 不涉及。
        :type vcpus: str
        :param ram: **参数解释**: 内存大小，单位GB。 **取值范围**: 不涉及。
        :type ram: str
        :param supported_ipv6: **参数解释**: 是否支持IPv6。 **取值范围**: - true：支持 - false：不支持
        :type supported_ipv6: bool
        :param az_status: **参数解释**: 规格在各个可用区的状态。 **取值范围**: - normal：正常。 - sellout：已售罄。 - unknown：状态未知。 - unsupported：不支持。 - abandon：已废弃。
        :type az_status: dict(str, str)
        """
        
        

        self._id = None
        self._spec_code = None
        self._iaas_code = None
        self._vcpus = None
        self._ram = None
        self._supported_ipv6 = None
        self._az_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if spec_code is not None:
            self.spec_code = spec_code
        if iaas_code is not None:
            self.iaas_code = iaas_code
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if supported_ipv6 is not None:
            self.supported_ipv6 = supported_ipv6
        if az_status is not None:
            self.az_status = az_status

    @property
    def id(self):
        r"""Gets the id of this ComputeFlavorItemDetail.

        **参数解释**: 规格ID。 **取值范围**: 不涉及。

        :return: The id of this ComputeFlavorItemDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComputeFlavorItemDetail.

        **参数解释**: 规格ID。 **取值范围**: 不涉及。

        :param id: The id of this ComputeFlavorItemDetail.
        :type id: str
        """
        self._id = id

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ComputeFlavorItemDetail.

        **参数解释**: 规格编码。 **取值范围**: 不涉及。

        :return: The spec_code of this ComputeFlavorItemDetail.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ComputeFlavorItemDetail.

        **参数解释**: 规格编码。 **取值范围**: 不涉及。

        :param spec_code: The spec_code of this ComputeFlavorItemDetail.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def iaas_code(self):
        r"""Gets the iaas_code of this ComputeFlavorItemDetail.

        **参数解释**: IaaS规格编码。 **取值范围**: 不涉及。

        :return: The iaas_code of this ComputeFlavorItemDetail.
        :rtype: str
        """
        return self._iaas_code

    @iaas_code.setter
    def iaas_code(self, iaas_code):
        r"""Sets the iaas_code of this ComputeFlavorItemDetail.

        **参数解释**: IaaS规格编码。 **取值范围**: 不涉及。

        :param iaas_code: The iaas_code of this ComputeFlavorItemDetail.
        :type iaas_code: str
        """
        self._iaas_code = iaas_code

    @property
    def vcpus(self):
        r"""Gets the vcpus of this ComputeFlavorItemDetail.

        **参数解释**: CPU核数。 **取值范围**: 不涉及。

        :return: The vcpus of this ComputeFlavorItemDetail.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this ComputeFlavorItemDetail.

        **参数解释**: CPU核数。 **取值范围**: 不涉及。

        :param vcpus: The vcpus of this ComputeFlavorItemDetail.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this ComputeFlavorItemDetail.

        **参数解释**: 内存大小，单位GB。 **取值范围**: 不涉及。

        :return: The ram of this ComputeFlavorItemDetail.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this ComputeFlavorItemDetail.

        **参数解释**: 内存大小，单位GB。 **取值范围**: 不涉及。

        :param ram: The ram of this ComputeFlavorItemDetail.
        :type ram: str
        """
        self._ram = ram

    @property
    def supported_ipv6(self):
        r"""Gets the supported_ipv6 of this ComputeFlavorItemDetail.

        **参数解释**: 是否支持IPv6。 **取值范围**: - true：支持 - false：不支持

        :return: The supported_ipv6 of this ComputeFlavorItemDetail.
        :rtype: bool
        """
        return self._supported_ipv6

    @supported_ipv6.setter
    def supported_ipv6(self, supported_ipv6):
        r"""Sets the supported_ipv6 of this ComputeFlavorItemDetail.

        **参数解释**: 是否支持IPv6。 **取值范围**: - true：支持 - false：不支持

        :param supported_ipv6: The supported_ipv6 of this ComputeFlavorItemDetail.
        :type supported_ipv6: bool
        """
        self._supported_ipv6 = supported_ipv6

    @property
    def az_status(self):
        r"""Gets the az_status of this ComputeFlavorItemDetail.

        **参数解释**: 规格在各个可用区的状态。 **取值范围**: - normal：正常。 - sellout：已售罄。 - unknown：状态未知。 - unsupported：不支持。 - abandon：已废弃。

        :return: The az_status of this ComputeFlavorItemDetail.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        r"""Sets the az_status of this ComputeFlavorItemDetail.

        **参数解释**: 规格在各个可用区的状态。 **取值范围**: - normal：正常。 - sellout：已售罄。 - unknown：状态未知。 - unsupported：不支持。 - abandon：已废弃。

        :param az_status: The az_status of this ComputeFlavorItemDetail.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

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
        if not isinstance(other, ComputeFlavorItemDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
