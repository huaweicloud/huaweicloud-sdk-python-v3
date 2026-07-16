# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CodeResponse:

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
        'source_id': 'str',
        'mount_path': 'str',
        'efs_sub_path': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'source': 'source',
        'address': 'address',
        'source_id': 'source_id',
        'mount_path': 'mount_path',
        'efs_sub_path': 'efs_sub_path',
        'read_only': 'read_only'
    }

    def __init__(self, source=None, address=None, source_id=None, mount_path=None, efs_sub_path=None, read_only=None):
        r"""CodeResponse

        The model defined in huaweicloud sdk

        :param source: **参数解释：** 代码来源类别。 **取值范围：** - OBS：对象存储服务。 - OBSFS：OBS的文件系统接口。 - EFS：弹性文件服务。
        :type source: str
        :param address: **参数解释：** 代码来源地址，格式遵循不同存储系统。 **取值范围：** 不涉及。
        :type address: str
        :param source_id: **参数解释：** 代码来源ID，与address二选一，当且仅当source为EFS时，可以传入sfs turbo的ID。 **取值范围：** 不涉及。
        :type source_id: str
        :param mount_path: **参数解释：** 挂载到容器内的路径。 **约束限制：** 不涉及。 **取值范围：** 以(/)开头和结尾，可包含字母、数字、中划线、下划线，整个挂载路径长度不能超过255位。 **默认取值：** 不涉及。
        :type mount_path: str
        :param efs_sub_path: **参数解释：** EFS子路径。 **取值范围：** 不涉及。
        :type efs_sub_path: str
        :param read_only: **参数解释：** 挂载权限设置, 是否只读。 **取值范围：** - true：只读。 - false：非只读。
        :type read_only: bool
        """
        
        

        self._source = None
        self._address = None
        self._source_id = None
        self._mount_path = None
        self._efs_sub_path = None
        self._read_only = None
        self.discriminator = None

        self.source = source
        if address is not None:
            self.address = address
        if source_id is not None:
            self.source_id = source_id
        self.mount_path = mount_path
        if efs_sub_path is not None:
            self.efs_sub_path = efs_sub_path
        if read_only is not None:
            self.read_only = read_only

    @property
    def source(self):
        r"""Gets the source of this CodeResponse.

        **参数解释：** 代码来源类别。 **取值范围：** - OBS：对象存储服务。 - OBSFS：OBS的文件系统接口。 - EFS：弹性文件服务。

        :return: The source of this CodeResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CodeResponse.

        **参数解释：** 代码来源类别。 **取值范围：** - OBS：对象存储服务。 - OBSFS：OBS的文件系统接口。 - EFS：弹性文件服务。

        :param source: The source of this CodeResponse.
        :type source: str
        """
        self._source = source

    @property
    def address(self):
        r"""Gets the address of this CodeResponse.

        **参数解释：** 代码来源地址，格式遵循不同存储系统。 **取值范围：** 不涉及。

        :return: The address of this CodeResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this CodeResponse.

        **参数解释：** 代码来源地址，格式遵循不同存储系统。 **取值范围：** 不涉及。

        :param address: The address of this CodeResponse.
        :type address: str
        """
        self._address = address

    @property
    def source_id(self):
        r"""Gets the source_id of this CodeResponse.

        **参数解释：** 代码来源ID，与address二选一，当且仅当source为EFS时，可以传入sfs turbo的ID。 **取值范围：** 不涉及。

        :return: The source_id of this CodeResponse.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this CodeResponse.

        **参数解释：** 代码来源ID，与address二选一，当且仅当source为EFS时，可以传入sfs turbo的ID。 **取值范围：** 不涉及。

        :param source_id: The source_id of this CodeResponse.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def mount_path(self):
        r"""Gets the mount_path of this CodeResponse.

        **参数解释：** 挂载到容器内的路径。 **约束限制：** 不涉及。 **取值范围：** 以(/)开头和结尾，可包含字母、数字、中划线、下划线，整个挂载路径长度不能超过255位。 **默认取值：** 不涉及。

        :return: The mount_path of this CodeResponse.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this CodeResponse.

        **参数解释：** 挂载到容器内的路径。 **约束限制：** 不涉及。 **取值范围：** 以(/)开头和结尾，可包含字母、数字、中划线、下划线，整个挂载路径长度不能超过255位。 **默认取值：** 不涉及。

        :param mount_path: The mount_path of this CodeResponse.
        :type mount_path: str
        """
        self._mount_path = mount_path

    @property
    def efs_sub_path(self):
        r"""Gets the efs_sub_path of this CodeResponse.

        **参数解释：** EFS子路径。 **取值范围：** 不涉及。

        :return: The efs_sub_path of this CodeResponse.
        :rtype: str
        """
        return self._efs_sub_path

    @efs_sub_path.setter
    def efs_sub_path(self, efs_sub_path):
        r"""Sets the efs_sub_path of this CodeResponse.

        **参数解释：** EFS子路径。 **取值范围：** 不涉及。

        :param efs_sub_path: The efs_sub_path of this CodeResponse.
        :type efs_sub_path: str
        """
        self._efs_sub_path = efs_sub_path

    @property
    def read_only(self):
        r"""Gets the read_only of this CodeResponse.

        **参数解释：** 挂载权限设置, 是否只读。 **取值范围：** - true：只读。 - false：非只读。

        :return: The read_only of this CodeResponse.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        r"""Sets the read_only of this CodeResponse.

        **参数解释：** 挂载权限设置, 是否只读。 **取值范围：** - true：只读。 - false：非只读。

        :param read_only: The read_only of this CodeResponse.
        :type read_only: bool
        """
        self._read_only = read_only

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
        if not isinstance(other, CodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
