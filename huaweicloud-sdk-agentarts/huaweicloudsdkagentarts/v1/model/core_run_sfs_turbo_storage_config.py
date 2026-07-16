# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunSfsTurboStorageConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sfs_turbo_id': 'str',
        'sfs_path': 'str',
        'mount_path': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'sfs_turbo_id': 'sfs_turbo_id',
        'sfs_path': 'sfs_path',
        'mount_path': 'mount_path',
        'read_only': 'read_only'
    }

    def __init__(self, sfs_turbo_id=None, sfs_path=None, mount_path=None, read_only=None):
        r"""CoreRunSfsTurboStorageConfig

        The model defined in huaweicloud sdk

        :param sfs_turbo_id: **参数解释**: SFS Turbo实例ID。
        :type sfs_turbo_id: str
        :param sfs_path: **参数解释**: SFS Turbo存储的目录路径。
        :type sfs_path: str
        :param mount_path: **参数解释**: 挂载到运行时的目录路径。
        :type mount_path: str
        :param read_only: **参数解释**: 是否以只读方式挂载。
        :type read_only: bool
        """
        
        

        self._sfs_turbo_id = None
        self._sfs_path = None
        self._mount_path = None
        self._read_only = None
        self.discriminator = None

        self.sfs_turbo_id = sfs_turbo_id
        if sfs_path is not None:
            self.sfs_path = sfs_path
        self.mount_path = mount_path
        if read_only is not None:
            self.read_only = read_only

    @property
    def sfs_turbo_id(self):
        r"""Gets the sfs_turbo_id of this CoreRunSfsTurboStorageConfig.

        **参数解释**: SFS Turbo实例ID。

        :return: The sfs_turbo_id of this CoreRunSfsTurboStorageConfig.
        :rtype: str
        """
        return self._sfs_turbo_id

    @sfs_turbo_id.setter
    def sfs_turbo_id(self, sfs_turbo_id):
        r"""Sets the sfs_turbo_id of this CoreRunSfsTurboStorageConfig.

        **参数解释**: SFS Turbo实例ID。

        :param sfs_turbo_id: The sfs_turbo_id of this CoreRunSfsTurboStorageConfig.
        :type sfs_turbo_id: str
        """
        self._sfs_turbo_id = sfs_turbo_id

    @property
    def sfs_path(self):
        r"""Gets the sfs_path of this CoreRunSfsTurboStorageConfig.

        **参数解释**: SFS Turbo存储的目录路径。

        :return: The sfs_path of this CoreRunSfsTurboStorageConfig.
        :rtype: str
        """
        return self._sfs_path

    @sfs_path.setter
    def sfs_path(self, sfs_path):
        r"""Sets the sfs_path of this CoreRunSfsTurboStorageConfig.

        **参数解释**: SFS Turbo存储的目录路径。

        :param sfs_path: The sfs_path of this CoreRunSfsTurboStorageConfig.
        :type sfs_path: str
        """
        self._sfs_path = sfs_path

    @property
    def mount_path(self):
        r"""Gets the mount_path of this CoreRunSfsTurboStorageConfig.

        **参数解释**: 挂载到运行时的目录路径。

        :return: The mount_path of this CoreRunSfsTurboStorageConfig.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this CoreRunSfsTurboStorageConfig.

        **参数解释**: 挂载到运行时的目录路径。

        :param mount_path: The mount_path of this CoreRunSfsTurboStorageConfig.
        :type mount_path: str
        """
        self._mount_path = mount_path

    @property
    def read_only(self):
        r"""Gets the read_only of this CoreRunSfsTurboStorageConfig.

        **参数解释**: 是否以只读方式挂载。

        :return: The read_only of this CoreRunSfsTurboStorageConfig.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        r"""Sets the read_only of this CoreRunSfsTurboStorageConfig.

        **参数解释**: 是否以只读方式挂载。

        :param read_only: The read_only of this CoreRunSfsTurboStorageConfig.
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
        if not isinstance(other, CoreRunSfsTurboStorageConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
