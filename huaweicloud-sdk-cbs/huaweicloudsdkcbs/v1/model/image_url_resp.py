# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageUrlResp:

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
        'url': 'str',
        'resolution': 'Resolution'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'url': 'url',
        'resolution': 'resolution'
    }

    def __init__(self, id=None, name=None, url=None, resolution=None):
        r"""ImageUrlResp

        The model defined in huaweicloud sdk

        :param id: 图片id
        :type id: str
        :param name: 
        :type name: str
        :param url: 访问地址
        :type url: str
        :param resolution: 
        :type resolution: :class:`huaweicloudsdkcbs.v1.Resolution`
        """
        
        

        self._id = None
        self._name = None
        self._url = None
        self._resolution = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        self.url = url
        self.resolution = resolution

    @property
    def id(self):
        r"""Gets the id of this ImageUrlResp.

        图片id

        :return: The id of this ImageUrlResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageUrlResp.

        图片id

        :param id: The id of this ImageUrlResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ImageUrlResp.

        

        :return: The name of this ImageUrlResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImageUrlResp.

        

        :param name: The name of this ImageUrlResp.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        r"""Gets the url of this ImageUrlResp.

        访问地址

        :return: The url of this ImageUrlResp.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ImageUrlResp.

        访问地址

        :param url: The url of this ImageUrlResp.
        :type url: str
        """
        self._url = url

    @property
    def resolution(self):
        r"""Gets the resolution of this ImageUrlResp.

        :return: The resolution of this ImageUrlResp.
        :rtype: :class:`huaweicloudsdkcbs.v1.Resolution`
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        r"""Sets the resolution of this ImageUrlResp.

        :param resolution: The resolution of this ImageUrlResp.
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
        if not isinstance(other, ImageUrlResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
