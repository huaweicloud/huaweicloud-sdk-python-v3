# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileStorageConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_id': 'str',
        'storage_name': 'str',
        'storage_path': 'str',
        'mount_path': 'str'
    }

    attribute_map = {
        'storage_id': 'storage_id',
        'storage_name': 'storage_name',
        'storage_path': 'storage_path',
        'mount_path': 'mount_path'
    }

    def __init__(self, storage_id=None, storage_name=None, storage_path=None, mount_path=None):
        r"""FileStorageConfig

        The model defined in huaweicloud sdk

        :param storage_id: **参数解释**：存储资源ID，可通过[查询存储资源列表](ListV2Storages.xml)获取存储资源ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type storage_id: str
        :param storage_name: **参数解释**：存储的名称，对应PVC的名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线的组合，长度为1~63个字符。 **默认取值**：不涉及。
        :type storage_name: str
        :param storage_path: **参数解释**：存储上的路径。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、斜杠及特殊字符，最小长度为1，最大长度为1024。 **默认取值**：不涉及。
        :type storage_path: str
        :param mount_path: **参数解释**：挂载到容器的路径。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、斜杠及特殊字符，最小长度为1，最大长度为1024。 **默认取值**：不涉及。
        :type mount_path: str
        """
        
        

        self._storage_id = None
        self._storage_name = None
        self._storage_path = None
        self._mount_path = None
        self.discriminator = None

        self.storage_id = storage_id
        if storage_name is not None:
            self.storage_name = storage_name
        if storage_path is not None:
            self.storage_path = storage_path
        if mount_path is not None:
            self.mount_path = mount_path

    @property
    def storage_id(self):
        r"""Gets the storage_id of this FileStorageConfig.

        **参数解释**：存储资源ID，可通过[查询存储资源列表](ListV2Storages.xml)获取存储资源ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The storage_id of this FileStorageConfig.
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        r"""Sets the storage_id of this FileStorageConfig.

        **参数解释**：存储资源ID，可通过[查询存储资源列表](ListV2Storages.xml)获取存储资源ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param storage_id: The storage_id of this FileStorageConfig.
        :type storage_id: str
        """
        self._storage_id = storage_id

    @property
    def storage_name(self):
        r"""Gets the storage_name of this FileStorageConfig.

        **参数解释**：存储的名称，对应PVC的名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线的组合，长度为1~63个字符。 **默认取值**：不涉及。

        :return: The storage_name of this FileStorageConfig.
        :rtype: str
        """
        return self._storage_name

    @storage_name.setter
    def storage_name(self, storage_name):
        r"""Sets the storage_name of this FileStorageConfig.

        **参数解释**：存储的名称，对应PVC的名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线的组合，长度为1~63个字符。 **默认取值**：不涉及。

        :param storage_name: The storage_name of this FileStorageConfig.
        :type storage_name: str
        """
        self._storage_name = storage_name

    @property
    def storage_path(self):
        r"""Gets the storage_path of this FileStorageConfig.

        **参数解释**：存储上的路径。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、斜杠及特殊字符，最小长度为1，最大长度为1024。 **默认取值**：不涉及。

        :return: The storage_path of this FileStorageConfig.
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        r"""Sets the storage_path of this FileStorageConfig.

        **参数解释**：存储上的路径。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、斜杠及特殊字符，最小长度为1，最大长度为1024。 **默认取值**：不涉及。

        :param storage_path: The storage_path of this FileStorageConfig.
        :type storage_path: str
        """
        self._storage_path = storage_path

    @property
    def mount_path(self):
        r"""Gets the mount_path of this FileStorageConfig.

        **参数解释**：挂载到容器的路径。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、斜杠及特殊字符，最小长度为1，最大长度为1024。 **默认取值**：不涉及。

        :return: The mount_path of this FileStorageConfig.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this FileStorageConfig.

        **参数解释**：挂载到容器的路径。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、斜杠及特殊字符，最小长度为1，最大长度为1024。 **默认取值**：不涉及。

        :param mount_path: The mount_path of this FileStorageConfig.
        :type mount_path: str
        """
        self._mount_path = mount_path

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
        if not isinstance(other, FileStorageConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
