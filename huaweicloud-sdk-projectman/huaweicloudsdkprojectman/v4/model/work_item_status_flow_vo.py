# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemStatusFlowVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_name': 'str',
        'parent_type': 'str',
        'status_id': 'str',
        'name': 'str',
        'status_type': 'str',
        'direct_to': 'list[StatusFlowDirectToVo]',
        'assign_to': 'str',
        'comment': 'str',
        'required_assign': 'bool',
        'required_notes': 'bool',
        'field_type': 'bool',
        'parent_id': 'str'
    }

    attribute_map = {
        'parent_name': 'parent_name',
        'parent_type': 'parent_type',
        'status_id': 'status_id',
        'name': 'name',
        'status_type': 'status_type',
        'direct_to': 'direct_to',
        'assign_to': 'assign_to',
        'comment': 'comment',
        'required_assign': 'required_assign',
        'required_notes': 'required_notes',
        'field_type': 'field_type',
        'parent_id': 'parent_id'
    }

    def __init__(self, parent_name=None, parent_type=None, status_id=None, name=None, status_type=None, direct_to=None, assign_to=None, comment=None, required_assign=None, required_notes=None, field_type=None, parent_id=None):
        """WorkItemStatusFlowVo

        The model defined in huaweicloud sdk

        :param parent_name:  父状态的名称
        :type parent_name: str
        :param parent_type: 父状态的类型
        :type parent_type: str
        :param status_id: 状态id
        :type status_id: str
        :param name: 状态名称
        :type name: str
        :param status_type: 状态类型
        :type status_type: str
        :param direct_to: 流转到的数据
        :type direct_to: list[:class:`huaweicloudsdkprojectman.v4.StatusFlowDirectToVo`]
        :param assign_to: 处理人的uuid
        :type assign_to: str
        :param comment: 评论内容
        :type comment: str
        :param required_assign: 处理人是否必填
        :type required_assign: bool
        :param required_notes: 评论是否必填
        :type required_notes: bool
        :param field_type: 是否是字段值，true 处理人的信息是字段值， false 处理人的值是用户的信息,固定值
        :type field_type: bool
        :param parent_id: 父状态的uuid
        :type parent_id: str
        """
        
        

        self._parent_name = None
        self._parent_type = None
        self._status_id = None
        self._name = None
        self._status_type = None
        self._direct_to = None
        self._assign_to = None
        self._comment = None
        self._required_assign = None
        self._required_notes = None
        self._field_type = None
        self._parent_id = None
        self.discriminator = None

        if parent_name is not None:
            self.parent_name = parent_name
        if parent_type is not None:
            self.parent_type = parent_type
        if status_id is not None:
            self.status_id = status_id
        if name is not None:
            self.name = name
        if status_type is not None:
            self.status_type = status_type
        if direct_to is not None:
            self.direct_to = direct_to
        if assign_to is not None:
            self.assign_to = assign_to
        if comment is not None:
            self.comment = comment
        if required_assign is not None:
            self.required_assign = required_assign
        if required_notes is not None:
            self.required_notes = required_notes
        if field_type is not None:
            self.field_type = field_type
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def parent_name(self):
        """Gets the parent_name of this WorkItemStatusFlowVo.

         父状态的名称

        :return: The parent_name of this WorkItemStatusFlowVo.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this WorkItemStatusFlowVo.

         父状态的名称

        :param parent_name: The parent_name of this WorkItemStatusFlowVo.
        :type parent_name: str
        """
        self._parent_name = parent_name

    @property
    def parent_type(self):
        """Gets the parent_type of this WorkItemStatusFlowVo.

        父状态的类型

        :return: The parent_type of this WorkItemStatusFlowVo.
        :rtype: str
        """
        return self._parent_type

    @parent_type.setter
    def parent_type(self, parent_type):
        """Sets the parent_type of this WorkItemStatusFlowVo.

        父状态的类型

        :param parent_type: The parent_type of this WorkItemStatusFlowVo.
        :type parent_type: str
        """
        self._parent_type = parent_type

    @property
    def status_id(self):
        """Gets the status_id of this WorkItemStatusFlowVo.

        状态id

        :return: The status_id of this WorkItemStatusFlowVo.
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this WorkItemStatusFlowVo.

        状态id

        :param status_id: The status_id of this WorkItemStatusFlowVo.
        :type status_id: str
        """
        self._status_id = status_id

    @property
    def name(self):
        """Gets the name of this WorkItemStatusFlowVo.

        状态名称

        :return: The name of this WorkItemStatusFlowVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkItemStatusFlowVo.

        状态名称

        :param name: The name of this WorkItemStatusFlowVo.
        :type name: str
        """
        self._name = name

    @property
    def status_type(self):
        """Gets the status_type of this WorkItemStatusFlowVo.

        状态类型

        :return: The status_type of this WorkItemStatusFlowVo.
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        """Sets the status_type of this WorkItemStatusFlowVo.

        状态类型

        :param status_type: The status_type of this WorkItemStatusFlowVo.
        :type status_type: str
        """
        self._status_type = status_type

    @property
    def direct_to(self):
        """Gets the direct_to of this WorkItemStatusFlowVo.

        流转到的数据

        :return: The direct_to of this WorkItemStatusFlowVo.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.StatusFlowDirectToVo`]
        """
        return self._direct_to

    @direct_to.setter
    def direct_to(self, direct_to):
        """Sets the direct_to of this WorkItemStatusFlowVo.

        流转到的数据

        :param direct_to: The direct_to of this WorkItemStatusFlowVo.
        :type direct_to: list[:class:`huaweicloudsdkprojectman.v4.StatusFlowDirectToVo`]
        """
        self._direct_to = direct_to

    @property
    def assign_to(self):
        """Gets the assign_to of this WorkItemStatusFlowVo.

        处理人的uuid

        :return: The assign_to of this WorkItemStatusFlowVo.
        :rtype: str
        """
        return self._assign_to

    @assign_to.setter
    def assign_to(self, assign_to):
        """Sets the assign_to of this WorkItemStatusFlowVo.

        处理人的uuid

        :param assign_to: The assign_to of this WorkItemStatusFlowVo.
        :type assign_to: str
        """
        self._assign_to = assign_to

    @property
    def comment(self):
        """Gets the comment of this WorkItemStatusFlowVo.

        评论内容

        :return: The comment of this WorkItemStatusFlowVo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this WorkItemStatusFlowVo.

        评论内容

        :param comment: The comment of this WorkItemStatusFlowVo.
        :type comment: str
        """
        self._comment = comment

    @property
    def required_assign(self):
        """Gets the required_assign of this WorkItemStatusFlowVo.

        处理人是否必填

        :return: The required_assign of this WorkItemStatusFlowVo.
        :rtype: bool
        """
        return self._required_assign

    @required_assign.setter
    def required_assign(self, required_assign):
        """Sets the required_assign of this WorkItemStatusFlowVo.

        处理人是否必填

        :param required_assign: The required_assign of this WorkItemStatusFlowVo.
        :type required_assign: bool
        """
        self._required_assign = required_assign

    @property
    def required_notes(self):
        """Gets the required_notes of this WorkItemStatusFlowVo.

        评论是否必填

        :return: The required_notes of this WorkItemStatusFlowVo.
        :rtype: bool
        """
        return self._required_notes

    @required_notes.setter
    def required_notes(self, required_notes):
        """Sets the required_notes of this WorkItemStatusFlowVo.

        评论是否必填

        :param required_notes: The required_notes of this WorkItemStatusFlowVo.
        :type required_notes: bool
        """
        self._required_notes = required_notes

    @property
    def field_type(self):
        """Gets the field_type of this WorkItemStatusFlowVo.

        是否是字段值，true 处理人的信息是字段值， false 处理人的值是用户的信息,固定值

        :return: The field_type of this WorkItemStatusFlowVo.
        :rtype: bool
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this WorkItemStatusFlowVo.

        是否是字段值，true 处理人的信息是字段值， false 处理人的值是用户的信息,固定值

        :param field_type: The field_type of this WorkItemStatusFlowVo.
        :type field_type: bool
        """
        self._field_type = field_type

    @property
    def parent_id(self):
        """Gets the parent_id of this WorkItemStatusFlowVo.

        父状态的uuid

        :return: The parent_id of this WorkItemStatusFlowVo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this WorkItemStatusFlowVo.

        父状态的uuid

        :param parent_id: The parent_id of this WorkItemStatusFlowVo.
        :type parent_id: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, WorkItemStatusFlowVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
