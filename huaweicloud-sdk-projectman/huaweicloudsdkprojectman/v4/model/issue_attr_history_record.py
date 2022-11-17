# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueAttrHistoryRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_key': 'str',
        'field_name': 'str',
        'id': 'int',
        'issue_id': 'int',
        'new_value': 'str',
        'old_value': 'str',
        'operated_time': 'int',
        'operation': 'str',
        'operator': 'IssueUser',
        '_property': 'str'
    }

    attribute_map = {
        'field_key': 'field_key',
        'field_name': 'field_name',
        'id': 'id',
        'issue_id': 'issue_id',
        'new_value': 'new_value',
        'old_value': 'old_value',
        'operated_time': 'operated_time',
        'operation': 'operation',
        'operator': 'operator',
        '_property': 'property'
    }

    def __init__(self, field_key=None, field_name=None, id=None, issue_id=None, new_value=None, old_value=None, operated_time=None, operation=None, operator=None, _property=None):
        """IssueAttrHistoryRecord

        The model defined in huaweicloud sdk

        :param field_key: 操作的字段
        :type field_key: str
        :param field_name: 操作字段的含义
        :type field_name: str
        :param id: 历史记录id
        :type id: int
        :param issue_id: 工作项id
        :type issue_id: int
        :param new_value: 变更后的值,json字符串
        :type new_value: str
        :param old_value: 变更前的值,json字符串
        :type old_value: str
        :param operated_time: 变更的时间
        :type operated_time: int
        :param operation: 操作类型,新建，修改，删除
        :type operation: str
        :param operator: 
        :type operator: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param _property: 变更的属性
        :type _property: str
        """
        
        

        self._field_key = None
        self._field_name = None
        self._id = None
        self._issue_id = None
        self._new_value = None
        self._old_value = None
        self._operated_time = None
        self._operation = None
        self._operator = None
        self.__property = None
        self.discriminator = None

        if field_key is not None:
            self.field_key = field_key
        if field_name is not None:
            self.field_name = field_name
        if id is not None:
            self.id = id
        if issue_id is not None:
            self.issue_id = issue_id
        if new_value is not None:
            self.new_value = new_value
        if old_value is not None:
            self.old_value = old_value
        if operated_time is not None:
            self.operated_time = operated_time
        if operation is not None:
            self.operation = operation
        if operator is not None:
            self.operator = operator
        if _property is not None:
            self._property = _property

    @property
    def field_key(self):
        """Gets the field_key of this IssueAttrHistoryRecord.

        操作的字段

        :return: The field_key of this IssueAttrHistoryRecord.
        :rtype: str
        """
        return self._field_key

    @field_key.setter
    def field_key(self, field_key):
        """Sets the field_key of this IssueAttrHistoryRecord.

        操作的字段

        :param field_key: The field_key of this IssueAttrHistoryRecord.
        :type field_key: str
        """
        self._field_key = field_key

    @property
    def field_name(self):
        """Gets the field_name of this IssueAttrHistoryRecord.

        操作字段的含义

        :return: The field_name of this IssueAttrHistoryRecord.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this IssueAttrHistoryRecord.

        操作字段的含义

        :param field_name: The field_name of this IssueAttrHistoryRecord.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def id(self):
        """Gets the id of this IssueAttrHistoryRecord.

        历史记录id

        :return: The id of this IssueAttrHistoryRecord.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IssueAttrHistoryRecord.

        历史记录id

        :param id: The id of this IssueAttrHistoryRecord.
        :type id: int
        """
        self._id = id

    @property
    def issue_id(self):
        """Gets the issue_id of this IssueAttrHistoryRecord.

        工作项id

        :return: The issue_id of this IssueAttrHistoryRecord.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this IssueAttrHistoryRecord.

        工作项id

        :param issue_id: The issue_id of this IssueAttrHistoryRecord.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def new_value(self):
        """Gets the new_value of this IssueAttrHistoryRecord.

        变更后的值,json字符串

        :return: The new_value of this IssueAttrHistoryRecord.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this IssueAttrHistoryRecord.

        变更后的值,json字符串

        :param new_value: The new_value of this IssueAttrHistoryRecord.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def old_value(self):
        """Gets the old_value of this IssueAttrHistoryRecord.

        变更前的值,json字符串

        :return: The old_value of this IssueAttrHistoryRecord.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this IssueAttrHistoryRecord.

        变更前的值,json字符串

        :param old_value: The old_value of this IssueAttrHistoryRecord.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def operated_time(self):
        """Gets the operated_time of this IssueAttrHistoryRecord.

        变更的时间

        :return: The operated_time of this IssueAttrHistoryRecord.
        :rtype: int
        """
        return self._operated_time

    @operated_time.setter
    def operated_time(self, operated_time):
        """Sets the operated_time of this IssueAttrHistoryRecord.

        变更的时间

        :param operated_time: The operated_time of this IssueAttrHistoryRecord.
        :type operated_time: int
        """
        self._operated_time = operated_time

    @property
    def operation(self):
        """Gets the operation of this IssueAttrHistoryRecord.

        操作类型,新建，修改，删除

        :return: The operation of this IssueAttrHistoryRecord.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this IssueAttrHistoryRecord.

        操作类型,新建，修改，删除

        :param operation: The operation of this IssueAttrHistoryRecord.
        :type operation: str
        """
        self._operation = operation

    @property
    def operator(self):
        """Gets the operator of this IssueAttrHistoryRecord.

        :return: The operator of this IssueAttrHistoryRecord.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this IssueAttrHistoryRecord.

        :param operator: The operator of this IssueAttrHistoryRecord.
        :type operator: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._operator = operator

    @property
    def _property(self):
        """Gets the _property of this IssueAttrHistoryRecord.

        变更的属性

        :return: The _property of this IssueAttrHistoryRecord.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this IssueAttrHistoryRecord.

        变更的属性

        :param _property: The _property of this IssueAttrHistoryRecord.
        :type _property: str
        """
        self.__property = _property

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
        if not isinstance(other, IssueAttrHistoryRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
