# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'var_name': 'str',
        'var_value': 'str',
        'project_id': 'str',
        'user_id': 'str',
        'is_sensitive': 'bool',
        'user_name': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'var_name': 'var_name',
        'var_value': 'var_value',
        'project_id': 'project_id',
        'user_id': 'user_id',
        'is_sensitive': 'is_sensitive',
        'user_name': 'user_name',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, var_name=None, var_value=None, project_id=None, user_id=None, is_sensitive=None, user_name=None, create_time=None, update_time=None):
        """ListGlobalValue

        The model defined in huaweicloud sdk

        :param id: 全局变量ID
        :type id: int
        :param var_name: 变量名称
        :type var_name: str
        :param var_value: 变量的值
        :type var_value: str
        :param project_id: 项目ID
        :type project_id: str
        :param user_id: 用户ID
        :type user_id: str
        :param is_sensitive: 是否为敏感变量
        :type is_sensitive: bool
        :param user_name: 用户名称
        :type user_name: str
        :param create_time: 创建时间。为UTC的时间戳。
        :type create_time: int
        :param update_time: 更新时间。为UTC的时间戳。
        :type update_time: int
        """
        
        

        self._id = None
        self._var_name = None
        self._var_value = None
        self._project_id = None
        self._user_id = None
        self._is_sensitive = None
        self._user_name = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if var_name is not None:
            self.var_name = var_name
        if var_value is not None:
            self.var_value = var_value
        if project_id is not None:
            self.project_id = project_id
        if user_id is not None:
            self.user_id = user_id
        if is_sensitive is not None:
            self.is_sensitive = is_sensitive
        if user_name is not None:
            self.user_name = user_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this ListGlobalValue.

        全局变量ID

        :return: The id of this ListGlobalValue.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListGlobalValue.

        全局变量ID

        :param id: The id of this ListGlobalValue.
        :type id: int
        """
        self._id = id

    @property
    def var_name(self):
        """Gets the var_name of this ListGlobalValue.

        变量名称

        :return: The var_name of this ListGlobalValue.
        :rtype: str
        """
        return self._var_name

    @var_name.setter
    def var_name(self, var_name):
        """Sets the var_name of this ListGlobalValue.

        变量名称

        :param var_name: The var_name of this ListGlobalValue.
        :type var_name: str
        """
        self._var_name = var_name

    @property
    def var_value(self):
        """Gets the var_value of this ListGlobalValue.

        变量的值

        :return: The var_value of this ListGlobalValue.
        :rtype: str
        """
        return self._var_value

    @var_value.setter
    def var_value(self, var_value):
        """Sets the var_value of this ListGlobalValue.

        变量的值

        :param var_value: The var_value of this ListGlobalValue.
        :type var_value: str
        """
        self._var_value = var_value

    @property
    def project_id(self):
        """Gets the project_id of this ListGlobalValue.

        项目ID

        :return: The project_id of this ListGlobalValue.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListGlobalValue.

        项目ID

        :param project_id: The project_id of this ListGlobalValue.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def user_id(self):
        """Gets the user_id of this ListGlobalValue.

        用户ID

        :return: The user_id of this ListGlobalValue.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ListGlobalValue.

        用户ID

        :param user_id: The user_id of this ListGlobalValue.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def is_sensitive(self):
        """Gets the is_sensitive of this ListGlobalValue.

        是否为敏感变量

        :return: The is_sensitive of this ListGlobalValue.
        :rtype: bool
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        """Sets the is_sensitive of this ListGlobalValue.

        是否为敏感变量

        :param is_sensitive: The is_sensitive of this ListGlobalValue.
        :type is_sensitive: bool
        """
        self._is_sensitive = is_sensitive

    @property
    def user_name(self):
        """Gets the user_name of this ListGlobalValue.

        用户名称

        :return: The user_name of this ListGlobalValue.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListGlobalValue.

        用户名称

        :param user_name: The user_name of this ListGlobalValue.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def create_time(self):
        """Gets the create_time of this ListGlobalValue.

        创建时间。为UTC的时间戳。

        :return: The create_time of this ListGlobalValue.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListGlobalValue.

        创建时间。为UTC的时间戳。

        :param create_time: The create_time of this ListGlobalValue.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ListGlobalValue.

        更新时间。为UTC的时间戳。

        :return: The update_time of this ListGlobalValue.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ListGlobalValue.

        更新时间。为UTC的时间戳。

        :param update_time: The update_time of this ListGlobalValue.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ListGlobalValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
