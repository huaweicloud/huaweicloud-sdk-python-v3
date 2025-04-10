# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServerDataVolumeExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'resource_type': 'str',
        'snapshot_id': 'str'
    }

    attribute_map = {
        'resource_spec_code': 'resourceSpecCode',
        'resource_type': 'resourceType',
        'snapshot_id': 'snapshotId'
    }

    def __init__(self, resource_spec_code=None, resource_type=None, snapshot_id=None):
        r"""PrePaidServerDataVolumeExtendParam

        The model defined in huaweicloud sdk

        :param resource_spec_code: 磁盘产品资源规格编码，如SATA，SAS和SSD。  &gt; 说明： &gt;  &gt; 废弃字段。
        :type resource_spec_code: str
        :param resource_type: 磁盘产品资源类型。  &gt; 说明： &gt;  &gt; 废弃字段。
        :type resource_type: str
        :param snapshot_id: 整机镜像中自带的原始数据盘（简称“原数据盘”）所对应的快照ID或原始数据盘ID。  使用场景：  使用整机镜像创建云服务器，并且选择的整机镜像自带1个或者多个数据盘。  用途：  使用整机镜像创建云服务器时，系统会自动恢复整机镜像中自带数据盘（如果有）的数据，但是磁盘类型将被恢复为默认属性：普通I/O、VBD、非共享盘。此时，您可以通过snapshotID，修改指定原数据盘恢复后的磁盘类型。  &gt; 说明： &gt;  &gt; 建议对每块原数据盘都指定snapshotID，否则，未指定的原数据盘将按默认属性进行创建。 &gt; 如需修改磁盘大小，修改后的磁盘大小需大于等于原数据盘大小。否则，会影响原数据盘的数据恢复。  实现原理：  snapshotId是整机镜像自带原始数据盘的唯一标识，通过snapshotId可以获取原数据盘的磁盘信息，从而恢复数据盘数据。  快照ID的获取方法：  登录管理控制台，打开\&quot;云硬盘 &gt; 快照\&quot;页面，根据原始数据盘的磁盘名称找到对应的快照ID。
        :type snapshot_id: str
        """
        
        

        self._resource_spec_code = None
        self._resource_type = None
        self._snapshot_id = None
        self.discriminator = None

        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_type is not None:
            self.resource_type = resource_type
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this PrePaidServerDataVolumeExtendParam.

        磁盘产品资源规格编码，如SATA，SAS和SSD。  > 说明： >  > 废弃字段。

        :return: The resource_spec_code of this PrePaidServerDataVolumeExtendParam.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this PrePaidServerDataVolumeExtendParam.

        磁盘产品资源规格编码，如SATA，SAS和SSD。  > 说明： >  > 废弃字段。

        :param resource_spec_code: The resource_spec_code of this PrePaidServerDataVolumeExtendParam.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_type(self):
        r"""Gets the resource_type of this PrePaidServerDataVolumeExtendParam.

        磁盘产品资源类型。  > 说明： >  > 废弃字段。

        :return: The resource_type of this PrePaidServerDataVolumeExtendParam.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this PrePaidServerDataVolumeExtendParam.

        磁盘产品资源类型。  > 说明： >  > 废弃字段。

        :param resource_type: The resource_type of this PrePaidServerDataVolumeExtendParam.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def snapshot_id(self):
        r"""Gets the snapshot_id of this PrePaidServerDataVolumeExtendParam.

        整机镜像中自带的原始数据盘（简称“原数据盘”）所对应的快照ID或原始数据盘ID。  使用场景：  使用整机镜像创建云服务器，并且选择的整机镜像自带1个或者多个数据盘。  用途：  使用整机镜像创建云服务器时，系统会自动恢复整机镜像中自带数据盘（如果有）的数据，但是磁盘类型将被恢复为默认属性：普通I/O、VBD、非共享盘。此时，您可以通过snapshotID，修改指定原数据盘恢复后的磁盘类型。  > 说明： >  > 建议对每块原数据盘都指定snapshotID，否则，未指定的原数据盘将按默认属性进行创建。 > 如需修改磁盘大小，修改后的磁盘大小需大于等于原数据盘大小。否则，会影响原数据盘的数据恢复。  实现原理：  snapshotId是整机镜像自带原始数据盘的唯一标识，通过snapshotId可以获取原数据盘的磁盘信息，从而恢复数据盘数据。  快照ID的获取方法：  登录管理控制台，打开\"云硬盘 > 快照\"页面，根据原始数据盘的磁盘名称找到对应的快照ID。

        :return: The snapshot_id of this PrePaidServerDataVolumeExtendParam.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        r"""Sets the snapshot_id of this PrePaidServerDataVolumeExtendParam.

        整机镜像中自带的原始数据盘（简称“原数据盘”）所对应的快照ID或原始数据盘ID。  使用场景：  使用整机镜像创建云服务器，并且选择的整机镜像自带1个或者多个数据盘。  用途：  使用整机镜像创建云服务器时，系统会自动恢复整机镜像中自带数据盘（如果有）的数据，但是磁盘类型将被恢复为默认属性：普通I/O、VBD、非共享盘。此时，您可以通过snapshotID，修改指定原数据盘恢复后的磁盘类型。  > 说明： >  > 建议对每块原数据盘都指定snapshotID，否则，未指定的原数据盘将按默认属性进行创建。 > 如需修改磁盘大小，修改后的磁盘大小需大于等于原数据盘大小。否则，会影响原数据盘的数据恢复。  实现原理：  snapshotId是整机镜像自带原始数据盘的唯一标识，通过snapshotId可以获取原数据盘的磁盘信息，从而恢复数据盘数据。  快照ID的获取方法：  登录管理控制台，打开\"云硬盘 > 快照\"页面，根据原始数据盘的磁盘名称找到对应的快照ID。

        :param snapshot_id: The snapshot_id of this PrePaidServerDataVolumeExtendParam.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

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
        if not isinstance(other, PrePaidServerDataVolumeExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
