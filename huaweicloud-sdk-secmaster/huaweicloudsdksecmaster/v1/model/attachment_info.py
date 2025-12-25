# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentInfo:

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
        'file_name': 'str',
        'file_folder': 'str',
        'workspace_id': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'is_deleted': 'str',
        'storage_type': 'str',
        'storage_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'file_name',
        'file_folder': 'file_folder',
        'workspace_id': 'workspace_id',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'is_deleted': 'is_deleted',
        'storage_type': 'storage_type',
        'storage_url': 'storage_url'
    }

    def __init__(self, id=None, file_name=None, file_folder=None, workspace_id=None, creator_id=None, creator_name=None, create_time=None, update_time=None, modifier_id=None, modifier_name=None, is_deleted=None, storage_type=None, storage_url=None):
        r"""AttachmentInfo

        The model defined in huaweicloud sdk

        :param id: 附件id
        :type id: str
        :param file_name: 附件名称
        :type file_name: str
        :param file_folder: 文件夹.
        :type file_folder: str
        :param workspace_id: 当前的工作空间id
        :type workspace_id: str
        :param creator_id: 创建者ID
        :type creator_id: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param modifier_id: 修改者ID
        :type modifier_id: str
        :param modifier_name: 修改者名称
        :type modifier_name: str
        :param is_deleted: 是否删除.
        :type is_deleted: str
        :param storage_type: 存储类型.
        :type storage_type: str
        :param storage_url: 存储url.
        :type storage_url: str
        """
        
        

        self._id = None
        self._file_name = None
        self._file_folder = None
        self._workspace_id = None
        self._creator_id = None
        self._creator_name = None
        self._create_time = None
        self._update_time = None
        self._modifier_id = None
        self._modifier_name = None
        self._is_deleted = None
        self._storage_type = None
        self._storage_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if file_folder is not None:
            self.file_folder = file_folder
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if storage_type is not None:
            self.storage_type = storage_type
        if storage_url is not None:
            self.storage_url = storage_url

    @property
    def id(self):
        r"""Gets the id of this AttachmentInfo.

        附件id

        :return: The id of this AttachmentInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AttachmentInfo.

        附件id

        :param id: The id of this AttachmentInfo.
        :type id: str
        """
        self._id = id

    @property
    def file_name(self):
        r"""Gets the file_name of this AttachmentInfo.

        附件名称

        :return: The file_name of this AttachmentInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this AttachmentInfo.

        附件名称

        :param file_name: The file_name of this AttachmentInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_folder(self):
        r"""Gets the file_folder of this AttachmentInfo.

        文件夹.

        :return: The file_folder of this AttachmentInfo.
        :rtype: str
        """
        return self._file_folder

    @file_folder.setter
    def file_folder(self, file_folder):
        r"""Sets the file_folder of this AttachmentInfo.

        文件夹.

        :param file_folder: The file_folder of this AttachmentInfo.
        :type file_folder: str
        """
        self._file_folder = file_folder

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AttachmentInfo.

        当前的工作空间id

        :return: The workspace_id of this AttachmentInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AttachmentInfo.

        当前的工作空间id

        :param workspace_id: The workspace_id of this AttachmentInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def creator_id(self):
        r"""Gets the creator_id of this AttachmentInfo.

        创建者ID

        :return: The creator_id of this AttachmentInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this AttachmentInfo.

        创建者ID

        :param creator_id: The creator_id of this AttachmentInfo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this AttachmentInfo.

        创建者名称

        :return: The creator_name of this AttachmentInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this AttachmentInfo.

        创建者名称

        :param creator_name: The creator_name of this AttachmentInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def create_time(self):
        r"""Gets the create_time of this AttachmentInfo.

        创建时间

        :return: The create_time of this AttachmentInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AttachmentInfo.

        创建时间

        :param create_time: The create_time of this AttachmentInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AttachmentInfo.

        更新时间

        :return: The update_time of this AttachmentInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AttachmentInfo.

        更新时间

        :param update_time: The update_time of this AttachmentInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this AttachmentInfo.

        修改者ID

        :return: The modifier_id of this AttachmentInfo.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this AttachmentInfo.

        修改者ID

        :param modifier_id: The modifier_id of this AttachmentInfo.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this AttachmentInfo.

        修改者名称

        :return: The modifier_name of this AttachmentInfo.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this AttachmentInfo.

        修改者名称

        :param modifier_name: The modifier_name of this AttachmentInfo.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this AttachmentInfo.

        是否删除.

        :return: The is_deleted of this AttachmentInfo.
        :rtype: str
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this AttachmentInfo.

        是否删除.

        :param is_deleted: The is_deleted of this AttachmentInfo.
        :type is_deleted: str
        """
        self._is_deleted = is_deleted

    @property
    def storage_type(self):
        r"""Gets the storage_type of this AttachmentInfo.

        存储类型.

        :return: The storage_type of this AttachmentInfo.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this AttachmentInfo.

        存储类型.

        :param storage_type: The storage_type of this AttachmentInfo.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def storage_url(self):
        r"""Gets the storage_url of this AttachmentInfo.

        存储url.

        :return: The storage_url of this AttachmentInfo.
        :rtype: str
        """
        return self._storage_url

    @storage_url.setter
    def storage_url(self, storage_url):
        r"""Sets the storage_url of this AttachmentInfo.

        存储url.

        :param storage_url: The storage_url of this AttachmentInfo.
        :type storage_url: str
        """
        self._storage_url = storage_url

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
        if not isinstance(other, AttachmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
