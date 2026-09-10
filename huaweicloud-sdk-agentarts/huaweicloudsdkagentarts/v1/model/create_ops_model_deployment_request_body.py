# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsModelDeploymentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'ma_pool_type': 'str',
        'ma_pool_id': 'str',
        'ma_instance_flavor': 'str',
        'ma_instance_count': 'int',
        'model_name': 'str',
        'model_service_name': 'str',
        'secret_name': 'str',
        'agency_name': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'ma_pool_type': 'ma_pool_type',
        'ma_pool_id': 'ma_pool_id',
        'ma_instance_flavor': 'ma_instance_flavor',
        'ma_instance_count': 'ma_instance_count',
        'model_name': 'model_name',
        'model_service_name': 'model_service_name',
        'secret_name': 'secret_name',
        'agency_name': 'agency_name'
    }

    def __init__(self, product_id=None, ma_pool_type=None, ma_pool_id=None, ma_instance_flavor=None, ma_instance_count=None, model_name=None, model_service_name=None, secret_name=None, agency_name=None):
        r"""CreateOpsModelDeploymentRequestBody

        The model defined in huaweicloud sdk

        :param product_id: **参数解释：** 模型优化任务产物ID，获取方法请参见查询模型优化任务产物列表。  **约束限制：** 不涉及  **取值范围：** 真实存在的产物ID字符串。  **默认取值：** 无
        :type product_id: str
        :param ma_pool_type: **参数解释：** ModelArts资源池类型。  **约束限制：** 不涉及  **取值范围：** public（公共资源池）或 dedicated（专属资源池）等支持的类型字符串。  **默认取值：** 无
        :type ma_pool_type: str
        :param ma_pool_id: **参数解释：** ModelArts资源池ID。在AgentArts平台智能体优化功能中，在部署并接入模型页面，按F12通过开发者工具可查看资源池的规格信息。  **约束限制：** ma_pool_type为专属资源池时必填。  **取值范围：** 真实存在的资源池ID字符串。  **默认取值：** 无
        :type ma_pool_id: str
        :param ma_instance_flavor: **参数解释：** AgentArts平台智能体优化功能中，在部署并接入模型页面，按F12通过开发者工具可查看资源池的规格信息。  **约束限制：** 不涉及  **取值范围：** ModelArts支持的计算实例规格字符串。  **默认取值：** 无
        :type ma_instance_flavor: str
        :param ma_instance_count: **参数解释：** ModelArts实例数，单位：个。  **约束限制：** 不涉及  **取值范围：** 大于等于1的正整数。  **默认取值：** 无
        :type ma_instance_count: int
        :param model_name: **参数解释：** 模型名称。  **约束限制：** 不涉及  **取值范围：** 部署模型的名称字符串，默认与模型优化任务训练完成后，产出的模型快照名称一致。  **默认取值：** 无
        :type model_name: str
        :param model_service_name: **参数解释：** 模型服务名称。  **约束限制：** 不涉及  **取值范围：** 可自定义，长度1-64个字符的字符串。  **默认取值：** 无
        :type model_service_name: str
        :param secret_name: **参数解释：** 认证凭据名称，在AgentArts平台智能体优化功能中，部署并接入模型时所填写的认证凭据名称。  **约束限制：** 不涉及  **取值范围：** 真实存在的凭据名称字符串。  **默认取值：** 无
        :type secret_name: str
        :param agency_name: **参数解释：** 委托名称，赋予服务访问用户资源的权限，在AgentArts平台智能体优化功能中，部署并接入模型时所填写的委托名称。  **约束限制：** 不涉及  **取值范围：** 具有ModelArts部署权限的IAM委托名称。  **默认取值：** 无
        :type agency_name: str
        """
        
        

        self._product_id = None
        self._ma_pool_type = None
        self._ma_pool_id = None
        self._ma_instance_flavor = None
        self._ma_instance_count = None
        self._model_name = None
        self._model_service_name = None
        self._secret_name = None
        self._agency_name = None
        self.discriminator = None

        self.product_id = product_id
        self.ma_pool_type = ma_pool_type
        if ma_pool_id is not None:
            self.ma_pool_id = ma_pool_id
        self.ma_instance_flavor = ma_instance_flavor
        self.ma_instance_count = ma_instance_count
        self.model_name = model_name
        self.model_service_name = model_service_name
        self.secret_name = secret_name
        self.agency_name = agency_name

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 模型优化任务产物ID，获取方法请参见查询模型优化任务产物列表。  **约束限制：** 不涉及  **取值范围：** 真实存在的产物ID字符串。  **默认取值：** 无

        :return: The product_id of this CreateOpsModelDeploymentRequestBody.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 模型优化任务产物ID，获取方法请参见查询模型优化任务产物列表。  **约束限制：** 不涉及  **取值范围：** 真实存在的产物ID字符串。  **默认取值：** 无

        :param product_id: The product_id of this CreateOpsModelDeploymentRequestBody.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def ma_pool_type(self):
        r"""Gets the ma_pool_type of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** ModelArts资源池类型。  **约束限制：** 不涉及  **取值范围：** public（公共资源池）或 dedicated（专属资源池）等支持的类型字符串。  **默认取值：** 无

        :return: The ma_pool_type of this CreateOpsModelDeploymentRequestBody.
        :rtype: str
        """
        return self._ma_pool_type

    @ma_pool_type.setter
    def ma_pool_type(self, ma_pool_type):
        r"""Sets the ma_pool_type of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** ModelArts资源池类型。  **约束限制：** 不涉及  **取值范围：** public（公共资源池）或 dedicated（专属资源池）等支持的类型字符串。  **默认取值：** 无

        :param ma_pool_type: The ma_pool_type of this CreateOpsModelDeploymentRequestBody.
        :type ma_pool_type: str
        """
        self._ma_pool_type = ma_pool_type

    @property
    def ma_pool_id(self):
        r"""Gets the ma_pool_id of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** ModelArts资源池ID。在AgentArts平台智能体优化功能中，在部署并接入模型页面，按F12通过开发者工具可查看资源池的规格信息。  **约束限制：** ma_pool_type为专属资源池时必填。  **取值范围：** 真实存在的资源池ID字符串。  **默认取值：** 无

        :return: The ma_pool_id of this CreateOpsModelDeploymentRequestBody.
        :rtype: str
        """
        return self._ma_pool_id

    @ma_pool_id.setter
    def ma_pool_id(self, ma_pool_id):
        r"""Sets the ma_pool_id of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** ModelArts资源池ID。在AgentArts平台智能体优化功能中，在部署并接入模型页面，按F12通过开发者工具可查看资源池的规格信息。  **约束限制：** ma_pool_type为专属资源池时必填。  **取值范围：** 真实存在的资源池ID字符串。  **默认取值：** 无

        :param ma_pool_id: The ma_pool_id of this CreateOpsModelDeploymentRequestBody.
        :type ma_pool_id: str
        """
        self._ma_pool_id = ma_pool_id

    @property
    def ma_instance_flavor(self):
        r"""Gets the ma_instance_flavor of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** AgentArts平台智能体优化功能中，在部署并接入模型页面，按F12通过开发者工具可查看资源池的规格信息。  **约束限制：** 不涉及  **取值范围：** ModelArts支持的计算实例规格字符串。  **默认取值：** 无

        :return: The ma_instance_flavor of this CreateOpsModelDeploymentRequestBody.
        :rtype: str
        """
        return self._ma_instance_flavor

    @ma_instance_flavor.setter
    def ma_instance_flavor(self, ma_instance_flavor):
        r"""Sets the ma_instance_flavor of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** AgentArts平台智能体优化功能中，在部署并接入模型页面，按F12通过开发者工具可查看资源池的规格信息。  **约束限制：** 不涉及  **取值范围：** ModelArts支持的计算实例规格字符串。  **默认取值：** 无

        :param ma_instance_flavor: The ma_instance_flavor of this CreateOpsModelDeploymentRequestBody.
        :type ma_instance_flavor: str
        """
        self._ma_instance_flavor = ma_instance_flavor

    @property
    def ma_instance_count(self):
        r"""Gets the ma_instance_count of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** ModelArts实例数，单位：个。  **约束限制：** 不涉及  **取值范围：** 大于等于1的正整数。  **默认取值：** 无

        :return: The ma_instance_count of this CreateOpsModelDeploymentRequestBody.
        :rtype: int
        """
        return self._ma_instance_count

    @ma_instance_count.setter
    def ma_instance_count(self, ma_instance_count):
        r"""Sets the ma_instance_count of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** ModelArts实例数，单位：个。  **约束限制：** 不涉及  **取值范围：** 大于等于1的正整数。  **默认取值：** 无

        :param ma_instance_count: The ma_instance_count of this CreateOpsModelDeploymentRequestBody.
        :type ma_instance_count: int
        """
        self._ma_instance_count = ma_instance_count

    @property
    def model_name(self):
        r"""Gets the model_name of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 模型名称。  **约束限制：** 不涉及  **取值范围：** 部署模型的名称字符串，默认与模型优化任务训练完成后，产出的模型快照名称一致。  **默认取值：** 无

        :return: The model_name of this CreateOpsModelDeploymentRequestBody.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 模型名称。  **约束限制：** 不涉及  **取值范围：** 部署模型的名称字符串，默认与模型优化任务训练完成后，产出的模型快照名称一致。  **默认取值：** 无

        :param model_name: The model_name of this CreateOpsModelDeploymentRequestBody.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def model_service_name(self):
        r"""Gets the model_service_name of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 模型服务名称。  **约束限制：** 不涉及  **取值范围：** 可自定义，长度1-64个字符的字符串。  **默认取值：** 无

        :return: The model_service_name of this CreateOpsModelDeploymentRequestBody.
        :rtype: str
        """
        return self._model_service_name

    @model_service_name.setter
    def model_service_name(self, model_service_name):
        r"""Sets the model_service_name of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 模型服务名称。  **约束限制：** 不涉及  **取值范围：** 可自定义，长度1-64个字符的字符串。  **默认取值：** 无

        :param model_service_name: The model_service_name of this CreateOpsModelDeploymentRequestBody.
        :type model_service_name: str
        """
        self._model_service_name = model_service_name

    @property
    def secret_name(self):
        r"""Gets the secret_name of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 认证凭据名称，在AgentArts平台智能体优化功能中，部署并接入模型时所填写的认证凭据名称。  **约束限制：** 不涉及  **取值范围：** 真实存在的凭据名称字符串。  **默认取值：** 无

        :return: The secret_name of this CreateOpsModelDeploymentRequestBody.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 认证凭据名称，在AgentArts平台智能体优化功能中，部署并接入模型时所填写的认证凭据名称。  **约束限制：** 不涉及  **取值范围：** 真实存在的凭据名称字符串。  **默认取值：** 无

        :param secret_name: The secret_name of this CreateOpsModelDeploymentRequestBody.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限，在AgentArts平台智能体优化功能中，部署并接入模型时所填写的委托名称。  **约束限制：** 不涉及  **取值范围：** 具有ModelArts部署权限的IAM委托名称。  **默认取值：** 无

        :return: The agency_name of this CreateOpsModelDeploymentRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateOpsModelDeploymentRequestBody.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限，在AgentArts平台智能体优化功能中，部署并接入模型时所填写的委托名称。  **约束限制：** 不涉及  **取值范围：** 具有ModelArts部署权限的IAM委托名称。  **默认取值：** 无

        :param agency_name: The agency_name of this CreateOpsModelDeploymentRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, CreateOpsModelDeploymentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
