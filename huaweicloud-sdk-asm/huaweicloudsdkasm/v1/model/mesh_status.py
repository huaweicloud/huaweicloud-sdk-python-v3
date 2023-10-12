# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MeshStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'phase': 'phase',
        'updated_at': 'updatedAt'
    }

    def __init__(self, phase=None, updated_at=None):
        """MeshStatus

        The model defined in huaweicloud sdk

        :param phase: 网格状态，取值如下 - Running：运行中，表示网格处于正常运行状态。 - Creating：创建中，表示网格正处于创建过程中。 - CreateFailed：创建失败。 - Deleting：删除中，表示网格正处于删除过程中。 - DeleteFailed：删除失败。 - Upgrading：升级中，表示网格正处于升级过程中。 - UpgradeFailed：升级失败。 - RollingBack：回滚中，表示网格正处于回滚过程中。 - RollbackFailed：回滚失败。
        :type phase: str
        :param updated_at: 网格更新时间
        :type updated_at: datetime
        """
        
        

        self._phase = None
        self._updated_at = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def phase(self):
        """Gets the phase of this MeshStatus.

        网格状态，取值如下 - Running：运行中，表示网格处于正常运行状态。 - Creating：创建中，表示网格正处于创建过程中。 - CreateFailed：创建失败。 - Deleting：删除中，表示网格正处于删除过程中。 - DeleteFailed：删除失败。 - Upgrading：升级中，表示网格正处于升级过程中。 - UpgradeFailed：升级失败。 - RollingBack：回滚中，表示网格正处于回滚过程中。 - RollbackFailed：回滚失败。

        :return: The phase of this MeshStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this MeshStatus.

        网格状态，取值如下 - Running：运行中，表示网格处于正常运行状态。 - Creating：创建中，表示网格正处于创建过程中。 - CreateFailed：创建失败。 - Deleting：删除中，表示网格正处于删除过程中。 - DeleteFailed：删除失败。 - Upgrading：升级中，表示网格正处于升级过程中。 - UpgradeFailed：升级失败。 - RollingBack：回滚中，表示网格正处于回滚过程中。 - RollbackFailed：回滚失败。

        :param phase: The phase of this MeshStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def updated_at(self):
        """Gets the updated_at of this MeshStatus.

        网格更新时间

        :return: The updated_at of this MeshStatus.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MeshStatus.

        网格更新时间

        :param updated_at: The updated_at of this MeshStatus.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, MeshStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
