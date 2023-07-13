# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterImageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'region_id': 'region_id'
    }

    def __init__(self, image_id=None, region_id=None):
        """RegisterImageRequestBody

        The model defined in huaweicloud sdk

        :param image_id: 注册到边缘云上的公有云IMS的私有镜像id。
        :type image_id: str
        :param region_id: 原私有镜像所在公有云的region。
        :type region_id: str
        """
        
        

        self._image_id = None
        self._region_id = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def image_id(self):
        """Gets the image_id of this RegisterImageRequestBody.

        注册到边缘云上的公有云IMS的私有镜像id。

        :return: The image_id of this RegisterImageRequestBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this RegisterImageRequestBody.

        注册到边缘云上的公有云IMS的私有镜像id。

        :param image_id: The image_id of this RegisterImageRequestBody.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def region_id(self):
        """Gets the region_id of this RegisterImageRequestBody.

        原私有镜像所在公有云的region。

        :return: The region_id of this RegisterImageRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this RegisterImageRequestBody.

        原私有镜像所在公有云的region。

        :param region_id: The region_id of this RegisterImageRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, RegisterImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
