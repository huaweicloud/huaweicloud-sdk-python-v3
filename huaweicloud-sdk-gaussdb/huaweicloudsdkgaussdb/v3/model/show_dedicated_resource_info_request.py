# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDedicatedResourceInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'dedicated_resource_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'dedicated_resource_id': 'dedicated_resource_id'
    }

    def __init__(self, x_language=None, dedicated_resource_id=None):
        """ShowDedicatedResourceInfoRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param dedicated_resource_id: 专属资源池ID。
        :type dedicated_resource_id: str
        """
        
        

        self._x_language = None
        self._dedicated_resource_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.dedicated_resource_id = dedicated_resource_id

    @property
    def x_language(self):
        """Gets the x_language of this ShowDedicatedResourceInfoRequest.

        语言。

        :return: The x_language of this ShowDedicatedResourceInfoRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowDedicatedResourceInfoRequest.

        语言。

        :param x_language: The x_language of this ShowDedicatedResourceInfoRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def dedicated_resource_id(self):
        """Gets the dedicated_resource_id of this ShowDedicatedResourceInfoRequest.

        专属资源池ID。

        :return: The dedicated_resource_id of this ShowDedicatedResourceInfoRequest.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        """Sets the dedicated_resource_id of this ShowDedicatedResourceInfoRequest.

        专属资源池ID。

        :param dedicated_resource_id: The dedicated_resource_id of this ShowDedicatedResourceInfoRequest.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

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
        if not isinstance(other, ShowDedicatedResourceInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
