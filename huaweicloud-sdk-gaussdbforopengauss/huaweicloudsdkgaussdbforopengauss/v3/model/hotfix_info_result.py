# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotfixInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'common_patch': 'str',
        'backup_sensitive': 'bool',
        'descripition': 'str'
    }

    attribute_map = {
        'version': 'version',
        'common_patch': 'common_patch',
        'backup_sensitive': 'backup_sensitive',
        'descripition': 'descripition'
    }

    def __init__(self, version=None, common_patch=None, backup_sensitive=None, descripition=None):
        r"""HotfixInfoResult

        The model defined in huaweicloud sdk

        :param version: 热补丁版本
        :type version: str
        :param common_patch: 通用非通用信息,common&#x3D;通用补丁,certain&#x3D;定制补丁
        :type common_patch: str
        :param backup_sensitive: 是否和备份相关
        :type backup_sensitive: bool
        :param descripition: 补丁的描述信息
        :type descripition: str
        """
        
        

        self._version = None
        self._common_patch = None
        self._backup_sensitive = None
        self._descripition = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if common_patch is not None:
            self.common_patch = common_patch
        if backup_sensitive is not None:
            self.backup_sensitive = backup_sensitive
        if descripition is not None:
            self.descripition = descripition

    @property
    def version(self):
        r"""Gets the version of this HotfixInfoResult.

        热补丁版本

        :return: The version of this HotfixInfoResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this HotfixInfoResult.

        热补丁版本

        :param version: The version of this HotfixInfoResult.
        :type version: str
        """
        self._version = version

    @property
    def common_patch(self):
        r"""Gets the common_patch of this HotfixInfoResult.

        通用非通用信息,common=通用补丁,certain=定制补丁

        :return: The common_patch of this HotfixInfoResult.
        :rtype: str
        """
        return self._common_patch

    @common_patch.setter
    def common_patch(self, common_patch):
        r"""Sets the common_patch of this HotfixInfoResult.

        通用非通用信息,common=通用补丁,certain=定制补丁

        :param common_patch: The common_patch of this HotfixInfoResult.
        :type common_patch: str
        """
        self._common_patch = common_patch

    @property
    def backup_sensitive(self):
        r"""Gets the backup_sensitive of this HotfixInfoResult.

        是否和备份相关

        :return: The backup_sensitive of this HotfixInfoResult.
        :rtype: bool
        """
        return self._backup_sensitive

    @backup_sensitive.setter
    def backup_sensitive(self, backup_sensitive):
        r"""Sets the backup_sensitive of this HotfixInfoResult.

        是否和备份相关

        :param backup_sensitive: The backup_sensitive of this HotfixInfoResult.
        :type backup_sensitive: bool
        """
        self._backup_sensitive = backup_sensitive

    @property
    def descripition(self):
        r"""Gets the descripition of this HotfixInfoResult.

        补丁的描述信息

        :return: The descripition of this HotfixInfoResult.
        :rtype: str
        """
        return self._descripition

    @descripition.setter
    def descripition(self, descripition):
        r"""Sets the descripition of this HotfixInfoResult.

        补丁的描述信息

        :param descripition: The descripition of this HotfixInfoResult.
        :type descripition: str
        """
        self._descripition = descripition

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
        if not isinstance(other, HotfixInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
