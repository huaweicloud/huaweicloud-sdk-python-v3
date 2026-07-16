# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolSpecModel:

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
        'resources': 'list[PoolSpecModelResources]',
        'containernetwork': 'PoolSpecModelContainernetwork',
        'network': 'PoolSpecModelNetwork',
        'job_flavors': 'list[str]',
        'driver': 'PoolDriver',
        'control_mode': 'int'
    }

    attribute_map = {
        'type': 'type',
        'scope': 'scope',
        'resources': 'resources',
        'containernetwork': 'containernetwork',
        'network': 'network',
        'job_flavors': 'jobFlavors',
        'driver': 'driver',
        'control_mode': 'controlMode'
    }

    def __init__(self, type=None, scope=None, resources=None, containernetwork=None, network=None, job_flavors=None, driver=None, control_mode=None):
        r"""PoolSpecModel

        The model defined in huaweicloud sdk

        :param type: **参数解释**：资源池类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Dedicate：物理资源池，独立的网络，支持网络打通，定制驱动，定制作业类型。 - Logical：逻辑资源池。没有独立的网络，不支持网络打通，资源池创建和扩缩容相较物理资源池更快。 **默认取值**：不涉及。
        :type type: str
        :param scope: **参数解释**：资源池支持的作业类型。
        :type scope: list[str]
        :param resources: **参数解释**：资源池中的资源规格信列表，包括资源规格和相应规格的资源数量。
        :type resources: list[:class:`huaweicloudsdkmodelarts.v1.PoolSpecModelResources`]
        :param containernetwork: 
        :type containernetwork: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelContainernetwork`
        :param network: 
        :type network: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelNetwork`
        :param job_flavors: **参数解释**：资源池支持的作业规格列表。参数为作业规格名称。
        :type job_flavors: list[str]
        :param driver: 
        :type driver: :class:`huaweicloudsdkmodelarts.v1.PoolDriver`
        :param control_mode: **参数解释**：资源池的受限状态。状态可以叠加，比如9代表转包周期受限和冻结状态。 **取值范围**：可选值如下： - 0：代表不受限 - 1：转包周期受限 - 2：规格变更受限 - 4：服务受限 - 8：冻结 - 16：公安冻结（不可退订）
        :type control_mode: int
        """
        
        

        self._type = None
        self._scope = None
        self._resources = None
        self._containernetwork = None
        self._network = None
        self._job_flavors = None
        self._driver = None
        self._control_mode = None
        self.discriminator = None

        self.type = type
        self.scope = scope
        self.resources = resources
        if containernetwork is not None:
            self.containernetwork = containernetwork
        if network is not None:
            self.network = network
        if job_flavors is not None:
            self.job_flavors = job_flavors
        if driver is not None:
            self.driver = driver
        if control_mode is not None:
            self.control_mode = control_mode

    @property
    def type(self):
        r"""Gets the type of this PoolSpecModel.

        **参数解释**：资源池类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Dedicate：物理资源池，独立的网络，支持网络打通，定制驱动，定制作业类型。 - Logical：逻辑资源池。没有独立的网络，不支持网络打通，资源池创建和扩缩容相较物理资源池更快。 **默认取值**：不涉及。

        :return: The type of this PoolSpecModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PoolSpecModel.

        **参数解释**：资源池类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Dedicate：物理资源池，独立的网络，支持网络打通，定制驱动，定制作业类型。 - Logical：逻辑资源池。没有独立的网络，不支持网络打通，资源池创建和扩缩容相较物理资源池更快。 **默认取值**：不涉及。

        :param type: The type of this PoolSpecModel.
        :type type: str
        """
        self._type = type

    @property
    def scope(self):
        r"""Gets the scope of this PoolSpecModel.

        **参数解释**：资源池支持的作业类型。

        :return: The scope of this PoolSpecModel.
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this PoolSpecModel.

        **参数解释**：资源池支持的作业类型。

        :param scope: The scope of this PoolSpecModel.
        :type scope: list[str]
        """
        self._scope = scope

    @property
    def resources(self):
        r"""Gets the resources of this PoolSpecModel.

        **参数解释**：资源池中的资源规格信列表，包括资源规格和相应规格的资源数量。

        :return: The resources of this PoolSpecModel.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PoolSpecModelResources`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PoolSpecModel.

        **参数解释**：资源池中的资源规格信列表，包括资源规格和相应规格的资源数量。

        :param resources: The resources of this PoolSpecModel.
        :type resources: list[:class:`huaweicloudsdkmodelarts.v1.PoolSpecModelResources`]
        """
        self._resources = resources

    @property
    def containernetwork(self):
        r"""Gets the containernetwork of this PoolSpecModel.

        :return: The containernetwork of this PoolSpecModel.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelContainernetwork`
        """
        return self._containernetwork

    @containernetwork.setter
    def containernetwork(self, containernetwork):
        r"""Sets the containernetwork of this PoolSpecModel.

        :param containernetwork: The containernetwork of this PoolSpecModel.
        :type containernetwork: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelContainernetwork`
        """
        self._containernetwork = containernetwork

    @property
    def network(self):
        r"""Gets the network of this PoolSpecModel.

        :return: The network of this PoolSpecModel.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelNetwork`
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this PoolSpecModel.

        :param network: The network of this PoolSpecModel.
        :type network: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelNetwork`
        """
        self._network = network

    @property
    def job_flavors(self):
        r"""Gets the job_flavors of this PoolSpecModel.

        **参数解释**：资源池支持的作业规格列表。参数为作业规格名称。

        :return: The job_flavors of this PoolSpecModel.
        :rtype: list[str]
        """
        return self._job_flavors

    @job_flavors.setter
    def job_flavors(self, job_flavors):
        r"""Sets the job_flavors of this PoolSpecModel.

        **参数解释**：资源池支持的作业规格列表。参数为作业规格名称。

        :param job_flavors: The job_flavors of this PoolSpecModel.
        :type job_flavors: list[str]
        """
        self._job_flavors = job_flavors

    @property
    def driver(self):
        r"""Gets the driver of this PoolSpecModel.

        :return: The driver of this PoolSpecModel.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolDriver`
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        r"""Sets the driver of this PoolSpecModel.

        :param driver: The driver of this PoolSpecModel.
        :type driver: :class:`huaweicloudsdkmodelarts.v1.PoolDriver`
        """
        self._driver = driver

    @property
    def control_mode(self):
        r"""Gets the control_mode of this PoolSpecModel.

        **参数解释**：资源池的受限状态。状态可以叠加，比如9代表转包周期受限和冻结状态。 **取值范围**：可选值如下： - 0：代表不受限 - 1：转包周期受限 - 2：规格变更受限 - 4：服务受限 - 8：冻结 - 16：公安冻结（不可退订）

        :return: The control_mode of this PoolSpecModel.
        :rtype: int
        """
        return self._control_mode

    @control_mode.setter
    def control_mode(self, control_mode):
        r"""Sets the control_mode of this PoolSpecModel.

        **参数解释**：资源池的受限状态。状态可以叠加，比如9代表转包周期受限和冻结状态。 **取值范围**：可选值如下： - 0：代表不受限 - 1：转包周期受限 - 2：规格变更受限 - 4：服务受限 - 8：冻结 - 16：公安冻结（不可退订）

        :param control_mode: The control_mode of this PoolSpecModel.
        :type control_mode: int
        """
        self._control_mode = control_mode

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
        if not isinstance(other, PoolSpecModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
