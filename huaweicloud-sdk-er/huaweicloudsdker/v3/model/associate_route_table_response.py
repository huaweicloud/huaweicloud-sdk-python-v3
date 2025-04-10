# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateRouteTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'association': 'Association',
        'request_id': 'str',
        'x_client_token': 'str'
    }

    attribute_map = {
        'association': 'association',
        'request_id': 'request_id',
        'x_client_token': 'X-Client-Token'
    }

    def __init__(self, association=None, request_id=None, x_client_token=None):
        r"""AssociateRouteTableResponse

        The model defined in huaweicloud sdk

        :param association: 
        :type association: :class:`huaweicloudsdker.v3.Association`
        :param request_id: 请求ID
        :type request_id: str
        :param x_client_token: 
        :type x_client_token: str
        """
        
        super(AssociateRouteTableResponse, self).__init__()

        self._association = None
        self._request_id = None
        self._x_client_token = None
        self.discriminator = None

        if association is not None:
            self.association = association
        if request_id is not None:
            self.request_id = request_id
        if x_client_token is not None:
            self.x_client_token = x_client_token

    @property
    def association(self):
        r"""Gets the association of this AssociateRouteTableResponse.

        :return: The association of this AssociateRouteTableResponse.
        :rtype: :class:`huaweicloudsdker.v3.Association`
        """
        return self._association

    @association.setter
    def association(self, association):
        r"""Sets the association of this AssociateRouteTableResponse.

        :param association: The association of this AssociateRouteTableResponse.
        :type association: :class:`huaweicloudsdker.v3.Association`
        """
        self._association = association

    @property
    def request_id(self):
        r"""Gets the request_id of this AssociateRouteTableResponse.

        请求ID

        :return: The request_id of this AssociateRouteTableResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this AssociateRouteTableResponse.

        请求ID

        :param request_id: The request_id of this AssociateRouteTableResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def x_client_token(self):
        r"""Gets the x_client_token of this AssociateRouteTableResponse.

        :return: The x_client_token of this AssociateRouteTableResponse.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        r"""Sets the x_client_token of this AssociateRouteTableResponse.

        :param x_client_token: The x_client_token of this AssociateRouteTableResponse.
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
        if not isinstance(other, AssociateRouteTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
