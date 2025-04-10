# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessCardImageUrl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'human_image_url': 'str',
        'logo_image': 'str'
    }

    attribute_map = {
        'human_image_url': 'human_image_url',
        'logo_image': 'logo_image'
    }

    def __init__(self, human_image_url=None, logo_image=None):
        r"""BusinessCardImageUrl

        The model defined in huaweicloud sdk

        :param human_image_url: 任务照片下载URL。
        :type human_image_url: str
        :param logo_image: Logo图片下载URL。
        :type logo_image: str
        """
        
        

        self._human_image_url = None
        self._logo_image = None
        self.discriminator = None

        if human_image_url is not None:
            self.human_image_url = human_image_url
        if logo_image is not None:
            self.logo_image = logo_image

    @property
    def human_image_url(self):
        r"""Gets the human_image_url of this BusinessCardImageUrl.

        任务照片下载URL。

        :return: The human_image_url of this BusinessCardImageUrl.
        :rtype: str
        """
        return self._human_image_url

    @human_image_url.setter
    def human_image_url(self, human_image_url):
        r"""Sets the human_image_url of this BusinessCardImageUrl.

        任务照片下载URL。

        :param human_image_url: The human_image_url of this BusinessCardImageUrl.
        :type human_image_url: str
        """
        self._human_image_url = human_image_url

    @property
    def logo_image(self):
        r"""Gets the logo_image of this BusinessCardImageUrl.

        Logo图片下载URL。

        :return: The logo_image of this BusinessCardImageUrl.
        :rtype: str
        """
        return self._logo_image

    @logo_image.setter
    def logo_image(self, logo_image):
        r"""Sets the logo_image of this BusinessCardImageUrl.

        Logo图片下载URL。

        :param logo_image: The logo_image of this BusinessCardImageUrl.
        :type logo_image: str
        """
        self._logo_image = logo_image

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
        if not isinstance(other, BusinessCardImageUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
