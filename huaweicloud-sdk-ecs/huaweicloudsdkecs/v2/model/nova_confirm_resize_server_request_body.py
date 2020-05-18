# coding: utf-8

import pprint
import re

import six


class NovaConfirmResizeServerRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'confirm_resize': 'str'
    }

    attribute_map = {
        'confirm_resize': 'confirmResize'
    }

    def __init__(self, confirm_resize=''):  # noqa: E501
        """NovaConfirmResizeServerRequestBody - a model defined in huaweicloud sdk"""

        self._confirm_resize = None
        self.discriminator = None

        self.confirm_resize = confirm_resize

    @property
    def confirm_resize(self):
        """Gets the confirm_resize of this NovaConfirmResizeServerRequestBody.

        确认云服务器规格调整。

        :return: The confirm_resize of this NovaConfirmResizeServerRequestBody.
        :rtype: str
        """
        return self._confirm_resize

    @confirm_resize.setter
    def confirm_resize(self, confirm_resize):
        """Sets the confirm_resize of this NovaConfirmResizeServerRequestBody.

        确认云服务器规格调整。

        :param confirm_resize: The confirm_resize of this NovaConfirmResizeServerRequestBody.
        :type: str
        """
        self._confirm_resize = confirm_resize

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
        if not isinstance(other, NovaConfirmResizeServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
