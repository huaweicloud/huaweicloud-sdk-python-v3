# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolSpecCreation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'scope': 'list[str]',
        'resources': 'list[PoolResourceFlavor]',
        'network': 'PoolSpecCreationNetwork',
        'job_flavors': 'list[str]',
        'driver': 'PoolDriver'
    }

    attribute_map = {
        'type': 'type',
        'scope': 'scope',
        'resources': 'resources',
        'network': 'network',
        'job_flavors': 'jobFlavors',
        'driver': 'driver'
    }

    def __init__(self, type=None, scope=None, resources=None, network=None, job_flavors=None, driver=None):
        r"""PoolSpecCreation

        The model defined in huaweicloud sdk

        :param type: **参数解释**：资源池类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Dedicate：物理资源池，独立的网络，支持网络打通，定制驱动，定制作业类型 - Logical：逻辑资源池。没有独立的网络，不支持网络打通，资源池创建和扩缩容相较物理资源池更快。 **默认取值**：不涉及。
        :type type: str
        :param scope: **参数解释**：资源池支持的作业类型。 **约束限制**：不涉及。 **取值范围**：用户创建标准资源池时至少选择一种，物理资源池支持全部选择。可选值如下： - Train：训练作业 - Infer：推理作业 - Notebook：Notebook作业 **默认取值**：不涉及。
        :type scope: list[str]
        :param resources: **参数解释**：资源池中的资源规格信列表，包括资源规格和相应规格的资源数量。 **约束限制**：不涉及。
        :type resources: list[:class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavor`]
        :param network: 
        :type network: :class:`huaweicloudsdkmodelarts.v1.PoolSpecCreationNetwork`
        :param job_flavors: **参数解释**：资源池支持的作业规格信息列表，内容为作业规格名称。 **约束限制**：不涉及。
        :type job_flavors: list[str]
        :param driver: 
        :type driver: :class:`huaweicloudsdkmodelarts.v1.PoolDriver`
        """
        
        

        self._type = None
        self._scope = None
        self._resources = None
        self._network = None
        self._job_flavors = None
        self._driver = None
        self.discriminator = None

        self.type = type
        self.scope = scope
        self.resources = resources
        self.network = network
        if job_flavors is not None:
            self.job_flavors = job_flavors
        if driver is not None:
            self.driver = driver

    @property
    def type(self):
        r"""Gets the type of this PoolSpecCreation.

        **参数解释**：资源池类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Dedicate：物理资源池，独立的网络，支持网络打通，定制驱动，定制作业类型 - Logical：逻辑资源池。没有独立的网络，不支持网络打通，资源池创建和扩缩容相较物理资源池更快。 **默认取值**：不涉及。

        :return: The type of this PoolSpecCreation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PoolSpecCreation.

        **参数解释**：资源池类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Dedicate：物理资源池，独立的网络，支持网络打通，定制驱动，定制作业类型 - Logical：逻辑资源池。没有独立的网络，不支持网络打通，资源池创建和扩缩容相较物理资源池更快。 **默认取值**：不涉及。

        :param type: The type of this PoolSpecCreation.
        :type type: str
        """
        self._type = type

    @property
    def scope(self):
        r"""Gets the scope of this PoolSpecCreation.

        **参数解释**：资源池支持的作业类型。 **约束限制**：不涉及。 **取值范围**：用户创建标准资源池时至少选择一种，物理资源池支持全部选择。可选值如下： - Train：训练作业 - Infer：推理作业 - Notebook：Notebook作业 **默认取值**：不涉及。

        :return: The scope of this PoolSpecCreation.
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this PoolSpecCreation.

        **参数解释**：资源池支持的作业类型。 **约束限制**：不涉及。 **取值范围**：用户创建标准资源池时至少选择一种，物理资源池支持全部选择。可选值如下： - Train：训练作业 - Infer：推理作业 - Notebook：Notebook作业 **默认取值**：不涉及。

        :param scope: The scope of this PoolSpecCreation.
        :type scope: list[str]
        """
        self._scope = scope

    @property
    def resources(self):
        r"""Gets the resources of this PoolSpecCreation.

        **参数解释**：资源池中的资源规格信列表，包括资源规格和相应规格的资源数量。 **约束限制**：不涉及。

        :return: The resources of this PoolSpecCreation.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavor`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PoolSpecCreation.

        **参数解释**：资源池中的资源规格信列表，包括资源规格和相应规格的资源数量。 **约束限制**：不涉及。

        :param resources: The resources of this PoolSpecCreation.
        :type resources: list[:class:`huaweicloudsdkmodelarts.v1.PoolResourceFlavor`]
        """
        self._resources = resources

    @property
    def network(self):
        r"""Gets the network of this PoolSpecCreation.

        :return: The network of this PoolSpecCreation.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolSpecCreationNetwork`
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this PoolSpecCreation.

        :param network: The network of this PoolSpecCreation.
        :type network: :class:`huaweicloudsdkmodelarts.v1.PoolSpecCreationNetwork`
        """
        self._network = network

    @property
    def job_flavors(self):
        r"""Gets the job_flavors of this PoolSpecCreation.

        **参数解释**：资源池支持的作业规格信息列表，内容为作业规格名称。 **约束限制**：不涉及。

        :return: The job_flavors of this PoolSpecCreation.
        :rtype: list[str]
        """
        return self._job_flavors

    @job_flavors.setter
    def job_flavors(self, job_flavors):
        r"""Sets the job_flavors of this PoolSpecCreation.

        **参数解释**：资源池支持的作业规格信息列表，内容为作业规格名称。 **约束限制**：不涉及。

        :param job_flavors: The job_flavors of this PoolSpecCreation.
        :type job_flavors: list[str]
        """
        self._job_flavors = job_flavors

    @property
    def driver(self):
        r"""Gets the driver of this PoolSpecCreation.

        :return: The driver of this PoolSpecCreation.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolDriver`
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        r"""Sets the driver of this PoolSpecCreation.

        :param driver: The driver of this PoolSpecCreation.
        :type driver: :class:`huaweicloudsdkmodelarts.v1.PoolDriver`
        """
        self._driver = driver

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
        if not isinstance(other, PoolSpecCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
