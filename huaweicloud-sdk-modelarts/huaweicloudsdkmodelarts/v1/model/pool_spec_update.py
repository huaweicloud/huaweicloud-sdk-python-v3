# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolSpecUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scope': 'list[str]',
        'resources': 'list[PoolSpecUpdateResources]',
        'job_flavors': 'list[str]',
        'driver': 'PoolDriver'
    }

    attribute_map = {
        'scope': 'scope',
        'resources': 'resources',
        'job_flavors': 'jobFlavors',
        'driver': 'driver'
    }

    def __init__(self, scope=None, resources=None, job_flavors=None, driver=None):
        r"""PoolSpecUpdate

        The model defined in huaweicloud sdk

        :param scope: **参数解释**：更新启用的作业类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Train：训练作业 - Infer：推理作业 - Notebook：Notebook作业 **默认取值**：不涉及。
        :type scope: list[str]
        :param resources: **参数解释**：更新的资源规格列表。
        :type resources: list[:class:`huaweicloudsdkmodelarts.v1.PoolSpecUpdateResources`]
        :param job_flavors: **参数解释**：资源池支持的作业规格信息列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type job_flavors: list[str]
        :param driver: 
        :type driver: :class:`huaweicloudsdkmodelarts.v1.PoolDriver`
        """
        
        

        self._scope = None
        self._resources = None
        self._job_flavors = None
        self._driver = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        if resources is not None:
            self.resources = resources
        if job_flavors is not None:
            self.job_flavors = job_flavors
        if driver is not None:
            self.driver = driver

    @property
    def scope(self):
        r"""Gets the scope of this PoolSpecUpdate.

        **参数解释**：更新启用的作业类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Train：训练作业 - Infer：推理作业 - Notebook：Notebook作业 **默认取值**：不涉及。

        :return: The scope of this PoolSpecUpdate.
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this PoolSpecUpdate.

        **参数解释**：更新启用的作业类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Train：训练作业 - Infer：推理作业 - Notebook：Notebook作业 **默认取值**：不涉及。

        :param scope: The scope of this PoolSpecUpdate.
        :type scope: list[str]
        """
        self._scope = scope

    @property
    def resources(self):
        r"""Gets the resources of this PoolSpecUpdate.

        **参数解释**：更新的资源规格列表。

        :return: The resources of this PoolSpecUpdate.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PoolSpecUpdateResources`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PoolSpecUpdate.

        **参数解释**：更新的资源规格列表。

        :param resources: The resources of this PoolSpecUpdate.
        :type resources: list[:class:`huaweicloudsdkmodelarts.v1.PoolSpecUpdateResources`]
        """
        self._resources = resources

    @property
    def job_flavors(self):
        r"""Gets the job_flavors of this PoolSpecUpdate.

        **参数解释**：资源池支持的作业规格信息列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The job_flavors of this PoolSpecUpdate.
        :rtype: list[str]
        """
        return self._job_flavors

    @job_flavors.setter
    def job_flavors(self, job_flavors):
        r"""Sets the job_flavors of this PoolSpecUpdate.

        **参数解释**：资源池支持的作业规格信息列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param job_flavors: The job_flavors of this PoolSpecUpdate.
        :type job_flavors: list[str]
        """
        self._job_flavors = job_flavors

    @property
    def driver(self):
        r"""Gets the driver of this PoolSpecUpdate.

        :return: The driver of this PoolSpecUpdate.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolDriver`
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        r"""Sets the driver of this PoolSpecUpdate.

        :param driver: The driver of this PoolSpecUpdate.
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
        if not isinstance(other, PoolSpecUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
