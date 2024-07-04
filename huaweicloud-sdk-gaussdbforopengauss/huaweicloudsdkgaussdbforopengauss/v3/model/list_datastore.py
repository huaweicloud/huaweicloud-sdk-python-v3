# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatastore:

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
        'version': 'str',
        'complete_version': 'str',
        'hotfix_versions': 'str',
        'target_version': 'str',
        'hotfix_finished_times': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'complete_version': 'complete_version',
        'hotfix_versions': 'hotfix_versions',
        'target_version': 'target_version',
        'hotfix_finished_times': 'hotfix_finished_times'
    }

    def __init__(self, type=None, version=None, complete_version=None, hotfix_versions=None, target_version=None, hotfix_finished_times=None):
        """ListDatastore

        The model defined in huaweicloud sdk

        :param type: 数据库引擎。
        :type type: str
        :param version: 数据库大版本。
        :type version: str
        :param complete_version: 数据库小版本。
        :type complete_version: str
        :param hotfix_versions: 数据库已升级的热补丁版本，当数据库热补丁升级成功后，该值不为空。
        :type hotfix_versions: str
        :param target_version: 数据库正在升级的目标版本。
        :type target_version: str
        :param hotfix_finished_times: 热补丁升级完成时间列表。  热补丁升级完成时间，格式为“yyyy-mm-dd hh:mm:ss timezone”。  其中timezone是指时区。 
        :type hotfix_finished_times: list[str]
        """
        
        

        self._type = None
        self._version = None
        self._complete_version = None
        self._hotfix_versions = None
        self._target_version = None
        self._hotfix_finished_times = None
        self.discriminator = None

        self.type = type
        self.version = version
        if complete_version is not None:
            self.complete_version = complete_version
        if hotfix_versions is not None:
            self.hotfix_versions = hotfix_versions
        if target_version is not None:
            self.target_version = target_version
        if hotfix_finished_times is not None:
            self.hotfix_finished_times = hotfix_finished_times

    @property
    def type(self):
        """Gets the type of this ListDatastore.

        数据库引擎。

        :return: The type of this ListDatastore.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListDatastore.

        数据库引擎。

        :param type: The type of this ListDatastore.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListDatastore.

        数据库大版本。

        :return: The version of this ListDatastore.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListDatastore.

        数据库大版本。

        :param version: The version of this ListDatastore.
        :type version: str
        """
        self._version = version

    @property
    def complete_version(self):
        """Gets the complete_version of this ListDatastore.

        数据库小版本。

        :return: The complete_version of this ListDatastore.
        :rtype: str
        """
        return self._complete_version

    @complete_version.setter
    def complete_version(self, complete_version):
        """Sets the complete_version of this ListDatastore.

        数据库小版本。

        :param complete_version: The complete_version of this ListDatastore.
        :type complete_version: str
        """
        self._complete_version = complete_version

    @property
    def hotfix_versions(self):
        """Gets the hotfix_versions of this ListDatastore.

        数据库已升级的热补丁版本，当数据库热补丁升级成功后，该值不为空。

        :return: The hotfix_versions of this ListDatastore.
        :rtype: str
        """
        return self._hotfix_versions

    @hotfix_versions.setter
    def hotfix_versions(self, hotfix_versions):
        """Sets the hotfix_versions of this ListDatastore.

        数据库已升级的热补丁版本，当数据库热补丁升级成功后，该值不为空。

        :param hotfix_versions: The hotfix_versions of this ListDatastore.
        :type hotfix_versions: str
        """
        self._hotfix_versions = hotfix_versions

    @property
    def target_version(self):
        """Gets the target_version of this ListDatastore.

        数据库正在升级的目标版本。

        :return: The target_version of this ListDatastore.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this ListDatastore.

        数据库正在升级的目标版本。

        :param target_version: The target_version of this ListDatastore.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def hotfix_finished_times(self):
        """Gets the hotfix_finished_times of this ListDatastore.

        热补丁升级完成时间列表。  热补丁升级完成时间，格式为“yyyy-mm-dd hh:mm:ss timezone”。  其中timezone是指时区。 

        :return: The hotfix_finished_times of this ListDatastore.
        :rtype: list[str]
        """
        return self._hotfix_finished_times

    @hotfix_finished_times.setter
    def hotfix_finished_times(self, hotfix_finished_times):
        """Sets the hotfix_finished_times of this ListDatastore.

        热补丁升级完成时间列表。  热补丁升级完成时间，格式为“yyyy-mm-dd hh:mm:ss timezone”。  其中timezone是指时区。 

        :param hotfix_finished_times: The hotfix_finished_times of this ListDatastore.
        :type hotfix_finished_times: list[str]
        """
        self._hotfix_finished_times = hotfix_finished_times

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
        if not isinstance(other, ListDatastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
