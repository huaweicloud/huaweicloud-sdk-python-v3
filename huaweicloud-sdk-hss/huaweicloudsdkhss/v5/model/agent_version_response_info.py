# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentVersionResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_type': 'str',
        'latest_version': 'str',
        'version_list': 'list[VersionList]'
    }

    attribute_map = {
        'os_type': 'os_type',
        'latest_version': 'latest_version',
        'version_list': 'version_list'
    }

    def __init__(self, os_type=None, latest_version=None, version_list=None):
        r"""AgentVersionResponseInfo

        The model defined in huaweicloud sdk

        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param latest_version: 最新版本的版本号
        :type latest_version: str
        :param version_list: 最新若干版本的版本号和版本说明
        :type version_list: list[:class:`huaweicloudsdkhss.v5.VersionList`]
        """
        
        

        self._os_type = None
        self._latest_version = None
        self._version_list = None
        self.discriminator = None

        if os_type is not None:
            self.os_type = os_type
        if latest_version is not None:
            self.latest_version = latest_version
        if version_list is not None:
            self.version_list = version_list

    @property
    def os_type(self):
        r"""Gets the os_type of this AgentVersionResponseInfo.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this AgentVersionResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AgentVersionResponseInfo.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this AgentVersionResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def latest_version(self):
        r"""Gets the latest_version of this AgentVersionResponseInfo.

        最新版本的版本号

        :return: The latest_version of this AgentVersionResponseInfo.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this AgentVersionResponseInfo.

        最新版本的版本号

        :param latest_version: The latest_version of this AgentVersionResponseInfo.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def version_list(self):
        r"""Gets the version_list of this AgentVersionResponseInfo.

        最新若干版本的版本号和版本说明

        :return: The version_list of this AgentVersionResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VersionList`]
        """
        return self._version_list

    @version_list.setter
    def version_list(self, version_list):
        r"""Sets the version_list of this AgentVersionResponseInfo.

        最新若干版本的版本号和版本说明

        :param version_list: The version_list of this AgentVersionResponseInfo.
        :type version_list: list[:class:`huaweicloudsdkhss.v5.VersionList`]
        """
        self._version_list = version_list

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
        if not isinstance(other, AgentVersionResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
