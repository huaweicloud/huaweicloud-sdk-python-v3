# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateHealthCheckResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'health_check_id': 'str'
    }

    attribute_map = {
        'health_check_id': 'health_check_id'
    }

    def __init__(self, health_check_id=None):
        """DisassociateHealthCheckResponse

        The model defined in huaweicloud sdk

        :param health_check_id: 健康检查ID。 通过云解析服务的管理控制台，在健康检查的详情页面中获取。
        :type health_check_id: str
        """
        
        super(DisassociateHealthCheckResponse, self).__init__()

        self._health_check_id = None
        self.discriminator = None

        if health_check_id is not None:
            self.health_check_id = health_check_id

    @property
    def health_check_id(self):
        """Gets the health_check_id of this DisassociateHealthCheckResponse.

        健康检查ID。 通过云解析服务的管理控制台，在健康检查的详情页面中获取。

        :return: The health_check_id of this DisassociateHealthCheckResponse.
        :rtype: str
        """
        return self._health_check_id

    @health_check_id.setter
    def health_check_id(self, health_check_id):
        """Sets the health_check_id of this DisassociateHealthCheckResponse.

        健康检查ID。 通过云解析服务的管理控制台，在健康检查的详情页面中获取。

        :param health_check_id: The health_check_id of this DisassociateHealthCheckResponse.
        :type health_check_id: str
        """
        self._health_check_id = health_check_id

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
        if not isinstance(other, DisassociateHealthCheckResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
