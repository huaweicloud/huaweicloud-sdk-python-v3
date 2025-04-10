# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineCreateReqFlavorType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_flavor': 'list[str]',
        'flavor': 'str',
        'available_prefix': 'str',
        'available_cpu_memory': 'str',
        'spec_type': 'str',
        'linear': 'bool',
        'license_amount': 'int',
        'node_limit': 'str',
        'id': 'str',
        'micro_gateway_flavor': 'str',
        'disable': 'bool',
        'spec': 'str',
        'cloud_service_type': 'str',
        'currentflavor': 'str'
    }

    attribute_map = {
        'node_flavor': 'nodeFlavor',
        'flavor': 'flavor',
        'available_prefix': 'availablePrefix',
        'available_cpu_memory': 'availableCpuMemory',
        'spec_type': 'specType',
        'linear': 'linear',
        'license_amount': 'licenseAmount',
        'node_limit': 'nodeLimit',
        'id': 'id',
        'micro_gateway_flavor': 'microGatewayFlavor',
        'disable': 'disable',
        'spec': 'spec',
        'cloud_service_type': 'cloudServiceType',
        'currentflavor': 'currentflavor'
    }

    def __init__(self, node_flavor=None, flavor=None, available_prefix=None, available_cpu_memory=None, spec_type=None, linear=None, license_amount=None, node_limit=None, id=None, micro_gateway_flavor=None, disable=None, spec=None, cloud_service_type=None, currentflavor=None):
        r"""EngineCreateReqFlavorType

        The model defined in huaweicloud sdk

        :param node_flavor: 网关节点规格
        :type node_flavor: list[str]
        :param flavor: 网关规格
        :type flavor: str
        :param available_prefix: 可用区前缀
        :type available_prefix: str
        :param available_cpu_memory: 可用区CPU内存
        :type available_cpu_memory: str
        :param spec_type: 引擎类型
        :type spec_type: str
        :param linear: 是否为线性
        :type linear: bool
        :param license_amount: 网关证书规模
        :type license_amount: int
        :param node_limit: 网关节点数限制
        :type node_limit: str
        :param id: 网关规格id
        :type id: str
        :param micro_gateway_flavor: 网关规格
        :type micro_gateway_flavor: str
        :param disable: 网关是否禁用
        :type disable: bool
        :param spec: 网关节点类型
        :type spec: str
        :param cloud_service_type: 云服务类型
        :type cloud_service_type: str
        :param currentflavor: 当前规格
        :type currentflavor: str
        """
        
        

        self._node_flavor = None
        self._flavor = None
        self._available_prefix = None
        self._available_cpu_memory = None
        self._spec_type = None
        self._linear = None
        self._license_amount = None
        self._node_limit = None
        self._id = None
        self._micro_gateway_flavor = None
        self._disable = None
        self._spec = None
        self._cloud_service_type = None
        self._currentflavor = None
        self.discriminator = None

        if node_flavor is not None:
            self.node_flavor = node_flavor
        if flavor is not None:
            self.flavor = flavor
        if available_prefix is not None:
            self.available_prefix = available_prefix
        if available_cpu_memory is not None:
            self.available_cpu_memory = available_cpu_memory
        if spec_type is not None:
            self.spec_type = spec_type
        if linear is not None:
            self.linear = linear
        if license_amount is not None:
            self.license_amount = license_amount
        if node_limit is not None:
            self.node_limit = node_limit
        if id is not None:
            self.id = id
        if micro_gateway_flavor is not None:
            self.micro_gateway_flavor = micro_gateway_flavor
        if disable is not None:
            self.disable = disable
        if spec is not None:
            self.spec = spec
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if currentflavor is not None:
            self.currentflavor = currentflavor

    @property
    def node_flavor(self):
        r"""Gets the node_flavor of this EngineCreateReqFlavorType.

        网关节点规格

        :return: The node_flavor of this EngineCreateReqFlavorType.
        :rtype: list[str]
        """
        return self._node_flavor

    @node_flavor.setter
    def node_flavor(self, node_flavor):
        r"""Sets the node_flavor of this EngineCreateReqFlavorType.

        网关节点规格

        :param node_flavor: The node_flavor of this EngineCreateReqFlavorType.
        :type node_flavor: list[str]
        """
        self._node_flavor = node_flavor

    @property
    def flavor(self):
        r"""Gets the flavor of this EngineCreateReqFlavorType.

        网关规格

        :return: The flavor of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this EngineCreateReqFlavorType.

        网关规格

        :param flavor: The flavor of this EngineCreateReqFlavorType.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def available_prefix(self):
        r"""Gets the available_prefix of this EngineCreateReqFlavorType.

        可用区前缀

        :return: The available_prefix of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._available_prefix

    @available_prefix.setter
    def available_prefix(self, available_prefix):
        r"""Sets the available_prefix of this EngineCreateReqFlavorType.

        可用区前缀

        :param available_prefix: The available_prefix of this EngineCreateReqFlavorType.
        :type available_prefix: str
        """
        self._available_prefix = available_prefix

    @property
    def available_cpu_memory(self):
        r"""Gets the available_cpu_memory of this EngineCreateReqFlavorType.

        可用区CPU内存

        :return: The available_cpu_memory of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._available_cpu_memory

    @available_cpu_memory.setter
    def available_cpu_memory(self, available_cpu_memory):
        r"""Sets the available_cpu_memory of this EngineCreateReqFlavorType.

        可用区CPU内存

        :param available_cpu_memory: The available_cpu_memory of this EngineCreateReqFlavorType.
        :type available_cpu_memory: str
        """
        self._available_cpu_memory = available_cpu_memory

    @property
    def spec_type(self):
        r"""Gets the spec_type of this EngineCreateReqFlavorType.

        引擎类型

        :return: The spec_type of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        r"""Sets the spec_type of this EngineCreateReqFlavorType.

        引擎类型

        :param spec_type: The spec_type of this EngineCreateReqFlavorType.
        :type spec_type: str
        """
        self._spec_type = spec_type

    @property
    def linear(self):
        r"""Gets the linear of this EngineCreateReqFlavorType.

        是否为线性

        :return: The linear of this EngineCreateReqFlavorType.
        :rtype: bool
        """
        return self._linear

    @linear.setter
    def linear(self, linear):
        r"""Sets the linear of this EngineCreateReqFlavorType.

        是否为线性

        :param linear: The linear of this EngineCreateReqFlavorType.
        :type linear: bool
        """
        self._linear = linear

    @property
    def license_amount(self):
        r"""Gets the license_amount of this EngineCreateReqFlavorType.

        网关证书规模

        :return: The license_amount of this EngineCreateReqFlavorType.
        :rtype: int
        """
        return self._license_amount

    @license_amount.setter
    def license_amount(self, license_amount):
        r"""Sets the license_amount of this EngineCreateReqFlavorType.

        网关证书规模

        :param license_amount: The license_amount of this EngineCreateReqFlavorType.
        :type license_amount: int
        """
        self._license_amount = license_amount

    @property
    def node_limit(self):
        r"""Gets the node_limit of this EngineCreateReqFlavorType.

        网关节点数限制

        :return: The node_limit of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._node_limit

    @node_limit.setter
    def node_limit(self, node_limit):
        r"""Sets the node_limit of this EngineCreateReqFlavorType.

        网关节点数限制

        :param node_limit: The node_limit of this EngineCreateReqFlavorType.
        :type node_limit: str
        """
        self._node_limit = node_limit

    @property
    def id(self):
        r"""Gets the id of this EngineCreateReqFlavorType.

        网关规格id

        :return: The id of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EngineCreateReqFlavorType.

        网关规格id

        :param id: The id of this EngineCreateReqFlavorType.
        :type id: str
        """
        self._id = id

    @property
    def micro_gateway_flavor(self):
        r"""Gets the micro_gateway_flavor of this EngineCreateReqFlavorType.

        网关规格

        :return: The micro_gateway_flavor of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._micro_gateway_flavor

    @micro_gateway_flavor.setter
    def micro_gateway_flavor(self, micro_gateway_flavor):
        r"""Sets the micro_gateway_flavor of this EngineCreateReqFlavorType.

        网关规格

        :param micro_gateway_flavor: The micro_gateway_flavor of this EngineCreateReqFlavorType.
        :type micro_gateway_flavor: str
        """
        self._micro_gateway_flavor = micro_gateway_flavor

    @property
    def disable(self):
        r"""Gets the disable of this EngineCreateReqFlavorType.

        网关是否禁用

        :return: The disable of this EngineCreateReqFlavorType.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this EngineCreateReqFlavorType.

        网关是否禁用

        :param disable: The disable of this EngineCreateReqFlavorType.
        :type disable: bool
        """
        self._disable = disable

    @property
    def spec(self):
        r"""Gets the spec of this EngineCreateReqFlavorType.

        网关节点类型

        :return: The spec of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this EngineCreateReqFlavorType.

        网关节点类型

        :param spec: The spec of this EngineCreateReqFlavorType.
        :type spec: str
        """
        self._spec = spec

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this EngineCreateReqFlavorType.

        云服务类型

        :return: The cloud_service_type of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this EngineCreateReqFlavorType.

        云服务类型

        :param cloud_service_type: The cloud_service_type of this EngineCreateReqFlavorType.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def currentflavor(self):
        r"""Gets the currentflavor of this EngineCreateReqFlavorType.

        当前规格

        :return: The currentflavor of this EngineCreateReqFlavorType.
        :rtype: str
        """
        return self._currentflavor

    @currentflavor.setter
    def currentflavor(self, currentflavor):
        r"""Sets the currentflavor of this EngineCreateReqFlavorType.

        当前规格

        :param currentflavor: The currentflavor of this EngineCreateReqFlavorType.
        :type currentflavor: str
        """
        self._currentflavor = currentflavor

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
        if not isinstance(other, EngineCreateReqFlavorType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
