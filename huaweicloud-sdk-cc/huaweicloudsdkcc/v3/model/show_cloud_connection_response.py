# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudConnectionResponse(SdkResponse):

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
        'cloud_connection': 'CloudConnection'
    }

    attribute_map = {
        'request_id': 'request_id',
        'cloud_connection': 'cloud_connection'
    }

    def __init__(self, request_id=None, cloud_connection=None):
        """ShowCloudConnectionResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param cloud_connection: 
        :type cloud_connection: :class:`huaweicloudsdkcc.v3.CloudConnection`
        """
        
        super(ShowCloudConnectionResponse, self).__init__()

        self._request_id = None
        self._cloud_connection = None
        self.discriminator = None

        self.request_id = request_id
        self.cloud_connection = cloud_connection

    @property
    def request_id(self):
        """Gets the request_id of this ShowCloudConnectionResponse.

        资源ID标识符。

        :return: The request_id of this ShowCloudConnectionResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowCloudConnectionResponse.

        资源ID标识符。

        :param request_id: The request_id of this ShowCloudConnectionResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def cloud_connection(self):
        """Gets the cloud_connection of this ShowCloudConnectionResponse.

        :return: The cloud_connection of this ShowCloudConnectionResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.CloudConnection`
        """
        return self._cloud_connection

    @cloud_connection.setter
    def cloud_connection(self, cloud_connection):
        """Sets the cloud_connection of this ShowCloudConnectionResponse.

        :param cloud_connection: The cloud_connection of this ShowCloudConnectionResponse.
        :type cloud_connection: :class:`huaweicloudsdkcc.v3.CloudConnection`
        """
        self._cloud_connection = cloud_connection

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
        if not isinstance(other, ShowCloudConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
