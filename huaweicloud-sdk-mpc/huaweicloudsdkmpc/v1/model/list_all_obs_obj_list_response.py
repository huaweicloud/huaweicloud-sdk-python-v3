# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListAllObsObjListResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'objects': 'list[ObsObject]'
    }

    attribute_map = {
        'objects': 'objects'
    }

    def __init__(self, objects=None):
        """ListAllObsObjListResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._objects = None
        self.discriminator = None

        if objects is not None:
            self.objects = objects

    @property
    def objects(self):
        """Gets the objects of this ListAllObsObjListResponse.

        返回OBS对象组

        :return: The objects of this ListAllObsObjListResponse.
        :rtype: list[ObsObject]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this ListAllObsObjListResponse.

        返回OBS对象组

        :param objects: The objects of this ListAllObsObjListResponse.
        :type: list[ObsObject]
        """
        self._objects = objects

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
        if not isinstance(other, ListAllObsObjListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
