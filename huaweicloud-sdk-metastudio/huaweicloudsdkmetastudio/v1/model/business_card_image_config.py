# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessCardImageConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'human_image': 'str',
        'logo_image': 'str'
    }

    attribute_map = {
        'human_image': 'human_image',
        'logo_image': 'logo_image'
    }

    def __init__(self, human_image=None, logo_image=None):
        r"""BusinessCardImageConfig

        The model defined in huaweicloud sdk

        :param human_image: 人物照片，需要Base64编码。
        :type human_image: str
        :param logo_image: Logo图片，需要Base64编码。
        :type logo_image: str
        """
        
        

        self._human_image = None
        self._logo_image = None
        self.discriminator = None

        self.human_image = human_image
        if logo_image is not None:
            self.logo_image = logo_image

    @property
    def human_image(self):
        r"""Gets the human_image of this BusinessCardImageConfig.

        人物照片，需要Base64编码。

        :return: The human_image of this BusinessCardImageConfig.
        :rtype: str
        """
        return self._human_image

    @human_image.setter
    def human_image(self, human_image):
        r"""Sets the human_image of this BusinessCardImageConfig.

        人物照片，需要Base64编码。

        :param human_image: The human_image of this BusinessCardImageConfig.
        :type human_image: str
        """
        self._human_image = human_image

    @property
    def logo_image(self):
        r"""Gets the logo_image of this BusinessCardImageConfig.

        Logo图片，需要Base64编码。

        :return: The logo_image of this BusinessCardImageConfig.
        :rtype: str
        """
        return self._logo_image

    @logo_image.setter
    def logo_image(self, logo_image):
        r"""Sets the logo_image of this BusinessCardImageConfig.

        Logo图片，需要Base64编码。

        :param logo_image: The logo_image of this BusinessCardImageConfig.
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
        if not isinstance(other, BusinessCardImageConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
