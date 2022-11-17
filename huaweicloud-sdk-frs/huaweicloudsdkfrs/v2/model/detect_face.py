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
        'attributes': 'Attributes'
    }

    attribute_map = {
        'bounding_box': 'bounding_box',
        'attributes': 'attributes'
    }

    def __init__(self, bounding_box=None, attributes=None):
        """DetectFace

        The model defined in huaweicloud sdk

        :param bounding_box: 
        :type bounding_box: :class:`huaweicloudsdkfrs.v2.BoundingBox`
        :param attributes: 
        :type attributes: :class:`huaweicloudsdkfrs.v2.Attributes`
        """
        
        

        self._bounding_box = None
        self._attributes = None
        self.discriminator = None

        self.bounding_box = bounding_box
        if attributes is not None:
            self.attributes = attributes

    @property
    def bounding_box(self):
        """Gets the bounding_box of this DetectFace.

        :return: The bounding_box of this DetectFace.
        :rtype: :class:`huaweicloudsdkfrs.v2.BoundingBox`
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        """Sets the bounding_box of this DetectFace.

        :param bounding_box: The bounding_box of this DetectFace.
        :type bounding_box: :class:`huaweicloudsdkfrs.v2.BoundingBox`
        """
        self._bounding_box = bounding_box

    @property
    def attributes(self):
        """Gets the attributes of this DetectFace.

        :return: The attributes of this DetectFace.
        :rtype: :class:`huaweicloudsdkfrs.v2.Attributes`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DetectFace.

        :param attributes: The attributes of this DetectFace.
        :type attributes: :class:`huaweicloudsdkfrs.v2.Attributes`
        """
        self._attributes = attributes

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
