# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotebookImage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_type': 'DevelopImageType',
        'image_info': 'ImageInfo'
    }

    attribute_map = {
        'image_type': 'image_type',
        'image_info': 'image_info'
    }

    def __init__(self, image_type=None, image_info=None):
        """NotebookImage

        The model defined in huaweicloud sdk

        :param image_type: 
        :type image_type: :class:`huaweicloudsdkeihealth.v1.DevelopImageType`
        :param image_info: 
        :type image_info: :class:`huaweicloudsdkeihealth.v1.ImageInfo`
        """
        
        

        self._image_type = None
        self._image_info = None
        self.discriminator = None

        self.image_type = image_type
        self.image_info = image_info

    @property
    def image_type(self):
        """Gets the image_type of this NotebookImage.

        :return: The image_type of this NotebookImage.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DevelopImageType`
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this NotebookImage.

        :param image_type: The image_type of this NotebookImage.
        :type image_type: :class:`huaweicloudsdkeihealth.v1.DevelopImageType`
        """
        self._image_type = image_type

    @property
    def image_info(self):
        """Gets the image_info of this NotebookImage.

        :return: The image_info of this NotebookImage.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImageInfo`
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        """Sets the image_info of this NotebookImage.

        :param image_info: The image_info of this NotebookImage.
        :type image_info: :class:`huaweicloudsdkeihealth.v1.ImageInfo`
        """
        self._image_info = image_info

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
        if not isinstance(other, NotebookImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
