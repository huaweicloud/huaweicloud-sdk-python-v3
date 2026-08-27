# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteTriggerUpgradeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_force_execute': 'int',
        'target_version': 'str',
        'description': 'str',
        'is_notify': 'int',
        'extra_params': 'str',
        'desktop_sids': 'list[str]'
    }

    attribute_map = {
        'is_force_execute': 'is_force_execute',
        'target_version': 'target_version',
        'description': 'description',
        'is_notify': 'is_notify',
        'extra_params': 'extra_params',
        'desktop_sids': 'desktop_sids'
    }

    def __init__(self, is_force_execute=None, target_version=None, description=None, is_notify=None, extra_params=None, desktop_sids=None):
        r"""ExecuteTriggerUpgradeRequestBody

        The model defined in huaweicloud sdk

        :param is_force_execute: 是否强制升级：0-否 1-是
        :type is_force_execute: int
        :param target_version: 升级目标版本
        :type target_version: str
        :param description: 升级任务描述
        :type description: str
        :param is_notify: 通知开启：0-未开启 1-开启
        :type is_notify: int
        :param extra_params: 扩展参数（JSON格式）
        :type extra_params: str
        :param desktop_sids: 桌面sids列表
        :type desktop_sids: list[str]
        """
        
        

        self._is_force_execute = None
        self._target_version = None
        self._description = None
        self._is_notify = None
        self._extra_params = None
        self._desktop_sids = None
        self.discriminator = None

        self.is_force_execute = is_force_execute
        self.target_version = target_version
        if description is not None:
            self.description = description
        self.is_notify = is_notify
        if extra_params is not None:
            self.extra_params = extra_params
        if desktop_sids is not None:
            self.desktop_sids = desktop_sids

    @property
    def is_force_execute(self):
        r"""Gets the is_force_execute of this ExecuteTriggerUpgradeRequestBody.

        是否强制升级：0-否 1-是

        :return: The is_force_execute of this ExecuteTriggerUpgradeRequestBody.
        :rtype: int
        """
        return self._is_force_execute

    @is_force_execute.setter
    def is_force_execute(self, is_force_execute):
        r"""Sets the is_force_execute of this ExecuteTriggerUpgradeRequestBody.

        是否强制升级：0-否 1-是

        :param is_force_execute: The is_force_execute of this ExecuteTriggerUpgradeRequestBody.
        :type is_force_execute: int
        """
        self._is_force_execute = is_force_execute

    @property
    def target_version(self):
        r"""Gets the target_version of this ExecuteTriggerUpgradeRequestBody.

        升级目标版本

        :return: The target_version of this ExecuteTriggerUpgradeRequestBody.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this ExecuteTriggerUpgradeRequestBody.

        升级目标版本

        :param target_version: The target_version of this ExecuteTriggerUpgradeRequestBody.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def description(self):
        r"""Gets the description of this ExecuteTriggerUpgradeRequestBody.

        升级任务描述

        :return: The description of this ExecuteTriggerUpgradeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExecuteTriggerUpgradeRequestBody.

        升级任务描述

        :param description: The description of this ExecuteTriggerUpgradeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def is_notify(self):
        r"""Gets the is_notify of this ExecuteTriggerUpgradeRequestBody.

        通知开启：0-未开启 1-开启

        :return: The is_notify of this ExecuteTriggerUpgradeRequestBody.
        :rtype: int
        """
        return self._is_notify

    @is_notify.setter
    def is_notify(self, is_notify):
        r"""Sets the is_notify of this ExecuteTriggerUpgradeRequestBody.

        通知开启：0-未开启 1-开启

        :param is_notify: The is_notify of this ExecuteTriggerUpgradeRequestBody.
        :type is_notify: int
        """
        self._is_notify = is_notify

    @property
    def extra_params(self):
        r"""Gets the extra_params of this ExecuteTriggerUpgradeRequestBody.

        扩展参数（JSON格式）

        :return: The extra_params of this ExecuteTriggerUpgradeRequestBody.
        :rtype: str
        """
        return self._extra_params

    @extra_params.setter
    def extra_params(self, extra_params):
        r"""Sets the extra_params of this ExecuteTriggerUpgradeRequestBody.

        扩展参数（JSON格式）

        :param extra_params: The extra_params of this ExecuteTriggerUpgradeRequestBody.
        :type extra_params: str
        """
        self._extra_params = extra_params

    @property
    def desktop_sids(self):
        r"""Gets the desktop_sids of this ExecuteTriggerUpgradeRequestBody.

        桌面sids列表

        :return: The desktop_sids of this ExecuteTriggerUpgradeRequestBody.
        :rtype: list[str]
        """
        return self._desktop_sids

    @desktop_sids.setter
    def desktop_sids(self, desktop_sids):
        r"""Sets the desktop_sids of this ExecuteTriggerUpgradeRequestBody.

        桌面sids列表

        :param desktop_sids: The desktop_sids of this ExecuteTriggerUpgradeRequestBody.
        :type desktop_sids: list[str]
        """
        self._desktop_sids = desktop_sids

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
        if not isinstance(other, ExecuteTriggerUpgradeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
