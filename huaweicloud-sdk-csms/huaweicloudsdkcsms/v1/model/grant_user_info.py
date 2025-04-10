# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrantUserInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'user_name': 'str',
        'create_time': 'int',
        'validity_time': 'int'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_name': 'user_name',
        'create_time': 'create_time',
        'validity_time': 'validity_time'
    }

    def __init__(self, user_id=None, user_name=None, create_time=None, validity_time=None):
        r"""GrantUserInfo

        The model defined in huaweicloud sdk

        :param user_id: 资源ID
        :type user_id: str
        :param user_name: 名称
        :type user_name: str
        :param create_time: 创建时间
        :type create_time: int
        :param validity_time: 有效时间
        :type validity_time: int
        """
        
        

        self._user_id = None
        self._user_name = None
        self._create_time = None
        self._validity_time = None
        self.discriminator = None

        self.user_id = user_id
        self.user_name = user_name
        self.create_time = create_time
        if validity_time is not None:
            self.validity_time = validity_time

    @property
    def user_id(self):
        r"""Gets the user_id of this GrantUserInfo.

        资源ID

        :return: The user_id of this GrantUserInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this GrantUserInfo.

        资源ID

        :param user_id: The user_id of this GrantUserInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this GrantUserInfo.

        名称

        :return: The user_name of this GrantUserInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this GrantUserInfo.

        名称

        :param user_name: The user_name of this GrantUserInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def create_time(self):
        r"""Gets the create_time of this GrantUserInfo.

        创建时间

        :return: The create_time of this GrantUserInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GrantUserInfo.

        创建时间

        :param create_time: The create_time of this GrantUserInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def validity_time(self):
        r"""Gets the validity_time of this GrantUserInfo.

        有效时间

        :return: The validity_time of this GrantUserInfo.
        :rtype: int
        """
        return self._validity_time

    @validity_time.setter
    def validity_time(self, validity_time):
        r"""Sets the validity_time of this GrantUserInfo.

        有效时间

        :param validity_time: The validity_time of this GrantUserInfo.
        :type validity_time: int
        """
        self._validity_time = validity_time

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
        if not isinstance(other, GrantUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
