# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PictureModelingByUrlReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'picture_url': 'str',
        'style_id': 'str',
        'name': 'str',
        'notify_url': 'str'
    }

    attribute_map = {
        'picture_url': 'picture_url',
        'style_id': 'style_id',
        'name': 'name',
        'notify_url': 'notify_url'
    }

    def __init__(self, picture_url=None, style_id=None, name=None, notify_url=None):
        r"""PictureModelingByUrlReq

        The model defined in huaweicloud sdk

        :param picture_url: 图片URL
        :type picture_url: str
        :param style_id: 风格ID
        :type style_id: str
        :param name: 模型名称
        :type name: str
        :param notify_url: 照片建模任务结束的回调地址。
        :type notify_url: str
        """
        
        

        self._picture_url = None
        self._style_id = None
        self._name = None
        self._notify_url = None
        self.discriminator = None

        self.picture_url = picture_url
        self.style_id = style_id
        self.name = name
        if notify_url is not None:
            self.notify_url = notify_url

    @property
    def picture_url(self):
        r"""Gets the picture_url of this PictureModelingByUrlReq.

        图片URL

        :return: The picture_url of this PictureModelingByUrlReq.
        :rtype: str
        """
        return self._picture_url

    @picture_url.setter
    def picture_url(self, picture_url):
        r"""Sets the picture_url of this PictureModelingByUrlReq.

        图片URL

        :param picture_url: The picture_url of this PictureModelingByUrlReq.
        :type picture_url: str
        """
        self._picture_url = picture_url

    @property
    def style_id(self):
        r"""Gets the style_id of this PictureModelingByUrlReq.

        风格ID

        :return: The style_id of this PictureModelingByUrlReq.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        r"""Sets the style_id of this PictureModelingByUrlReq.

        风格ID

        :param style_id: The style_id of this PictureModelingByUrlReq.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def name(self):
        r"""Gets the name of this PictureModelingByUrlReq.

        模型名称

        :return: The name of this PictureModelingByUrlReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PictureModelingByUrlReq.

        模型名称

        :param name: The name of this PictureModelingByUrlReq.
        :type name: str
        """
        self._name = name

    @property
    def notify_url(self):
        r"""Gets the notify_url of this PictureModelingByUrlReq.

        照片建模任务结束的回调地址。

        :return: The notify_url of this PictureModelingByUrlReq.
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        r"""Sets the notify_url of this PictureModelingByUrlReq.

        照片建模任务结束的回调地址。

        :param notify_url: The notify_url of this PictureModelingByUrlReq.
        :type notify_url: str
        """
        self._notify_url = notify_url

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
        if not isinstance(other, PictureModelingByUrlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
