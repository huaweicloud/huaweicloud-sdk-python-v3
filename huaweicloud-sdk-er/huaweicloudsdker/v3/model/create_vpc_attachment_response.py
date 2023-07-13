# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpcAttachmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_attachment': 'VpcAttachmentDetails',
        'request_id': 'str',
        'x_client_token': 'str'
    }

    attribute_map = {
        'vpc_attachment': 'vpc_attachment',
        'request_id': 'request_id',
        'x_client_token': 'X-Client-Token'
    }

    def __init__(self, vpc_attachment=None, request_id=None, x_client_token=None):
        """CreateVpcAttachmentResponse

        The model defined in huaweicloud sdk

        :param vpc_attachment: 
        :type vpc_attachment: :class:`huaweicloudsdker.v3.VpcAttachmentDetails`
        :param request_id: 请求id
        :type request_id: str
        :param x_client_token: 
        :type x_client_token: str
        """
        
        super(CreateVpcAttachmentResponse, self).__init__()

        self._vpc_attachment = None
        self._request_id = None
        self._x_client_token = None
        self.discriminator = None

        if vpc_attachment is not None:
            self.vpc_attachment = vpc_attachment
        if request_id is not None:
            self.request_id = request_id
        if x_client_token is not None:
            self.x_client_token = x_client_token

    @property
    def vpc_attachment(self):
        """Gets the vpc_attachment of this CreateVpcAttachmentResponse.

        :return: The vpc_attachment of this CreateVpcAttachmentResponse.
        :rtype: :class:`huaweicloudsdker.v3.VpcAttachmentDetails`
        """
        return self._vpc_attachment

    @vpc_attachment.setter
    def vpc_attachment(self, vpc_attachment):
        """Sets the vpc_attachment of this CreateVpcAttachmentResponse.

        :param vpc_attachment: The vpc_attachment of this CreateVpcAttachmentResponse.
        :type vpc_attachment: :class:`huaweicloudsdker.v3.VpcAttachmentDetails`
        """
        self._vpc_attachment = vpc_attachment

    @property
    def request_id(self):
        """Gets the request_id of this CreateVpcAttachmentResponse.

        请求id

        :return: The request_id of this CreateVpcAttachmentResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateVpcAttachmentResponse.

        请求id

        :param request_id: The request_id of this CreateVpcAttachmentResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def x_client_token(self):
        """Gets the x_client_token of this CreateVpcAttachmentResponse.

        :return: The x_client_token of this CreateVpcAttachmentResponse.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        """Sets the x_client_token of this CreateVpcAttachmentResponse.

        :param x_client_token: The x_client_token of this CreateVpcAttachmentResponse.
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
        if not isinstance(other, CreateVpcAttachmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
