# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceDatastore:

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
        'target_version': 'str',
        'complete_kernel_version': 'str',
        'hotfix_version_infos': 'list[HotfixVersionInfo]'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'complete_version': 'complete_version',
        'target_version': 'target_version',
        'complete_kernel_version': 'complete_kernel_version',
        'hotfix_version_infos': 'hotfix_version_infos'
    }

    def __init__(self, type=None, version=None, complete_version=None, target_version=None, complete_kernel_version=None, hotfix_version_infos=None):
        """ListInstanceDatastore

        The model defined in huaweicloud sdk

        :param type: 数据库引擎。
        :type type: str
        :param version: 数据库大版本。
        :type version: str
        :param complete_version: 数据库小版本。
        :type complete_version: str
        :param target_version: 数据库正在升级的目标版本。
        :type target_version: str
        :param complete_kernel_version: 数据库内核版本
        :type complete_kernel_version: str
        :param hotfix_version_infos: 热补丁信息列表
        :type hotfix_version_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HotfixVersionInfo`]
        """
        
        

        self._type = None
        self._version = None
        self._complete_version = None
        self._target_version = None
        self._complete_kernel_version = None
        self._hotfix_version_infos = None
        self.discriminator = None

        self.type = type
        self.version = version
        if complete_version is not None:
            self.complete_version = complete_version
        if target_version is not None:
            self.target_version = target_version
        if complete_kernel_version is not None:
            self.complete_kernel_version = complete_kernel_version
        if hotfix_version_infos is not None:
            self.hotfix_version_infos = hotfix_version_infos

    @property
    def type(self):
        """Gets the type of this ListInstanceDatastore.

        数据库引擎。

        :return: The type of this ListInstanceDatastore.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInstanceDatastore.

        数据库引擎。

        :param type: The type of this ListInstanceDatastore.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListInstanceDatastore.

        数据库大版本。

        :return: The version of this ListInstanceDatastore.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListInstanceDatastore.

        数据库大版本。

        :param version: The version of this ListInstanceDatastore.
        :type version: str
        """
        self._version = version

    @property
    def complete_version(self):
        """Gets the complete_version of this ListInstanceDatastore.

        数据库小版本。

        :return: The complete_version of this ListInstanceDatastore.
        :rtype: str
        """
        return self._complete_version

    @complete_version.setter
    def complete_version(self, complete_version):
        """Sets the complete_version of this ListInstanceDatastore.

        数据库小版本。

        :param complete_version: The complete_version of this ListInstanceDatastore.
        :type complete_version: str
        """
        self._complete_version = complete_version

    @property
    def target_version(self):
        """Gets the target_version of this ListInstanceDatastore.

        数据库正在升级的目标版本。

        :return: The target_version of this ListInstanceDatastore.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this ListInstanceDatastore.

        数据库正在升级的目标版本。

        :param target_version: The target_version of this ListInstanceDatastore.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def complete_kernel_version(self):
        """Gets the complete_kernel_version of this ListInstanceDatastore.

        数据库内核版本

        :return: The complete_kernel_version of this ListInstanceDatastore.
        :rtype: str
        """
        return self._complete_kernel_version

    @complete_kernel_version.setter
    def complete_kernel_version(self, complete_kernel_version):
        """Sets the complete_kernel_version of this ListInstanceDatastore.

        数据库内核版本

        :param complete_kernel_version: The complete_kernel_version of this ListInstanceDatastore.
        :type complete_kernel_version: str
        """
        self._complete_kernel_version = complete_kernel_version

    @property
    def hotfix_version_infos(self):
        """Gets the hotfix_version_infos of this ListInstanceDatastore.

        热补丁信息列表

        :return: The hotfix_version_infos of this ListInstanceDatastore.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HotfixVersionInfo`]
        """
        return self._hotfix_version_infos

    @hotfix_version_infos.setter
    def hotfix_version_infos(self, hotfix_version_infos):
        """Sets the hotfix_version_infos of this ListInstanceDatastore.

        热补丁信息列表

        :param hotfix_version_infos: The hotfix_version_infos of this ListInstanceDatastore.
        :type hotfix_version_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HotfixVersionInfo`]
        """
        self._hotfix_version_infos = hotfix_version_infos

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
        if not isinstance(other, ListInstanceDatastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
