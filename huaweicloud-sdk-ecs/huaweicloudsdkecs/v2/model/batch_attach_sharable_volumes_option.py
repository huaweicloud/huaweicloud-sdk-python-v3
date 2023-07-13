# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAttachSharableVolumesOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'device': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'device': 'device'
    }

    def __init__(self, server_id=None, device=None):
        """BatchAttachSharableVolumesOption

        The model defined in huaweicloud sdk

        :param server_id: 共享磁盘需要挂载的弹性云服务器ID。
        :type server_id: str
        :param device: 磁盘挂载点。  &gt; 说明： &gt;  &gt; - 新增加的磁盘挂载点不能和已有的磁盘挂载点相同。 &gt; - 对于采用XEN虚拟化类型的弹性云服务器，device为必选参数；系统盘挂载点请指定/dev/sda；数据盘挂载点请按英文字母顺序依次指定，如/dev/sdb，/dev/sdc，如果指定了以“/dev/vd”开头的挂载点，系统默认改为“/dev/sd”。 &gt; - 对于采用KVM虚拟化类型的弹性云服务器，系统盘挂载点请指定/dev/vda；数据盘挂载点可不用指定，也可按英文字母顺序依次指定，如/dev/vdb，/dev/vdc，如果指定了以“/dev/sd”开头的挂载点，系统默认改为“/dev/vd”。
        :type device: str
        """
        
        

        self._server_id = None
        self._device = None
        self.discriminator = None

        self.server_id = server_id
        if device is not None:
            self.device = device

    @property
    def server_id(self):
        """Gets the server_id of this BatchAttachSharableVolumesOption.

        共享磁盘需要挂载的弹性云服务器ID。

        :return: The server_id of this BatchAttachSharableVolumesOption.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this BatchAttachSharableVolumesOption.

        共享磁盘需要挂载的弹性云服务器ID。

        :param server_id: The server_id of this BatchAttachSharableVolumesOption.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def device(self):
        """Gets the device of this BatchAttachSharableVolumesOption.

        磁盘挂载点。  > 说明： >  > - 新增加的磁盘挂载点不能和已有的磁盘挂载点相同。 > - 对于采用XEN虚拟化类型的弹性云服务器，device为必选参数；系统盘挂载点请指定/dev/sda；数据盘挂载点请按英文字母顺序依次指定，如/dev/sdb，/dev/sdc，如果指定了以“/dev/vd”开头的挂载点，系统默认改为“/dev/sd”。 > - 对于采用KVM虚拟化类型的弹性云服务器，系统盘挂载点请指定/dev/vda；数据盘挂载点可不用指定，也可按英文字母顺序依次指定，如/dev/vdb，/dev/vdc，如果指定了以“/dev/sd”开头的挂载点，系统默认改为“/dev/vd”。

        :return: The device of this BatchAttachSharableVolumesOption.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this BatchAttachSharableVolumesOption.

        磁盘挂载点。  > 说明： >  > - 新增加的磁盘挂载点不能和已有的磁盘挂载点相同。 > - 对于采用XEN虚拟化类型的弹性云服务器，device为必选参数；系统盘挂载点请指定/dev/sda；数据盘挂载点请按英文字母顺序依次指定，如/dev/sdb，/dev/sdc，如果指定了以“/dev/vd”开头的挂载点，系统默认改为“/dev/sd”。 > - 对于采用KVM虚拟化类型的弹性云服务器，系统盘挂载点请指定/dev/vda；数据盘挂载点可不用指定，也可按英文字母顺序依次指定，如/dev/vdb，/dev/vdc，如果指定了以“/dev/sd”开头的挂载点，系统默认改为“/dev/vd”。

        :param device: The device of this BatchAttachSharableVolumesOption.
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
        if not isinstance(other, BatchAttachSharableVolumesOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
