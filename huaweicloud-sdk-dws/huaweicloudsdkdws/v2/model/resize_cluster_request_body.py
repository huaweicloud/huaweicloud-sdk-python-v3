# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeClusterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scale_out': 'ScaleOut'
    }

    attribute_map = {
        'scale_out': 'scale_out'
    }

    def __init__(self, scale_out=None):
        """ResizeClusterRequestBody

        The model defined in huaweicloud sdk

        :param scale_out: 
        :type scale_out: :class:`huaweicloudsdkdws.v2.ScaleOut`
        """
        
        

        self._scale_out = None
        self.discriminator = None

        if scale_out is not None:
            self.scale_out = scale_out

    @property
    def scale_out(self):
        """Gets the scale_out of this ResizeClusterRequestBody.

        :return: The scale_out of this ResizeClusterRequestBody.
        :rtype: :class:`huaweicloudsdkdws.v2.ScaleOut`
        """
        return self._scale_out

    @scale_out.setter
    def scale_out(self, scale_out):
        """Sets the scale_out of this ResizeClusterRequestBody.

        :param scale_out: The scale_out of this ResizeClusterRequestBody.
        :type scale_out: :class:`huaweicloudsdkdws.v2.ScaleOut`
        """
        self._scale_out = scale_out

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
        if not isinstance(other, ResizeClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
