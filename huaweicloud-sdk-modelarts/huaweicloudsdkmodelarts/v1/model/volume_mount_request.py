# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeMountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'ownership': 'str',
        'uri': 'str',
        'id': 'str',
        'mount_path': 'str',
        'read_only': 'bool',
        'dew_secret_name': 'str',
        'capacity': 'int'
    }

    attribute_map = {
        'category': 'category',
        'ownership': 'ownership',
        'uri': 'uri',
        'id': 'id',
        'mount_path': 'mount_path',
        'read_only': 'read_only',
        'dew_secret_name': 'dew_secret_name',
        'capacity': 'capacity'
    }

    def __init__(self, category=None, ownership=None, uri=None, id=None, mount_path=None, read_only=None, dew_secret_name=None, capacity=None):
        r"""VolumeMountRequest

        The model defined in huaweicloud sdk

        :param category: **参数解释**：notebook支持的扩展存储类型，详见[[开发环境中如何选择存储](https://support.huaweicloud.com/usermanual-standard-modelarts/devtool-modelarts_0004.html#section7)](tag:hc)[[开发环境中如何选择存储](https://support.huaweicloud.com/intl/zh-cn/usermanual-standard-modelarts/devtool-modelarts_0004.html#section6)](tag:hk)[《用户指南》的“开发环境中如何选择存储”章节](tag:fcs,fcs-super) **约束限制**：不涉及 **默认取值**：不涉及。 **取值范围**：枚举类型，取值如下： - EVS：云硬盘 - OBS：对象存储服务 - OBSFS：并行文件系统（PFS） - EFS：弹性文件服务（SFS Turbo）
        :type category: str
        :param ownership: **参数解释**：资源所属 **参数约束**：不涉及。 **取值范围**：枚举类型，取值如下： - MANAGED：托管，即资源在服务上。 - DEDICATED：非托管，即资源在用户账号上，只有在category为EFS时支持。 **默认取值**：不涉及。
        :type ownership: str
        :param uri: **参数解释**：EFS专属存储盘uri或OBS并行文件系统路径 - EFS：登录弹性文件服务控制台，在文件系统列表中，单击文件系统名称进入详情页。其中，“共享路径”即为此参数的参数值。 - OBS：并行文件系统命名格式为：obs://&lt;桶名&gt;/&lt;目录路径&gt;/。登录对象存储服务控制台，在并行文件系统列表中，文件系统名称为桶名。单击文件系统名称进入详情页，在文件栏选择特定目录后，单击右侧“更多/复制路径”，该路径即为目录路径。 **参数约束**：只有当category为EFS或OBS或OBSFS，同时ownership为DEDICATED时必填，最大长度1024字符
        :type uri: str
        :param id: **参数解释**：EFS专属存储盘ID，参数值获取方式如下：登录弹性文件服务控制台，在文件系统列表中，单击文件系统名称进入详情页。其中，“ID”即为此参数的参数值。 **参数约束**：只有当category为EFS，同时ownership为DEDICATED时必填。必须符合 UUID 格式（如 280a8bd5-03e2-4a5c-bea1-83d81e75bc53）。
        :type id: str
        :param mount_path: **参数解释**：在Notebook实例中挂载的路径 **参数约束**：最大长度 256 字符
        :type mount_path: str
        :param read_only: **参数解释**：扩展存储挂载目录是否只读。默认值为false，可读写 **参数约束**：不涉及
        :type read_only: bool
        :param dew_secret_name: **参数解释**：DEW存储的用户AKSK凭据名称 **参数约束**：当category为OBS时必填，仅支持大小写字母、数字、中划线、下划线，长度 1-64 字符
        :type dew_secret_name: str
        :param capacity: **参数解释**：EVS云硬盘存储容量，单位GB。 **约束限制**：category为EVS时有效。 **取值范围**：不涉及。 **默认取值**：5。
        :type capacity: int
        """
        
        

        self._category = None
        self._ownership = None
        self._uri = None
        self._id = None
        self._mount_path = None
        self._read_only = None
        self._dew_secret_name = None
        self._capacity = None
        self.discriminator = None

        self.category = category
        self.ownership = ownership
        if uri is not None:
            self.uri = uri
        if id is not None:
            self.id = id
        if mount_path is not None:
            self.mount_path = mount_path
        if read_only is not None:
            self.read_only = read_only
        if dew_secret_name is not None:
            self.dew_secret_name = dew_secret_name
        if capacity is not None:
            self.capacity = capacity

    @property
    def category(self):
        r"""Gets the category of this VolumeMountRequest.

        **参数解释**：notebook支持的扩展存储类型，详见[[开发环境中如何选择存储](https://support.huaweicloud.com/usermanual-standard-modelarts/devtool-modelarts_0004.html#section7)](tag:hc)[[开发环境中如何选择存储](https://support.huaweicloud.com/intl/zh-cn/usermanual-standard-modelarts/devtool-modelarts_0004.html#section6)](tag:hk)[《用户指南》的“开发环境中如何选择存储”章节](tag:fcs,fcs-super) **约束限制**：不涉及 **默认取值**：不涉及。 **取值范围**：枚举类型，取值如下： - EVS：云硬盘 - OBS：对象存储服务 - OBSFS：并行文件系统（PFS） - EFS：弹性文件服务（SFS Turbo）

        :return: The category of this VolumeMountRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this VolumeMountRequest.

        **参数解释**：notebook支持的扩展存储类型，详见[[开发环境中如何选择存储](https://support.huaweicloud.com/usermanual-standard-modelarts/devtool-modelarts_0004.html#section7)](tag:hc)[[开发环境中如何选择存储](https://support.huaweicloud.com/intl/zh-cn/usermanual-standard-modelarts/devtool-modelarts_0004.html#section6)](tag:hk)[《用户指南》的“开发环境中如何选择存储”章节](tag:fcs,fcs-super) **约束限制**：不涉及 **默认取值**：不涉及。 **取值范围**：枚举类型，取值如下： - EVS：云硬盘 - OBS：对象存储服务 - OBSFS：并行文件系统（PFS） - EFS：弹性文件服务（SFS Turbo）

        :param category: The category of this VolumeMountRequest.
        :type category: str
        """
        self._category = category

    @property
    def ownership(self):
        r"""Gets the ownership of this VolumeMountRequest.

        **参数解释**：资源所属 **参数约束**：不涉及。 **取值范围**：枚举类型，取值如下： - MANAGED：托管，即资源在服务上。 - DEDICATED：非托管，即资源在用户账号上，只有在category为EFS时支持。 **默认取值**：不涉及。

        :return: The ownership of this VolumeMountRequest.
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        r"""Sets the ownership of this VolumeMountRequest.

        **参数解释**：资源所属 **参数约束**：不涉及。 **取值范围**：枚举类型，取值如下： - MANAGED：托管，即资源在服务上。 - DEDICATED：非托管，即资源在用户账号上，只有在category为EFS时支持。 **默认取值**：不涉及。

        :param ownership: The ownership of this VolumeMountRequest.
        :type ownership: str
        """
        self._ownership = ownership

    @property
    def uri(self):
        r"""Gets the uri of this VolumeMountRequest.

        **参数解释**：EFS专属存储盘uri或OBS并行文件系统路径 - EFS：登录弹性文件服务控制台，在文件系统列表中，单击文件系统名称进入详情页。其中，“共享路径”即为此参数的参数值。 - OBS：并行文件系统命名格式为：obs://<桶名>/<目录路径>/。登录对象存储服务控制台，在并行文件系统列表中，文件系统名称为桶名。单击文件系统名称进入详情页，在文件栏选择特定目录后，单击右侧“更多/复制路径”，该路径即为目录路径。 **参数约束**：只有当category为EFS或OBS或OBSFS，同时ownership为DEDICATED时必填，最大长度1024字符

        :return: The uri of this VolumeMountRequest.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this VolumeMountRequest.

        **参数解释**：EFS专属存储盘uri或OBS并行文件系统路径 - EFS：登录弹性文件服务控制台，在文件系统列表中，单击文件系统名称进入详情页。其中，“共享路径”即为此参数的参数值。 - OBS：并行文件系统命名格式为：obs://<桶名>/<目录路径>/。登录对象存储服务控制台，在并行文件系统列表中，文件系统名称为桶名。单击文件系统名称进入详情页，在文件栏选择特定目录后，单击右侧“更多/复制路径”，该路径即为目录路径。 **参数约束**：只有当category为EFS或OBS或OBSFS，同时ownership为DEDICATED时必填，最大长度1024字符

        :param uri: The uri of this VolumeMountRequest.
        :type uri: str
        """
        self._uri = uri

    @property
    def id(self):
        r"""Gets the id of this VolumeMountRequest.

        **参数解释**：EFS专属存储盘ID，参数值获取方式如下：登录弹性文件服务控制台，在文件系统列表中，单击文件系统名称进入详情页。其中，“ID”即为此参数的参数值。 **参数约束**：只有当category为EFS，同时ownership为DEDICATED时必填。必须符合 UUID 格式（如 280a8bd5-03e2-4a5c-bea1-83d81e75bc53）。

        :return: The id of this VolumeMountRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VolumeMountRequest.

        **参数解释**：EFS专属存储盘ID，参数值获取方式如下：登录弹性文件服务控制台，在文件系统列表中，单击文件系统名称进入详情页。其中，“ID”即为此参数的参数值。 **参数约束**：只有当category为EFS，同时ownership为DEDICATED时必填。必须符合 UUID 格式（如 280a8bd5-03e2-4a5c-bea1-83d81e75bc53）。

        :param id: The id of this VolumeMountRequest.
        :type id: str
        """
        self._id = id

    @property
    def mount_path(self):
        r"""Gets the mount_path of this VolumeMountRequest.

        **参数解释**：在Notebook实例中挂载的路径 **参数约束**：最大长度 256 字符

        :return: The mount_path of this VolumeMountRequest.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this VolumeMountRequest.

        **参数解释**：在Notebook实例中挂载的路径 **参数约束**：最大长度 256 字符

        :param mount_path: The mount_path of this VolumeMountRequest.
        :type mount_path: str
        """
        self._mount_path = mount_path

    @property
    def read_only(self):
        r"""Gets the read_only of this VolumeMountRequest.

        **参数解释**：扩展存储挂载目录是否只读。默认值为false，可读写 **参数约束**：不涉及

        :return: The read_only of this VolumeMountRequest.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        r"""Sets the read_only of this VolumeMountRequest.

        **参数解释**：扩展存储挂载目录是否只读。默认值为false，可读写 **参数约束**：不涉及

        :param read_only: The read_only of this VolumeMountRequest.
        :type read_only: bool
        """
        self._read_only = read_only

    @property
    def dew_secret_name(self):
        r"""Gets the dew_secret_name of this VolumeMountRequest.

        **参数解释**：DEW存储的用户AKSK凭据名称 **参数约束**：当category为OBS时必填，仅支持大小写字母、数字、中划线、下划线，长度 1-64 字符

        :return: The dew_secret_name of this VolumeMountRequest.
        :rtype: str
        """
        return self._dew_secret_name

    @dew_secret_name.setter
    def dew_secret_name(self, dew_secret_name):
        r"""Sets the dew_secret_name of this VolumeMountRequest.

        **参数解释**：DEW存储的用户AKSK凭据名称 **参数约束**：当category为OBS时必填，仅支持大小写字母、数字、中划线、下划线，长度 1-64 字符

        :param dew_secret_name: The dew_secret_name of this VolumeMountRequest.
        :type dew_secret_name: str
        """
        self._dew_secret_name = dew_secret_name

    @property
    def capacity(self):
        r"""Gets the capacity of this VolumeMountRequest.

        **参数解释**：EVS云硬盘存储容量，单位GB。 **约束限制**：category为EVS时有效。 **取值范围**：不涉及。 **默认取值**：5。

        :return: The capacity of this VolumeMountRequest.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this VolumeMountRequest.

        **参数解释**：EVS云硬盘存储容量，单位GB。 **约束限制**：category为EVS时有效。 **取值范围**：不涉及。 **默认取值**：5。

        :param capacity: The capacity of this VolumeMountRequest.
        :type capacity: int
        """
        self._capacity = capacity

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
        if not isinstance(other, VolumeMountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
