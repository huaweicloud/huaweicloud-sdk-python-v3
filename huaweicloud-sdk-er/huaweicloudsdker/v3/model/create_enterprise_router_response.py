# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEnterpriseRouterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'EnterpriseRouter',
        'request_id': 'str',
        'x_client_token': 'str'
    }

    attribute_map = {
        'instance': 'instance',
        'request_id': 'request_id',
        'x_client_token': 'X-Client-Token'
    }

    def __init__(self, instance=None, request_id=None, x_client_token=None):
        """CreateEnterpriseRouterResponse

        The model defined in huaweicloud sdk

        :param instance: 
        :type instance: :class:`huaweicloudsdker.v3.EnterpriseRouter`
        :param request_id: 请求ID
        :type request_id: str
        :param x_client_token: 
        :type x_client_token: str
        """
        
        super(CreateEnterpriseRouterResponse, self).__init__()

        self._instance = None
        self._request_id = None
        self._x_client_token = None
        self.discriminator = None

        if instance is not None:
            self.instance = instance
        if request_id is not None:
            self.request_id = request_id
        if x_client_token is not None:
            self.x_client_token = x_client_token

    @property
    def instance(self):
        """Gets the instance of this CreateEnterpriseRouterResponse.

        :return: The instance of this CreateEnterpriseRouterResponse.
        :rtype: :class:`huaweicloudsdker.v3.EnterpriseRouter`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this CreateEnterpriseRouterResponse.

        :param instance: The instance of this CreateEnterpriseRouterResponse.
        :type instance: :class:`huaweicloudsdker.v3.EnterpriseRouter`
        """
        self._instance = instance

    @property
    def request_id(self):
        """Gets the request_id of this CreateEnterpriseRouterResponse.

        请求ID

        :return: The request_id of this CreateEnterpriseRouterResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateEnterpriseRouterResponse.

        请求ID

        :param request_id: The request_id of this CreateEnterpriseRouterResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def x_client_token(self):
        """Gets the x_client_token of this CreateEnterpriseRouterResponse.

        :return: The x_client_token of this CreateEnterpriseRouterResponse.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        """Sets the x_client_token of this CreateEnterpriseRouterResponse.

        :param x_client_token: The x_client_token of this CreateEnterpriseRouterResponse.
        :type x_client_token: str
        """
        self._x_client_token = x_client_token

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
        if not isinstance(other, CreateEnterpriseRouterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
