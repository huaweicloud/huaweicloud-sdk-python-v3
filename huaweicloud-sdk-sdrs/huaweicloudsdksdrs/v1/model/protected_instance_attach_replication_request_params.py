# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectedInstanceAttachReplicationRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replication_id': 'str',
        'device': 'str'
    }

    attribute_map = {
        'replication_id': 'replication_id',
        'device': 'device'
    }

    def __init__(self, replication_id=None, device=None):
        r"""ProtectedInstanceAttachReplicationRequestParams

        The model defined in huaweicloud sdk

        :param replication_id: 复制对的ID。
        :type replication_id: str
        :param device: 复制对中使用的磁盘挂载点。  说明:新增加的磁盘挂载点不能和已有的磁盘挂载点相同。 对于采用XEN虚拟化类型的弹性云服务器组成的保护实例，系统盘挂载点请指定/dev/sda；数据盘挂载点请按英文字母顺序依次指定，如/dev/sdb，/dev/sdc，如果指定了以“/dev/vd”开头的挂载点，系统默认改为“/dev/sd”。对于采用KVM虚拟化类型的弹性云服务器组成的保护实例，系统盘挂载点请指定/dev/vda；数据盘挂载点请按英文字母顺序依次指定，如/dev/vdb，/dev/vdc，如果指定了以“/dev/sd”开头的挂载点，系统默认改为“/dev/vd”。
        :type device: str
        """
        
        

        self._replication_id = None
        self._device = None
        self.discriminator = None

        self.replication_id = replication_id
        self.device = device

    @property
    def replication_id(self):
        r"""Gets the replication_id of this ProtectedInstanceAttachReplicationRequestParams.

        复制对的ID。

        :return: The replication_id of this ProtectedInstanceAttachReplicationRequestParams.
        :rtype: str
        """
        return self._replication_id

    @replication_id.setter
    def replication_id(self, replication_id):
        r"""Sets the replication_id of this ProtectedInstanceAttachReplicationRequestParams.

        复制对的ID。

        :param replication_id: The replication_id of this ProtectedInstanceAttachReplicationRequestParams.
        :type replication_id: str
        """
        self._replication_id = replication_id

    @property
    def device(self):
        r"""Gets the device of this ProtectedInstanceAttachReplicationRequestParams.

        复制对中使用的磁盘挂载点。  说明:新增加的磁盘挂载点不能和已有的磁盘挂载点相同。 对于采用XEN虚拟化类型的弹性云服务器组成的保护实例，系统盘挂载点请指定/dev/sda；数据盘挂载点请按英文字母顺序依次指定，如/dev/sdb，/dev/sdc，如果指定了以“/dev/vd”开头的挂载点，系统默认改为“/dev/sd”。对于采用KVM虚拟化类型的弹性云服务器组成的保护实例，系统盘挂载点请指定/dev/vda；数据盘挂载点请按英文字母顺序依次指定，如/dev/vdb，/dev/vdc，如果指定了以“/dev/sd”开头的挂载点，系统默认改为“/dev/vd”。

        :return: The device of this ProtectedInstanceAttachReplicationRequestParams.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        r"""Sets the device of this ProtectedInstanceAttachReplicationRequestParams.

        复制对中使用的磁盘挂载点。  说明:新增加的磁盘挂载点不能和已有的磁盘挂载点相同。 对于采用XEN虚拟化类型的弹性云服务器组成的保护实例，系统盘挂载点请指定/dev/sda；数据盘挂载点请按英文字母顺序依次指定，如/dev/sdb，/dev/sdc，如果指定了以“/dev/vd”开头的挂载点，系统默认改为“/dev/sd”。对于采用KVM虚拟化类型的弹性云服务器组成的保护实例，系统盘挂载点请指定/dev/vda；数据盘挂载点请按英文字母顺序依次指定，如/dev/vdb，/dev/vdc，如果指定了以“/dev/sd”开头的挂载点，系统默认改为“/dev/vd”。

        :param device: The device of this ProtectedInstanceAttachReplicationRequestParams.
        :type device: str
        """
        self._device = device

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
        if not isinstance(other, ProtectedInstanceAttachReplicationRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
