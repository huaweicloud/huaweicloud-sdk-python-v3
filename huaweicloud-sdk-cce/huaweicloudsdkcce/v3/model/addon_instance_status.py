# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonInstanceStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'reason': 'str',
        'message': 'str',
        'target_versions': 'list[str]',
        'current_version': 'Versions',
        'is_rollbackable': 'bool',
        'previous_version': 'str'
    }

    attribute_map = {
        'status': 'status',
        'reason': 'Reason',
        'message': 'message',
        'target_versions': 'targetVersions',
        'current_version': 'currentVersion',
        'is_rollbackable': 'isRollbackable',
        'previous_version': 'previousVersion'
    }

    def __init__(self, status=None, reason=None, message=None, target_versions=None, current_version=None, is_rollbackable=None, previous_version=None):
        """AddonInstanceStatus

        The model defined in huaweicloud sdk

        :param status: 插件实例状态, 取值如下 - running：运行中，表示插件全部实例状态都在运行中，插件正常使用。 - abnormal：不可用，表示插件状态异常，插件不可使用。可单击插件名称查看实例异常事件。 - installing：安装中，表示插件正在安装中。 - installFailed：安装失败，表示插件安装失败，需要卸载后重新安装。 - upgrading：升级中，表示插件正在更新中。 - upgradeFailed：升级失败，表示插件升级失败，可重试升级或卸载后重新安装。 - deleting：删除中，表示插件正在删除中。 - deleteFailed：删除失败，表示插件删除失败，可重试卸载。 - deleteSuccess：删除成功，表示插件删除成功。 - available：部分就绪，表示插件下只有部分实例状态为运行中，插件部分功能可用。 - rollbacking：回滚中，表示插件正在回滚中。 - rollbackFailed：回滚失败，表示插件回滚失败，可重试回滚或卸载后重新安装。 - unknown：未知状态，表示插件模板实例不存在。
        :type status: str
        :param reason: 插件安装失败原因
        :type reason: str
        :param message: 安装错误详情
        :type message: str
        :param target_versions: 此插件版本，支持升级的集群版本
        :type target_versions: list[str]
        :param current_version: 
        :type current_version: :class:`huaweicloudsdkcce.v3.Versions`
        :param is_rollbackable: 是否支持回滚到插件升级前的插件版本
        :type is_rollbackable: bool
        :param previous_version: 插件升级或回滚前的版本
        :type previous_version: str
        """
        
        

        self._status = None
        self._reason = None
        self._message = None
        self._target_versions = None
        self._current_version = None
        self._is_rollbackable = None
        self._previous_version = None
        self.discriminator = None

        self.status = status
        self.reason = reason
        self.message = message
        if target_versions is not None:
            self.target_versions = target_versions
        self.current_version = current_version
        if is_rollbackable is not None:
            self.is_rollbackable = is_rollbackable
        if previous_version is not None:
            self.previous_version = previous_version

    @property
    def status(self):
        """Gets the status of this AddonInstanceStatus.

        插件实例状态, 取值如下 - running：运行中，表示插件全部实例状态都在运行中，插件正常使用。 - abnormal：不可用，表示插件状态异常，插件不可使用。可单击插件名称查看实例异常事件。 - installing：安装中，表示插件正在安装中。 - installFailed：安装失败，表示插件安装失败，需要卸载后重新安装。 - upgrading：升级中，表示插件正在更新中。 - upgradeFailed：升级失败，表示插件升级失败，可重试升级或卸载后重新安装。 - deleting：删除中，表示插件正在删除中。 - deleteFailed：删除失败，表示插件删除失败，可重试卸载。 - deleteSuccess：删除成功，表示插件删除成功。 - available：部分就绪，表示插件下只有部分实例状态为运行中，插件部分功能可用。 - rollbacking：回滚中，表示插件正在回滚中。 - rollbackFailed：回滚失败，表示插件回滚失败，可重试回滚或卸载后重新安装。 - unknown：未知状态，表示插件模板实例不存在。

        :return: The status of this AddonInstanceStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AddonInstanceStatus.

        插件实例状态, 取值如下 - running：运行中，表示插件全部实例状态都在运行中，插件正常使用。 - abnormal：不可用，表示插件状态异常，插件不可使用。可单击插件名称查看实例异常事件。 - installing：安装中，表示插件正在安装中。 - installFailed：安装失败，表示插件安装失败，需要卸载后重新安装。 - upgrading：升级中，表示插件正在更新中。 - upgradeFailed：升级失败，表示插件升级失败，可重试升级或卸载后重新安装。 - deleting：删除中，表示插件正在删除中。 - deleteFailed：删除失败，表示插件删除失败，可重试卸载。 - deleteSuccess：删除成功，表示插件删除成功。 - available：部分就绪，表示插件下只有部分实例状态为运行中，插件部分功能可用。 - rollbacking：回滚中，表示插件正在回滚中。 - rollbackFailed：回滚失败，表示插件回滚失败，可重试回滚或卸载后重新安装。 - unknown：未知状态，表示插件模板实例不存在。

        :param status: The status of this AddonInstanceStatus.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        """Gets the reason of this AddonInstanceStatus.

        插件安装失败原因

        :return: The reason of this AddonInstanceStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this AddonInstanceStatus.

        插件安装失败原因

        :param reason: The reason of this AddonInstanceStatus.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        """Gets the message of this AddonInstanceStatus.

        安装错误详情

        :return: The message of this AddonInstanceStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AddonInstanceStatus.

        安装错误详情

        :param message: The message of this AddonInstanceStatus.
        :type message: str
        """
        self._message = message

    @property
    def target_versions(self):
        """Gets the target_versions of this AddonInstanceStatus.

        此插件版本，支持升级的集群版本

        :return: The target_versions of this AddonInstanceStatus.
        :rtype: list[str]
        """
        return self._target_versions

    @target_versions.setter
    def target_versions(self, target_versions):
        """Sets the target_versions of this AddonInstanceStatus.

        此插件版本，支持升级的集群版本

        :param target_versions: The target_versions of this AddonInstanceStatus.
        :type target_versions: list[str]
        """
        self._target_versions = target_versions

    @property
    def current_version(self):
        """Gets the current_version of this AddonInstanceStatus.

        :return: The current_version of this AddonInstanceStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.Versions`
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this AddonInstanceStatus.

        :param current_version: The current_version of this AddonInstanceStatus.
        :type current_version: :class:`huaweicloudsdkcce.v3.Versions`
        """
        self._current_version = current_version

    @property
    def is_rollbackable(self):
        """Gets the is_rollbackable of this AddonInstanceStatus.

        是否支持回滚到插件升级前的插件版本

        :return: The is_rollbackable of this AddonInstanceStatus.
        :rtype: bool
        """
        return self._is_rollbackable

    @is_rollbackable.setter
    def is_rollbackable(self, is_rollbackable):
        """Sets the is_rollbackable of this AddonInstanceStatus.

        是否支持回滚到插件升级前的插件版本

        :param is_rollbackable: The is_rollbackable of this AddonInstanceStatus.
        :type is_rollbackable: bool
        """
        self._is_rollbackable = is_rollbackable

    @property
    def previous_version(self):
        """Gets the previous_version of this AddonInstanceStatus.

        插件升级或回滚前的版本

        :return: The previous_version of this AddonInstanceStatus.
        :rtype: str
        """
        return self._previous_version

    @previous_version.setter
    def previous_version(self, previous_version):
        """Sets the previous_version of this AddonInstanceStatus.

        插件升级或回滚前的版本

        :param previous_version: The previous_version of this AddonInstanceStatus.
        :type previous_version: str
        """
        self._previous_version = previous_version

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
        if not isinstance(other, AddonInstanceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
