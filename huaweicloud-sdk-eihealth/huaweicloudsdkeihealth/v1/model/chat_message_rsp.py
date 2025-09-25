# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatMessageRsp:

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
        'role': 'MessageRole',
        'type': 'QaType',
        'create_time': 'str',
        'update_time': 'str',
        'message': 'ChatMessage',
        'addition': 'ChatAddition'
    }

    attribute_map = {
        'id': 'id',
        'role': 'role',
        'type': 'type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'message': 'message',
        'addition': 'addition'
    }

    def __init__(self, id=None, role=None, type=None, create_time=None, update_time=None, message=None, addition=None):
        r"""ChatMessageRsp

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 问答ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type id: str
        :param role: 
        :type role: :class:`huaweicloudsdkeihealth.v1.MessageRole`
        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.QaType`
        :param create_time: **参数解释**： 问答创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type create_time: str
        :param update_time: **参数解释**： 问答更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type update_time: str
        :param message: 
        :type message: :class:`huaweicloudsdkeihealth.v1.ChatMessage`
        :param addition: 
        :type addition: :class:`huaweicloudsdkeihealth.v1.ChatAddition`
        """
        
        

        self._id = None
        self._role = None
        self._type = None
        self._create_time = None
        self._update_time = None
        self._message = None
        self._addition = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if role is not None:
            self.role = role
        if type is not None:
            self.type = type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if message is not None:
            self.message = message
        if addition is not None:
            self.addition = addition

    @property
    def id(self):
        r"""Gets the id of this ChatMessageRsp.

        **参数解释**： 问答ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The id of this ChatMessageRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChatMessageRsp.

        **参数解释**： 问答ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param id: The id of this ChatMessageRsp.
        :type id: str
        """
        self._id = id

    @property
    def role(self):
        r"""Gets the role of this ChatMessageRsp.

        :return: The role of this ChatMessageRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.MessageRole`
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ChatMessageRsp.

        :param role: The role of this ChatMessageRsp.
        :type role: :class:`huaweicloudsdkeihealth.v1.MessageRole`
        """
        self._role = role

    @property
    def type(self):
        r"""Gets the type of this ChatMessageRsp.

        :return: The type of this ChatMessageRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.QaType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ChatMessageRsp.

        :param type: The type of this ChatMessageRsp.
        :type type: :class:`huaweicloudsdkeihealth.v1.QaType`
        """
        self._type = type

    @property
    def create_time(self):
        r"""Gets the create_time of this ChatMessageRsp.

        **参数解释**： 问答创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The create_time of this ChatMessageRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ChatMessageRsp.

        **参数解释**： 问答创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param create_time: The create_time of this ChatMessageRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ChatMessageRsp.

        **参数解释**： 问答更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The update_time of this ChatMessageRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ChatMessageRsp.

        **参数解释**： 问答更新时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param update_time: The update_time of this ChatMessageRsp.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def message(self):
        r"""Gets the message of this ChatMessageRsp.

        :return: The message of this ChatMessageRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ChatMessage`
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ChatMessageRsp.

        :param message: The message of this ChatMessageRsp.
        :type message: :class:`huaweicloudsdkeihealth.v1.ChatMessage`
        """
        self._message = message

    @property
    def addition(self):
        r"""Gets the addition of this ChatMessageRsp.

        :return: The addition of this ChatMessageRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ChatAddition`
        """
        return self._addition

    @addition.setter
    def addition(self, addition):
        r"""Sets the addition of this ChatMessageRsp.

        :param addition: The addition of this ChatMessageRsp.
        :type addition: :class:`huaweicloudsdkeihealth.v1.ChatAddition`
        """
        self._addition = addition

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChatMessageRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
