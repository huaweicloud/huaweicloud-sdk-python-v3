# coding: utf-8

import pprint
import re

import six





class AddOrUpdateTagsRequestBody:


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
        'tag': 'str',
        'image_tag': 'ResourceTag'
    }

    attribute_map = {
        'image_id': 'image_id',
        'tag': 'tag',
        'image_tag': 'image_tag'
    }

    def __init__(self, image_id=None, tag=None, image_tag=None):
        """AddOrUpdateTagsRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._image_id = None
        self._tag = None
        self._image_tag = None
        self.discriminator = None

        self.image_id = image_id
        if tag is not None:
            self.tag = tag
        if image_tag is not None:
            self.image_tag = image_tag

    @property
    def image_id(self):
        """Gets the image_id of this AddOrUpdateTagsRequestBody.

        镜像ID。

        :return: The image_id of this AddOrUpdateTagsRequestBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this AddOrUpdateTagsRequestBody.

        镜像ID。

        :param image_id: The image_id of this AddOrUpdateTagsRequestBody.
        :type: str
        """
        self._image_id = image_id

    @property
    def tag(self):
        """Gets the tag of this AddOrUpdateTagsRequestBody.

        标签数据。 tag和image_tag只能使用一个。

        :return: The tag of this AddOrUpdateTagsRequestBody.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AddOrUpdateTagsRequestBody.

        标签数据。 tag和image_tag只能使用一个。

        :param tag: The tag of this AddOrUpdateTagsRequestBody.
        :type: str
        """
        self._tag = tag

    @property
    def image_tag(self):
        """Gets the image_tag of this AddOrUpdateTagsRequestBody.


        :return: The image_tag of this AddOrUpdateTagsRequestBody.
        :rtype: ResourceTag
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this AddOrUpdateTagsRequestBody.


        :param image_tag: The image_tag of this AddOrUpdateTagsRequestBody.
        :type: ResourceTag
        """
        self._image_tag = image_tag

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddOrUpdateTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
