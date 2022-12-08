# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountPublicIpResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elasticip_size': 'int'
    }

    attribute_map = {
        'elasticip_size': 'elasticip_size'
    }

    def __init__(self, elasticip_size=None):
        """CountPublicIpResponse

        The model defined in huaweicloud sdk

        :param elasticip_size: 弹性公网数量
        :type elasticip_size: int
        """
        
        super(CountPublicIpResponse, self).__init__()

        self._elasticip_size = None
        self.discriminator = None

        if elasticip_size is not None:
            self.elasticip_size = elasticip_size

    @property
    def elasticip_size(self):
        """Gets the elasticip_size of this CountPublicIpResponse.

        弹性公网数量

        :return: The elasticip_size of this CountPublicIpResponse.
        :rtype: int
        """
        return self._elasticip_size

    @elasticip_size.setter
    def elasticip_size(self, elasticip_size):
        """Sets the elasticip_size of this CountPublicIpResponse.

        弹性公网数量

        :param elasticip_size: The elasticip_size of this CountPublicIpResponse.
        :type elasticip_size: int
        """
        self._elasticip_size = elasticip_size

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
        if not isinstance(other, CountPublicIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
