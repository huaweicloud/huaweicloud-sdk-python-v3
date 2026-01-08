# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'image_type': 'str',
        'os_type': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'image_type': 'image_type',
        'os_type': 'os_type'
    }

    def __init__(self, desktop_id=None, image_id=None, image_name=None, image_type=None, os_type=None):
        r"""DesktopImageInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param image_id: 镜像ID。
        :type image_id: str
        :param image_name: 镜像名称。
        :type image_name: str
        :param image_type: 镜像类型。
        :type image_type: str
        :param os_type: 镜像系统类型。
        :type os_type: str
        """
        
        

        self._desktop_id = None
        self._image_id = None
        self._image_name = None
        self._image_type = None
        self._os_type = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if image_type is not None:
            self.image_type = image_type
        if os_type is not None:
            self.os_type = os_type

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this DesktopImageInfo.

        桌面id。

        :return: The desktop_id of this DesktopImageInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this DesktopImageInfo.

        桌面id。

        :param desktop_id: The desktop_id of this DesktopImageInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def image_id(self):
        r"""Gets the image_id of this DesktopImageInfo.

        镜像ID。

        :return: The image_id of this DesktopImageInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this DesktopImageInfo.

        镜像ID。

        :param image_id: The image_id of this DesktopImageInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this DesktopImageInfo.

        镜像名称。

        :return: The image_name of this DesktopImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this DesktopImageInfo.

        镜像名称。

        :param image_name: The image_name of this DesktopImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_type(self):
        r"""Gets the image_type of this DesktopImageInfo.

        镜像类型。

        :return: The image_type of this DesktopImageInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this DesktopImageInfo.

        镜像类型。

        :param image_type: The image_type of this DesktopImageInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def os_type(self):
        r"""Gets the os_type of this DesktopImageInfo.

        镜像系统类型。

        :return: The os_type of this DesktopImageInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this DesktopImageInfo.

        镜像系统类型。

        :param os_type: The os_type of this DesktopImageInfo.
        :type os_type: str
        """
        self._os_type = os_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DesktopImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
