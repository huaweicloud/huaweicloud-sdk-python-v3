# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetProjectInfoV4ResultProjectCreator:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_num_id': 'int',
        'user_id': 'str',
        'user_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'nick_name': 'str'
    }

    attribute_map = {
        'user_num_id': 'user_num_id',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'nick_name': 'nick_name'
    }

    def __init__(self, user_num_id=None, user_id=None, user_name=None, domain_id=None, domain_name=None, nick_name=None):
        """GetProjectInfoV4ResultProjectCreator

        The model defined in huaweicloud sdk

        :param user_num_id: 创建人num_id
        :type user_num_id: int
        :param user_id: 创建人uuid
        :type user_id: str
        :param user_name: 创建人姓名
        :type user_name: str
        :param domain_id: 创建人租户id
        :type domain_id: str
        :param domain_name: 创建人租户名称
        :type domain_name: str
        :param nick_name: 创建人昵称
        :type nick_name: str
        """
        
        

        self._user_num_id = None
        self._user_id = None
        self._user_name = None
        self._domain_id = None
        self._domain_name = None
        self._nick_name = None
        self.discriminator = None

        if user_num_id is not None:
            self.user_num_id = user_num_id
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if nick_name is not None:
            self.nick_name = nick_name

    @property
    def user_num_id(self):
        """Gets the user_num_id of this GetProjectInfoV4ResultProjectCreator.

        创建人num_id

        :return: The user_num_id of this GetProjectInfoV4ResultProjectCreator.
        :rtype: int
        """
        return self._user_num_id

    @user_num_id.setter
    def user_num_id(self, user_num_id):
        """Sets the user_num_id of this GetProjectInfoV4ResultProjectCreator.

        创建人num_id

        :param user_num_id: The user_num_id of this GetProjectInfoV4ResultProjectCreator.
        :type user_num_id: int
        """
        self._user_num_id = user_num_id

    @property
    def user_id(self):
        """Gets the user_id of this GetProjectInfoV4ResultProjectCreator.

        创建人uuid

        :return: The user_id of this GetProjectInfoV4ResultProjectCreator.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GetProjectInfoV4ResultProjectCreator.

        创建人uuid

        :param user_id: The user_id of this GetProjectInfoV4ResultProjectCreator.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this GetProjectInfoV4ResultProjectCreator.

        创建人姓名

        :return: The user_name of this GetProjectInfoV4ResultProjectCreator.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this GetProjectInfoV4ResultProjectCreator.

        创建人姓名

        :param user_name: The user_name of this GetProjectInfoV4ResultProjectCreator.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        """Gets the domain_id of this GetProjectInfoV4ResultProjectCreator.

        创建人租户id

        :return: The domain_id of this GetProjectInfoV4ResultProjectCreator.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this GetProjectInfoV4ResultProjectCreator.

        创建人租户id

        :param domain_id: The domain_id of this GetProjectInfoV4ResultProjectCreator.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this GetProjectInfoV4ResultProjectCreator.

        创建人租户名称

        :return: The domain_name of this GetProjectInfoV4ResultProjectCreator.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this GetProjectInfoV4ResultProjectCreator.

        创建人租户名称

        :param domain_name: The domain_name of this GetProjectInfoV4ResultProjectCreator.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def nick_name(self):
        """Gets the nick_name of this GetProjectInfoV4ResultProjectCreator.

        创建人昵称

        :return: The nick_name of this GetProjectInfoV4ResultProjectCreator.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this GetProjectInfoV4ResultProjectCreator.

        创建人昵称

        :param nick_name: The nick_name of this GetProjectInfoV4ResultProjectCreator.
        :type nick_name: str
        """
        self._nick_name = nick_name

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
        if not isinstance(other, GetProjectInfoV4ResultProjectCreator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
