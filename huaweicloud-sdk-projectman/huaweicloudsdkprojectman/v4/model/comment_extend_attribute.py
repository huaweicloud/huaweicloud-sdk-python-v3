# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommentExtendAttribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operator': 'UserVO',
        'operator_id': 'str',
        'action': 'str',
        'action_us': 'str',
        'object_type': 'str',
        'pre_status_code': 'str',
        'new_status_code': 'str',
        'pre_status': 'object',
        'new_status': 'object',
        'field_type': 'str',
        'field_type_id': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'operator': 'operator',
        'operator_id': 'operator_id',
        'action': 'action',
        'action_us': 'action_us',
        'object_type': 'object_type',
        'pre_status_code': 'pre_status_code',
        'new_status_code': 'new_status_code',
        'pre_status': 'pre_status',
        'new_status': 'new_status',
        'field_type': 'field_type',
        'field_type_id': 'field_type_id',
        'display_name': 'display_name'
    }

    def __init__(self, operator=None, operator_id=None, action=None, action_us=None, object_type=None, pre_status_code=None, new_status_code=None, pre_status=None, new_status=None, field_type=None, field_type_id=None, display_name=None):
        r"""CommentExtendAttribute

        The model defined in huaweicloud sdk

        :param operator: 
        :type operator: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param operator_id: 操作人Id
        :type operator_id: str
        :param action: 系统生成评论时执行的动作
        :type action: str
        :param action_us: 系统生成评论时执行的动作(英文)
        :type action_us: str
        :param object_type: 系统生成评论对应的对象类型
        :type object_type: str
        :param pre_status_code: 工作项流转前的状态Code
        :type pre_status_code: str
        :param new_status_code: 工作项流转后的状态Code
        :type new_status_code: str
        :param pre_status: 对象类型根据field_type_id值变化而变化。 field_type_id&#x3D;10001时，为StatusVO field_type_id&#x3D;10007、10008时，为字符串 field_type_id&#x3D;10003、10004时，为日期时间 field_type_id&#x3D;10005、10006时，为数字
        :type pre_status: object
        :param new_status: 对象类型根据field_type_id值变化而变化。 field_type_id&#x3D;10001、10002时，为StatusVO field_type_id&#x3D;10007、10008时，为字符串 field_type_id&#x3D;10003、10004时，为日期时间 field_type_id&#x3D;10005、10006时，为数字 field_type_id&#x3D;10009、10010时，为UserVO
        :type new_status: object
        :param field_type: 字段类型
        :type field_type: str
        :param field_type_id: 字段类型对应的Id
        :type field_type_id: str
        :param display_name: 字段显示名
        :type display_name: str
        """
        
        

        self._operator = None
        self._operator_id = None
        self._action = None
        self._action_us = None
        self._object_type = None
        self._pre_status_code = None
        self._new_status_code = None
        self._pre_status = None
        self._new_status = None
        self._field_type = None
        self._field_type_id = None
        self._display_name = None
        self.discriminator = None

        if operator is not None:
            self.operator = operator
        if operator_id is not None:
            self.operator_id = operator_id
        if action is not None:
            self.action = action
        if action_us is not None:
            self.action_us = action_us
        if object_type is not None:
            self.object_type = object_type
        if pre_status_code is not None:
            self.pre_status_code = pre_status_code
        if new_status_code is not None:
            self.new_status_code = new_status_code
        if pre_status is not None:
            self.pre_status = pre_status
        if new_status is not None:
            self.new_status = new_status
        if field_type is not None:
            self.field_type = field_type
        if field_type_id is not None:
            self.field_type_id = field_type_id
        if display_name is not None:
            self.display_name = display_name

    @property
    def operator(self):
        r"""Gets the operator of this CommentExtendAttribute.

        :return: The operator of this CommentExtendAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this CommentExtendAttribute.

        :param operator: The operator of this CommentExtendAttribute.
        :type operator: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._operator = operator

    @property
    def operator_id(self):
        r"""Gets the operator_id of this CommentExtendAttribute.

        操作人Id

        :return: The operator_id of this CommentExtendAttribute.
        :rtype: str
        """
        return self._operator_id

    @operator_id.setter
    def operator_id(self, operator_id):
        r"""Sets the operator_id of this CommentExtendAttribute.

        操作人Id

        :param operator_id: The operator_id of this CommentExtendAttribute.
        :type operator_id: str
        """
        self._operator_id = operator_id

    @property
    def action(self):
        r"""Gets the action of this CommentExtendAttribute.

        系统生成评论时执行的动作

        :return: The action of this CommentExtendAttribute.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CommentExtendAttribute.

        系统生成评论时执行的动作

        :param action: The action of this CommentExtendAttribute.
        :type action: str
        """
        self._action = action

    @property
    def action_us(self):
        r"""Gets the action_us of this CommentExtendAttribute.

        系统生成评论时执行的动作(英文)

        :return: The action_us of this CommentExtendAttribute.
        :rtype: str
        """
        return self._action_us

    @action_us.setter
    def action_us(self, action_us):
        r"""Sets the action_us of this CommentExtendAttribute.

        系统生成评论时执行的动作(英文)

        :param action_us: The action_us of this CommentExtendAttribute.
        :type action_us: str
        """
        self._action_us = action_us

    @property
    def object_type(self):
        r"""Gets the object_type of this CommentExtendAttribute.

        系统生成评论对应的对象类型

        :return: The object_type of this CommentExtendAttribute.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this CommentExtendAttribute.

        系统生成评论对应的对象类型

        :param object_type: The object_type of this CommentExtendAttribute.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def pre_status_code(self):
        r"""Gets the pre_status_code of this CommentExtendAttribute.

        工作项流转前的状态Code

        :return: The pre_status_code of this CommentExtendAttribute.
        :rtype: str
        """
        return self._pre_status_code

    @pre_status_code.setter
    def pre_status_code(self, pre_status_code):
        r"""Sets the pre_status_code of this CommentExtendAttribute.

        工作项流转前的状态Code

        :param pre_status_code: The pre_status_code of this CommentExtendAttribute.
        :type pre_status_code: str
        """
        self._pre_status_code = pre_status_code

    @property
    def new_status_code(self):
        r"""Gets the new_status_code of this CommentExtendAttribute.

        工作项流转后的状态Code

        :return: The new_status_code of this CommentExtendAttribute.
        :rtype: str
        """
        return self._new_status_code

    @new_status_code.setter
    def new_status_code(self, new_status_code):
        r"""Sets the new_status_code of this CommentExtendAttribute.

        工作项流转后的状态Code

        :param new_status_code: The new_status_code of this CommentExtendAttribute.
        :type new_status_code: str
        """
        self._new_status_code = new_status_code

    @property
    def pre_status(self):
        r"""Gets the pre_status of this CommentExtendAttribute.

        对象类型根据field_type_id值变化而变化。 field_type_id=10001时，为StatusVO field_type_id=10007、10008时，为字符串 field_type_id=10003、10004时，为日期时间 field_type_id=10005、10006时，为数字

        :return: The pre_status of this CommentExtendAttribute.
        :rtype: object
        """
        return self._pre_status

    @pre_status.setter
    def pre_status(self, pre_status):
        r"""Sets the pre_status of this CommentExtendAttribute.

        对象类型根据field_type_id值变化而变化。 field_type_id=10001时，为StatusVO field_type_id=10007、10008时，为字符串 field_type_id=10003、10004时，为日期时间 field_type_id=10005、10006时，为数字

        :param pre_status: The pre_status of this CommentExtendAttribute.
        :type pre_status: object
        """
        self._pre_status = pre_status

    @property
    def new_status(self):
        r"""Gets the new_status of this CommentExtendAttribute.

        对象类型根据field_type_id值变化而变化。 field_type_id=10001、10002时，为StatusVO field_type_id=10007、10008时，为字符串 field_type_id=10003、10004时，为日期时间 field_type_id=10005、10006时，为数字 field_type_id=10009、10010时，为UserVO

        :return: The new_status of this CommentExtendAttribute.
        :rtype: object
        """
        return self._new_status

    @new_status.setter
    def new_status(self, new_status):
        r"""Sets the new_status of this CommentExtendAttribute.

        对象类型根据field_type_id值变化而变化。 field_type_id=10001、10002时，为StatusVO field_type_id=10007、10008时，为字符串 field_type_id=10003、10004时，为日期时间 field_type_id=10005、10006时，为数字 field_type_id=10009、10010时，为UserVO

        :param new_status: The new_status of this CommentExtendAttribute.
        :type new_status: object
        """
        self._new_status = new_status

    @property
    def field_type(self):
        r"""Gets the field_type of this CommentExtendAttribute.

        字段类型

        :return: The field_type of this CommentExtendAttribute.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this CommentExtendAttribute.

        字段类型

        :param field_type: The field_type of this CommentExtendAttribute.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def field_type_id(self):
        r"""Gets the field_type_id of this CommentExtendAttribute.

        字段类型对应的Id

        :return: The field_type_id of this CommentExtendAttribute.
        :rtype: str
        """
        return self._field_type_id

    @field_type_id.setter
    def field_type_id(self, field_type_id):
        r"""Sets the field_type_id of this CommentExtendAttribute.

        字段类型对应的Id

        :param field_type_id: The field_type_id of this CommentExtendAttribute.
        :type field_type_id: str
        """
        self._field_type_id = field_type_id

    @property
    def display_name(self):
        r"""Gets the display_name of this CommentExtendAttribute.

        字段显示名

        :return: The display_name of this CommentExtendAttribute.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CommentExtendAttribute.

        字段显示名

        :param display_name: The display_name of this CommentExtendAttribute.
        :type display_name: str
        """
        self._display_name = display_name

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
        if not isinstance(other, CommentExtendAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
