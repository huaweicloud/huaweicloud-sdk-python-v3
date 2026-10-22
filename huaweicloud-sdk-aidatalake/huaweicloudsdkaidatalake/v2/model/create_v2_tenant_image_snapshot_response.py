# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateV2TenantImageSnapshotResponse(SdkResponse):

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
        'image_id': 'str',
        'image_version_id': 'str',
        'name': 'str',
        'image_address': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'status': 'ImageSnapshotStatus',
        'image_snapshot_size': 'int',
        'creation_mode': 'str',
        'reserved_days': 'int',
        'expire_time': 'datetime',
        'failed_message': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'image_id': 'image_id',
        'image_version_id': 'image_version_id',
        'name': 'name',
        'image_address': 'image_address',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'status': 'status',
        'image_snapshot_size': 'image_snapshot_size',
        'creation_mode': 'creation_mode',
        'reserved_days': 'reserved_days',
        'expire_time': 'expire_time',
        'failed_message': 'failed_message',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, image_id=None, image_version_id=None, name=None, image_address=None, image_name=None, image_version=None, status=None, image_snapshot_size=None, creation_mode=None, reserved_days=None, expire_time=None, failed_message=None, create_time=None, update_time=None):
        r"""CreateV2TenantImageSnapshotResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：镜像快照记录ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type id: str
        :param image_id: **参数解释**：镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type image_id: str
        :param image_version_id: **参数解释**：镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type image_version_id: str
        :param name: **参数解释**：镜像快照名称（用户指定）。 **约束限制**：不涉及。 **取值范围**：以小写字母开头，小写字母、数字、中划线（-）组成，小写字母或数字结尾的1到190字符的字符串。 **默认取值**：不涉及。 
        :type name: str
        :param image_address: **参数解释**：镜像完整地址（含registry/namespace/name:version）。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、冒号、斜杠及连字符，长度为0~1024个字符。 **默认取值**：不涉及。 
        :type image_address: str
        :param image_name: **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、斜杠、冒号、下划线和连字符，长度为0~128个字符。 **默认取值**：不涉及。 
        :type image_name: str
        :param image_version: **参数解释**：镜像版本。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、冒号、下划线和连字符，长度为0~1024个字符。 **默认取值**：不涉及。 
        :type image_version: str
        :param status: 
        :type status: :class:`huaweicloudsdkaidatalake.v2.ImageSnapshotStatus`
        :param image_snapshot_size: **参数解释**：快照大小，单位GiB。 **约束限制**：不涉及。 **取值范围**：20~400。 **默认取值**：不涉及。 
        :type image_snapshot_size: int
        :param creation_mode: **参数解释**：创建方式。 **约束限制**：不涉及。 **取值范围**：   - Created：直接创建。   - Associated：关联CCI已有快照。 **默认取值**：不涉及。 
        :type creation_mode: str
        :param reserved_days: **参数解释**：镜像快照保留天数。超过保留天数自动失效，0表示永久保留。 **约束限制**：不涉及。 **取值范围**：0~65536。 **默认取值**：不涉及。 
        :type reserved_days: int
        :param expire_time: **参数解释**：超期时间，null表示永久有效。使用UTC时间，ISO 8601格式，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 
        :type expire_time: datetime
        :param failed_message: **参数解释**：镜像快照失效的提示信息。 **约束限制**：不涉及。 **取值范围**：支持中文字符、英文字母、数字及常用符号，长度为0~65535个字符。 **默认取值**：不涉及。 
        :type failed_message: str
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        :param update_time: **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type update_time: datetime
        """
        
        super().__init__()

        self._id = None
        self._image_id = None
        self._image_version_id = None
        self._name = None
        self._image_address = None
        self._image_name = None
        self._image_version = None
        self._status = None
        self._image_snapshot_size = None
        self._creation_mode = None
        self._reserved_days = None
        self._expire_time = None
        self._failed_message = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if image_id is not None:
            self.image_id = image_id
        if image_version_id is not None:
            self.image_version_id = image_version_id
        if name is not None:
            self.name = name
        if image_address is not None:
            self.image_address = image_address
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if status is not None:
            self.status = status
        if image_snapshot_size is not None:
            self.image_snapshot_size = image_snapshot_size
        if creation_mode is not None:
            self.creation_mode = creation_mode
        if reserved_days is not None:
            self.reserved_days = reserved_days
        if expire_time is not None:
            self.expire_time = expire_time
        if failed_message is not None:
            self.failed_message = failed_message
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像快照记录ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The id of this CreateV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像快照记录ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param id: The id of this CreateV2TenantImageSnapshotResponse.
        :type id: str
        """
        self._id = id

    @property
    def image_id(self):
        r"""Gets the image_id of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The image_id of this CreateV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param image_id: The image_id of this CreateV2TenantImageSnapshotResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_version_id(self):
        r"""Gets the image_version_id of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The image_version_id of this CreateV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._image_version_id

    @image_version_id.setter
    def image_version_id(self, image_version_id):
        r"""Sets the image_version_id of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param image_version_id: The image_version_id of this CreateV2TenantImageSnapshotResponse.
        :type image_version_id: str
        """
        self._image_version_id = image_version_id

    @property
    def name(self):
        r"""Gets the name of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像快照名称（用户指定）。 **约束限制**：不涉及。 **取值范围**：以小写字母开头，小写字母、数字、中划线（-）组成，小写字母或数字结尾的1到190字符的字符串。 **默认取值**：不涉及。 

        :return: The name of this CreateV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像快照名称（用户指定）。 **约束限制**：不涉及。 **取值范围**：以小写字母开头，小写字母、数字、中划线（-）组成，小写字母或数字结尾的1到190字符的字符串。 **默认取值**：不涉及。 

        :param name: The name of this CreateV2TenantImageSnapshotResponse.
        :type name: str
        """
        self._name = name

    @property
    def image_address(self):
        r"""Gets the image_address of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像完整地址（含registry/namespace/name:version）。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、冒号、斜杠及连字符，长度为0~1024个字符。 **默认取值**：不涉及。 

        :return: The image_address of this CreateV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._image_address

    @image_address.setter
    def image_address(self, image_address):
        r"""Sets the image_address of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像完整地址（含registry/namespace/name:version）。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、冒号、斜杠及连字符，长度为0~1024个字符。 **默认取值**：不涉及。 

        :param image_address: The image_address of this CreateV2TenantImageSnapshotResponse.
        :type image_address: str
        """
        self._image_address = image_address

    @property
    def image_name(self):
        r"""Gets the image_name of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、斜杠、冒号、下划线和连字符，长度为0~128个字符。 **默认取值**：不涉及。 

        :return: The image_name of this CreateV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、斜杠、冒号、下划线和连字符，长度为0~128个字符。 **默认取值**：不涉及。 

        :param image_name: The image_name of this CreateV2TenantImageSnapshotResponse.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像版本。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、冒号、下划线和连字符，长度为0~1024个字符。 **默认取值**：不涉及。 

        :return: The image_version of this CreateV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像版本。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、冒号、下划线和连字符，长度为0~1024个字符。 **默认取值**：不涉及。 

        :param image_version: The image_version of this CreateV2TenantImageSnapshotResponse.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def status(self):
        r"""Gets the status of this CreateV2TenantImageSnapshotResponse.

        :return: The status of this CreateV2TenantImageSnapshotResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ImageSnapshotStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateV2TenantImageSnapshotResponse.

        :param status: The status of this CreateV2TenantImageSnapshotResponse.
        :type status: :class:`huaweicloudsdkaidatalake.v2.ImageSnapshotStatus`
        """
        self._status = status

    @property
    def image_snapshot_size(self):
        r"""Gets the image_snapshot_size of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：快照大小，单位GiB。 **约束限制**：不涉及。 **取值范围**：20~400。 **默认取值**：不涉及。 

        :return: The image_snapshot_size of this CreateV2TenantImageSnapshotResponse.
        :rtype: int
        """
        return self._image_snapshot_size

    @image_snapshot_size.setter
    def image_snapshot_size(self, image_snapshot_size):
        r"""Sets the image_snapshot_size of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：快照大小，单位GiB。 **约束限制**：不涉及。 **取值范围**：20~400。 **默认取值**：不涉及。 

        :param image_snapshot_size: The image_snapshot_size of this CreateV2TenantImageSnapshotResponse.
        :type image_snapshot_size: int
        """
        self._image_snapshot_size = image_snapshot_size

    @property
    def creation_mode(self):
        r"""Gets the creation_mode of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：创建方式。 **约束限制**：不涉及。 **取值范围**：   - Created：直接创建。   - Associated：关联CCI已有快照。 **默认取值**：不涉及。 

        :return: The creation_mode of this CreateV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._creation_mode

    @creation_mode.setter
    def creation_mode(self, creation_mode):
        r"""Sets the creation_mode of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：创建方式。 **约束限制**：不涉及。 **取值范围**：   - Created：直接创建。   - Associated：关联CCI已有快照。 **默认取值**：不涉及。 

        :param creation_mode: The creation_mode of this CreateV2TenantImageSnapshotResponse.
        :type creation_mode: str
        """
        self._creation_mode = creation_mode

    @property
    def reserved_days(self):
        r"""Gets the reserved_days of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像快照保留天数。超过保留天数自动失效，0表示永久保留。 **约束限制**：不涉及。 **取值范围**：0~65536。 **默认取值**：不涉及。 

        :return: The reserved_days of this CreateV2TenantImageSnapshotResponse.
        :rtype: int
        """
        return self._reserved_days

    @reserved_days.setter
    def reserved_days(self, reserved_days):
        r"""Sets the reserved_days of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像快照保留天数。超过保留天数自动失效，0表示永久保留。 **约束限制**：不涉及。 **取值范围**：0~65536。 **默认取值**：不涉及。 

        :param reserved_days: The reserved_days of this CreateV2TenantImageSnapshotResponse.
        :type reserved_days: int
        """
        self._reserved_days = reserved_days

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：超期时间，null表示永久有效。使用UTC时间，ISO 8601格式，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 

        :return: The expire_time of this CreateV2TenantImageSnapshotResponse.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：超期时间，null表示永久有效。使用UTC时间，ISO 8601格式，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 

        :param expire_time: The expire_time of this CreateV2TenantImageSnapshotResponse.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

    @property
    def failed_message(self):
        r"""Gets the failed_message of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像快照失效的提示信息。 **约束限制**：不涉及。 **取值范围**：支持中文字符、英文字母、数字及常用符号，长度为0~65535个字符。 **默认取值**：不涉及。 

        :return: The failed_message of this CreateV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        r"""Sets the failed_message of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：镜像快照失效的提示信息。 **约束限制**：不涉及。 **取值范围**：支持中文字符、英文字母、数字及常用符号，长度为0~65535个字符。 **默认取值**：不涉及。 

        :param failed_message: The failed_message of this CreateV2TenantImageSnapshotResponse.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this CreateV2TenantImageSnapshotResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this CreateV2TenantImageSnapshotResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The update_time of this CreateV2TenantImageSnapshotResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateV2TenantImageSnapshotResponse.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param update_time: The update_time of this CreateV2TenantImageSnapshotResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("CreateV2TenantImageSnapshotResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateV2TenantImageSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
