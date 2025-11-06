# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupResp:

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
        'name': 'str',
        'image_type': 'str',
        'vault_id': 'str',
        'status': 'str',
        'resource_size': 'int',
        'resource_id': 'str',
        'resource_type': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'image_type': 'image_type',
        'vault_id': 'vault_id',
        'status': 'status',
        'resource_size': 'resource_size',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'resource_name': 'resource_name'
    }

    def __init__(self, id=None, name=None, image_type=None, vault_id=None, status=None, resource_size=None, resource_id=None, resource_type=None, resource_name=None):
        r"""BackupResp

        The model defined in huaweicloud sdk

        :param id: **参数解释** 卷备份ID **取值范围** 字符长度0-65535位 
        :type id: str
        :param name: **参数解释** 磁盘备份名称 **取值范围** 字符长度0-65535位 
        :type name: str
        :param image_type: **参数解释** 备份类型 **取值范围** 字符长度0-65535位 
        :type image_type: str
        :param vault_id: **参数解释** 备份所在的存储库ID **取值范围** 字符长度0-65535位 
        :type vault_id: str
        :param status: **参数解释** 备份状态 **取值范围** 字符长度0-65535位 
        :type status: str
        :param resource_size: **参数解释** 创建时间 **取值范围** 取值0-2147483647 
        :type resource_size: int
        :param resource_id: **参数解释** 资源ID 对应host主机ID **取值范围** 字符长度0-65535位 
        :type resource_id: str
        :param resource_type: **参数解释** 资源类型 **取值范围** 字符长度0-65535位 
        :type resource_type: str
        :param resource_name: **参数解释** 资源名称 对应host主机名称 **取值范围** 字符长度0-65535位 
        :type resource_name: str
        """
        
        

        self._id = None
        self._name = None
        self._image_type = None
        self._vault_id = None
        self._status = None
        self._resource_size = None
        self._resource_id = None
        self._resource_type = None
        self._resource_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if image_type is not None:
            self.image_type = image_type
        if vault_id is not None:
            self.vault_id = vault_id
        if status is not None:
            self.status = status
        if resource_size is not None:
            self.resource_size = resource_size
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def id(self):
        r"""Gets the id of this BackupResp.

        **参数解释** 卷备份ID **取值范围** 字符长度0-65535位 

        :return: The id of this BackupResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackupResp.

        **参数解释** 卷备份ID **取值范围** 字符长度0-65535位 

        :param id: The id of this BackupResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BackupResp.

        **参数解释** 磁盘备份名称 **取值范围** 字符长度0-65535位 

        :return: The name of this BackupResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupResp.

        **参数解释** 磁盘备份名称 **取值范围** 字符长度0-65535位 

        :param name: The name of this BackupResp.
        :type name: str
        """
        self._name = name

    @property
    def image_type(self):
        r"""Gets the image_type of this BackupResp.

        **参数解释** 备份类型 **取值范围** 字符长度0-65535位 

        :return: The image_type of this BackupResp.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this BackupResp.

        **参数解释** 备份类型 **取值范围** 字符长度0-65535位 

        :param image_type: The image_type of this BackupResp.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def vault_id(self):
        r"""Gets the vault_id of this BackupResp.

        **参数解释** 备份所在的存储库ID **取值范围** 字符长度0-65535位 

        :return: The vault_id of this BackupResp.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this BackupResp.

        **参数解释** 备份所在的存储库ID **取值范围** 字符长度0-65535位 

        :param vault_id: The vault_id of this BackupResp.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def status(self):
        r"""Gets the status of this BackupResp.

        **参数解释** 备份状态 **取值范围** 字符长度0-65535位 

        :return: The status of this BackupResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BackupResp.

        **参数解释** 备份状态 **取值范围** 字符长度0-65535位 

        :param status: The status of this BackupResp.
        :type status: str
        """
        self._status = status

    @property
    def resource_size(self):
        r"""Gets the resource_size of this BackupResp.

        **参数解释** 创建时间 **取值范围** 取值0-2147483647 

        :return: The resource_size of this BackupResp.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this BackupResp.

        **参数解释** 创建时间 **取值范围** 取值0-2147483647 

        :param resource_size: The resource_size of this BackupResp.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def resource_id(self):
        r"""Gets the resource_id of this BackupResp.

        **参数解释** 资源ID 对应host主机ID **取值范围** 字符长度0-65535位 

        :return: The resource_id of this BackupResp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this BackupResp.

        **参数解释** 资源ID 对应host主机ID **取值范围** 字符长度0-65535位 

        :param resource_id: The resource_id of this BackupResp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this BackupResp.

        **参数解释** 资源类型 **取值范围** 字符长度0-65535位 

        :return: The resource_type of this BackupResp.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this BackupResp.

        **参数解释** 资源类型 **取值范围** 字符长度0-65535位 

        :param resource_type: The resource_type of this BackupResp.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        r"""Gets the resource_name of this BackupResp.

        **参数解释** 资源名称 对应host主机名称 **取值范围** 字符长度0-65535位 

        :return: The resource_name of this BackupResp.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this BackupResp.

        **参数解释** 资源名称 对应host主机名称 **取值范围** 字符长度0-65535位 

        :param resource_name: The resource_name of this BackupResp.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, BackupResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
