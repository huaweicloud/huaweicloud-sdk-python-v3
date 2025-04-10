# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseAvailableVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'versions': 'list[str]',
        'current_version': 'str',
        'latest_version': 'str',
        'current_favored_version': 'str',
        'previous_version': 'str'
    }

    attribute_map = {
        'versions': 'versions',
        'current_version': 'current_version',
        'latest_version': 'latest_version',
        'current_favored_version': 'current_favored_version',
        'previous_version': 'previous_version'
    }

    def __init__(self, versions=None, current_version=None, latest_version=None, current_favored_version=None, previous_version=None):
        r"""ListDatabaseAvailableVersionsResponse

        The model defined in huaweicloud sdk

        :param versions: 可变更版本
        :type versions: list[str]
        :param current_version: 当前版本
        :type current_version: str
        :param latest_version: 最新优选版本
        :type latest_version: str
        :param current_favored_version: 本系列优选版本，如3.0.8系列优选版本为3.0.8.5
        :type current_favored_version: str
        :param previous_version: 当前实例上一个版本
        :type previous_version: str
        """
        
        super(ListDatabaseAvailableVersionsResponse, self).__init__()

        self._versions = None
        self._current_version = None
        self._latest_version = None
        self._current_favored_version = None
        self._previous_version = None
        self.discriminator = None

        if versions is not None:
            self.versions = versions
        if current_version is not None:
            self.current_version = current_version
        if latest_version is not None:
            self.latest_version = latest_version
        if current_favored_version is not None:
            self.current_favored_version = current_favored_version
        if previous_version is not None:
            self.previous_version = previous_version

    @property
    def versions(self):
        r"""Gets the versions of this ListDatabaseAvailableVersionsResponse.

        可变更版本

        :return: The versions of this ListDatabaseAvailableVersionsResponse.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ListDatabaseAvailableVersionsResponse.

        可变更版本

        :param versions: The versions of this ListDatabaseAvailableVersionsResponse.
        :type versions: list[str]
        """
        self._versions = versions

    @property
    def current_version(self):
        r"""Gets the current_version of this ListDatabaseAvailableVersionsResponse.

        当前版本

        :return: The current_version of this ListDatabaseAvailableVersionsResponse.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this ListDatabaseAvailableVersionsResponse.

        当前版本

        :param current_version: The current_version of this ListDatabaseAvailableVersionsResponse.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def latest_version(self):
        r"""Gets the latest_version of this ListDatabaseAvailableVersionsResponse.

        最新优选版本

        :return: The latest_version of this ListDatabaseAvailableVersionsResponse.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this ListDatabaseAvailableVersionsResponse.

        最新优选版本

        :param latest_version: The latest_version of this ListDatabaseAvailableVersionsResponse.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def current_favored_version(self):
        r"""Gets the current_favored_version of this ListDatabaseAvailableVersionsResponse.

        本系列优选版本，如3.0.8系列优选版本为3.0.8.5

        :return: The current_favored_version of this ListDatabaseAvailableVersionsResponse.
        :rtype: str
        """
        return self._current_favored_version

    @current_favored_version.setter
    def current_favored_version(self, current_favored_version):
        r"""Sets the current_favored_version of this ListDatabaseAvailableVersionsResponse.

        本系列优选版本，如3.0.8系列优选版本为3.0.8.5

        :param current_favored_version: The current_favored_version of this ListDatabaseAvailableVersionsResponse.
        :type current_favored_version: str
        """
        self._current_favored_version = current_favored_version

    @property
    def previous_version(self):
        r"""Gets the previous_version of this ListDatabaseAvailableVersionsResponse.

        当前实例上一个版本

        :return: The previous_version of this ListDatabaseAvailableVersionsResponse.
        :rtype: str
        """
        return self._previous_version

    @previous_version.setter
    def previous_version(self, previous_version):
        r"""Sets the previous_version of this ListDatabaseAvailableVersionsResponse.

        当前实例上一个版本

        :param previous_version: The previous_version of this ListDatabaseAvailableVersionsResponse.
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
        if not isinstance(other, ListDatabaseAvailableVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
