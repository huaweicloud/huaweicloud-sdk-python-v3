# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFavoriteReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'display_info': 'str',
        'location_info': 'str'
    }

    attribute_map = {
        'type': 'type',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'display_info': 'display_info',
        'location_info': 'location_info'
    }

    def __init__(self, type=None, resource_id=None, resource_name=None, resource_type=None, display_info=None, location_info=None):
        r"""CreateFavoriteReq

        The model defined in huaweicloud sdk

        :param type: 收藏类型。
        :type type: str
        :param resource_id: 收藏的资源ID。
        :type resource_id: str
        :param resource_name: 收藏的资源名称，正则匹配中文，英文字母和数字及下划线。
        :type resource_name: str
        :param resource_type: 收藏的资源类型，正则匹配英文字母和数字及下划线。
        :type resource_type: str
        :param display_info: 展示信息。
        :type display_info: str
        :param location_info: 定位信息。
        :type location_info: str
        """
        
        

        self._type = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._display_info = None
        self._location_info = None
        self.discriminator = None

        self.type = type
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.display_info = display_info
        self.location_info = location_info

    @property
    def type(self):
        r"""Gets the type of this CreateFavoriteReq.

        收藏类型。

        :return: The type of this CreateFavoriteReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateFavoriteReq.

        收藏类型。

        :param type: The type of this CreateFavoriteReq.
        :type type: str
        """
        self._type = type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CreateFavoriteReq.

        收藏的资源ID。

        :return: The resource_id of this CreateFavoriteReq.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateFavoriteReq.

        收藏的资源ID。

        :param resource_id: The resource_id of this CreateFavoriteReq.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this CreateFavoriteReq.

        收藏的资源名称，正则匹配中文，英文字母和数字及下划线。

        :return: The resource_name of this CreateFavoriteReq.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this CreateFavoriteReq.

        收藏的资源名称，正则匹配中文，英文字母和数字及下划线。

        :param resource_name: The resource_name of this CreateFavoriteReq.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CreateFavoriteReq.

        收藏的资源类型，正则匹配英文字母和数字及下划线。

        :return: The resource_type of this CreateFavoriteReq.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CreateFavoriteReq.

        收藏的资源类型，正则匹配英文字母和数字及下划线。

        :param resource_type: The resource_type of this CreateFavoriteReq.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def display_info(self):
        r"""Gets the display_info of this CreateFavoriteReq.

        展示信息。

        :return: The display_info of this CreateFavoriteReq.
        :rtype: str
        """
        return self._display_info

    @display_info.setter
    def display_info(self, display_info):
        r"""Sets the display_info of this CreateFavoriteReq.

        展示信息。

        :param display_info: The display_info of this CreateFavoriteReq.
        :type display_info: str
        """
        self._display_info = display_info

    @property
    def location_info(self):
        r"""Gets the location_info of this CreateFavoriteReq.

        定位信息。

        :return: The location_info of this CreateFavoriteReq.
        :rtype: str
        """
        return self._location_info

    @location_info.setter
    def location_info(self, location_info):
        r"""Sets the location_info of this CreateFavoriteReq.

        定位信息。

        :param location_info: The location_info of this CreateFavoriteReq.
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
        if not isinstance(other, CreateFavoriteReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
