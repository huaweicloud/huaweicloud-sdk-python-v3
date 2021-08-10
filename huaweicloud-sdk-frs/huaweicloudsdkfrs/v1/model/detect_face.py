# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectFace:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bounding_box': 'BoundingBox',
        'attributes': 'Attributes',
        'landmark': 'Landmark'
    }

    attribute_map = {
        'bounding_box': 'bounding_box',
        'attributes': 'attributes',
        'landmark': 'landmark'
    }

    def __init__(self, bounding_box=None, attributes=None, landmark=None):
        """DetectFace - a model defined in huaweicloud sdk"""
        
        

        self._bounding_box = None
        self._attributes = None
        self._landmark = None
        self.discriminator = None

        self.bounding_box = bounding_box
        if attributes is not None:
            self.attributes = attributes
        if landmark is not None:
            self.landmark = landmark

    @property
    def bounding_box(self):
        """Gets the bounding_box of this DetectFace.


        :return: The bounding_box of this DetectFace.
        :rtype: BoundingBox
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        """Sets the bounding_box of this DetectFace.


        :param bounding_box: The bounding_box of this DetectFace.
        :type: BoundingBox
        """
        self._bounding_box = bounding_box

    @property
    def attributes(self):
        """Gets the attributes of this DetectFace.


        :return: The attributes of this DetectFace.
        :rtype: Attributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DetectFace.


        :param attributes: The attributes of this DetectFace.
        :type: Attributes
        """
        self._attributes = attributes

    @property
    def landmark(self):
        """Gets the landmark of this DetectFace.


        :return: The landmark of this DetectFace.
        :rtype: Landmark
        """
        return self._landmark

    @landmark.setter
    def landmark(self, landmark):
        """Sets the landmark of this DetectFace.


        :param landmark: The landmark of this DetectFace.
        :type: Landmark
        """
        self._landmark = landmark

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
        if not isinstance(other, DetectFace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
