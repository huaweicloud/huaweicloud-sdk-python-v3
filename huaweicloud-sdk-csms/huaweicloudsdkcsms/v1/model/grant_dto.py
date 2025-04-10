# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrantDTO:

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
        'type': 'str',
        'grantee_user': 'list[GrantUserInfo]',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'grantee_user': 'grantee_user',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, type=None, grantee_user=None, create_time=None, update_time=None):
        r"""GrantDTO

        The model defined in huaweicloud sdk

        :param id: 授权id，授权给个人时存在
        :type id: str
        :param name: 授权name
        :type name: str
        :param type: 授权类型（SECRET，GROUP）
        :type type: str
        :param grantee_user: 被授权用户信息
        :type grantee_user: list[:class:`huaweicloudsdkcsms.v1.GrantUserInfo`]
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._grantee_user = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        self.grantee_user = grantee_user
        self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this GrantDTO.

        授权id，授权给个人时存在

        :return: The id of this GrantDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GrantDTO.

        授权id，授权给个人时存在

        :param id: The id of this GrantDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GrantDTO.

        授权name

        :return: The name of this GrantDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GrantDTO.

        授权name

        :param name: The name of this GrantDTO.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this GrantDTO.

        授权类型（SECRET，GROUP）

        :return: The type of this GrantDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GrantDTO.

        授权类型（SECRET，GROUP）

        :param type: The type of this GrantDTO.
        :type type: str
        """
        self._type = type

    @property
    def grantee_user(self):
        r"""Gets the grantee_user of this GrantDTO.

        被授权用户信息

        :return: The grantee_user of this GrantDTO.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.GrantUserInfo`]
        """
        return self._grantee_user

    @grantee_user.setter
    def grantee_user(self, grantee_user):
        r"""Sets the grantee_user of this GrantDTO.

        被授权用户信息

        :param grantee_user: The grantee_user of this GrantDTO.
        :type grantee_user: list[:class:`huaweicloudsdkcsms.v1.GrantUserInfo`]
        """
        self._grantee_user = grantee_user

    @property
    def create_time(self):
        r"""Gets the create_time of this GrantDTO.

        创建时间

        :return: The create_time of this GrantDTO.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GrantDTO.

        创建时间

        :param create_time: The create_time of this GrantDTO.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this GrantDTO.

        更新时间

        :return: The update_time of this GrantDTO.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this GrantDTO.

        更新时间

        :param update_time: The update_time of this GrantDTO.
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
        if not isinstance(other, GrantDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
