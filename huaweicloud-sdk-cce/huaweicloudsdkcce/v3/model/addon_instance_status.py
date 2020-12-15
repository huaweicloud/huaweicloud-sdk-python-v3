# coding: utf-8

import pprint
import re

import six





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
        'current_version': 'Versions',
        'message': 'str',
        'reason': 'str',
        'status': 'str',
        'target_versions': 'list[str]'
    }

    attribute_map = {
        'current_version': 'currentVersion',
        'message': 'message',
        'reason': 'reason',
        'status': 'status',
        'target_versions': 'targetVersions'
    }

    def __init__(self, current_version=None, message=None, reason=None, status=None, target_versions=None):
        """AddonInstanceStatus - a model defined in huaweicloud sdk"""
        
        

        self._current_version = None
        self._message = None
        self._reason = None
        self._status = None
        self._target_versions = None
        self.discriminator = None

        self.current_version = current_version
        self.message = message
        self.reason = reason
        self.status = status
        if target_versions is not None:
            self.target_versions = target_versions

    @property
    def current_version(self):
        """Gets the current_version of this AddonInstanceStatus.


        :return: The current_version of this AddonInstanceStatus.
        :rtype: Versions
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this AddonInstanceStatus.


        :param current_version: The current_version of this AddonInstanceStatus.
        :type: Versions
        """
        self._current_version = current_version

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
        :type: str
        """
        self._message = message

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
        :type: str
        """
        self._reason = reason

    @property
    def status(self):
        """Gets the status of this AddonInstanceStatus.

        插件实例状态

        :return: The status of this AddonInstanceStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AddonInstanceStatus.

        插件实例状态

        :param status: The status of this AddonInstanceStatus.
        :type: str
        """
        self._status = status

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
        :type: list[str]
        """
        self._target_versions = target_versions

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddonInstanceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
