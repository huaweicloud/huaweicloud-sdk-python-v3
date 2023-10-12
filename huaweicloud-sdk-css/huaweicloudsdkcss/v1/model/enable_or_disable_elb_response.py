# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableOrDisableElbResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elb_id': 'str'
    }

    attribute_map = {
        'elb_id': 'elb_id'
    }

    def __init__(self, elb_id=None):
        """EnableOrDisableElbResponse

        The model defined in huaweicloud sdk

        :param elb_id: 负载均衡器id。
        :type elb_id: str
        """
        
        super(EnableOrDisableElbResponse, self).__init__()

        self._elb_id = None
        self.discriminator = None

        if elb_id is not None:
            self.elb_id = elb_id

    @property
    def elb_id(self):
        """Gets the elb_id of this EnableOrDisableElbResponse.

        负载均衡器id。

        :return: The elb_id of this EnableOrDisableElbResponse.
        :rtype: str
        """
        return self._elb_id

    @elb_id.setter
    def elb_id(self, elb_id):
        """Sets the elb_id of this EnableOrDisableElbResponse.

        负载均衡器id。

        :param elb_id: The elb_id of this EnableOrDisableElbResponse.
        :type elb_id: str
        """
        self._elb_id = elb_id

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
        if not isinstance(other, EnableOrDisableElbResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
