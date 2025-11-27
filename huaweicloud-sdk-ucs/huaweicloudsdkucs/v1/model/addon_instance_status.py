# coding: utf-8

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
        'current_version': 'AddonVersion'
    }

    attribute_map = {
        'status': 'status',
        'reason': 'Reason',
        'message': 'message',
        'target_versions': 'targetVersions',
        'current_version': 'currentVersion'
    }

    def __init__(self, status=None, reason=None, message=None, target_versions=None, current_version=None):
        r"""AddonInstanceStatus

        The model defined in huaweicloud sdk

        :param status: 状态信息
        :type status: str
        :param reason: 变化原因信息
        :type reason: str
        :param message: 变化详细信息
        :type message: str
        :param target_versions: 目标版本信息
        :type target_versions: list[str]
        :param current_version: 
        :type current_version: :class:`huaweicloudsdkucs.v1.AddonVersion`
        """
        
        

        self._status = None
        self._reason = None
        self._message = None
        self._target_versions = None
        self._current_version = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message
        if target_versions is not None:
            self.target_versions = target_versions
        if current_version is not None:
            self.current_version = current_version

    @property
    def status(self):
        r"""Gets the status of this AddonInstanceStatus.

        状态信息

        :return: The status of this AddonInstanceStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AddonInstanceStatus.

        状态信息

        :param status: The status of this AddonInstanceStatus.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this AddonInstanceStatus.

        变化原因信息

        :return: The reason of this AddonInstanceStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this AddonInstanceStatus.

        变化原因信息

        :param reason: The reason of this AddonInstanceStatus.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        r"""Gets the message of this AddonInstanceStatus.

        变化详细信息

        :return: The message of this AddonInstanceStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this AddonInstanceStatus.

        变化详细信息

        :param message: The message of this AddonInstanceStatus.
        :type message: str
        """
        self._message = message

    @property
    def target_versions(self):
        r"""Gets the target_versions of this AddonInstanceStatus.

        目标版本信息

        :return: The target_versions of this AddonInstanceStatus.
        :rtype: list[str]
        """
        return self._target_versions

    @target_versions.setter
    def target_versions(self, target_versions):
        r"""Sets the target_versions of this AddonInstanceStatus.

        目标版本信息

        :param target_versions: The target_versions of this AddonInstanceStatus.
        :type target_versions: list[str]
        """
        self._target_versions = target_versions

    @property
    def current_version(self):
        r"""Gets the current_version of this AddonInstanceStatus.

        :return: The current_version of this AddonInstanceStatus.
        :rtype: :class:`huaweicloudsdkucs.v1.AddonVersion`
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this AddonInstanceStatus.

        :param current_version: The current_version of this AddonInstanceStatus.
        :type current_version: :class:`huaweicloudsdkucs.v1.AddonVersion`
        """
        self._current_version = current_version

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
        if not isinstance(other, AddonInstanceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
