# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNoteRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'war_room_id': 'str',
        'type': 'str',
        'content': 'str',
        'note_type': 'str'
    }

    attribute_map = {
        'war_room_id': 'war_room_id',
        'type': 'type',
        'content': 'content',
        'note_type': 'note_type'
    }

    def __init__(self, war_room_id=None, type=None, content=None, note_type=None):
        r"""CreateNoteRequestBody

        The model defined in huaweicloud sdk

        :param war_room_id: 评论的对象ID
        :type war_room_id: str
        :param type: 评论的类型
        :type type: str
        :param content: 评论的内容
        :type content: str
        :param note_type: 评论的动作类型
        :type note_type: str
        """
        
        

        self._war_room_id = None
        self._type = None
        self._content = None
        self._note_type = None
        self.discriminator = None

        if war_room_id is not None:
            self.war_room_id = war_room_id
        self.type = type
        self.content = content
        if note_type is not None:
            self.note_type = note_type

    @property
    def war_room_id(self):
        r"""Gets the war_room_id of this CreateNoteRequestBody.

        评论的对象ID

        :return: The war_room_id of this CreateNoteRequestBody.
        :rtype: str
        """
        return self._war_room_id

    @war_room_id.setter
    def war_room_id(self, war_room_id):
        r"""Sets the war_room_id of this CreateNoteRequestBody.

        评论的对象ID

        :param war_room_id: The war_room_id of this CreateNoteRequestBody.
        :type war_room_id: str
        """
        self._war_room_id = war_room_id

    @property
    def type(self):
        r"""Gets the type of this CreateNoteRequestBody.

        评论的类型

        :return: The type of this CreateNoteRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateNoteRequestBody.

        评论的类型

        :param type: The type of this CreateNoteRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this CreateNoteRequestBody.

        评论的内容

        :return: The content of this CreateNoteRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this CreateNoteRequestBody.

        评论的内容

        :param content: The content of this CreateNoteRequestBody.
        :type content: str
        """
        self._content = content

    @property
    def note_type(self):
        r"""Gets the note_type of this CreateNoteRequestBody.

        评论的动作类型

        :return: The note_type of this CreateNoteRequestBody.
        :rtype: str
        """
        return self._note_type

    @note_type.setter
    def note_type(self, note_type):
        r"""Sets the note_type of this CreateNoteRequestBody.

        评论的动作类型

        :param note_type: The note_type of this CreateNoteRequestBody.
        :type note_type: str
        """
        self._note_type = note_type

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
        if not isinstance(other, CreateNoteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
