# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCurUserInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'user_num_id': 'int',
        'user_id': 'str',
        'user_name': 'str',
        'nick_name': 'str',
        'created_time': 'int',
        'updated_time': 'int',
        'gender': 'str',
        'user_type': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'user_num_id': 'user_num_id',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'nick_name': 'nick_name',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'gender': 'gender',
        'user_type': 'user_type'
    }

    def __init__(self, domain_id=None, domain_name=None, user_num_id=None, user_id=None, user_name=None, nick_name=None, created_time=None, updated_time=None, gender=None, user_type=None):
        r"""ShowCurUserInfoResponse

        The model defined in huaweicloud sdk

        :param domain_id: 租户id
        :type domain_id: str
        :param domain_name: 租户名
        :type domain_name: str
        :param user_num_id: 用户数字id
        :type user_num_id: int
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param created_time: 创建时间
        :type created_time: int
        :param updated_time: 更新时间
        :type updated_time: int
        :param gender: 性别
        :type gender: str
        :param user_type: 用户类型, User 云用户, Federation 联邦账号,
        :type user_type: str
        """
        
        super(ShowCurUserInfoResponse, self).__init__()

        self._domain_id = None
        self._domain_name = None
        self._user_num_id = None
        self._user_id = None
        self._user_name = None
        self._nick_name = None
        self._created_time = None
        self._updated_time = None
        self._gender = None
        self._user_type = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if user_num_id is not None:
            self.user_num_id = user_num_id
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if nick_name is not None:
            self.nick_name = nick_name
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if gender is not None:
            self.gender = gender
        if user_type is not None:
            self.user_type = user_type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowCurUserInfoResponse.

        租户id

        :return: The domain_id of this ShowCurUserInfoResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowCurUserInfoResponse.

        租户id

        :param domain_id: The domain_id of this ShowCurUserInfoResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowCurUserInfoResponse.

        租户名

        :return: The domain_name of this ShowCurUserInfoResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowCurUserInfoResponse.

        租户名

        :param domain_name: The domain_name of this ShowCurUserInfoResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def user_num_id(self):
        r"""Gets the user_num_id of this ShowCurUserInfoResponse.

        用户数字id

        :return: The user_num_id of this ShowCurUserInfoResponse.
        :rtype: int
        """
        return self._user_num_id

    @user_num_id.setter
    def user_num_id(self, user_num_id):
        r"""Sets the user_num_id of this ShowCurUserInfoResponse.

        用户数字id

        :param user_num_id: The user_num_id of this ShowCurUserInfoResponse.
        :type user_num_id: int
        """
        self._user_num_id = user_num_id

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowCurUserInfoResponse.

        用户id

        :return: The user_id of this ShowCurUserInfoResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowCurUserInfoResponse.

        用户id

        :param user_id: The user_id of this ShowCurUserInfoResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowCurUserInfoResponse.

        用户名

        :return: The user_name of this ShowCurUserInfoResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowCurUserInfoResponse.

        用户名

        :param user_name: The user_name of this ShowCurUserInfoResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ShowCurUserInfoResponse.

        用户昵称

        :return: The nick_name of this ShowCurUserInfoResponse.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ShowCurUserInfoResponse.

        用户昵称

        :param nick_name: The nick_name of this ShowCurUserInfoResponse.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def created_time(self):
        r"""Gets the created_time of this ShowCurUserInfoResponse.

        创建时间

        :return: The created_time of this ShowCurUserInfoResponse.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ShowCurUserInfoResponse.

        创建时间

        :param created_time: The created_time of this ShowCurUserInfoResponse.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ShowCurUserInfoResponse.

        更新时间

        :return: The updated_time of this ShowCurUserInfoResponse.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ShowCurUserInfoResponse.

        更新时间

        :param updated_time: The updated_time of this ShowCurUserInfoResponse.
        :type updated_time: int
        """
        self._updated_time = updated_time

    @property
    def gender(self):
        r"""Gets the gender of this ShowCurUserInfoResponse.

        性别

        :return: The gender of this ShowCurUserInfoResponse.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        r"""Sets the gender of this ShowCurUserInfoResponse.

        性别

        :param gender: The gender of this ShowCurUserInfoResponse.
        :type gender: str
        """
        self._gender = gender

    @property
    def user_type(self):
        r"""Gets the user_type of this ShowCurUserInfoResponse.

        用户类型, User 云用户, Federation 联邦账号,

        :return: The user_type of this ShowCurUserInfoResponse.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this ShowCurUserInfoResponse.

        用户类型, User 云用户, Federation 联邦账号,

        :param user_type: The user_type of this ShowCurUserInfoResponse.
        :type user_type: str
        """
        self._user_type = user_type

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
        if not isinstance(other, ShowCurUserInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
