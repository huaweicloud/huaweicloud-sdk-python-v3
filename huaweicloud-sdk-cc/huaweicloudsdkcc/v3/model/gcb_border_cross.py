# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GcbBorderCross:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bordercross': 'bool'
    }

    attribute_map = {
        'bordercross': 'bordercross'
    }

    def __init__(self, bordercross=None):
        r"""GcbBorderCross

        The model defined in huaweicloud sdk

        :param bordercross: 功能说明：全域互联带宽是否跨境，判断依据：带宽是否涉及从中国大陆到其他国家。 取值范围：True：跨境；False：非跨境 
        :type bordercross: bool
        """
        
        

        self._bordercross = None
        self.discriminator = None

        self.bordercross = bordercross

    @property
    def bordercross(self):
        r"""Gets the bordercross of this GcbBorderCross.

        功能说明：全域互联带宽是否跨境，判断依据：带宽是否涉及从中国大陆到其他国家。 取值范围：True：跨境；False：非跨境 

        :return: The bordercross of this GcbBorderCross.
        :rtype: bool
        """
        return self._bordercross

    @bordercross.setter
    def bordercross(self, bordercross):
        r"""Sets the bordercross of this GcbBorderCross.

        功能说明：全域互联带宽是否跨境，判断依据：带宽是否涉及从中国大陆到其他国家。 取值范围：True：跨境；False：非跨境 

        :param bordercross: The bordercross of this GcbBorderCross.
        :type bordercross: bool
        """
        self._bordercross = bordercross

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
        if not isinstance(other, GcbBorderCross):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
