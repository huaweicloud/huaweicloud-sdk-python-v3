# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetIdentityCenterServiceStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_status': 'str',
        'service_status_reasons': 'list[str]'
    }

    attribute_map = {
        'service_status': 'serviceStatus',
        'service_status_reasons': 'serviceStatusReasons'
    }

    def __init__(self, service_status=None, service_status_reasons=None):
        r"""GetIdentityCenterServiceStatusResponse

        The model defined in huaweicloud sdk

        :param service_status: IAM身份中心服务实例状态
        :type service_status: str
        :param service_status_reasons: IAM身份中心服务实例状态呈现原因
        :type service_status_reasons: list[str]
        """
        
        super(GetIdentityCenterServiceStatusResponse, self).__init__()

        self._service_status = None
        self._service_status_reasons = None
        self.discriminator = None

        if service_status is not None:
            self.service_status = service_status
        if service_status_reasons is not None:
            self.service_status_reasons = service_status_reasons

    @property
    def service_status(self):
        r"""Gets the service_status of this GetIdentityCenterServiceStatusResponse.

        IAM身份中心服务实例状态

        :return: The service_status of this GetIdentityCenterServiceStatusResponse.
        :rtype: str
        """
        return self._service_status

    @service_status.setter
    def service_status(self, service_status):
        r"""Sets the service_status of this GetIdentityCenterServiceStatusResponse.

        IAM身份中心服务实例状态

        :param service_status: The service_status of this GetIdentityCenterServiceStatusResponse.
        :type service_status: str
        """
        self._service_status = service_status

    @property
    def service_status_reasons(self):
        r"""Gets the service_status_reasons of this GetIdentityCenterServiceStatusResponse.

        IAM身份中心服务实例状态呈现原因

        :return: The service_status_reasons of this GetIdentityCenterServiceStatusResponse.
        :rtype: list[str]
        """
        return self._service_status_reasons

    @service_status_reasons.setter
    def service_status_reasons(self, service_status_reasons):
        r"""Sets the service_status_reasons of this GetIdentityCenterServiceStatusResponse.

        IAM身份中心服务实例状态呈现原因

        :param service_status_reasons: The service_status_reasons of this GetIdentityCenterServiceStatusResponse.
        :type service_status_reasons: list[str]
        """
        self._service_status_reasons = service_status_reasons

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
        if not isinstance(other, GetIdentityCenterServiceStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
