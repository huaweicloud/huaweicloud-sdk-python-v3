# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClobDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clob_string': 'str'
    }

    attribute_map = {
        'clob_string': 'clob_string'
    }

    def __init__(self, clob_string=None):
        """ShowClobDetailResponse

        The model defined in huaweicloud sdk

        :param clob_string: clob详情。
        :type clob_string: str
        """
        
        super(ShowClobDetailResponse, self).__init__()

        self._clob_string = None
        self.discriminator = None

        if clob_string is not None:
            self.clob_string = clob_string

    @property
    def clob_string(self):
        """Gets the clob_string of this ShowClobDetailResponse.

        clob详情。

        :return: The clob_string of this ShowClobDetailResponse.
        :rtype: str
        """
        return self._clob_string

    @clob_string.setter
    def clob_string(self, clob_string):
        """Sets the clob_string of this ShowClobDetailResponse.

        clob详情。

        :param clob_string: The clob_string of this ShowClobDetailResponse.
        :type clob_string: str
        """
        self._clob_string = clob_string

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
        if not isinstance(other, ShowClobDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
