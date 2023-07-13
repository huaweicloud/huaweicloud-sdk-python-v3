# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFilePublisherRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_publisher_token')

    openapi_types = {
        'x_publisher_token': 'str',
        'body': 'UploadFilePublisherRequestBody'
    }

    attribute_map = {
        'x_publisher_token': 'x-publisher-token',
        'body': 'body'
    }

    def __init__(self, x_publisher_token=None, body=None):
        """UploadFilePublisherRequest

        The model defined in huaweicloud sdk

        :param x_publisher_token: 发布商凭证,x-publisher-token和X-Auth-Token必传一个
        :type x_publisher_token: str
        :param body: Body of the UploadFilePublisherRequest
        :type body: :class:`huaweicloudsdkcloudide.v2.UploadFilePublisherRequestBody`
        """
        
        

        self._x_publisher_token = None
        self._body = None
        self.discriminator = None

        if x_publisher_token is not None:
            self.x_publisher_token = x_publisher_token
        if body is not None:
            self.body = body

    @property
    def x_publisher_token(self):
        """Gets the x_publisher_token of this UploadFilePublisherRequest.

        发布商凭证,x-publisher-token和X-Auth-Token必传一个

        :return: The x_publisher_token of this UploadFilePublisherRequest.
        :rtype: str
        """
        return self._x_publisher_token

    @x_publisher_token.setter
    def x_publisher_token(self, x_publisher_token):
        """Sets the x_publisher_token of this UploadFilePublisherRequest.

        发布商凭证,x-publisher-token和X-Auth-Token必传一个

        :param x_publisher_token: The x_publisher_token of this UploadFilePublisherRequest.
        :type x_publisher_token: str
        """
        self._x_publisher_token = x_publisher_token

    @property
    def body(self):
        """Gets the body of this UploadFilePublisherRequest.

        :return: The body of this UploadFilePublisherRequest.
        :rtype: :class:`huaweicloudsdkcloudide.v2.UploadFilePublisherRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UploadFilePublisherRequest.

        :param body: The body of this UploadFilePublisherRequest.
        :type body: :class:`huaweicloudsdkcloudide.v2.UploadFilePublisherRequestBody`
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
        if not isinstance(other, UploadFilePublisherRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
