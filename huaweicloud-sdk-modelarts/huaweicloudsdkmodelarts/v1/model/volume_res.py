# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capacity': 'int',
        'category': 'str',
        'mount_path': 'str',
        'ownership': 'str',
        'status': 'str',
        'id': 'str',
        'read_only': 'bool',
        'dew_secret_name': 'str',
        'evs_sku_code': 'str',
        'uri': 'str',
        'mount_type': 'str'
    }

    attribute_map = {
        'capacity': 'capacity',
        'category': 'category',
        'mount_path': 'mount_path',
        'ownership': 'ownership',
        'status': 'status',
        'id': 'id',
        'read_only': 'read_only',
        'dew_secret_name': 'dew_secret_name',
        'evs_sku_code': 'evs_sku_code',
        'uri': 'uri',
        'mount_type': 'mount_type'
    }

    def __init__(self, capacity=None, category=None, mount_path=None, ownership=None, status=None, id=None, read_only=None, dew_secret_name=None, evs_sku_code=None, uri=None, mount_type=None):
        r"""VolumeRes

        The model defined in huaweicloud sdk

        :param capacity: **参数解释**：存储容量。 **取值范围**：EVS默认5G，EFS默认50G，最大限制4096G。
        :type capacity: int
        :param category: **参数解释**：支持的存储类型。不同存储类型的差异，详见[[开发环境中如何选择存储](https://support.huaweicloud.com/usermanual-standard-modelarts/devtool-modelarts_0004.html#section6)](tag:hc)[[开发环境中如何选择存储](https://support.huaweicloud.com/intl/zh-cn/usermanual-standard-modelarts/devtool-modelarts_0004.html#section5)](tag:hk)[《用户指南》的“开发环境中如何选择存储”章节](tag:fcs,fcs-super)。 **取值范围**：枚举类型，取值如下： - SFS：弹性文件服务 - EVS：云硬盘 - OBS：对象存储服务 - OBSFS：并行文件系统 - EFS：弹性文件服务（SFS Turbo）
        :type category: str
        :param mount_path: **参数解释**：存储挂载至Notebook实例的目录，当前固定在/home/ma-user/work/下。 **取值范围**：不涉及。
        :type mount_path: str
        :param ownership: **参数解释**：资源所属。 **取值范围**：枚举类型，取值如下： - MANAGED：托管，即资源在服务上。 - DEDICATED：非托管，即资源在用户账号上，只有在category为EFS时支持。
        :type ownership: str
        :param status: **参数解释**：EVS扩容状态，扩容时的状态为RESIZING，此时实例可以正常使用。 **取值范围**：不涉及。
        :type status: str
        :param id: **参数解释**：EFS专属存储盘ID或OBS存储ID，只有作为扩展存储时返回。 **取值范围**：不涉及。
        :type id: str
        :param read_only: **参数解释**：扩展存储挂载目录是否只读。 **取值范围**：不涉及。
        :type read_only: bool
        :param dew_secret_name: **参数解释**：DEW存储的用户AKSK凭据名称。 **取值范围**：不涉及。
        :type dew_secret_name: str
        :param evs_sku_code: **参数解释**：规格包含的evs时，evs存储的sku编码。 **取值范围**：不涉及。
        :type evs_sku_code: str
        :param uri: **参数解释**：只有当category为EFS或OBS或OBSFS时，挂载存储源路径。 **取值范围**：不涉及。
        :type uri: str
        :param mount_type: **参数解释**：存储挂载类型。 **取值范围**：枚举类型，取值如下：  - STATIC:不支持在实例运行期间挂载以及卸载的存储 - DYNAMIC:支持在实例运行期间挂载以及卸载的存储
        :type mount_type: str
        """
        
        

        self._capacity = None
        self._category = None
        self._mount_path = None
        self._ownership = None
        self._status = None
        self._id = None
        self._read_only = None
        self._dew_secret_name = None
        self._evs_sku_code = None
        self._uri = None
        self._mount_type = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if category is not None:
            self.category = category
        if mount_path is not None:
            self.mount_path = mount_path
        if ownership is not None:
            self.ownership = ownership
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if read_only is not None:
            self.read_only = read_only
        if dew_secret_name is not None:
            self.dew_secret_name = dew_secret_name
        if evs_sku_code is not None:
            self.evs_sku_code = evs_sku_code
        if uri is not None:
            self.uri = uri
        if mount_type is not None:
            self.mount_type = mount_type

    @property
    def capacity(self):
        r"""Gets the capacity of this VolumeRes.

        **参数解释**：存储容量。 **取值范围**：EVS默认5G，EFS默认50G，最大限制4096G。

        :return: The capacity of this VolumeRes.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this VolumeRes.

        **参数解释**：存储容量。 **取值范围**：EVS默认5G，EFS默认50G，最大限制4096G。

        :param capacity: The capacity of this VolumeRes.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def category(self):
        r"""Gets the category of this VolumeRes.

        **参数解释**：支持的存储类型。不同存储类型的差异，详见[[开发环境中如何选择存储](https://support.huaweicloud.com/usermanual-standard-modelarts/devtool-modelarts_0004.html#section6)](tag:hc)[[开发环境中如何选择存储](https://support.huaweicloud.com/intl/zh-cn/usermanual-standard-modelarts/devtool-modelarts_0004.html#section5)](tag:hk)[《用户指南》的“开发环境中如何选择存储”章节](tag:fcs,fcs-super)。 **取值范围**：枚举类型，取值如下： - SFS：弹性文件服务 - EVS：云硬盘 - OBS：对象存储服务 - OBSFS：并行文件系统 - EFS：弹性文件服务（SFS Turbo）

        :return: The category of this VolumeRes.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this VolumeRes.

        **参数解释**：支持的存储类型。不同存储类型的差异，详见[[开发环境中如何选择存储](https://support.huaweicloud.com/usermanual-standard-modelarts/devtool-modelarts_0004.html#section6)](tag:hc)[[开发环境中如何选择存储](https://support.huaweicloud.com/intl/zh-cn/usermanual-standard-modelarts/devtool-modelarts_0004.html#section5)](tag:hk)[《用户指南》的“开发环境中如何选择存储”章节](tag:fcs,fcs-super)。 **取值范围**：枚举类型，取值如下： - SFS：弹性文件服务 - EVS：云硬盘 - OBS：对象存储服务 - OBSFS：并行文件系统 - EFS：弹性文件服务（SFS Turbo）

        :param category: The category of this VolumeRes.
        :type category: str
        """
        self._category = category

    @property
    def mount_path(self):
        r"""Gets the mount_path of this VolumeRes.

        **参数解释**：存储挂载至Notebook实例的目录，当前固定在/home/ma-user/work/下。 **取值范围**：不涉及。

        :return: The mount_path of this VolumeRes.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this VolumeRes.

        **参数解释**：存储挂载至Notebook实例的目录，当前固定在/home/ma-user/work/下。 **取值范围**：不涉及。

        :param mount_path: The mount_path of this VolumeRes.
        :type mount_path: str
        """
        self._mount_path = mount_path

    @property
    def ownership(self):
        r"""Gets the ownership of this VolumeRes.

        **参数解释**：资源所属。 **取值范围**：枚举类型，取值如下： - MANAGED：托管，即资源在服务上。 - DEDICATED：非托管，即资源在用户账号上，只有在category为EFS时支持。

        :return: The ownership of this VolumeRes.
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        r"""Sets the ownership of this VolumeRes.

        **参数解释**：资源所属。 **取值范围**：枚举类型，取值如下： - MANAGED：托管，即资源在服务上。 - DEDICATED：非托管，即资源在用户账号上，只有在category为EFS时支持。

        :param ownership: The ownership of this VolumeRes.
        :type ownership: str
        """
        self._ownership = ownership

    @property
    def status(self):
        r"""Gets the status of this VolumeRes.

        **参数解释**：EVS扩容状态，扩容时的状态为RESIZING，此时实例可以正常使用。 **取值范围**：不涉及。

        :return: The status of this VolumeRes.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VolumeRes.

        **参数解释**：EVS扩容状态，扩容时的状态为RESIZING，此时实例可以正常使用。 **取值范围**：不涉及。

        :param status: The status of this VolumeRes.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        r"""Gets the id of this VolumeRes.

        **参数解释**：EFS专属存储盘ID或OBS存储ID，只有作为扩展存储时返回。 **取值范围**：不涉及。

        :return: The id of this VolumeRes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VolumeRes.

        **参数解释**：EFS专属存储盘ID或OBS存储ID，只有作为扩展存储时返回。 **取值范围**：不涉及。

        :param id: The id of this VolumeRes.
        :type id: str
        """
        self._id = id

    @property
    def read_only(self):
        r"""Gets the read_only of this VolumeRes.

        **参数解释**：扩展存储挂载目录是否只读。 **取值范围**：不涉及。

        :return: The read_only of this VolumeRes.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        r"""Sets the read_only of this VolumeRes.

        **参数解释**：扩展存储挂载目录是否只读。 **取值范围**：不涉及。

        :param read_only: The read_only of this VolumeRes.
        :type read_only: bool
        """
        self._read_only = read_only

    @property
    def dew_secret_name(self):
        r"""Gets the dew_secret_name of this VolumeRes.

        **参数解释**：DEW存储的用户AKSK凭据名称。 **取值范围**：不涉及。

        :return: The dew_secret_name of this VolumeRes.
        :rtype: str
        """
        return self._dew_secret_name

    @dew_secret_name.setter
    def dew_secret_name(self, dew_secret_name):
        r"""Sets the dew_secret_name of this VolumeRes.

        **参数解释**：DEW存储的用户AKSK凭据名称。 **取值范围**：不涉及。

        :param dew_secret_name: The dew_secret_name of this VolumeRes.
        :type dew_secret_name: str
        """
        self._dew_secret_name = dew_secret_name

    @property
    def evs_sku_code(self):
        r"""Gets the evs_sku_code of this VolumeRes.

        **参数解释**：规格包含的evs时，evs存储的sku编码。 **取值范围**：不涉及。

        :return: The evs_sku_code of this VolumeRes.
        :rtype: str
        """
        return self._evs_sku_code

    @evs_sku_code.setter
    def evs_sku_code(self, evs_sku_code):
        r"""Sets the evs_sku_code of this VolumeRes.

        **参数解释**：规格包含的evs时，evs存储的sku编码。 **取值范围**：不涉及。

        :param evs_sku_code: The evs_sku_code of this VolumeRes.
        :type evs_sku_code: str
        """
        self._evs_sku_code = evs_sku_code

    @property
    def uri(self):
        r"""Gets the uri of this VolumeRes.

        **参数解释**：只有当category为EFS或OBS或OBSFS时，挂载存储源路径。 **取值范围**：不涉及。

        :return: The uri of this VolumeRes.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this VolumeRes.

        **参数解释**：只有当category为EFS或OBS或OBSFS时，挂载存储源路径。 **取值范围**：不涉及。

        :param uri: The uri of this VolumeRes.
        :type uri: str
        """
        self._uri = uri

    @property
    def mount_type(self):
        r"""Gets the mount_type of this VolumeRes.

        **参数解释**：存储挂载类型。 **取值范围**：枚举类型，取值如下：  - STATIC:不支持在实例运行期间挂载以及卸载的存储 - DYNAMIC:支持在实例运行期间挂载以及卸载的存储

        :return: The mount_type of this VolumeRes.
        :rtype: str
        """
        return self._mount_type

    @mount_type.setter
    def mount_type(self, mount_type):
        r"""Sets the mount_type of this VolumeRes.

        **参数解释**：存储挂载类型。 **取值范围**：枚举类型，取值如下：  - STATIC:不支持在实例运行期间挂载以及卸载的存储 - DYNAMIC:支持在实例运行期间挂载以及卸载的存储

        :param mount_type: The mount_type of this VolumeRes.
        :type mount_type: str
        """
        self._mount_type = mount_type

    def to_dict(self):
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
        if not isinstance(other, VolumeRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
