# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateApplicationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'application_urn': 'str',
        'application_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'application_urn': 'application_urn',
        'application_id': 'application_id'
    }

    def __init__(self, request_id=None, application_urn=None, application_id=None):
        """CreateApplicationResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param application_urn: Application的唯一资源标识。
        :type application_urn: str
        :param application_id: Application资源的ID。
        :type application_id: str
        """
        
        super(CreateApplicationResponse, self).__init__()

        self._request_id = None
        self._application_urn = None
        self._application_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if application_urn is not None:
            self.application_urn = application_urn
        if application_id is not None:
            self.application_id = application_id

    @property
    def request_id(self):
        """Gets the request_id of this CreateApplicationResponse.

        请求的唯一标识ID。

        :return: The request_id of this CreateApplicationResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateApplicationResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this CreateApplicationResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def application_urn(self):
        """Gets the application_urn of this CreateApplicationResponse.

        Application的唯一资源标识。

        :return: The application_urn of this CreateApplicationResponse.
        :rtype: str
        """
        return self._application_urn

    @application_urn.setter
    def application_urn(self, application_urn):
        """Sets the application_urn of this CreateApplicationResponse.

        Application的唯一资源标识。

        :param application_urn: The application_urn of this CreateApplicationResponse.
        :type application_urn: str
        """
        self._application_urn = application_urn

    @property
    def application_id(self):
        """Gets the application_id of this CreateApplicationResponse.

        Application资源的ID。

        :return: The application_id of this CreateApplicationResponse.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this CreateApplicationResponse.

        Application资源的ID。

        :param application_id: The application_id of this CreateApplicationResponse.
        :type application_id: str
        """
        self._application_id = application_id

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
        if not isinstance(other, CreateApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
