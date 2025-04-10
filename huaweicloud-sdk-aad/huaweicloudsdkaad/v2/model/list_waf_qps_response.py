# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWafQpsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'curve': 'list[Point]'
    }

    attribute_map = {
        'curve': 'curve'
    }

    def __init__(self, curve=None):
        r"""ListWafQpsResponse

        The model defined in huaweicloud sdk

        :param curve: curve
        :type curve: list[:class:`huaweicloudsdkaad.v2.Point`]
        """
        
        super(ListWafQpsResponse, self).__init__()

        self._curve = None
        self.discriminator = None

        if curve is not None:
            self.curve = curve

    @property
    def curve(self):
        r"""Gets the curve of this ListWafQpsResponse.

        curve

        :return: The curve of this ListWafQpsResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v2.Point`]
        """
        return self._curve

    @curve.setter
    def curve(self, curve):
        r"""Sets the curve of this ListWafQpsResponse.

        curve

        :param curve: The curve of this ListWafQpsResponse.
        :type curve: list[:class:`huaweicloudsdkaad.v2.Point`]
        """
        self._curve = curve

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
        if not isinstance(other, ListWafQpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
