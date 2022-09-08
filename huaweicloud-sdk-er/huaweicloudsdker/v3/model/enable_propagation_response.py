# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnablePropagationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'propagation': 'Propagation',
        'request_id': 'str',
        'x_client_token': 'str'
    }

    attribute_map = {
        'propagation': 'propagation',
        'request_id': 'request_id',
        'x_client_token': 'X-Client-Token'
    }

    def __init__(self, propagation=None, request_id=None, x_client_token=None):
        """EnablePropagationResponse

        The model defined in huaweicloud sdk

        :param propagation: 
        :type propagation: :class:`huaweicloudsdker.v3.Propagation`
        :param request_id: 请求ID
        :type request_id: str
        :param x_client_token: 
        :type x_client_token: str
        """
        
        super(EnablePropagationResponse, self).__init__()

        self._propagation = None
        self._request_id = None
        self._x_client_token = None
        self.discriminator = None

        if propagation is not None:
            self.propagation = propagation
        if request_id is not None:
            self.request_id = request_id
        if x_client_token is not None:
            self.x_client_token = x_client_token

    @property
    def propagation(self):
        """Gets the propagation of this EnablePropagationResponse.


        :return: The propagation of this EnablePropagationResponse.
        :rtype: :class:`huaweicloudsdker.v3.Propagation`
        """
        return self._propagation

    @propagation.setter
    def propagation(self, propagation):
        """Sets the propagation of this EnablePropagationResponse.


        :param propagation: The propagation of this EnablePropagationResponse.
        :type propagation: :class:`huaweicloudsdker.v3.Propagation`
        """
        self._propagation = propagation

    @property
    def request_id(self):
        """Gets the request_id of this EnablePropagationResponse.

        请求ID

        :return: The request_id of this EnablePropagationResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this EnablePropagationResponse.

        请求ID

        :param request_id: The request_id of this EnablePropagationResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def x_client_token(self):
        """Gets the x_client_token of this EnablePropagationResponse.


        :return: The x_client_token of this EnablePropagationResponse.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        """Sets the x_client_token of this EnablePropagationResponse.


        :param x_client_token: The x_client_token of this EnablePropagationResponse.
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
        if not isinstance(other, EnablePropagationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
