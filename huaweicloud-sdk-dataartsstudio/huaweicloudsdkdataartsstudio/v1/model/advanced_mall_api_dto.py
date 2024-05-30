# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdvancedMallApiDTO:

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
        'auth_type': 'str',
        'application_num': 'int',
        'call_num': 'int',
        'user_name': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'is_owner': 'bool',
        'is_authorized': 'bool',
        'is_update_recently': 'bool',
        'is_release_recently': 'bool',
        'is_hot_recently': 'bool',
        'success_rate': 'str',
        'failure_rate': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'auth_type': 'auth_type',
        'application_num': 'application_num',
        'call_num': 'call_num',
        'user_name': 'user_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'is_owner': 'is_owner',
        'is_authorized': 'is_authorized',
        'is_update_recently': 'is_update_recently',
        'is_release_recently': 'is_release_recently',
        'is_hot_recently': 'is_hot_recently',
        'success_rate': 'success_rate',
        'failure_rate': 'failure_rate'
    }

    def __init__(self, id=None, name=None, auth_type=None, application_num=None, call_num=None, user_name=None, create_time=None, update_time=None, is_owner=None, is_authorized=None, is_update_recently=None, is_release_recently=None, is_hot_recently=None, success_rate=None, failure_rate=None):
        """AdvancedMallApiDTO

        The model defined in huaweicloud sdk

        :param id: API ID。
        :type id: str
        :param name: API名称。
        :type name: str
        :param auth_type: 认证类型。
        :type auth_type: str
        :param application_num: 授权使用的应用数量。
        :type application_num: int
        :param call_num: 被调用量。
        :type call_num: int
        :param user_name: 创建者。
        :type user_name: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 更新时间。
        :type update_time: int
        :param is_owner: 是否当前空间的API。
        :type is_owner: bool
        :param is_authorized: 是否已被授权。
        :type is_authorized: bool
        :param is_update_recently: 是否最近更新（三天内更新过该API）。
        :type is_update_recently: bool
        :param is_release_recently: 是否新品上市（三天内新发布的API）。
        :type is_release_recently: bool
        :param is_hot_recently: 是否热销产品（三天内有其他空间用户申请该API）。
        :type is_hot_recently: bool
        :param success_rate: 7天内调用成功率。
        :type success_rate: str
        :param failure_rate: 7天内调用失败率。
        :type failure_rate: str
        """
        
        

        self._id = None
        self._name = None
        self._auth_type = None
        self._application_num = None
        self._call_num = None
        self._user_name = None
        self._create_time = None
        self._update_time = None
        self._is_owner = None
        self._is_authorized = None
        self._is_update_recently = None
        self._is_release_recently = None
        self._is_hot_recently = None
        self._success_rate = None
        self._failure_rate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if auth_type is not None:
            self.auth_type = auth_type
        if application_num is not None:
            self.application_num = application_num
        if call_num is not None:
            self.call_num = call_num
        if user_name is not None:
            self.user_name = user_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if is_owner is not None:
            self.is_owner = is_owner
        if is_authorized is not None:
            self.is_authorized = is_authorized
        if is_update_recently is not None:
            self.is_update_recently = is_update_recently
        if is_release_recently is not None:
            self.is_release_recently = is_release_recently
        if is_hot_recently is not None:
            self.is_hot_recently = is_hot_recently
        if success_rate is not None:
            self.success_rate = success_rate
        if failure_rate is not None:
            self.failure_rate = failure_rate

    @property
    def id(self):
        """Gets the id of this AdvancedMallApiDTO.

        API ID。

        :return: The id of this AdvancedMallApiDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdvancedMallApiDTO.

        API ID。

        :param id: The id of this AdvancedMallApiDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AdvancedMallApiDTO.

        API名称。

        :return: The name of this AdvancedMallApiDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AdvancedMallApiDTO.

        API名称。

        :param name: The name of this AdvancedMallApiDTO.
        :type name: str
        """
        self._name = name

    @property
    def auth_type(self):
        """Gets the auth_type of this AdvancedMallApiDTO.

        认证类型。

        :return: The auth_type of this AdvancedMallApiDTO.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this AdvancedMallApiDTO.

        认证类型。

        :param auth_type: The auth_type of this AdvancedMallApiDTO.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def application_num(self):
        """Gets the application_num of this AdvancedMallApiDTO.

        授权使用的应用数量。

        :return: The application_num of this AdvancedMallApiDTO.
        :rtype: int
        """
        return self._application_num

    @application_num.setter
    def application_num(self, application_num):
        """Sets the application_num of this AdvancedMallApiDTO.

        授权使用的应用数量。

        :param application_num: The application_num of this AdvancedMallApiDTO.
        :type application_num: int
        """
        self._application_num = application_num

    @property
    def call_num(self):
        """Gets the call_num of this AdvancedMallApiDTO.

        被调用量。

        :return: The call_num of this AdvancedMallApiDTO.
        :rtype: int
        """
        return self._call_num

    @call_num.setter
    def call_num(self, call_num):
        """Sets the call_num of this AdvancedMallApiDTO.

        被调用量。

        :param call_num: The call_num of this AdvancedMallApiDTO.
        :type call_num: int
        """
        self._call_num = call_num

    @property
    def user_name(self):
        """Gets the user_name of this AdvancedMallApiDTO.

        创建者。

        :return: The user_name of this AdvancedMallApiDTO.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AdvancedMallApiDTO.

        创建者。

        :param user_name: The user_name of this AdvancedMallApiDTO.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def create_time(self):
        """Gets the create_time of this AdvancedMallApiDTO.

        创建时间。

        :return: The create_time of this AdvancedMallApiDTO.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AdvancedMallApiDTO.

        创建时间。

        :param create_time: The create_time of this AdvancedMallApiDTO.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this AdvancedMallApiDTO.

        更新时间。

        :return: The update_time of this AdvancedMallApiDTO.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AdvancedMallApiDTO.

        更新时间。

        :param update_time: The update_time of this AdvancedMallApiDTO.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def is_owner(self):
        """Gets the is_owner of this AdvancedMallApiDTO.

        是否当前空间的API。

        :return: The is_owner of this AdvancedMallApiDTO.
        :rtype: bool
        """
        return self._is_owner

    @is_owner.setter
    def is_owner(self, is_owner):
        """Sets the is_owner of this AdvancedMallApiDTO.

        是否当前空间的API。

        :param is_owner: The is_owner of this AdvancedMallApiDTO.
        :type is_owner: bool
        """
        self._is_owner = is_owner

    @property
    def is_authorized(self):
        """Gets the is_authorized of this AdvancedMallApiDTO.

        是否已被授权。

        :return: The is_authorized of this AdvancedMallApiDTO.
        :rtype: bool
        """
        return self._is_authorized

    @is_authorized.setter
    def is_authorized(self, is_authorized):
        """Sets the is_authorized of this AdvancedMallApiDTO.

        是否已被授权。

        :param is_authorized: The is_authorized of this AdvancedMallApiDTO.
        :type is_authorized: bool
        """
        self._is_authorized = is_authorized

    @property
    def is_update_recently(self):
        """Gets the is_update_recently of this AdvancedMallApiDTO.

        是否最近更新（三天内更新过该API）。

        :return: The is_update_recently of this AdvancedMallApiDTO.
        :rtype: bool
        """
        return self._is_update_recently

    @is_update_recently.setter
    def is_update_recently(self, is_update_recently):
        """Sets the is_update_recently of this AdvancedMallApiDTO.

        是否最近更新（三天内更新过该API）。

        :param is_update_recently: The is_update_recently of this AdvancedMallApiDTO.
        :type is_update_recently: bool
        """
        self._is_update_recently = is_update_recently

    @property
    def is_release_recently(self):
        """Gets the is_release_recently of this AdvancedMallApiDTO.

        是否新品上市（三天内新发布的API）。

        :return: The is_release_recently of this AdvancedMallApiDTO.
        :rtype: bool
        """
        return self._is_release_recently

    @is_release_recently.setter
    def is_release_recently(self, is_release_recently):
        """Sets the is_release_recently of this AdvancedMallApiDTO.

        是否新品上市（三天内新发布的API）。

        :param is_release_recently: The is_release_recently of this AdvancedMallApiDTO.
        :type is_release_recently: bool
        """
        self._is_release_recently = is_release_recently

    @property
    def is_hot_recently(self):
        """Gets the is_hot_recently of this AdvancedMallApiDTO.

        是否热销产品（三天内有其他空间用户申请该API）。

        :return: The is_hot_recently of this AdvancedMallApiDTO.
        :rtype: bool
        """
        return self._is_hot_recently

    @is_hot_recently.setter
    def is_hot_recently(self, is_hot_recently):
        """Sets the is_hot_recently of this AdvancedMallApiDTO.

        是否热销产品（三天内有其他空间用户申请该API）。

        :param is_hot_recently: The is_hot_recently of this AdvancedMallApiDTO.
        :type is_hot_recently: bool
        """
        self._is_hot_recently = is_hot_recently

    @property
    def success_rate(self):
        """Gets the success_rate of this AdvancedMallApiDTO.

        7天内调用成功率。

        :return: The success_rate of this AdvancedMallApiDTO.
        :rtype: str
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this AdvancedMallApiDTO.

        7天内调用成功率。

        :param success_rate: The success_rate of this AdvancedMallApiDTO.
        :type success_rate: str
        """
        self._success_rate = success_rate

    @property
    def failure_rate(self):
        """Gets the failure_rate of this AdvancedMallApiDTO.

        7天内调用失败率。

        :return: The failure_rate of this AdvancedMallApiDTO.
        :rtype: str
        """
        return self._failure_rate

    @failure_rate.setter
    def failure_rate(self, failure_rate):
        """Sets the failure_rate of this AdvancedMallApiDTO.

        7天内调用失败率。

        :param failure_rate: The failure_rate of this AdvancedMallApiDTO.
        :type failure_rate: str
        """
        self._failure_rate = failure_rate

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
        if not isinstance(other, AdvancedMallApiDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
