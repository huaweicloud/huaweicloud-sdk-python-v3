# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_key': 'str'
    }

    attribute_map = {
        'object_key': 'object_key'
    }

    def __init__(self, object_key=None):
        r"""PicInfo

        The model defined in huaweicloud sdk

        :param object_key: 截图在obs桶中路径
        :type object_key: str
        """
        
        

        self._object_key = None
        self.discriminator = None

        if object_key is not None:
            self.object_key = object_key

    @property
    def object_key(self):
        r"""Gets the object_key of this PicInfo.

        截图在obs桶中路径

        :return: The object_key of this PicInfo.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this PicInfo.

        截图在obs桶中路径

        :param object_key: The object_key of this PicInfo.
        :type object_key: str
        """
        self._object_key = object_key

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
        if not isinstance(other, PicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
