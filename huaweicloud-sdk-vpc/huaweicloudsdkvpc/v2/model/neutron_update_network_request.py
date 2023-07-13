# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronUpdateNetworkRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_id': 'str',
        'body': 'NeutronUpdateNetworkRequestBody'
    }

    attribute_map = {
        'network_id': 'network_id',
        'body': 'body'
    }

    def __init__(self, network_id=None, body=None):
        """NeutronUpdateNetworkRequest

        The model defined in huaweicloud sdk

        :param network_id: 网络ID
        :type network_id: str
        :param body: Body of the NeutronUpdateNetworkRequest
        :type body: :class:`huaweicloudsdkvpc.v2.NeutronUpdateNetworkRequestBody`
        """
        
        

        self._network_id = None
        self._body = None
        self.discriminator = None

        self.network_id = network_id
        if body is not None:
            self.body = body

    @property
    def network_id(self):
        """Gets the network_id of this NeutronUpdateNetworkRequest.

        网络ID

        :return: The network_id of this NeutronUpdateNetworkRequest.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NeutronUpdateNetworkRequest.

        网络ID

        :param network_id: The network_id of this NeutronUpdateNetworkRequest.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def body(self):
        """Gets the body of this NeutronUpdateNetworkRequest.

        :return: The body of this NeutronUpdateNetworkRequest.
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateNetworkRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NeutronUpdateNetworkRequest.

        :param body: The body of this NeutronUpdateNetworkRequest.
        :type body: :class:`huaweicloudsdkvpc.v2.NeutronUpdateNetworkRequestBody`
        """
        self._body = body

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
        if not isinstance(other, NeutronUpdateNetworkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
