# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'address': 'str',
        'mount_path': 'str',
        'host_cache': 'bool',
        'efs_sub_path': 'str',
        'read_only': 'bool',
        'os_warm_up': 'bool',
        'source_name': 'str',
        'asset_id': 'str'
    }

    attribute_map = {
        'source': 'source',
        'address': 'address',
        'mount_path': 'mount_path',
        'host_cache': 'host_cache',
        'efs_sub_path': 'efs_sub_path',
        'read_only': 'read_only',
        'os_warm_up': 'os_warm_up',
        'source_name': 'source_name',
        'asset_id': 'asset_id'
    }

    def __init__(self, source=None, address=None, mount_path=None, host_cache=None, efs_sub_path=None, read_only=None, os_warm_up=None, source_name=None, asset_id=None):
        r"""ModelResource

        The model defined in huaweicloud sdk

        :param source: **参数解释：** 代码来源类别。 **约束限制：** 不涉及。 **取值范围：** 如下参数不区分大小写 - OBS：对象存储服务。 - OBSFS：OBS的文件系统接口。 - EFS：弹性文件服务。 - LOCAL：挂载宿主机本地存储目录。 **默认取值：** 不涉及。
        :type source: str
        :param address: **参数解释：** 代码来源地址，格式遵循不同存储系统。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type address: str
        :param mount_path: **参数解释：** 挂载到容器内的路径，要求以/开头，后面可包含中划线、反斜杠、下划线、点号、字母、数字。 **约束限制：** 不涉及。 **取值范围：** 以(/)开头和结尾，可包含字母、数字、中划线、下划线，整个挂载路径长度不能超过255位。 **默认取值：** 不涉及。
        :type mount_path: str
        :param host_cache: **参数解释：** 是否支持模型本地缓存，默认是不支持。 **约束限制：** 不涉及。 **取值范围：** - true：支持。 - false：不支持。 **默认取值：** false。
        :type host_cache: bool
        :param efs_sub_path: **参数解释：** 当存储类别为EFS时，支持配置子目录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type efs_sub_path: str
        :param read_only: **参数解释：** 挂载权限设置，是否只读。 **约束限制：** 不涉及。 **取值范围：** - true：只读。 - false：非只读。 **默认取值：** 不涉及。
        :type read_only: bool
        :param os_warm_up: **参数解释：** OS预热。 **约束限制：** 不涉及。 **取值范围：** - true：预热。 - false：不预热。 **默认取值：** 不涉及。
        :type os_warm_up: bool
        :param source_name: **参数解释：** 预热名称。 **约束限制：** os_warm_up为true时必填。 **取值范围：** 支持1-64位字符，可包含字母、中文、数字、中划线、下划线。 **默认取值：** 不涉及。
        :type source_name: str
        :param asset_id: **参数解释：** 预置资产id。 **约束限制：** 使用预置资产时必填。 **取值范围：** 支持1-64位字符，可包含字母、中文、数字、中划线、下划线。 **默认取值：** 不涉及。
        :type asset_id: str
        """
        
        

        self._source = None
        self._address = None
        self._mount_path = None
        self._host_cache = None
        self._efs_sub_path = None
        self._read_only = None
        self._os_warm_up = None
        self._source_name = None
        self._asset_id = None
        self.discriminator = None

        self.source = source
        if address is not None:
            self.address = address
        self.mount_path = mount_path
        if host_cache is not None:
            self.host_cache = host_cache
        if efs_sub_path is not None:
            self.efs_sub_path = efs_sub_path
        if read_only is not None:
            self.read_only = read_only
        if os_warm_up is not None:
            self.os_warm_up = os_warm_up
        if source_name is not None:
            self.source_name = source_name
        if asset_id is not None:
            self.asset_id = asset_id

    @property
    def source(self):
        r"""Gets the source of this ModelResource.

        **参数解释：** 代码来源类别。 **约束限制：** 不涉及。 **取值范围：** 如下参数不区分大小写 - OBS：对象存储服务。 - OBSFS：OBS的文件系统接口。 - EFS：弹性文件服务。 - LOCAL：挂载宿主机本地存储目录。 **默认取值：** 不涉及。

        :return: The source of this ModelResource.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ModelResource.

        **参数解释：** 代码来源类别。 **约束限制：** 不涉及。 **取值范围：** 如下参数不区分大小写 - OBS：对象存储服务。 - OBSFS：OBS的文件系统接口。 - EFS：弹性文件服务。 - LOCAL：挂载宿主机本地存储目录。 **默认取值：** 不涉及。

        :param source: The source of this ModelResource.
        :type source: str
        """
        self._source = source

    @property
    def address(self):
        r"""Gets the address of this ModelResource.

        **参数解释：** 代码来源地址，格式遵循不同存储系统。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The address of this ModelResource.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ModelResource.

        **参数解释：** 代码来源地址，格式遵循不同存储系统。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param address: The address of this ModelResource.
        :type address: str
        """
        self._address = address

    @property
    def mount_path(self):
        r"""Gets the mount_path of this ModelResource.

        **参数解释：** 挂载到容器内的路径，要求以/开头，后面可包含中划线、反斜杠、下划线、点号、字母、数字。 **约束限制：** 不涉及。 **取值范围：** 以(/)开头和结尾，可包含字母、数字、中划线、下划线，整个挂载路径长度不能超过255位。 **默认取值：** 不涉及。

        :return: The mount_path of this ModelResource.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this ModelResource.

        **参数解释：** 挂载到容器内的路径，要求以/开头，后面可包含中划线、反斜杠、下划线、点号、字母、数字。 **约束限制：** 不涉及。 **取值范围：** 以(/)开头和结尾，可包含字母、数字、中划线、下划线，整个挂载路径长度不能超过255位。 **默认取值：** 不涉及。

        :param mount_path: The mount_path of this ModelResource.
        :type mount_path: str
        """
        self._mount_path = mount_path

    @property
    def host_cache(self):
        r"""Gets the host_cache of this ModelResource.

        **参数解释：** 是否支持模型本地缓存，默认是不支持。 **约束限制：** 不涉及。 **取值范围：** - true：支持。 - false：不支持。 **默认取值：** false。

        :return: The host_cache of this ModelResource.
        :rtype: bool
        """
        return self._host_cache

    @host_cache.setter
    def host_cache(self, host_cache):
        r"""Sets the host_cache of this ModelResource.

        **参数解释：** 是否支持模型本地缓存，默认是不支持。 **约束限制：** 不涉及。 **取值范围：** - true：支持。 - false：不支持。 **默认取值：** false。

        :param host_cache: The host_cache of this ModelResource.
        :type host_cache: bool
        """
        self._host_cache = host_cache

    @property
    def efs_sub_path(self):
        r"""Gets the efs_sub_path of this ModelResource.

        **参数解释：** 当存储类别为EFS时，支持配置子目录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The efs_sub_path of this ModelResource.
        :rtype: str
        """
        return self._efs_sub_path

    @efs_sub_path.setter
    def efs_sub_path(self, efs_sub_path):
        r"""Sets the efs_sub_path of this ModelResource.

        **参数解释：** 当存储类别为EFS时，支持配置子目录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param efs_sub_path: The efs_sub_path of this ModelResource.
        :type efs_sub_path: str
        """
        self._efs_sub_path = efs_sub_path

    @property
    def read_only(self):
        r"""Gets the read_only of this ModelResource.

        **参数解释：** 挂载权限设置，是否只读。 **约束限制：** 不涉及。 **取值范围：** - true：只读。 - false：非只读。 **默认取值：** 不涉及。

        :return: The read_only of this ModelResource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        r"""Sets the read_only of this ModelResource.

        **参数解释：** 挂载权限设置，是否只读。 **约束限制：** 不涉及。 **取值范围：** - true：只读。 - false：非只读。 **默认取值：** 不涉及。

        :param read_only: The read_only of this ModelResource.
        :type read_only: bool
        """
        self._read_only = read_only

    @property
    def os_warm_up(self):
        r"""Gets the os_warm_up of this ModelResource.

        **参数解释：** OS预热。 **约束限制：** 不涉及。 **取值范围：** - true：预热。 - false：不预热。 **默认取值：** 不涉及。

        :return: The os_warm_up of this ModelResource.
        :rtype: bool
        """
        return self._os_warm_up

    @os_warm_up.setter
    def os_warm_up(self, os_warm_up):
        r"""Sets the os_warm_up of this ModelResource.

        **参数解释：** OS预热。 **约束限制：** 不涉及。 **取值范围：** - true：预热。 - false：不预热。 **默认取值：** 不涉及。

        :param os_warm_up: The os_warm_up of this ModelResource.
        :type os_warm_up: bool
        """
        self._os_warm_up = os_warm_up

    @property
    def source_name(self):
        r"""Gets the source_name of this ModelResource.

        **参数解释：** 预热名称。 **约束限制：** os_warm_up为true时必填。 **取值范围：** 支持1-64位字符，可包含字母、中文、数字、中划线、下划线。 **默认取值：** 不涉及。

        :return: The source_name of this ModelResource.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this ModelResource.

        **参数解释：** 预热名称。 **约束限制：** os_warm_up为true时必填。 **取值范围：** 支持1-64位字符，可包含字母、中文、数字、中划线、下划线。 **默认取值：** 不涉及。

        :param source_name: The source_name of this ModelResource.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ModelResource.

        **参数解释：** 预置资产id。 **约束限制：** 使用预置资产时必填。 **取值范围：** 支持1-64位字符，可包含字母、中文、数字、中划线、下划线。 **默认取值：** 不涉及。

        :return: The asset_id of this ModelResource.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ModelResource.

        **参数解释：** 预置资产id。 **约束限制：** 使用预置资产时必填。 **取值范围：** 支持1-64位字符，可包含字母、中文、数字、中划线、下划线。 **默认取值：** 不涉及。

        :param asset_id: The asset_id of this ModelResource.
        :type asset_id: str
        """
        self._asset_id = asset_id

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
        if not isinstance(other, ModelResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
