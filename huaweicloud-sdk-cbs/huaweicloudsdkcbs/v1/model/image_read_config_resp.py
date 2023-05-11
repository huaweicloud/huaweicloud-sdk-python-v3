# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageReadConfigResp:

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
        'resolution': 'Resolution',
        'image_url': 'str',
        'name': 'str'
    }

    attribute_map = {
        'read_content': 'read_content',
        'image_id': 'image_id',
        'resolution': 'resolution',
        'image_url': 'image_url',
        'name': 'name'
    }

    def __init__(self, read_content=None, image_id=None, resolution=None, image_url=None, name=None):
        """ImageReadConfigResp

        The model defined in huaweicloud sdk

        :param read_content: 播报内容，长度为1~2500
        :type read_content: str
        :param image_id: 图片id
        :type image_id: str
        :param resolution: 
        :type resolution: :class:`huaweicloudsdkcbs.v1.Resolution`
        :param image_url: 图片地址
        :type image_url: str
        :param name: 图片名
        :type name: str
        """
        
        

        self._read_content = None
        self._image_id = None
        self._resolution = None
        self._image_url = None
        self._name = None
        self.discriminator = None

        self.read_content = read_content
        self.image_id = image_id
        self.resolution = resolution
        self.image_url = image_url
        self.name = name

    @property
    def read_content(self):
        """Gets the read_content of this ImageReadConfigResp.

        播报内容，长度为1~2500

        :return: The read_content of this ImageReadConfigResp.
        :rtype: str
        """
        return self._read_content

    @read_content.setter
    def read_content(self, read_content):
        """Sets the read_content of this ImageReadConfigResp.

        播报内容，长度为1~2500

        :param read_content: The read_content of this ImageReadConfigResp.
        :type read_content: str
        """
        self._read_content = read_content

    @property
    def image_id(self):
        """Gets the image_id of this ImageReadConfigResp.

        图片id

        :return: The image_id of this ImageReadConfigResp.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageReadConfigResp.

        图片id

        :param image_id: The image_id of this ImageReadConfigResp.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def resolution(self):
        """Gets the resolution of this ImageReadConfigResp.

        :return: The resolution of this ImageReadConfigResp.
        :rtype: :class:`huaweicloudsdkcbs.v1.Resolution`
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ImageReadConfigResp.

        :param resolution: The resolution of this ImageReadConfigResp.
        :type resolution: :class:`huaweicloudsdkcbs.v1.Resolution`
        """
        self._resolution = resolution

    @property
    def image_url(self):
        """Gets the image_url of this ImageReadConfigResp.

        图片地址

        :return: The image_url of this ImageReadConfigResp.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ImageReadConfigResp.

        图片地址

        :param image_url: The image_url of this ImageReadConfigResp.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def name(self):
        """Gets the name of this ImageReadConfigResp.

        图片名

        :return: The name of this ImageReadConfigResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageReadConfigResp.

        图片名

        :param name: The name of this ImageReadConfigResp.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ImageReadConfigResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
