# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageReadConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'read_content': 'str',
        'image_id': 'str',
        'resolution': 'Resolution'
    }

    attribute_map = {
        'read_content': 'read_content',
        'image_id': 'image_id',
        'resolution': 'resolution'
    }

    def __init__(self, read_content=None, image_id=None, resolution=None):
        """ImageReadConfig

        The model defined in huaweicloud sdk

        :param read_content: 播报内容，长度为1~2500
        :type read_content: str
        :param image_id: 图片id
        :type image_id: str
        :param resolution: 
        :type resolution: :class:`huaweicloudsdkcbs.v1.Resolution`
        """
        
        

        self._read_content = None
        self._image_id = None
        self._resolution = None
        self.discriminator = None

        self.read_content = read_content
        self.image_id = image_id
        self.resolution = resolution

    @property
    def read_content(self):
        """Gets the read_content of this ImageReadConfig.

        播报内容，长度为1~2500

        :return: The read_content of this ImageReadConfig.
        :rtype: str
        """
        return self._read_content

    @read_content.setter
    def read_content(self, read_content):
        """Sets the read_content of this ImageReadConfig.

        播报内容，长度为1~2500

        :param read_content: The read_content of this ImageReadConfig.
        :type read_content: str
        """
        self._read_content = read_content

    @property
    def image_id(self):
        """Gets the image_id of this ImageReadConfig.

        图片id

        :return: The image_id of this ImageReadConfig.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageReadConfig.

        图片id

        :param image_id: The image_id of this ImageReadConfig.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def resolution(self):
        """Gets the resolution of this ImageReadConfig.

        :return: The resolution of this ImageReadConfig.
        :rtype: :class:`huaweicloudsdkcbs.v1.Resolution`
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ImageReadConfig.

        :param resolution: The resolution of this ImageReadConfig.
        :type resolution: :class:`huaweicloudsdkcbs.v1.Resolution`
        """
        self._resolution = resolution

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
        if not isinstance(other, ImageReadConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
