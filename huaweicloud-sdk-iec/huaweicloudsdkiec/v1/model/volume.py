# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Volume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'size': 'int',
        'availability_zone': 'str',
        'attachments': 'list[Attachment]',
        'name': 'str',
        'description': 'str',
        'volume_type': 'str',
        'bootable': 'str',
        'encrypted': 'bool',
        'multiattach': 'bool',
        'metadata': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'size': 'size',
        'availability_zone': 'availability_zone',
        'attachments': 'attachments',
        'name': 'name',
        'description': 'description',
        'volume_type': 'volume_type',
        'bootable': 'bootable',
        'encrypted': 'encrypted',
        'multiattach': 'multiattach',
        'metadata': 'metadata'
    }

    def __init__(self, id=None, status=None, size=None, availability_zone=None, attachments=None, name=None, description=None, volume_type=None, bootable=None, encrypted=None, multiattach=None, metadata=None):
        """Volume

        The model defined in huaweicloud sdk

        :param id: 硬盘ID。
        :type id: str
        :param status: 磁盘状态。
        :type status: str
        :param size: 磁盘大小。
        :type size: int
        :param availability_zone: 硬盘所属的AZ信息。
        :type availability_zone: str
        :param attachments: 硬盘的挂载信息。
        :type attachments: list[:class:`huaweicloudsdkiec.v1.Attachment`]
        :param name: 磁盘名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param volume_type: 磁盘类型。
        :type volume_type: str
        :param bootable: 显示这个卷是否可启动。
        :type bootable: str
        :param encrypted: 显示该卷是否已被加密。
        :type encrypted: bool
        :param multiattach: 磁盘是否多挂载。
        :type multiattach: bool
        :param metadata: 硬盘的元数据。
        :type metadata: dict(str, str)
        """
        
        

        self._id = None
        self._status = None
        self._size = None
        self._availability_zone = None
        self._attachments = None
        self._name = None
        self._description = None
        self._volume_type = None
        self._bootable = None
        self._encrypted = None
        self._multiattach = None
        self._metadata = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if size is not None:
            self.size = size
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if attachments is not None:
            self.attachments = attachments
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if volume_type is not None:
            self.volume_type = volume_type
        if bootable is not None:
            self.bootable = bootable
        if encrypted is not None:
            self.encrypted = encrypted
        self.multiattach = multiattach
        if metadata is not None:
            self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this Volume.

        硬盘ID。

        :return: The id of this Volume.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Volume.

        硬盘ID。

        :param id: The id of this Volume.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this Volume.

        磁盘状态。

        :return: The status of this Volume.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Volume.

        磁盘状态。

        :param status: The status of this Volume.
        :type status: str
        """
        self._status = status

    @property
    def size(self):
        """Gets the size of this Volume.

        磁盘大小。

        :return: The size of this Volume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Volume.

        磁盘大小。

        :param size: The size of this Volume.
        :type size: int
        """
        self._size = size

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Volume.

        硬盘所属的AZ信息。

        :return: The availability_zone of this Volume.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Volume.

        硬盘所属的AZ信息。

        :param availability_zone: The availability_zone of this Volume.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def attachments(self):
        """Gets the attachments of this Volume.

        硬盘的挂载信息。

        :return: The attachments of this Volume.
        :rtype: list[:class:`huaweicloudsdkiec.v1.Attachment`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Volume.

        硬盘的挂载信息。

        :param attachments: The attachments of this Volume.
        :type attachments: list[:class:`huaweicloudsdkiec.v1.Attachment`]
        """
        self._attachments = attachments

    @property
    def name(self):
        """Gets the name of this Volume.

        磁盘名称。

        :return: The name of this Volume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Volume.

        磁盘名称。

        :param name: The name of this Volume.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Volume.

        描述。

        :return: The description of this Volume.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Volume.

        描述。

        :param description: The description of this Volume.
        :type description: str
        """
        self._description = description

    @property
    def volume_type(self):
        """Gets the volume_type of this Volume.

        磁盘类型。

        :return: The volume_type of this Volume.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this Volume.

        磁盘类型。

        :param volume_type: The volume_type of this Volume.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def bootable(self):
        """Gets the bootable of this Volume.

        显示这个卷是否可启动。

        :return: The bootable of this Volume.
        :rtype: str
        """
        return self._bootable

    @bootable.setter
    def bootable(self, bootable):
        """Sets the bootable of this Volume.

        显示这个卷是否可启动。

        :param bootable: The bootable of this Volume.
        :type bootable: str
        """
        self._bootable = bootable

    @property
    def encrypted(self):
        """Gets the encrypted of this Volume.

        显示该卷是否已被加密。

        :return: The encrypted of this Volume.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this Volume.

        显示该卷是否已被加密。

        :param encrypted: The encrypted of this Volume.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def multiattach(self):
        """Gets the multiattach of this Volume.

        磁盘是否多挂载。

        :return: The multiattach of this Volume.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this Volume.

        磁盘是否多挂载。

        :param multiattach: The multiattach of this Volume.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def metadata(self):
        """Gets the metadata of this Volume.

        硬盘的元数据。

        :return: The metadata of this Volume.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Volume.

        硬盘的元数据。

        :param metadata: The metadata of this Volume.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
