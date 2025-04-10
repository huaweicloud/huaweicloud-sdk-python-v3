# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSnapshotOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'force': 'bool',
        'metadata': 'dict(str, str)',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'force': 'force',
        'metadata': 'metadata',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, volume_id=None, force=None, metadata=None, description=None, name=None):
        r"""CreateSnapshotOption

        The model defined in huaweicloud sdk

        :param volume_id: 源云硬盘的ID。
        :type volume_id: str
        :param force: 强制创快照标示，默认为false。 当force标记为false时，云硬盘处于挂载状态时，不能强制创建快照。 当force标记为true时，即使云硬盘处于挂载状态时，仍可以创建快照。
        :type force: bool
        :param metadata: 云硬盘快照的元数据信息。
        :type metadata: dict(str, str)
        :param description: 云硬盘快照描述，最大支持255个字节。
        :type description: str
        :param name: 云硬盘快照名称。最大支持255个字节。  &gt; &gt; 说明： &gt; 对云硬盘创建备份时，同时会创建以autobk_snapshot_为名称前缀的快照，云硬盘控制台对此类快照会有操作限制。因此建议不要创建以&gt; &gt; autobk_snapshot_为名称前缀的快照，避免影响快照的正常使用
        :type name: str
        """
        
        

        self._volume_id = None
        self._force = None
        self._metadata = None
        self._description = None
        self._name = None
        self.discriminator = None

        self.volume_id = volume_id
        if force is not None:
            self.force = force
        if metadata is not None:
            self.metadata = metadata
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def volume_id(self):
        r"""Gets the volume_id of this CreateSnapshotOption.

        源云硬盘的ID。

        :return: The volume_id of this CreateSnapshotOption.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this CreateSnapshotOption.

        源云硬盘的ID。

        :param volume_id: The volume_id of this CreateSnapshotOption.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def force(self):
        r"""Gets the force of this CreateSnapshotOption.

        强制创快照标示，默认为false。 当force标记为false时，云硬盘处于挂载状态时，不能强制创建快照。 当force标记为true时，即使云硬盘处于挂载状态时，仍可以创建快照。

        :return: The force of this CreateSnapshotOption.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        r"""Sets the force of this CreateSnapshotOption.

        强制创快照标示，默认为false。 当force标记为false时，云硬盘处于挂载状态时，不能强制创建快照。 当force标记为true时，即使云硬盘处于挂载状态时，仍可以创建快照。

        :param force: The force of this CreateSnapshotOption.
        :type force: bool
        """
        self._force = force

    @property
    def metadata(self):
        r"""Gets the metadata of this CreateSnapshotOption.

        云硬盘快照的元数据信息。

        :return: The metadata of this CreateSnapshotOption.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CreateSnapshotOption.

        云硬盘快照的元数据信息。

        :param metadata: The metadata of this CreateSnapshotOption.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def description(self):
        r"""Gets the description of this CreateSnapshotOption.

        云硬盘快照描述，最大支持255个字节。

        :return: The description of this CreateSnapshotOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSnapshotOption.

        云硬盘快照描述，最大支持255个字节。

        :param description: The description of this CreateSnapshotOption.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this CreateSnapshotOption.

        云硬盘快照名称。最大支持255个字节。  > > 说明： > 对云硬盘创建备份时，同时会创建以autobk_snapshot_为名称前缀的快照，云硬盘控制台对此类快照会有操作限制。因此建议不要创建以> > autobk_snapshot_为名称前缀的快照，避免影响快照的正常使用

        :return: The name of this CreateSnapshotOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSnapshotOption.

        云硬盘快照名称。最大支持255个字节。  > > 说明： > 对云硬盘创建备份时，同时会创建以autobk_snapshot_为名称前缀的快照，云硬盘控制台对此类快照会有操作限制。因此建议不要创建以> > autobk_snapshot_为名称前缀的快照，避免影响快照的正常使用

        :param name: The name of this CreateSnapshotOption.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateSnapshotOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
