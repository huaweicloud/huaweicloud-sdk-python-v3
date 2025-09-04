# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_linked_id': 'str',
        'service_transaction_id': 'str',
        'body': 'CreateAppServerReq'
    }

    attribute_map = {
        'x_linked_id': 'X-Linked-Id',
        'service_transaction_id': 'Service-Transaction-Id',
        'body': 'body'
    }

    def __init__(self, x_linked_id=None, service_transaction_id=None, body=None):
        r"""CreateAppServersRequest

        The model defined in huaweicloud sdk

        :param x_linked_id: 交易组件调用时下发的关联ID。
        :type x_linked_id: str
        :param service_transaction_id: CBC接口回调时，请求头里带上的业务ID 包周期场景必填 按需场景无。
        :type service_transaction_id: str
        :param body: Body of the CreateAppServersRequest
        :type body: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppServerReq`
        """
        
        

        self._x_linked_id = None
        self._service_transaction_id = None
        self._body = None
        self.discriminator = None

        if x_linked_id is not None:
            self.x_linked_id = x_linked_id
        if service_transaction_id is not None:
            self.service_transaction_id = service_transaction_id
        if body is not None:
            self.body = body

    @property
    def x_linked_id(self):
        r"""Gets the x_linked_id of this CreateAppServersRequest.

        交易组件调用时下发的关联ID。

        :return: The x_linked_id of this CreateAppServersRequest.
        :rtype: str
        """
        return self._x_linked_id

    @x_linked_id.setter
    def x_linked_id(self, x_linked_id):
        r"""Sets the x_linked_id of this CreateAppServersRequest.

        交易组件调用时下发的关联ID。

        :param x_linked_id: The x_linked_id of this CreateAppServersRequest.
        :type x_linked_id: str
        """
        self._x_linked_id = x_linked_id

    @property
    def service_transaction_id(self):
        r"""Gets the service_transaction_id of this CreateAppServersRequest.

        CBC接口回调时，请求头里带上的业务ID 包周期场景必填 按需场景无。

        :return: The service_transaction_id of this CreateAppServersRequest.
        :rtype: str
        """
        return self._service_transaction_id

    @service_transaction_id.setter
    def service_transaction_id(self, service_transaction_id):
        r"""Sets the service_transaction_id of this CreateAppServersRequest.

        CBC接口回调时，请求头里带上的业务ID 包周期场景必填 按需场景无。

        :param service_transaction_id: The service_transaction_id of this CreateAppServersRequest.
        :type service_transaction_id: str
        """
        self._service_transaction_id = service_transaction_id

    @property
    def body(self):
        r"""Gets the body of this CreateAppServersRequest.

        :return: The body of this CreateAppServersRequest.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppServerReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateAppServersRequest.

        :param body: The body of this CreateAppServersRequest.
        :type body: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppServerReq`
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
        if not isinstance(other, CreateAppServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
