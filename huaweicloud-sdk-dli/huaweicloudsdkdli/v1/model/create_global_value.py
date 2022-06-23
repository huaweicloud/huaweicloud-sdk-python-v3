# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'var_name': 'str',
        'var_value': 'str',
        'project_id': 'str',
        'user_id': 'str',
        'id': 'int'
    }

    attribute_map = {
        'var_name': 'var_name',
        'var_value': 'var_value',
        'project_id': 'project_id',
        'user_id': 'user_id',
        'id': 'id'
    }

    def __init__(self, var_name=None, var_value=None, project_id=None, user_id=None, id=None):
        """CreateGlobalValue

        The model defined in huaweicloud sdk

        :param var_name: 变量名称
        :type var_name: str
        :param var_value: 变量的值
        :type var_value: str
        :param project_id: 项目ID
        :type project_id: str
        :param user_id: 用户ID
        :type user_id: str
        :param id: 全局变量ID
        :type id: int
        """
        
        

        self._var_name = None
        self._var_value = None
        self._project_id = None
        self._user_id = None
        self._id = None
        self.discriminator = None

        self.var_name = var_name
        self.var_value = var_value
        if project_id is not None:
            self.project_id = project_id
        if user_id is not None:
            self.user_id = user_id
        if id is not None:
            self.id = id

    @property
    def var_name(self):
        """Gets the var_name of this CreateGlobalValue.

        变量名称

        :return: The var_name of this CreateGlobalValue.
        :rtype: str
        """
        return self._var_name

    @var_name.setter
    def var_name(self, var_name):
        """Sets the var_name of this CreateGlobalValue.

        变量名称

        :param var_name: The var_name of this CreateGlobalValue.
        :type var_name: str
        """
        self._var_name = var_name

    @property
    def var_value(self):
        """Gets the var_value of this CreateGlobalValue.

        变量的值

        :return: The var_value of this CreateGlobalValue.
        :rtype: str
        """
        return self._var_value

    @var_value.setter
    def var_value(self, var_value):
        """Sets the var_value of this CreateGlobalValue.

        变量的值

        :param var_value: The var_value of this CreateGlobalValue.
        :type var_value: str
        """
        self._var_value = var_value

    @property
    def project_id(self):
        """Gets the project_id of this CreateGlobalValue.

        项目ID

        :return: The project_id of this CreateGlobalValue.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateGlobalValue.

        项目ID

        :param project_id: The project_id of this CreateGlobalValue.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def user_id(self):
        """Gets the user_id of this CreateGlobalValue.

        用户ID

        :return: The user_id of this CreateGlobalValue.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateGlobalValue.

        用户ID

        :param user_id: The user_id of this CreateGlobalValue.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def id(self):
        """Gets the id of this CreateGlobalValue.

        全局变量ID

        :return: The id of this CreateGlobalValue.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateGlobalValue.

        全局变量ID

        :param id: The id of this CreateGlobalValue.
        :type id: int
        """
        self._id = id

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
        if not isinstance(other, CreateGlobalValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
