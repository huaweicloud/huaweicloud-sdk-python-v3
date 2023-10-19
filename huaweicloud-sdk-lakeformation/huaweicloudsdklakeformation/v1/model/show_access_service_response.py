# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAccessServiceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_services': 'list[AccessServiceInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'access_services': 'access_services',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, access_services=None, x_request_id=None):
        """ShowAccessServiceResponse

        The model defined in huaweicloud sdk

        :param access_services: 接入服务授权信息列表
        :type access_services: list[:class:`huaweicloudsdklakeformation.v1.AccessServiceInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowAccessServiceResponse, self).__init__()

        self._access_services = None
        self._x_request_id = None
        self.discriminator = None

        if access_services is not None:
            self.access_services = access_services
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def access_services(self):
        """Gets the access_services of this ShowAccessServiceResponse.

        接入服务授权信息列表

        :return: The access_services of this ShowAccessServiceResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.AccessServiceInfo`]
        """
        return self._access_services

    @access_services.setter
    def access_services(self, access_services):
        """Sets the access_services of this ShowAccessServiceResponse.

        接入服务授权信息列表

        :param access_services: The access_services of this ShowAccessServiceResponse.
        :type access_services: list[:class:`huaweicloudsdklakeformation.v1.AccessServiceInfo`]
        """
        self._access_services = access_services

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowAccessServiceResponse.

        :return: The x_request_id of this ShowAccessServiceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowAccessServiceResponse.

        :param x_request_id: The x_request_id of this ShowAccessServiceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowAccessServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
