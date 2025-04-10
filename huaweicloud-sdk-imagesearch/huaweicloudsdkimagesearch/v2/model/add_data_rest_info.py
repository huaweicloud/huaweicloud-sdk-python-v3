# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDataRestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_info': 'AddDataRestInfoImageInfo'
    }

    attribute_map = {
        'image_info': 'image_info'
    }

    def __init__(self, image_info=None):
        r"""AddDataRestInfo

        The model defined in huaweicloud sdk

        :param image_info: 
        :type image_info: :class:`huaweicloudsdkimagesearch.v2.AddDataRestInfoImageInfo`
        """
        
        

        self._image_info = None
        self.discriminator = None

        if image_info is not None:
            self.image_info = image_info

    @property
    def image_info(self):
        r"""Gets the image_info of this AddDataRestInfo.

        :return: The image_info of this AddDataRestInfo.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.AddDataRestInfoImageInfo`
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        r"""Sets the image_info of this AddDataRestInfo.

        :param image_info: The image_info of this AddDataRestInfo.
        :type image_info: :class:`huaweicloudsdkimagesearch.v2.AddDataRestInfoImageInfo`
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
        if not isinstance(other, AddDataRestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
