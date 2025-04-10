# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDatabaseVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_version': 'str',
        'current_kernel_version': 'str',
        'latest_version': 'str',
        'latest_kernel_version': 'str'
    }

    attribute_map = {
        'current_version': 'current_version',
        'current_kernel_version': 'current_kernel_version',
        'latest_version': 'latest_version',
        'latest_kernel_version': 'latest_kernel_version'
    }

    def __init__(self, current_version=None, current_kernel_version=None, latest_version=None, latest_kernel_version=None):
        r"""InstanceDatabaseVersionInfo

        The model defined in huaweicloud sdk

        :param current_version: 当前数据库版本。
        :type current_version: str
        :param current_kernel_version: 当前数据库内核版本。
        :type current_kernel_version: str
        :param latest_version: 最新数据库版本。
        :type latest_version: str
        :param latest_kernel_version: 最新数据库内核版本。
        :type latest_kernel_version: str
        """
        
        

        self._current_version = None
        self._current_kernel_version = None
        self._latest_version = None
        self._latest_kernel_version = None
        self.discriminator = None

        if current_version is not None:
            self.current_version = current_version
        if current_kernel_version is not None:
            self.current_kernel_version = current_kernel_version
        if latest_version is not None:
            self.latest_version = latest_version
        if latest_kernel_version is not None:
            self.latest_kernel_version = latest_kernel_version

    @property
    def current_version(self):
        r"""Gets the current_version of this InstanceDatabaseVersionInfo.

        当前数据库版本。

        :return: The current_version of this InstanceDatabaseVersionInfo.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this InstanceDatabaseVersionInfo.

        当前数据库版本。

        :param current_version: The current_version of this InstanceDatabaseVersionInfo.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def current_kernel_version(self):
        r"""Gets the current_kernel_version of this InstanceDatabaseVersionInfo.

        当前数据库内核版本。

        :return: The current_kernel_version of this InstanceDatabaseVersionInfo.
        :rtype: str
        """
        return self._current_kernel_version

    @current_kernel_version.setter
    def current_kernel_version(self, current_kernel_version):
        r"""Sets the current_kernel_version of this InstanceDatabaseVersionInfo.

        当前数据库内核版本。

        :param current_kernel_version: The current_kernel_version of this InstanceDatabaseVersionInfo.
        :type current_kernel_version: str
        """
        self._current_kernel_version = current_kernel_version

    @property
    def latest_version(self):
        r"""Gets the latest_version of this InstanceDatabaseVersionInfo.

        最新数据库版本。

        :return: The latest_version of this InstanceDatabaseVersionInfo.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this InstanceDatabaseVersionInfo.

        最新数据库版本。

        :param latest_version: The latest_version of this InstanceDatabaseVersionInfo.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def latest_kernel_version(self):
        r"""Gets the latest_kernel_version of this InstanceDatabaseVersionInfo.

        最新数据库内核版本。

        :return: The latest_kernel_version of this InstanceDatabaseVersionInfo.
        :rtype: str
        """
        return self._latest_kernel_version

    @latest_kernel_version.setter
    def latest_kernel_version(self, latest_kernel_version):
        r"""Sets the latest_kernel_version of this InstanceDatabaseVersionInfo.

        最新数据库内核版本。

        :param latest_kernel_version: The latest_kernel_version of this InstanceDatabaseVersionInfo.
        :type latest_kernel_version: str
        """
        self._latest_kernel_version = latest_kernel_version

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
        if not isinstance(other, InstanceDatabaseVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
