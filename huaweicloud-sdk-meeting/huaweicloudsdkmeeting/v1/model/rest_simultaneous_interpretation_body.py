# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestSimultaneousInterpretationBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'simultaneous_interpretation': 'int'
    }

    attribute_map = {
        'simultaneous_interpretation': 'simultaneousInterpretation'
    }

    def __init__(self, simultaneous_interpretation=None):
        r"""RestSimultaneousInterpretationBody

        The model defined in huaweicloud sdk

        :param simultaneous_interpretation: * 0：停止同声传译 * 1：启动同声传译 
        :type simultaneous_interpretation: int
        """
        
        

        self._simultaneous_interpretation = None
        self.discriminator = None

        self.simultaneous_interpretation = simultaneous_interpretation

    @property
    def simultaneous_interpretation(self):
        r"""Gets the simultaneous_interpretation of this RestSimultaneousInterpretationBody.

        * 0：停止同声传译 * 1：启动同声传译 

        :return: The simultaneous_interpretation of this RestSimultaneousInterpretationBody.
        :rtype: int
        """
        return self._simultaneous_interpretation

    @simultaneous_interpretation.setter
    def simultaneous_interpretation(self, simultaneous_interpretation):
        r"""Sets the simultaneous_interpretation of this RestSimultaneousInterpretationBody.

        * 0：停止同声传译 * 1：启动同声传译 

        :param simultaneous_interpretation: The simultaneous_interpretation of this RestSimultaneousInterpretationBody.
        :type simultaneous_interpretation: int
        """
        self._simultaneous_interpretation = simultaneous_interpretation

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
        if not isinstance(other, RestSimultaneousInterpretationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
