# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOttChannelInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_control_allow_internal': 'str',
        'access_control_allow_external': 'str',
        'body': 'CreateOttChannelInfoReq'
    }

    attribute_map = {
        'access_control_allow_internal': 'Access-Control-Allow-Internal',
        'access_control_allow_external': 'Access-Control-Allow-External',
        'body': 'body'
    }

    def __init__(self, access_control_allow_internal=None, access_control_allow_external=None, body=None):
        r"""CreateOttChannelInfoRequest

        The model defined in huaweicloud sdk

        :param access_control_allow_internal: 服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-Internal访问服务。
        :type access_control_allow_internal: str
        :param access_control_allow_external: 服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-External访问服务。
        :type access_control_allow_external: str
        :param body: Body of the CreateOttChannelInfoRequest
        :type body: :class:`huaweicloudsdklive.v1.CreateOttChannelInfoReq`
        """
        
        

        self._access_control_allow_internal = None
        self._access_control_allow_external = None
        self._body = None
        self.discriminator = None

        if access_control_allow_internal is not None:
            self.access_control_allow_internal = access_control_allow_internal
        if access_control_allow_external is not None:
            self.access_control_allow_external = access_control_allow_external
        if body is not None:
            self.body = body

    @property
    def access_control_allow_internal(self):
        r"""Gets the access_control_allow_internal of this CreateOttChannelInfoRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-Internal访问服务。

        :return: The access_control_allow_internal of this CreateOttChannelInfoRequest.
        :rtype: str
        """
        return self._access_control_allow_internal

    @access_control_allow_internal.setter
    def access_control_allow_internal(self, access_control_allow_internal):
        r"""Sets the access_control_allow_internal of this CreateOttChannelInfoRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-Internal访问服务。

        :param access_control_allow_internal: The access_control_allow_internal of this CreateOttChannelInfoRequest.
        :type access_control_allow_internal: str
        """
        self._access_control_allow_internal = access_control_allow_internal

    @property
    def access_control_allow_external(self):
        r"""Gets the access_control_allow_external of this CreateOttChannelInfoRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-External访问服务。

        :return: The access_control_allow_external of this CreateOttChannelInfoRequest.
        :rtype: str
        """
        return self._access_control_allow_external

    @access_control_allow_external.setter
    def access_control_allow_external(self, access_control_allow_external):
        r"""Sets the access_control_allow_external of this CreateOttChannelInfoRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-External访问服务。

        :param access_control_allow_external: The access_control_allow_external of this CreateOttChannelInfoRequest.
        :type access_control_allow_external: str
        """
        self._access_control_allow_external = access_control_allow_external

    @property
    def body(self):
        r"""Gets the body of this CreateOttChannelInfoRequest.

        :return: The body of this CreateOttChannelInfoRequest.
        :rtype: :class:`huaweicloudsdklive.v1.CreateOttChannelInfoReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateOttChannelInfoRequest.

        :param body: The body of this CreateOttChannelInfoRequest.
        :type body: :class:`huaweicloudsdklive.v1.CreateOttChannelInfoReq`
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
        if not isinstance(other, CreateOttChannelInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
