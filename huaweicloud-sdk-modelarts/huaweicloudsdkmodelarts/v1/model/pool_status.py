# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'message': 'str',
        'resources': 'PoolStatusResources',
        'scope': 'list[PoolStatusScope]',
        'driver': 'PoolStatusDriver',
        'parent': 'str',
        'root': 'str',
        'clusters': 'PoolStatusClusters'
    }

    attribute_map = {
        'phase': 'phase',
        'message': 'message',
        'resources': 'resources',
        'scope': 'scope',
        'driver': 'driver',
        'parent': 'parent',
        'root': 'root',
        'clusters': 'clusters'
    }

    def __init__(self, phase=None, message=None, resources=None, scope=None, driver=None, parent=None, root=None, clusters=None):
        r"""PoolStatus

        The model defined in huaweicloud sdk

        :param phase: **参数解释**：资源池的状态。 **取值范围**：可选值如下： - Creating：资源池在创建中。 - Running：资源池在运行中。 - Abnormal：资源池异常。 - Deleting：资源池在删除中。 - Error：资源池错误。
        :type phase: str
        :param message: **参数解释**：资源池当前状态的提示信息。 **取值范围**：不涉及。
        :type message: str
        :param resources: 
        :type resources: :class:`huaweicloudsdkmodelarts.v1.PoolStatusResources`
        :param scope: **参数解释**：资源池当前支持的业务类型的状态信息。
        :type scope: list[:class:`huaweicloudsdkmodelarts.v1.PoolStatusScope`]
        :param driver: 
        :type driver: :class:`huaweicloudsdkmodelarts.v1.PoolStatusDriver`
        :param parent: **参数解释**：资源池所属父资源池的ID。物理池为空。 **取值范围**：不涉及。
        :type parent: str
        :param root: **参数解释**：资源池根资源池的ID。 **取值范围**：不涉及。
        :type root: str
        :param clusters: 
        :type clusters: :class:`huaweicloudsdkmodelarts.v1.PoolStatusClusters`
        """
        
        

        self._phase = None
        self._message = None
        self._resources = None
        self._scope = None
        self._driver = None
        self._parent = None
        self._root = None
        self._clusters = None
        self.discriminator = None

        self.phase = phase
        if message is not None:
            self.message = message
        if resources is not None:
            self.resources = resources
        if scope is not None:
            self.scope = scope
        if driver is not None:
            self.driver = driver
        if parent is not None:
            self.parent = parent
        if root is not None:
            self.root = root
        if clusters is not None:
            self.clusters = clusters

    @property
    def phase(self):
        r"""Gets the phase of this PoolStatus.

        **参数解释**：资源池的状态。 **取值范围**：可选值如下： - Creating：资源池在创建中。 - Running：资源池在运行中。 - Abnormal：资源池异常。 - Deleting：资源池在删除中。 - Error：资源池错误。

        :return: The phase of this PoolStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this PoolStatus.

        **参数解释**：资源池的状态。 **取值范围**：可选值如下： - Creating：资源池在创建中。 - Running：资源池在运行中。 - Abnormal：资源池异常。 - Deleting：资源池在删除中。 - Error：资源池错误。

        :param phase: The phase of this PoolStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def message(self):
        r"""Gets the message of this PoolStatus.

        **参数解释**：资源池当前状态的提示信息。 **取值范围**：不涉及。

        :return: The message of this PoolStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this PoolStatus.

        **参数解释**：资源池当前状态的提示信息。 **取值范围**：不涉及。

        :param message: The message of this PoolStatus.
        :type message: str
        """
        self._message = message

    @property
    def resources(self):
        r"""Gets the resources of this PoolStatus.

        :return: The resources of this PoolStatus.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolStatusResources`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PoolStatus.

        :param resources: The resources of this PoolStatus.
        :type resources: :class:`huaweicloudsdkmodelarts.v1.PoolStatusResources`
        """
        self._resources = resources

    @property
    def scope(self):
        r"""Gets the scope of this PoolStatus.

        **参数解释**：资源池当前支持的业务类型的状态信息。

        :return: The scope of this PoolStatus.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PoolStatusScope`]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this PoolStatus.

        **参数解释**：资源池当前支持的业务类型的状态信息。

        :param scope: The scope of this PoolStatus.
        :type scope: list[:class:`huaweicloudsdkmodelarts.v1.PoolStatusScope`]
        """
        self._scope = scope

    @property
    def driver(self):
        r"""Gets the driver of this PoolStatus.

        :return: The driver of this PoolStatus.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolStatusDriver`
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        r"""Sets the driver of this PoolStatus.

        :param driver: The driver of this PoolStatus.
        :type driver: :class:`huaweicloudsdkmodelarts.v1.PoolStatusDriver`
        """
        self._driver = driver

    @property
    def parent(self):
        r"""Gets the parent of this PoolStatus.

        **参数解释**：资源池所属父资源池的ID。物理池为空。 **取值范围**：不涉及。

        :return: The parent of this PoolStatus.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        r"""Sets the parent of this PoolStatus.

        **参数解释**：资源池所属父资源池的ID。物理池为空。 **取值范围**：不涉及。

        :param parent: The parent of this PoolStatus.
        :type parent: str
        """
        self._parent = parent

    @property
    def root(self):
        r"""Gets the root of this PoolStatus.

        **参数解释**：资源池根资源池的ID。 **取值范围**：不涉及。

        :return: The root of this PoolStatus.
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        r"""Sets the root of this PoolStatus.

        **参数解释**：资源池根资源池的ID。 **取值范围**：不涉及。

        :param root: The root of this PoolStatus.
        :type root: str
        """
        self._root = root

    @property
    def clusters(self):
        r"""Gets the clusters of this PoolStatus.

        :return: The clusters of this PoolStatus.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolStatusClusters`
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this PoolStatus.

        :param clusters: The clusters of this PoolStatus.
        :type clusters: :class:`huaweicloudsdkmodelarts.v1.PoolStatusClusters`
        """
        self._clusters = clusters

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
        if not isinstance(other, PoolStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
