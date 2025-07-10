# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPersonalizedDataMgmtUserDataRoamingOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'profile_streaming_enable': 'bool',
        'roamed_files_local_path': 'str',
        'exclude_folders_path': 'str',
        'roaming_registry_method': 'str',
        'roaming_registry_path': 'str'
    }

    attribute_map = {
        'profile_streaming_enable': 'profile_streaming_enable',
        'roamed_files_local_path': 'roamed_files_local_path',
        'exclude_folders_path': 'exclude_folders_path',
        'roaming_registry_method': 'roaming_registry_method',
        'roaming_registry_path': 'roaming_registry_path'
    }

    def __init__(self, profile_streaming_enable=None, roamed_files_local_path=None, exclude_folders_path=None, roaming_registry_method=None, roaming_registry_path=None):
        r"""PoliciesPersonalizedDataMgmtUserDataRoamingOptions

        The model defined in huaweicloud sdk

        :param profile_streaming_enable: 配置文件流式处理启用。
        :type profile_streaming_enable: bool
        :param roamed_files_local_path: 漫游文件本地路径。
        :type roamed_files_local_path: str
        :param exclude_folders_path: 排除文件夹路径。
        :type exclude_folders_path: str
        :param roaming_registry_method: 排除文件夹路径。
        :type roaming_registry_method: str
        :param roaming_registry_path: 漫游注册路径。
        :type roaming_registry_path: str
        """
        
        

        self._profile_streaming_enable = None
        self._roamed_files_local_path = None
        self._exclude_folders_path = None
        self._roaming_registry_method = None
        self._roaming_registry_path = None
        self.discriminator = None

        if profile_streaming_enable is not None:
            self.profile_streaming_enable = profile_streaming_enable
        if roamed_files_local_path is not None:
            self.roamed_files_local_path = roamed_files_local_path
        if exclude_folders_path is not None:
            self.exclude_folders_path = exclude_folders_path
        if roaming_registry_method is not None:
            self.roaming_registry_method = roaming_registry_method
        if roaming_registry_path is not None:
            self.roaming_registry_path = roaming_registry_path

    @property
    def profile_streaming_enable(self):
        r"""Gets the profile_streaming_enable of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        配置文件流式处理启用。

        :return: The profile_streaming_enable of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :rtype: bool
        """
        return self._profile_streaming_enable

    @profile_streaming_enable.setter
    def profile_streaming_enable(self, profile_streaming_enable):
        r"""Sets the profile_streaming_enable of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        配置文件流式处理启用。

        :param profile_streaming_enable: The profile_streaming_enable of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :type profile_streaming_enable: bool
        """
        self._profile_streaming_enable = profile_streaming_enable

    @property
    def roamed_files_local_path(self):
        r"""Gets the roamed_files_local_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        漫游文件本地路径。

        :return: The roamed_files_local_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :rtype: str
        """
        return self._roamed_files_local_path

    @roamed_files_local_path.setter
    def roamed_files_local_path(self, roamed_files_local_path):
        r"""Sets the roamed_files_local_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        漫游文件本地路径。

        :param roamed_files_local_path: The roamed_files_local_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :type roamed_files_local_path: str
        """
        self._roamed_files_local_path = roamed_files_local_path

    @property
    def exclude_folders_path(self):
        r"""Gets the exclude_folders_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        排除文件夹路径。

        :return: The exclude_folders_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :rtype: str
        """
        return self._exclude_folders_path

    @exclude_folders_path.setter
    def exclude_folders_path(self, exclude_folders_path):
        r"""Sets the exclude_folders_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        排除文件夹路径。

        :param exclude_folders_path: The exclude_folders_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :type exclude_folders_path: str
        """
        self._exclude_folders_path = exclude_folders_path

    @property
    def roaming_registry_method(self):
        r"""Gets the roaming_registry_method of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        排除文件夹路径。

        :return: The roaming_registry_method of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :rtype: str
        """
        return self._roaming_registry_method

    @roaming_registry_method.setter
    def roaming_registry_method(self, roaming_registry_method):
        r"""Sets the roaming_registry_method of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        排除文件夹路径。

        :param roaming_registry_method: The roaming_registry_method of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :type roaming_registry_method: str
        """
        self._roaming_registry_method = roaming_registry_method

    @property
    def roaming_registry_path(self):
        r"""Gets the roaming_registry_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        漫游注册路径。

        :return: The roaming_registry_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :rtype: str
        """
        return self._roaming_registry_path

    @roaming_registry_path.setter
    def roaming_registry_path(self, roaming_registry_path):
        r"""Sets the roaming_registry_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.

        漫游注册路径。

        :param roaming_registry_path: The roaming_registry_path of this PoliciesPersonalizedDataMgmtUserDataRoamingOptions.
        :type roaming_registry_path: str
        """
        self._roaming_registry_path = roaming_registry_path

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
        if not isinstance(other, PoliciesPersonalizedDataMgmtUserDataRoamingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
