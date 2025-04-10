# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradePgMajorVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_version': 'str',
        'is_change_private_ip': 'bool',
        'statistics_collection_mode': 'str'
    }

    attribute_map = {
        'target_version': 'target_version',
        'is_change_private_ip': 'is_change_private_ip',
        'statistics_collection_mode': 'statistics_collection_mode'
    }

    def __init__(self, target_version=None, is_change_private_ip=None, statistics_collection_mode=None):
        r"""UpgradePgMajorVersion

        The model defined in huaweicloud sdk

        :param target_version: 目标版本。 高于实例当前的大版本，如当前为12，目标版本需要是13或14。
        :type target_version: str
        :param is_change_private_ip: 是否将实例内网IP切换到大版本实例  true：升级后切换当前实例的内网IP到大版本实例 false：升级后当前实例的内网IP不变，大版本实例使用新的内网IP
        :type is_change_private_ip: bool
        :param statistics_collection_mode: 统计信息收集方式。is_change_private_ip为true时必选  before_change_private_ip：将实例内网IP切换到大版本实例前收集  after_change_private_ip：将实例内网IP切换到大版本实例后收集
        :type statistics_collection_mode: str
        """
        
        

        self._target_version = None
        self._is_change_private_ip = None
        self._statistics_collection_mode = None
        self.discriminator = None

        self.target_version = target_version
        self.is_change_private_ip = is_change_private_ip
        if statistics_collection_mode is not None:
            self.statistics_collection_mode = statistics_collection_mode

    @property
    def target_version(self):
        r"""Gets the target_version of this UpgradePgMajorVersion.

        目标版本。 高于实例当前的大版本，如当前为12，目标版本需要是13或14。

        :return: The target_version of this UpgradePgMajorVersion.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this UpgradePgMajorVersion.

        目标版本。 高于实例当前的大版本，如当前为12，目标版本需要是13或14。

        :param target_version: The target_version of this UpgradePgMajorVersion.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def is_change_private_ip(self):
        r"""Gets the is_change_private_ip of this UpgradePgMajorVersion.

        是否将实例内网IP切换到大版本实例  true：升级后切换当前实例的内网IP到大版本实例 false：升级后当前实例的内网IP不变，大版本实例使用新的内网IP

        :return: The is_change_private_ip of this UpgradePgMajorVersion.
        :rtype: bool
        """
        return self._is_change_private_ip

    @is_change_private_ip.setter
    def is_change_private_ip(self, is_change_private_ip):
        r"""Sets the is_change_private_ip of this UpgradePgMajorVersion.

        是否将实例内网IP切换到大版本实例  true：升级后切换当前实例的内网IP到大版本实例 false：升级后当前实例的内网IP不变，大版本实例使用新的内网IP

        :param is_change_private_ip: The is_change_private_ip of this UpgradePgMajorVersion.
        :type is_change_private_ip: bool
        """
        self._is_change_private_ip = is_change_private_ip

    @property
    def statistics_collection_mode(self):
        r"""Gets the statistics_collection_mode of this UpgradePgMajorVersion.

        统计信息收集方式。is_change_private_ip为true时必选  before_change_private_ip：将实例内网IP切换到大版本实例前收集  after_change_private_ip：将实例内网IP切换到大版本实例后收集

        :return: The statistics_collection_mode of this UpgradePgMajorVersion.
        :rtype: str
        """
        return self._statistics_collection_mode

    @statistics_collection_mode.setter
    def statistics_collection_mode(self, statistics_collection_mode):
        r"""Sets the statistics_collection_mode of this UpgradePgMajorVersion.

        统计信息收集方式。is_change_private_ip为true时必选  before_change_private_ip：将实例内网IP切换到大版本实例前收集  after_change_private_ip：将实例内网IP切换到大版本实例后收集

        :param statistics_collection_mode: The statistics_collection_mode of this UpgradePgMajorVersion.
        :type statistics_collection_mode: str
        """
        self._statistics_collection_mode = statistics_collection_mode

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
        if not isinstance(other, UpgradePgMajorVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
