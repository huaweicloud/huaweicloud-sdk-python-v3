# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIngressRequestBody:

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
        'description': 'str',
        'enable_public_network': 'bool',
        'vpc': 'CoreIngressVpcConfig'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enable_public_network': 'enable_public_network',
        'vpc': 'vpc'
    }

    def __init__(self, name=None, description=None, enable_public_network=None, vpc=None):
        r"""CreateIngressRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**： Ingress名称，同一账号下名称不可重复。
        :type name: str
        :param description: **参数解释**： Ingress描述信息。
        :type description: str
        :param enable_public_network: **参数解释**： 是否启用公网访问。
        :type enable_public_network: bool
        :param vpc: 
        :type vpc: :class:`huaweicloudsdkagentarts.v1.CoreIngressVpcConfig`
        """
        
        

        self._name = None
        self._description = None
        self._enable_public_network = None
        self._vpc = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if enable_public_network is not None:
            self.enable_public_network = enable_public_network
        if vpc is not None:
            self.vpc = vpc

    @property
    def name(self):
        r"""Gets the name of this CreateIngressRequestBody.

        **参数解释**： Ingress名称，同一账号下名称不可重复。

        :return: The name of this CreateIngressRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateIngressRequestBody.

        **参数解释**： Ingress名称，同一账号下名称不可重复。

        :param name: The name of this CreateIngressRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateIngressRequestBody.

        **参数解释**： Ingress描述信息。

        :return: The description of this CreateIngressRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateIngressRequestBody.

        **参数解释**： Ingress描述信息。

        :param description: The description of this CreateIngressRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enable_public_network(self):
        r"""Gets the enable_public_network of this CreateIngressRequestBody.

        **参数解释**： 是否启用公网访问。

        :return: The enable_public_network of this CreateIngressRequestBody.
        :rtype: bool
        """
        return self._enable_public_network

    @enable_public_network.setter
    def enable_public_network(self, enable_public_network):
        r"""Sets the enable_public_network of this CreateIngressRequestBody.

        **参数解释**： 是否启用公网访问。

        :param enable_public_network: The enable_public_network of this CreateIngressRequestBody.
        :type enable_public_network: bool
        """
        self._enable_public_network = enable_public_network

    @property
    def vpc(self):
        r"""Gets the vpc of this CreateIngressRequestBody.

        :return: The vpc of this CreateIngressRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreIngressVpcConfig`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this CreateIngressRequestBody.

        :param vpc: The vpc of this CreateIngressRequestBody.
        :type vpc: :class:`huaweicloudsdkagentarts.v1.CoreIngressVpcConfig`
        """
        self._vpc = vpc

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
        if not isinstance(other, CreateIngressRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
