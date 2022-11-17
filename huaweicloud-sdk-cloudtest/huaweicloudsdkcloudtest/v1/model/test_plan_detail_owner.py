# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestPlanDetailOwner:

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
        'nick_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'nick_name': 'nick_name',
        'user_name': 'user_name'
    }

    def __init__(self, id=None, name=None, nick_name=None, user_name=None):
        """TestPlanDetailOwner

        The model defined in huaweicloud sdk

        :param id: 测试计划处理者id
        :type id: str
        :param name: 测试计划处理者名称，优先返回nickName，不存在则返回userName
        :type name: str
        :param nick_name: 测试计划处理者的昵称，当用户未设置昵称时不返回该字段
        :type nick_name: str
        :param user_name: 测试计划处理者的用户名称
        :type user_name: str
        """
        
        

        self._id = None
        self._name = None
        self._nick_name = None
        self._user_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if nick_name is not None:
            self.nick_name = nick_name
        if user_name is not None:
            self.user_name = user_name

    @property
    def id(self):
        """Gets the id of this TestPlanDetailOwner.

        测试计划处理者id

        :return: The id of this TestPlanDetailOwner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestPlanDetailOwner.

        测试计划处理者id

        :param id: The id of this TestPlanDetailOwner.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TestPlanDetailOwner.

        测试计划处理者名称，优先返回nickName，不存在则返回userName

        :return: The name of this TestPlanDetailOwner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestPlanDetailOwner.

        测试计划处理者名称，优先返回nickName，不存在则返回userName

        :param name: The name of this TestPlanDetailOwner.
        :type name: str
        """
        self._name = name

    @property
    def nick_name(self):
        """Gets the nick_name of this TestPlanDetailOwner.

        测试计划处理者的昵称，当用户未设置昵称时不返回该字段

        :return: The nick_name of this TestPlanDetailOwner.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this TestPlanDetailOwner.

        测试计划处理者的昵称，当用户未设置昵称时不返回该字段

        :param nick_name: The nick_name of this TestPlanDetailOwner.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def user_name(self):
        """Gets the user_name of this TestPlanDetailOwner.

        测试计划处理者的用户名称

        :return: The user_name of this TestPlanDetailOwner.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TestPlanDetailOwner.

        测试计划处理者的用户名称

        :param user_name: The user_name of this TestPlanDetailOwner.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, TestPlanDetailOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
