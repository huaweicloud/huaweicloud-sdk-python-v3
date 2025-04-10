# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebImageExtractedData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'contact_info': 'WebImageContactInfo',
        'image_size': 'WebImageImageSize'
    }

    attribute_map = {
        'contact_info': 'contact_info',
        'image_size': 'image_size'
    }

    def __init__(self, contact_info=None, image_size=None):
        r"""WebImageExtractedData

        The model defined in huaweicloud sdk

        :param contact_info: 
        :type contact_info: :class:`huaweicloudsdkocr.v1.WebImageContactInfo`
        :param image_size: 
        :type image_size: :class:`huaweicloudsdkocr.v1.WebImageImageSize`
        """
        
        

        self._contact_info = None
        self._image_size = None
        self.discriminator = None

        if contact_info is not None:
            self.contact_info = contact_info
        if image_size is not None:
            self.image_size = image_size

    @property
    def contact_info(self):
        r"""Gets the contact_info of this WebImageExtractedData.

        :return: The contact_info of this WebImageExtractedData.
        :rtype: :class:`huaweicloudsdkocr.v1.WebImageContactInfo`
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        r"""Sets the contact_info of this WebImageExtractedData.

        :param contact_info: The contact_info of this WebImageExtractedData.
        :type contact_info: :class:`huaweicloudsdkocr.v1.WebImageContactInfo`
        """
        self._contact_info = contact_info

    @property
    def image_size(self):
        r"""Gets the image_size of this WebImageExtractedData.

        :return: The image_size of this WebImageExtractedData.
        :rtype: :class:`huaweicloudsdkocr.v1.WebImageImageSize`
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this WebImageExtractedData.

        :param image_size: The image_size of this WebImageExtractedData.
        :type image_size: :class:`huaweicloudsdkocr.v1.WebImageImageSize`
        """
        self._image_size = image_size

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
        if not isinstance(other, WebImageExtractedData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
