# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeDesktopRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_transaction_id': 'str',
        'body': 'ResizeDesktopReq'
    }

    attribute_map = {
        'service_transaction_id': 'Service-Transaction-Id',
        'body': 'body'
    }

    def __init__(self, service_transaction_id=None, body=None):
        """ResizeDesktopRequest

        The model defined in huaweicloud sdk

        :param service_transaction_id: CBC接口回调时，请求头里带上的业务ID
        :type service_transaction_id: str
        :param body: Body of the ResizeDesktopRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopReq`
        """
        
        

        self._service_transaction_id = None
        self._body = None
        self.discriminator = None

        if service_transaction_id is not None:
            self.service_transaction_id = service_transaction_id
        if body is not None:
            self.body = body

    @property
    def service_transaction_id(self):
        """Gets the service_transaction_id of this ResizeDesktopRequest.

        CBC接口回调时，请求头里带上的业务ID

        :return: The service_transaction_id of this ResizeDesktopRequest.
        :rtype: str
        """
        return self._service_transaction_id

    @service_transaction_id.setter
    def service_transaction_id(self, service_transaction_id):
        """Sets the service_transaction_id of this ResizeDesktopRequest.

        CBC接口回调时，请求头里带上的业务ID

        :param service_transaction_id: The service_transaction_id of this ResizeDesktopRequest.
        :type service_transaction_id: str
        """
        self._service_transaction_id = service_transaction_id

    @property
    def body(self):
        """Gets the body of this ResizeDesktopRequest.

        :return: The body of this ResizeDesktopRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ResizeDesktopRequest.

        :param body: The body of this ResizeDesktopRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.ResizeDesktopReq`
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
        if not isinstance(other, ResizeDesktopRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
