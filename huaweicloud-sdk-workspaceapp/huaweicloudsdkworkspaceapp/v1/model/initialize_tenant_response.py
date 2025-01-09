# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InitializeTenantResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'service_status': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'service_status': 'service_status'
    }

    def __init__(self, project_id=None, service_status=None):
        """InitializeTenantResponse

        The model defined in huaweicloud sdk

        :param project_id: 租户ID 同tenant_id。
        :type project_id: str
        :param service_status: 企业是否激活：active(激活)，inactive(未激活)。
        :type service_status: str
        """
        
        super(InitializeTenantResponse, self).__init__()

        self._project_id = None
        self._service_status = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if service_status is not None:
            self.service_status = service_status

    @property
    def project_id(self):
        """Gets the project_id of this InitializeTenantResponse.

        租户ID 同tenant_id。

        :return: The project_id of this InitializeTenantResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this InitializeTenantResponse.

        租户ID 同tenant_id。

        :param project_id: The project_id of this InitializeTenantResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def service_status(self):
        """Gets the service_status of this InitializeTenantResponse.

        企业是否激活：active(激活)，inactive(未激活)。

        :return: The service_status of this InitializeTenantResponse.
        :rtype: str
        """
        return self._service_status

    @service_status.setter
    def service_status(self, service_status):
        """Sets the service_status of this InitializeTenantResponse.

        企业是否激活：active(激活)，inactive(未激活)。

        :param service_status: The service_status of this InitializeTenantResponse.
        :type service_status: str
        """
        self._service_status = service_status

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
        if not isinstance(other, InitializeTenantResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
