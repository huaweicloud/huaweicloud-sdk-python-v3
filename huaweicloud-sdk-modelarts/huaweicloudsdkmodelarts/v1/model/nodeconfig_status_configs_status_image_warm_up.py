# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeconfigStatusConfigsStatusImageWarmUp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'message': 'str'
    }

    attribute_map = {
        'state': 'state',
        'message': 'message'
    }

    def __init__(self, state=None, message=None):
        r"""NodeconfigStatusConfigsStatusImageWarmUp

        The model defined in huaweicloud sdk

        :param state: **参数解释**：镜像预热任务的整体状态。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Success：全部成功，所有镜像在所有节点上均预热成功。 - Failed：全部失败，所有镜像在所有节点上均预热失败。 - Pulling：预热中，镜像正在被拉取。 - PartialCompletion：部分完成，部分镜像成功、部分失败或部分节点成功。 - Unknown：未知状态，解析节点上报数据异常。 **默认取值**：不涉及。
        :type state: str
        :param message: **参数解释**：镜像预热任务的详细结果信息（JSON格式字符串），包含以下字段： - successfulImages：预热成功的镜像列表 - failedImages：预热失败的镜像列表 - partialSuccess：部分节点成功的镜像列表 - pendingImages：尚未完成预热的镜像列表 - additionalInfos：失败原因等附加信息（如镜像不存在、拉取超时、拉取失败、镜像仓库中manifest不存在） - successfulImagesConfig：成功镜像的配置详情（id、name、creationTimestamp、type、image） - failedImagesConfig：失败镜像的配置详情 - partialSuccessConfig：部分成功镜像的配置详情 - pendingImagesConfig：待预热镜像的配置详情 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type message: str
        """
        
        

        self._state = None
        self._message = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if message is not None:
            self.message = message

    @property
    def state(self):
        r"""Gets the state of this NodeconfigStatusConfigsStatusImageWarmUp.

        **参数解释**：镜像预热任务的整体状态。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Success：全部成功，所有镜像在所有节点上均预热成功。 - Failed：全部失败，所有镜像在所有节点上均预热失败。 - Pulling：预热中，镜像正在被拉取。 - PartialCompletion：部分完成，部分镜像成功、部分失败或部分节点成功。 - Unknown：未知状态，解析节点上报数据异常。 **默认取值**：不涉及。

        :return: The state of this NodeconfigStatusConfigsStatusImageWarmUp.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this NodeconfigStatusConfigsStatusImageWarmUp.

        **参数解释**：镜像预热任务的整体状态。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Success：全部成功，所有镜像在所有节点上均预热成功。 - Failed：全部失败，所有镜像在所有节点上均预热失败。 - Pulling：预热中，镜像正在被拉取。 - PartialCompletion：部分完成，部分镜像成功、部分失败或部分节点成功。 - Unknown：未知状态，解析节点上报数据异常。 **默认取值**：不涉及。

        :param state: The state of this NodeconfigStatusConfigsStatusImageWarmUp.
        :type state: str
        """
        self._state = state

    @property
    def message(self):
        r"""Gets the message of this NodeconfigStatusConfigsStatusImageWarmUp.

        **参数解释**：镜像预热任务的详细结果信息（JSON格式字符串），包含以下字段： - successfulImages：预热成功的镜像列表 - failedImages：预热失败的镜像列表 - partialSuccess：部分节点成功的镜像列表 - pendingImages：尚未完成预热的镜像列表 - additionalInfos：失败原因等附加信息（如镜像不存在、拉取超时、拉取失败、镜像仓库中manifest不存在） - successfulImagesConfig：成功镜像的配置详情（id、name、creationTimestamp、type、image） - failedImagesConfig：失败镜像的配置详情 - partialSuccessConfig：部分成功镜像的配置详情 - pendingImagesConfig：待预热镜像的配置详情 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The message of this NodeconfigStatusConfigsStatusImageWarmUp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this NodeconfigStatusConfigsStatusImageWarmUp.

        **参数解释**：镜像预热任务的详细结果信息（JSON格式字符串），包含以下字段： - successfulImages：预热成功的镜像列表 - failedImages：预热失败的镜像列表 - partialSuccess：部分节点成功的镜像列表 - pendingImages：尚未完成预热的镜像列表 - additionalInfos：失败原因等附加信息（如镜像不存在、拉取超时、拉取失败、镜像仓库中manifest不存在） - successfulImagesConfig：成功镜像的配置详情（id、name、creationTimestamp、type、image） - failedImagesConfig：失败镜像的配置详情 - partialSuccessConfig：部分成功镜像的配置详情 - pendingImagesConfig：待预热镜像的配置详情 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param message: The message of this NodeconfigStatusConfigsStatusImageWarmUp.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, NodeconfigStatusConfigsStatusImageWarmUp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
