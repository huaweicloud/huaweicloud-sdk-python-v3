# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackCopyByHostIdResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'backup_name': 'str',
        'backup_status': 'str',
        'create_time': 'int',
        'os_images_data': 'list[ImageData]',
        'backup_tag': 'int'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'backup_name': 'backup_name',
        'backup_status': 'backup_status',
        'create_time': 'create_time',
        'os_images_data': 'os_images_data',
        'backup_tag': 'backup_tag'
    }

    def __init__(self, backup_id=None, backup_name=None, backup_status=None, create_time=None, os_images_data=None, backup_tag=None):
        r"""BackCopyByHostIdResponse

        The model defined in huaweicloud sdk

        :param backup_id: **参数解释** 备份ID **取值范围** 字符长度0-65535位 
        :type backup_id: str
        :param backup_name: **参数解释** 备份名称 **取值范围** 字符长度0-65535位 
        :type backup_name: str
        :param backup_status: **参数解释** 备份状态 **取值范围** 字符长度0-65535位 
        :type backup_status: str
        :param create_time: **参数解释** 创建时间 **取值范围** 取值0-2147483647 
        :type create_time: int
        :param os_images_data: **参数解释** 备份注册镜像ID列表 **取值范围** 取值0-200 
        :type os_images_data: list[:class:`huaweicloudsdkhss.v5.ImageData`]
        :param backup_tag: **参数解释** 备份标识 **取值范围** - 0：定时周期 - 1：勒索加密 
        :type backup_tag: int
        """
        
        

        self._backup_id = None
        self._backup_name = None
        self._backup_status = None
        self._create_time = None
        self._os_images_data = None
        self._backup_tag = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if backup_name is not None:
            self.backup_name = backup_name
        if backup_status is not None:
            self.backup_status = backup_status
        if create_time is not None:
            self.create_time = create_time
        if os_images_data is not None:
            self.os_images_data = os_images_data
        if backup_tag is not None:
            self.backup_tag = backup_tag

    @property
    def backup_id(self):
        r"""Gets the backup_id of this BackCopyByHostIdResponse.

        **参数解释** 备份ID **取值范围** 字符长度0-65535位 

        :return: The backup_id of this BackCopyByHostIdResponse.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this BackCopyByHostIdResponse.

        **参数解释** 备份ID **取值范围** 字符长度0-65535位 

        :param backup_id: The backup_id of this BackCopyByHostIdResponse.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_name(self):
        r"""Gets the backup_name of this BackCopyByHostIdResponse.

        **参数解释** 备份名称 **取值范围** 字符长度0-65535位 

        :return: The backup_name of this BackCopyByHostIdResponse.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        r"""Sets the backup_name of this BackCopyByHostIdResponse.

        **参数解释** 备份名称 **取值范围** 字符长度0-65535位 

        :param backup_name: The backup_name of this BackCopyByHostIdResponse.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def backup_status(self):
        r"""Gets the backup_status of this BackCopyByHostIdResponse.

        **参数解释** 备份状态 **取值范围** 字符长度0-65535位 

        :return: The backup_status of this BackCopyByHostIdResponse.
        :rtype: str
        """
        return self._backup_status

    @backup_status.setter
    def backup_status(self, backup_status):
        r"""Sets the backup_status of this BackCopyByHostIdResponse.

        **参数解释** 备份状态 **取值范围** 字符长度0-65535位 

        :param backup_status: The backup_status of this BackCopyByHostIdResponse.
        :type backup_status: str
        """
        self._backup_status = backup_status

    @property
    def create_time(self):
        r"""Gets the create_time of this BackCopyByHostIdResponse.

        **参数解释** 创建时间 **取值范围** 取值0-2147483647 

        :return: The create_time of this BackCopyByHostIdResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BackCopyByHostIdResponse.

        **参数解释** 创建时间 **取值范围** 取值0-2147483647 

        :param create_time: The create_time of this BackCopyByHostIdResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def os_images_data(self):
        r"""Gets the os_images_data of this BackCopyByHostIdResponse.

        **参数解释** 备份注册镜像ID列表 **取值范围** 取值0-200 

        :return: The os_images_data of this BackCopyByHostIdResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ImageData`]
        """
        return self._os_images_data

    @os_images_data.setter
    def os_images_data(self, os_images_data):
        r"""Sets the os_images_data of this BackCopyByHostIdResponse.

        **参数解释** 备份注册镜像ID列表 **取值范围** 取值0-200 

        :param os_images_data: The os_images_data of this BackCopyByHostIdResponse.
        :type os_images_data: list[:class:`huaweicloudsdkhss.v5.ImageData`]
        """
        self._os_images_data = os_images_data

    @property
    def backup_tag(self):
        r"""Gets the backup_tag of this BackCopyByHostIdResponse.

        **参数解释** 备份标识 **取值范围** - 0：定时周期 - 1：勒索加密 

        :return: The backup_tag of this BackCopyByHostIdResponse.
        :rtype: int
        """
        return self._backup_tag

    @backup_tag.setter
    def backup_tag(self, backup_tag):
        r"""Sets the backup_tag of this BackCopyByHostIdResponse.

        **参数解释** 备份标识 **取值范围** - 0：定时周期 - 1：勒索加密 

        :param backup_tag: The backup_tag of this BackCopyByHostIdResponse.
        :type backup_tag: int
        """
        self._backup_tag = backup_tag

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
        if not isinstance(other, BackCopyByHostIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
