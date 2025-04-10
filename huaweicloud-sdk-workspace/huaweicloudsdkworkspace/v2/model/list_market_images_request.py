# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMarketImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_ids': 'list[str]'
    }

    attribute_map = {
        'image_ids': 'image_ids'
    }

    def __init__(self, image_ids=None):
        r"""ListMarketImagesRequest

        The model defined in huaweicloud sdk

        :param image_ids: 镜像id，支持传1到100个。
        :type image_ids: list[str]
        """
        
        

        self._image_ids = None
        self.discriminator = None

        self.image_ids = image_ids

    @property
    def image_ids(self):
        r"""Gets the image_ids of this ListMarketImagesRequest.

        镜像id，支持传1到100个。

        :return: The image_ids of this ListMarketImagesRequest.
        :rtype: list[str]
        """
        return self._image_ids

    @image_ids.setter
    def image_ids(self, image_ids):
        r"""Sets the image_ids of this ListMarketImagesRequest.

        镜像id，支持传1到100个。

        :param image_ids: The image_ids of this ListMarketImagesRequest.
        :type image_ids: list[str]
        """
        self._image_ids = image_ids

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
        if not isinstance(other, ListMarketImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
