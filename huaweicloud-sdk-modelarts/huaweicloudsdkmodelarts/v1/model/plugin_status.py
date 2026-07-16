# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginStatus:

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
        'version': 'str',
        'reason': 'str',
        'values': 'str',
        'resources': 'list[PluginResources]'
    }

    attribute_map = {
        'phase': 'phase',
        'version': 'version',
        'reason': 'reason',
        'values': 'values',
        'resources': 'resources'
    }

    def __init__(self, phase=None, version=None, reason=None, values=None, resources=None):
        r"""PluginStatus

        The model defined in huaweicloud sdk

        :param phase: **参数解释**： 插件实例的状态。 **取值范围**：可选值如下： - Pending：安装中，表示插件正在安装中。 - Running：运行中，表示插件全部实例状态都在运行中，插件正常使用。 - Updating：升级中，表示插件正在更新中。 - Abnormal：不可用，表示插件状态异常，插件不可使用。可单击状态查看失败原因。 - Deleting：删除中，表示插件正在删除中。
        :type phase: str
        :param version: **参数解释**： 插件实例的版本。 **取值范围**： 不涉及。
        :type version: str
        :param reason: **参数解释**： 插件实例安装失败的详细信息。 **取值范围**： 不涉及。
        :type reason: str
        :param values: **参数解释**： 插件实例的安装参数（各插件不同）。 **取值范围**： 不涉及。
        :type values: str
        :param resources: **参数解释**： 插件实例占用的资源量。
        :type resources: list[:class:`huaweicloudsdkmodelarts.v1.PluginResources`]
        """
        
        

        self._phase = None
        self._version = None
        self._reason = None
        self._values = None
        self._resources = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if version is not None:
            self.version = version
        if reason is not None:
            self.reason = reason
        if values is not None:
            self.values = values
        if resources is not None:
            self.resources = resources

    @property
    def phase(self):
        r"""Gets the phase of this PluginStatus.

        **参数解释**： 插件实例的状态。 **取值范围**：可选值如下： - Pending：安装中，表示插件正在安装中。 - Running：运行中，表示插件全部实例状态都在运行中，插件正常使用。 - Updating：升级中，表示插件正在更新中。 - Abnormal：不可用，表示插件状态异常，插件不可使用。可单击状态查看失败原因。 - Deleting：删除中，表示插件正在删除中。

        :return: The phase of this PluginStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this PluginStatus.

        **参数解释**： 插件实例的状态。 **取值范围**：可选值如下： - Pending：安装中，表示插件正在安装中。 - Running：运行中，表示插件全部实例状态都在运行中，插件正常使用。 - Updating：升级中，表示插件正在更新中。 - Abnormal：不可用，表示插件状态异常，插件不可使用。可单击状态查看失败原因。 - Deleting：删除中，表示插件正在删除中。

        :param phase: The phase of this PluginStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def version(self):
        r"""Gets the version of this PluginStatus.

        **参数解释**： 插件实例的版本。 **取值范围**： 不涉及。

        :return: The version of this PluginStatus.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PluginStatus.

        **参数解释**： 插件实例的版本。 **取值范围**： 不涉及。

        :param version: The version of this PluginStatus.
        :type version: str
        """
        self._version = version

    @property
    def reason(self):
        r"""Gets the reason of this PluginStatus.

        **参数解释**： 插件实例安装失败的详细信息。 **取值范围**： 不涉及。

        :return: The reason of this PluginStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this PluginStatus.

        **参数解释**： 插件实例安装失败的详细信息。 **取值范围**： 不涉及。

        :param reason: The reason of this PluginStatus.
        :type reason: str
        """
        self._reason = reason

    @property
    def values(self):
        r"""Gets the values of this PluginStatus.

        **参数解释**： 插件实例的安装参数（各插件不同）。 **取值范围**： 不涉及。

        :return: The values of this PluginStatus.
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this PluginStatus.

        **参数解释**： 插件实例的安装参数（各插件不同）。 **取值范围**： 不涉及。

        :param values: The values of this PluginStatus.
        :type values: str
        """
        self._values = values

    @property
    def resources(self):
        r"""Gets the resources of this PluginStatus.

        **参数解释**： 插件实例占用的资源量。

        :return: The resources of this PluginStatus.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PluginResources`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PluginStatus.

        **参数解释**： 插件实例占用的资源量。

        :param resources: The resources of this PluginStatus.
        :type resources: list[:class:`huaweicloudsdkmodelarts.v1.PluginResources`]
        """
        self._resources = resources

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
        if not isinstance(other, PluginStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
