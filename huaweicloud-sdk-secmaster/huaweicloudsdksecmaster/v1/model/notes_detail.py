# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotesDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'update_time': 'str',
        'data': 'NotesDetailData',
        'id': 'str',
        'is_deleted': 'bool',
        'marked_note': 'bool',
        'note_type': 'str',
        'project_id': 'str',
        'type': 'str',
        'user': 'NotesDetailUser',
        'war_room_id': 'str',
        'workspace_id': 'str',
        'content': 'object'
    }

    attribute_map = {
        'create_time': 'create_time',
        'update_time': 'update_time',
        'data': 'data',
        'id': 'id',
        'is_deleted': 'is_deleted',
        'marked_note': 'marked_note',
        'note_type': 'note_type',
        'project_id': 'project_id',
        'type': 'type',
        'user': 'user',
        'war_room_id': 'war_room_id',
        'workspace_id': 'workspace_id',
        'content': 'content'
    }

    def __init__(self, create_time=None, update_time=None, data=None, id=None, is_deleted=None, marked_note=None, note_type=None, project_id=None, type=None, user=None, war_room_id=None, workspace_id=None, content=None):
        r"""NotesDetail

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param data: 
        :type data: :class:`huaweicloudsdksecmaster.v1.NotesDetailData`
        :param id: 评论唯一UUID
        :type id: str
        :param is_deleted: 是否已删除
        :type is_deleted: bool
        :param marked_note: 标识是否是评论
        :type marked_note: bool
        :param note_type: 评论的动作类型
        :type note_type: str
        :param project_id: 项目ID
        :type project_id: str
        :param type: 评论的类型
        :type type: str
        :param user: 
        :type user: :class:`huaweicloudsdksecmaster.v1.NotesDetailUser`
        :param war_room_id: 评论的对象ID
        :type war_room_id: str
        :param workspace_id: 空间
        :type workspace_id: str
        :param content: 评论详情信息
        :type content: object
        """
        
        

        self._create_time = None
        self._update_time = None
        self._data = None
        self._id = None
        self._is_deleted = None
        self._marked_note = None
        self._note_type = None
        self._project_id = None
        self._type = None
        self._user = None
        self._war_room_id = None
        self._workspace_id = None
        self._content = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if data is not None:
            self.data = data
        if id is not None:
            self.id = id
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if marked_note is not None:
            self.marked_note = marked_note
        if note_type is not None:
            self.note_type = note_type
        if project_id is not None:
            self.project_id = project_id
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user
        if war_room_id is not None:
            self.war_room_id = war_room_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if content is not None:
            self.content = content

    @property
    def create_time(self):
        r"""Gets the create_time of this NotesDetail.

        创建时间

        :return: The create_time of this NotesDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this NotesDetail.

        创建时间

        :param create_time: The create_time of this NotesDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this NotesDetail.

        更新时间

        :return: The update_time of this NotesDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this NotesDetail.

        更新时间

        :param update_time: The update_time of this NotesDetail.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def data(self):
        r"""Gets the data of this NotesDetail.

        :return: The data of this NotesDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.NotesDetailData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this NotesDetail.

        :param data: The data of this NotesDetail.
        :type data: :class:`huaweicloudsdksecmaster.v1.NotesDetailData`
        """
        self._data = data

    @property
    def id(self):
        r"""Gets the id of this NotesDetail.

        评论唯一UUID

        :return: The id of this NotesDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NotesDetail.

        评论唯一UUID

        :param id: The id of this NotesDetail.
        :type id: str
        """
        self._id = id

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this NotesDetail.

        是否已删除

        :return: The is_deleted of this NotesDetail.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this NotesDetail.

        是否已删除

        :param is_deleted: The is_deleted of this NotesDetail.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def marked_note(self):
        r"""Gets the marked_note of this NotesDetail.

        标识是否是评论

        :return: The marked_note of this NotesDetail.
        :rtype: bool
        """
        return self._marked_note

    @marked_note.setter
    def marked_note(self, marked_note):
        r"""Sets the marked_note of this NotesDetail.

        标识是否是评论

        :param marked_note: The marked_note of this NotesDetail.
        :type marked_note: bool
        """
        self._marked_note = marked_note

    @property
    def note_type(self):
        r"""Gets the note_type of this NotesDetail.

        评论的动作类型

        :return: The note_type of this NotesDetail.
        :rtype: str
        """
        return self._note_type

    @note_type.setter
    def note_type(self, note_type):
        r"""Sets the note_type of this NotesDetail.

        评论的动作类型

        :param note_type: The note_type of this NotesDetail.
        :type note_type: str
        """
        self._note_type = note_type

    @property
    def project_id(self):
        r"""Gets the project_id of this NotesDetail.

        项目ID

        :return: The project_id of this NotesDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this NotesDetail.

        项目ID

        :param project_id: The project_id of this NotesDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        r"""Gets the type of this NotesDetail.

        评论的类型

        :return: The type of this NotesDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NotesDetail.

        评论的类型

        :param type: The type of this NotesDetail.
        :type type: str
        """
        self._type = type

    @property
    def user(self):
        r"""Gets the user of this NotesDetail.

        :return: The user of this NotesDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.NotesDetailUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this NotesDetail.

        :param user: The user of this NotesDetail.
        :type user: :class:`huaweicloudsdksecmaster.v1.NotesDetailUser`
        """
        self._user = user

    @property
    def war_room_id(self):
        r"""Gets the war_room_id of this NotesDetail.

        评论的对象ID

        :return: The war_room_id of this NotesDetail.
        :rtype: str
        """
        return self._war_room_id

    @war_room_id.setter
    def war_room_id(self, war_room_id):
        r"""Sets the war_room_id of this NotesDetail.

        评论的对象ID

        :param war_room_id: The war_room_id of this NotesDetail.
        :type war_room_id: str
        """
        self._war_room_id = war_room_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this NotesDetail.

        空间

        :return: The workspace_id of this NotesDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this NotesDetail.

        空间

        :param workspace_id: The workspace_id of this NotesDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def content(self):
        r"""Gets the content of this NotesDetail.

        评论详情信息

        :return: The content of this NotesDetail.
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this NotesDetail.

        评论详情信息

        :param content: The content of this NotesDetail.
        :type content: object
        """
        self._content = content

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
        if not isinstance(other, NotesDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
