# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVolumeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'backup_id': 'str',
        'count': 'int',
        'description': 'str',
        'enterprise_project_id': 'str',
        'image_ref': 'str',
        'metadata': 'dict(str, str)',
        'multiattach': 'bool',
        'name': 'str',
        'size': 'int',
        'snapshot_id': 'str',
        'volume_type': 'str',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'backup_id': 'backup_id',
        'count': 'count',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'image_ref': 'imageRef',
        'metadata': 'metadata',
        'multiattach': 'multiattach',
        'name': 'name',
        'size': 'size',
        'snapshot_id': 'snapshot_id',
        'volume_type': 'volume_type',
        'tags': 'tags'
    }

    def __init__(self, availability_zone=None, backup_id=None, count=None, description=None, enterprise_project_id=None, image_ref=None, metadata=None, multiattach=None, name=None, size=None, snapshot_id=None, volume_type=None, tags=None):
        """CreateVolumeOption

        The model defined in huaweicloud sdk

        :param availability_zone: 指定要创建云硬盘的可用区。 获取方法请参见\&quot;[获取可用区](https://apiexplorer.developer.huaweicloud.com/apiexplorer/sdk?product&#x3D;EVS&amp;api&#x3D;CinderListAvailabilityZones)\&quot;。
        :type availability_zone: str
        :param backup_id: 备份ID，从备份创建云硬盘时为必选。
        :type backup_id: str
        :param count: 批量创云硬盘的个数。如果无该参数，表明只创建1个云硬盘，目前最多支持批量创建100个。 从备份创建云硬盘时，不支持批量创建，数量只能为“1”。  如果发送请求时，将参数值设置为小数，则默认取小数点前的整数。
        :type count: int
        :param description: 云硬盘的描述。最大支持255个字节。
        :type description: str
        :param enterprise_project_id: 企业项目ID。创建云硬盘时，给云硬盘绑定企业项目ID。
        :type enterprise_project_id: str
        :param image_ref: 镜像ID，指定该参数表示创建云硬盘方式为从镜像创建云硬盘。
        :type image_ref: str
        :param metadata: 创建云硬盘的metadata信息     可选参数如下:    [\\_\\_system\\_\\_cmkid]   metadata中的加密cmkid字段，与\\_\\_system\\_\\_encrypted配合表示需要加密，cmkid长度固定为36个字节。 &gt; 说明： &gt;  &gt; 请求获取密钥ID的方法请参考：\&quot;[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)\&quot;。   [\\_\\_system\\_\\_encrypted]   metadata中的表示加密功能的字段,0代表不加密,1代表加密。不指定该字段时,云硬盘的加密属性与数据源保持一致,如果不是从数据源创建的场景,则默认不加密。    [full_clone]   从快照创建云硬盘时，如需使用link克隆方式，请指定该字段的值为0。    [hw:passthrough]    * true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。   * false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。   * 该字段不存在时，云硬盘默认为VBD类型。    [create\\_for\\_volume\\_id]  * true表示接口响应中会通过volume_ids字段返回本次创建的云硬盘ID。 * false表示接口响应中不会返回本次创建的云硬盘ID。  该字段不存在时，默认为false。
        :type metadata: dict(str, str)
        :param multiattach: 是否为共享云硬盘。true为共享盘，false为普通云硬盘。
        :type multiattach: bool
        :param name: 云硬盘名称。 如果为创建单个云硬盘，name为云硬盘名称。最大支持255个字节。 创建的云硬盘数量（count字段对应的值）大于1时，为区分不同云硬盘，创建过程中系统会自动在名称后加“-0000”的类似标记。例如：volume-0001、volume-0002。最大支持250个字节。
        :type name: str
        :param size: 云硬盘大小，单位为GB，其限制如下： 系统盘：1GB-1024GB 数据盘：10GB-32768GB 创建空白云硬盘和从 镜像/快照 创建云硬盘时，size为必选，且云硬盘大小不能小于 镜像/快照 大小。 从备份创建云硬盘时，size为可选，不指定size时，云硬盘大小和备份大小一致。
        :type size: int
        :param snapshot_id: 快照ID，指定该参数表示创建云硬盘方式为从快照创建云硬盘
        :type snapshot_id: str
        :param volume_type: 云硬盘类型。  目前支持\&quot;SATA\&quot;，\&quot;SAS\&quot;，\&quot;GPSSD\&quot;，\&quot;SSD\&quot;和\&quot;ESSD\&quot;五种。  - \&quot;SATA\&quot;为普通IO云硬盘(已售罄) - \&quot;SAS\&quot;为高IO云硬盘 - \&quot;GPSSD\&quot;为通用型SSD云硬盘 - \&quot;SSD\&quot;为超高IO云硬盘 - \&quot;ESSD\&quot;为极速IO云硬盘 当指定的云硬盘类型在avaliability_zone内不存在时，则创建云硬盘失败。  说明： 从快照创建云硬盘时，volume_type字段必须和快照源云硬盘保持一致。 了解不同磁盘类型的详细信息，请参见 [磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 获取region可用的卷类型，请参见[查询云硬盘类型列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;EVS&amp;api&#x3D;CinderListVolumeTypes)
        :type volume_type: str
        :param tags: 云硬盘标签信息。
        :type tags: dict(str, str)
        """
        
        

        self._availability_zone = None
        self._backup_id = None
        self._count = None
        self._description = None
        self._enterprise_project_id = None
        self._image_ref = None
        self._metadata = None
        self._multiattach = None
        self._name = None
        self._size = None
        self._snapshot_id = None
        self._volume_type = None
        self._tags = None
        self.discriminator = None

        self.availability_zone = availability_zone
        if backup_id is not None:
            self.backup_id = backup_id
        if count is not None:
            self.count = count
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_ref is not None:
            self.image_ref = image_ref
        if metadata is not None:
            self.metadata = metadata
        if multiattach is not None:
            self.multiattach = multiattach
        if name is not None:
            self.name = name
        self.size = size
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        self.volume_type = volume_type
        if tags is not None:
            self.tags = tags

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateVolumeOption.

        指定要创建云硬盘的可用区。 获取方法请参见\"[获取可用区](https://apiexplorer.developer.huaweicloud.com/apiexplorer/sdk?product=EVS&api=CinderListAvailabilityZones)\"。

        :return: The availability_zone of this CreateVolumeOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateVolumeOption.

        指定要创建云硬盘的可用区。 获取方法请参见\"[获取可用区](https://apiexplorer.developer.huaweicloud.com/apiexplorer/sdk?product=EVS&api=CinderListAvailabilityZones)\"。

        :param availability_zone: The availability_zone of this CreateVolumeOption.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def backup_id(self):
        """Gets the backup_id of this CreateVolumeOption.

        备份ID，从备份创建云硬盘时为必选。

        :return: The backup_id of this CreateVolumeOption.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this CreateVolumeOption.

        备份ID，从备份创建云硬盘时为必选。

        :param backup_id: The backup_id of this CreateVolumeOption.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def count(self):
        """Gets the count of this CreateVolumeOption.

        批量创云硬盘的个数。如果无该参数，表明只创建1个云硬盘，目前最多支持批量创建100个。 从备份创建云硬盘时，不支持批量创建，数量只能为“1”。  如果发送请求时，将参数值设置为小数，则默认取小数点前的整数。

        :return: The count of this CreateVolumeOption.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreateVolumeOption.

        批量创云硬盘的个数。如果无该参数，表明只创建1个云硬盘，目前最多支持批量创建100个。 从备份创建云硬盘时，不支持批量创建，数量只能为“1”。  如果发送请求时，将参数值设置为小数，则默认取小数点前的整数。

        :param count: The count of this CreateVolumeOption.
        :type count: int
        """
        self._count = count

    @property
    def description(self):
        """Gets the description of this CreateVolumeOption.

        云硬盘的描述。最大支持255个字节。

        :return: The description of this CreateVolumeOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateVolumeOption.

        云硬盘的描述。最大支持255个字节。

        :param description: The description of this CreateVolumeOption.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateVolumeOption.

        企业项目ID。创建云硬盘时，给云硬盘绑定企业项目ID。

        :return: The enterprise_project_id of this CreateVolumeOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateVolumeOption.

        企业项目ID。创建云硬盘时，给云硬盘绑定企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateVolumeOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_ref(self):
        """Gets the image_ref of this CreateVolumeOption.

        镜像ID，指定该参数表示创建云硬盘方式为从镜像创建云硬盘。

        :return: The image_ref of this CreateVolumeOption.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this CreateVolumeOption.

        镜像ID，指定该参数表示创建云硬盘方式为从镜像创建云硬盘。

        :param image_ref: The image_ref of this CreateVolumeOption.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def metadata(self):
        """Gets the metadata of this CreateVolumeOption.

        创建云硬盘的metadata信息     可选参数如下:    [\\_\\_system\\_\\_cmkid]   metadata中的加密cmkid字段，与\\_\\_system\\_\\_encrypted配合表示需要加密，cmkid长度固定为36个字节。 > 说明： >  > 请求获取密钥ID的方法请参考：\"[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)\"。   [\\_\\_system\\_\\_encrypted]   metadata中的表示加密功能的字段,0代表不加密,1代表加密。不指定该字段时,云硬盘的加密属性与数据源保持一致,如果不是从数据源创建的场景,则默认不加密。    [full_clone]   从快照创建云硬盘时，如需使用link克隆方式，请指定该字段的值为0。    [hw:passthrough]    * true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。   * false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。   * 该字段不存在时，云硬盘默认为VBD类型。    [create\\_for\\_volume\\_id]  * true表示接口响应中会通过volume_ids字段返回本次创建的云硬盘ID。 * false表示接口响应中不会返回本次创建的云硬盘ID。  该字段不存在时，默认为false。

        :return: The metadata of this CreateVolumeOption.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateVolumeOption.

        创建云硬盘的metadata信息     可选参数如下:    [\\_\\_system\\_\\_cmkid]   metadata中的加密cmkid字段，与\\_\\_system\\_\\_encrypted配合表示需要加密，cmkid长度固定为36个字节。 > 说明： >  > 请求获取密钥ID的方法请参考：\"[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)\"。   [\\_\\_system\\_\\_encrypted]   metadata中的表示加密功能的字段,0代表不加密,1代表加密。不指定该字段时,云硬盘的加密属性与数据源保持一致,如果不是从数据源创建的场景,则默认不加密。    [full_clone]   从快照创建云硬盘时，如需使用link克隆方式，请指定该字段的值为0。    [hw:passthrough]    * true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。   * false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。   * 该字段不存在时，云硬盘默认为VBD类型。    [create\\_for\\_volume\\_id]  * true表示接口响应中会通过volume_ids字段返回本次创建的云硬盘ID。 * false表示接口响应中不会返回本次创建的云硬盘ID。  该字段不存在时，默认为false。

        :param metadata: The metadata of this CreateVolumeOption.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def multiattach(self):
        """Gets the multiattach of this CreateVolumeOption.

        是否为共享云硬盘。true为共享盘，false为普通云硬盘。

        :return: The multiattach of this CreateVolumeOption.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this CreateVolumeOption.

        是否为共享云硬盘。true为共享盘，false为普通云硬盘。

        :param multiattach: The multiattach of this CreateVolumeOption.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def name(self):
        """Gets the name of this CreateVolumeOption.

        云硬盘名称。 如果为创建单个云硬盘，name为云硬盘名称。最大支持255个字节。 创建的云硬盘数量（count字段对应的值）大于1时，为区分不同云硬盘，创建过程中系统会自动在名称后加“-0000”的类似标记。例如：volume-0001、volume-0002。最大支持250个字节。

        :return: The name of this CreateVolumeOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVolumeOption.

        云硬盘名称。 如果为创建单个云硬盘，name为云硬盘名称。最大支持255个字节。 创建的云硬盘数量（count字段对应的值）大于1时，为区分不同云硬盘，创建过程中系统会自动在名称后加“-0000”的类似标记。例如：volume-0001、volume-0002。最大支持250个字节。

        :param name: The name of this CreateVolumeOption.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this CreateVolumeOption.

        云硬盘大小，单位为GB，其限制如下： 系统盘：1GB-1024GB 数据盘：10GB-32768GB 创建空白云硬盘和从 镜像/快照 创建云硬盘时，size为必选，且云硬盘大小不能小于 镜像/快照 大小。 从备份创建云硬盘时，size为可选，不指定size时，云硬盘大小和备份大小一致。

        :return: The size of this CreateVolumeOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateVolumeOption.

        云硬盘大小，单位为GB，其限制如下： 系统盘：1GB-1024GB 数据盘：10GB-32768GB 创建空白云硬盘和从 镜像/快照 创建云硬盘时，size为必选，且云硬盘大小不能小于 镜像/快照 大小。 从备份创建云硬盘时，size为可选，不指定size时，云硬盘大小和备份大小一致。

        :param size: The size of this CreateVolumeOption.
        :type size: int
        """
        self._size = size

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this CreateVolumeOption.

        快照ID，指定该参数表示创建云硬盘方式为从快照创建云硬盘

        :return: The snapshot_id of this CreateVolumeOption.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this CreateVolumeOption.

        快照ID，指定该参数表示创建云硬盘方式为从快照创建云硬盘

        :param snapshot_id: The snapshot_id of this CreateVolumeOption.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def volume_type(self):
        """Gets the volume_type of this CreateVolumeOption.

        云硬盘类型。  目前支持\"SATA\"，\"SAS\"，\"GPSSD\"，\"SSD\"和\"ESSD\"五种。  - \"SATA\"为普通IO云硬盘(已售罄) - \"SAS\"为高IO云硬盘 - \"GPSSD\"为通用型SSD云硬盘 - \"SSD\"为超高IO云硬盘 - \"ESSD\"为极速IO云硬盘 当指定的云硬盘类型在avaliability_zone内不存在时，则创建云硬盘失败。  说明： 从快照创建云硬盘时，volume_type字段必须和快照源云硬盘保持一致。 了解不同磁盘类型的详细信息，请参见 [磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 获取region可用的卷类型，请参见[查询云硬盘类型列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=EVS&api=CinderListVolumeTypes)

        :return: The volume_type of this CreateVolumeOption.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this CreateVolumeOption.

        云硬盘类型。  目前支持\"SATA\"，\"SAS\"，\"GPSSD\"，\"SSD\"和\"ESSD\"五种。  - \"SATA\"为普通IO云硬盘(已售罄) - \"SAS\"为高IO云硬盘 - \"GPSSD\"为通用型SSD云硬盘 - \"SSD\"为超高IO云硬盘 - \"ESSD\"为极速IO云硬盘 当指定的云硬盘类型在avaliability_zone内不存在时，则创建云硬盘失败。  说明： 从快照创建云硬盘时，volume_type字段必须和快照源云硬盘保持一致。 了解不同磁盘类型的详细信息，请参见 [磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 获取region可用的卷类型，请参见[查询云硬盘类型列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=EVS&api=CinderListVolumeTypes)

        :param volume_type: The volume_type of this CreateVolumeOption.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def tags(self):
        """Gets the tags of this CreateVolumeOption.

        云硬盘标签信息。

        :return: The tags of this CreateVolumeOption.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateVolumeOption.

        云硬盘标签信息。

        :param tags: The tags of this CreateVolumeOption.
        :type tags: dict(str, str)
        """
        self._tags = tags

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
        if not isinstance(other, CreateVolumeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
