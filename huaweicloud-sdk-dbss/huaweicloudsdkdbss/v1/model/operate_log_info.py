# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateLogInfo:

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
        'user': 'str',
        'time': 'str',
        'function': 'str',
        'action': 'str',
        'name': 'str',
        'description': 'str',
        'result': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'time': 'time',
        'function': 'function',
        'action': 'action',
        'name': 'name',
        'description': 'description',
        'result': 'result'
    }

    def __init__(self, id=None, user=None, time=None, function=None, action=None, name=None, description=None, result=None):
        """OperateLogInfo

        The model defined in huaweicloud sdk

        :param id: 操作日志ID
        :type id: str
        :param user: 操作日志用户
        :type user: str
        :param time: 该条记录发生的时间，格式为时间戳
        :type time: str
        :param function: 该条记录的功能类型
        :type function: str
        :param action: 该条记录的操作类型  create：创建  update：更新  operate：操作（开关）  delete：删除
        :type action: str
        :param name: 该条记录对应的用户操作对象
        :type name: str
        :param description: 该条记录具体的描述
        :type description: str
        :param result: 该条记录对应用户执行的结果  success表示成功  fail表示失败
        :type result: str
        """
        
        

        self._id = None
        self._user = None
        self._time = None
        self._function = None
        self._action = None
        self._name = None
        self._description = None
        self._result = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if time is not None:
            self.time = time
        if function is not None:
            self.function = function
        if action is not None:
            self.action = action
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if result is not None:
            self.result = result

    @property
    def id(self):
        """Gets the id of this OperateLogInfo.

        操作日志ID

        :return: The id of this OperateLogInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperateLogInfo.

        操作日志ID

        :param id: The id of this OperateLogInfo.
        :type id: str
        """
        self._id = id

    @property
    def user(self):
        """Gets the user of this OperateLogInfo.

        操作日志用户

        :return: The user of this OperateLogInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OperateLogInfo.

        操作日志用户

        :param user: The user of this OperateLogInfo.
        :type user: str
        """
        self._user = user

    @property
    def time(self):
        """Gets the time of this OperateLogInfo.

        该条记录发生的时间，格式为时间戳

        :return: The time of this OperateLogInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OperateLogInfo.

        该条记录发生的时间，格式为时间戳

        :param time: The time of this OperateLogInfo.
        :type time: str
        """
        self._time = time

    @property
    def function(self):
        """Gets the function of this OperateLogInfo.

        该条记录的功能类型

        :return: The function of this OperateLogInfo.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this OperateLogInfo.

        该条记录的功能类型

        :param function: The function of this OperateLogInfo.
        :type function: str
        """
        self._function = function

    @property
    def action(self):
        """Gets the action of this OperateLogInfo.

        该条记录的操作类型  create：创建  update：更新  operate：操作（开关）  delete：删除

        :return: The action of this OperateLogInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this OperateLogInfo.

        该条记录的操作类型  create：创建  update：更新  operate：操作（开关）  delete：删除

        :param action: The action of this OperateLogInfo.
        :type action: str
        """
        self._action = action

    @property
    def name(self):
        """Gets the name of this OperateLogInfo.

        该条记录对应的用户操作对象

        :return: The name of this OperateLogInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OperateLogInfo.

        该条记录对应的用户操作对象

        :param name: The name of this OperateLogInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this OperateLogInfo.

        该条记录具体的描述

        :return: The description of this OperateLogInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OperateLogInfo.

        该条记录具体的描述

        :param description: The description of this OperateLogInfo.
        :type description: str
        """
        self._description = description

    @property
    def result(self):
        """Gets the result of this OperateLogInfo.

        该条记录对应用户执行的结果  success表示成功  fail表示失败

        :return: The result of this OperateLogInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this OperateLogInfo.

        该条记录对应用户执行的结果  success表示成功  fail表示失败

        :param result: The result of this OperateLogInfo.
        :type result: str
        """
        self._result = result

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
        if not isinstance(other, OperateLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
