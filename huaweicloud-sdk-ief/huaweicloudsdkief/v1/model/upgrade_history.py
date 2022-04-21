# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'from_version': 'str',
        'to_version': 'str',
        'upgrade_time': 'int',
        'result': 'str',
        'dur_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'from_version': 'from_version',
        'to_version': 'to_version',
        'upgrade_time': 'upgrade_time',
        'result': 'result',
        'dur_time': 'dur_time'
    }

    def __init__(self, id=None, from_version=None, to_version=None, upgrade_time=None, result=None, dur_time=None):
        """UpgradeHistory

        The model defined in huaweicloud sdk

        :param id: 节点升级或安装历史版本id
        :type id: int
        :param from_version: 节点升级前节点上edgecore版本号，形式如2.1.0，其中每一位都是整数
        :type from_version: str
        :param to_version: 节点升级或安装后节点行edgecore版本号，形式如2.1.0，其中每一位都是整数
        :type to_version: str
        :param upgrade_time: 节点升级或安装的十位时间戳
        :type upgrade_time: int
        :param result: 节点升级或安装状态，包含 - install_success：边缘节点安装成功 - upgrade_success：边缘节点升级成功 - install_failed：边缘节点安装失败 - upgrade_failed：边缘节点升级失败 - upgrade_failed_rollback_success：边缘节点升级失败回滚成功 - upgrade_failed_rollback_failed：边缘节点升级失败回滚失败
        :type result: str
        :param dur_time: 节点升级所消耗的时间
        :type dur_time: int
        """
        
        

        self._id = None
        self._from_version = None
        self._to_version = None
        self._upgrade_time = None
        self._result = None
        self._dur_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if from_version is not None:
            self.from_version = from_version
        if to_version is not None:
            self.to_version = to_version
        if upgrade_time is not None:
            self.upgrade_time = upgrade_time
        if result is not None:
            self.result = result
        if dur_time is not None:
            self.dur_time = dur_time

    @property
    def id(self):
        """Gets the id of this UpgradeHistory.

        节点升级或安装历史版本id

        :return: The id of this UpgradeHistory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpgradeHistory.

        节点升级或安装历史版本id

        :param id: The id of this UpgradeHistory.
        :type id: int
        """
        self._id = id

    @property
    def from_version(self):
        """Gets the from_version of this UpgradeHistory.

        节点升级前节点上edgecore版本号，形式如2.1.0，其中每一位都是整数

        :return: The from_version of this UpgradeHistory.
        :rtype: str
        """
        return self._from_version

    @from_version.setter
    def from_version(self, from_version):
        """Sets the from_version of this UpgradeHistory.

        节点升级前节点上edgecore版本号，形式如2.1.0，其中每一位都是整数

        :param from_version: The from_version of this UpgradeHistory.
        :type from_version: str
        """
        self._from_version = from_version

    @property
    def to_version(self):
        """Gets the to_version of this UpgradeHistory.

        节点升级或安装后节点行edgecore版本号，形式如2.1.0，其中每一位都是整数

        :return: The to_version of this UpgradeHistory.
        :rtype: str
        """
        return self._to_version

    @to_version.setter
    def to_version(self, to_version):
        """Sets the to_version of this UpgradeHistory.

        节点升级或安装后节点行edgecore版本号，形式如2.1.0，其中每一位都是整数

        :param to_version: The to_version of this UpgradeHistory.
        :type to_version: str
        """
        self._to_version = to_version

    @property
    def upgrade_time(self):
        """Gets the upgrade_time of this UpgradeHistory.

        节点升级或安装的十位时间戳

        :return: The upgrade_time of this UpgradeHistory.
        :rtype: int
        """
        return self._upgrade_time

    @upgrade_time.setter
    def upgrade_time(self, upgrade_time):
        """Sets the upgrade_time of this UpgradeHistory.

        节点升级或安装的十位时间戳

        :param upgrade_time: The upgrade_time of this UpgradeHistory.
        :type upgrade_time: int
        """
        self._upgrade_time = upgrade_time

    @property
    def result(self):
        """Gets the result of this UpgradeHistory.

        节点升级或安装状态，包含 - install_success：边缘节点安装成功 - upgrade_success：边缘节点升级成功 - install_failed：边缘节点安装失败 - upgrade_failed：边缘节点升级失败 - upgrade_failed_rollback_success：边缘节点升级失败回滚成功 - upgrade_failed_rollback_failed：边缘节点升级失败回滚失败

        :return: The result of this UpgradeHistory.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this UpgradeHistory.

        节点升级或安装状态，包含 - install_success：边缘节点安装成功 - upgrade_success：边缘节点升级成功 - install_failed：边缘节点安装失败 - upgrade_failed：边缘节点升级失败 - upgrade_failed_rollback_success：边缘节点升级失败回滚成功 - upgrade_failed_rollback_failed：边缘节点升级失败回滚失败

        :param result: The result of this UpgradeHistory.
        :type result: str
        """
        self._result = result

    @property
    def dur_time(self):
        """Gets the dur_time of this UpgradeHistory.

        节点升级所消耗的时间

        :return: The dur_time of this UpgradeHistory.
        :rtype: int
        """
        return self._dur_time

    @dur_time.setter
    def dur_time(self, dur_time):
        """Sets the dur_time of this UpgradeHistory.

        节点升级所消耗的时间

        :param dur_time: The dur_time of this UpgradeHistory.
        :type dur_time: int
        """
        self._dur_time = dur_time

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
        if not isinstance(other, UpgradeHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
