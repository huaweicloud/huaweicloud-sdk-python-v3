# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageToVideoInference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_config': 'ImageToVideoInfo'
    }

    attribute_map = {
        'image_config': 'image_config'
    }

    def __init__(self, image_config=None):
        """ImageToVideoInference

        The model defined in huaweicloud sdk

        :param image_config: 
        :type image_config: :class:`huaweicloudsdkimage.v2.ImageToVideoInfo`
        """
        
        

        self._image_config = None
        self.discriminator = None

        self.image_config = image_config

    @property
    def image_config(self):
        """Gets the image_config of this ImageToVideoInference.

        :return: The image_config of this ImageToVideoInference.
        :rtype: :class:`huaweicloudsdkimage.v2.ImageToVideoInfo`
        """
        return self._image_config

    @image_config.setter
    def image_config(self, image_config):
        """Sets the image_config of this ImageToVideoInference.

        :param image_config: The image_config of this ImageToVideoInference.
        :type image_config: :class:`huaweicloudsdkimage.v2.ImageToVideoInfo`
        """
        self._image_config = image_config

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
        if not isinstance(other, ImageToVideoInference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
