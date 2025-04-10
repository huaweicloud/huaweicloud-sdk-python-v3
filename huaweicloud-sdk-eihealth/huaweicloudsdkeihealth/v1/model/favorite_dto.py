# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FavoriteDto:

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
        'type': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'create_time': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'display_info': 'str',
        'location_info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'create_time': 'create_time',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'display_info': 'display_info',
        'location_info': 'location_info'
    }

    def __init__(self, id=None, type=None, user_id=None, user_name=None, create_time=None, resource_id=None, resource_name=None, resource_type=None, display_info=None, location_info=None):
        r"""FavoriteDto

        The model defined in huaweicloud sdk

        :param id: 收藏ID。
        :type id: str
        :param type: 收藏类型。
        :type type: str
        :param user_id: 收藏者的用户ID。
        :type user_id: str
        :param user_name: 收藏者的用户名称。
        :type user_name: str
        :param create_time: 收藏时间。
        :type create_time: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param resource_type: 资源类型。
        :type resource_type: str
        :param display_info: 展示信息。
        :type display_info: str
        :param location_info: 定位信息。
        :type location_info: str
        """
        
        

        self._id = None
        self._type = None
        self._user_id = None
        self._user_name = None
        self._create_time = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._display_info = None
        self._location_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if create_time is not None:
            self.create_time = create_time
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if display_info is not None:
            self.display_info = display_info
        if location_info is not None:
            self.location_info = location_info

    @property
    def id(self):
        r"""Gets the id of this FavoriteDto.

        收藏ID。

        :return: The id of this FavoriteDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FavoriteDto.

        收藏ID。

        :param id: The id of this FavoriteDto.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this FavoriteDto.

        收藏类型。

        :return: The type of this FavoriteDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FavoriteDto.

        收藏类型。

        :param type: The type of this FavoriteDto.
        :type type: str
        """
        self._type = type

    @property
    def user_id(self):
        r"""Gets the user_id of this FavoriteDto.

        收藏者的用户ID。

        :return: The user_id of this FavoriteDto.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this FavoriteDto.

        收藏者的用户ID。

        :param user_id: The user_id of this FavoriteDto.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this FavoriteDto.

        收藏者的用户名称。

        :return: The user_name of this FavoriteDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this FavoriteDto.

        收藏者的用户名称。

        :param user_name: The user_name of this FavoriteDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def create_time(self):
        r"""Gets the create_time of this FavoriteDto.

        收藏时间。

        :return: The create_time of this FavoriteDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this FavoriteDto.

        收藏时间。

        :param create_time: The create_time of this FavoriteDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this FavoriteDto.

        资源ID。

        :return: The resource_id of this FavoriteDto.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this FavoriteDto.

        资源ID。

        :param resource_id: The resource_id of this FavoriteDto.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this FavoriteDto.

        资源名称。

        :return: The resource_name of this FavoriteDto.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this FavoriteDto.

        资源名称。

        :param resource_name: The resource_name of this FavoriteDto.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this FavoriteDto.

        资源类型。

        :return: The resource_type of this FavoriteDto.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this FavoriteDto.

        资源类型。

        :param resource_type: The resource_type of this FavoriteDto.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def display_info(self):
        r"""Gets the display_info of this FavoriteDto.

        展示信息。

        :return: The display_info of this FavoriteDto.
        :rtype: str
        """
        return self._display_info

    @display_info.setter
    def display_info(self, display_info):
        r"""Sets the display_info of this FavoriteDto.

        展示信息。

        :param display_info: The display_info of this FavoriteDto.
        :type display_info: str
        """
        self._display_info = display_info

    @property
    def location_info(self):
        r"""Gets the location_info of this FavoriteDto.

        定位信息。

        :return: The location_info of this FavoriteDto.
        :rtype: str
        """
        return self._location_info

    @location_info.setter
    def location_info(self, location_info):
        r"""Sets the location_info of this FavoriteDto.

        定位信息。

        :param location_info: The location_info of this FavoriteDto.
        :type location_info: str
        """
        self._location_info = location_info

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
        if not isinstance(other, FavoriteDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
