# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Dress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'glass': 'str',
        'hat': 'str'
    }

    attribute_map = {
        'glass': 'glass',
        'hat': 'hat'
    }

    def __init__(self, glass=None, hat=None):
        """Dress

        The model defined in huaweicloud sdk

        :param glass: 是否带眼镜： • yes：带眼镜 • dark：带墨镜 • none：未戴眼镜 • unknown：未知
        :type glass: str
        :param hat: 是否戴帽子： • yes：戴帽子 • none：未戴帽子 • unknown：未知
        :type hat: str
        """
        
        

        self._glass = None
        self._hat = None
        self.discriminator = None

        if glass is not None:
            self.glass = glass
        if hat is not None:
            self.hat = hat

    @property
    def glass(self):
        """Gets the glass of this Dress.

        是否带眼镜： • yes：带眼镜 • dark：带墨镜 • none：未戴眼镜 • unknown：未知

        :return: The glass of this Dress.
        :rtype: str
        """
        return self._glass

    @glass.setter
    def glass(self, glass):
        """Sets the glass of this Dress.

        是否带眼镜： • yes：带眼镜 • dark：带墨镜 • none：未戴眼镜 • unknown：未知

        :param glass: The glass of this Dress.
        :type glass: str
        """
        self._glass = glass

    @property
    def hat(self):
        """Gets the hat of this Dress.

        是否戴帽子： • yes：戴帽子 • none：未戴帽子 • unknown：未知

        :return: The hat of this Dress.
        :rtype: str
        """
        return self._hat

    @hat.setter
    def hat(self, hat):
        """Sets the hat of this Dress.

        是否戴帽子： • yes：戴帽子 • none：未戴帽子 • unknown：未知

        :param hat: The hat of this Dress.
        :type hat: str
        """
        self._hat = hat

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
        if not isinstance(other, Dress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
