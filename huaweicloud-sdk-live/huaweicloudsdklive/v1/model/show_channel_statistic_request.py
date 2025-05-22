# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowChannelStatisticRequest:

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
        'limit': 'int',
        'offset': 'int',
        'body': 'ShowChannelStatisticReq'
    }

    attribute_map = {
        'access_control_allow_internal': 'Access-Control-Allow-Internal',
        'access_control_allow_external': 'Access-Control-Allow-External',
        'limit': 'limit',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, access_control_allow_internal=None, access_control_allow_external=None, limit=None, offset=None, body=None):
        r"""ShowChannelStatisticRequest

        The model defined in huaweicloud sdk

        :param access_control_allow_internal: 服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-Internal访问服务。
        :type access_control_allow_internal: str
        :param access_control_allow_external: 服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-External访问服务。
        :type access_control_allow_external: str
        :param limit: 每页记录数，取值范围[1,100]，默认值10。
        :type limit: int
        :param offset: 偏移量。表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param body: Body of the ShowChannelStatisticRequest
        :type body: :class:`huaweicloudsdklive.v1.ShowChannelStatisticReq`
        """
        
        

        self._access_control_allow_internal = None
        self._access_control_allow_external = None
        self._limit = None
        self._offset = None
        self._body = None
        self.discriminator = None

        if access_control_allow_internal is not None:
            self.access_control_allow_internal = access_control_allow_internal
        if access_control_allow_external is not None:
            self.access_control_allow_external = access_control_allow_external
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if body is not None:
            self.body = body

    @property
    def access_control_allow_internal(self):
        r"""Gets the access_control_allow_internal of this ShowChannelStatisticRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-Internal访问服务。

        :return: The access_control_allow_internal of this ShowChannelStatisticRequest.
        :rtype: str
        """
        return self._access_control_allow_internal

    @access_control_allow_internal.setter
    def access_control_allow_internal(self, access_control_allow_internal):
        r"""Sets the access_control_allow_internal of this ShowChannelStatisticRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-Internal访问服务。

        :param access_control_allow_internal: The access_control_allow_internal of this ShowChannelStatisticRequest.
        :type access_control_allow_internal: str
        """
        self._access_control_allow_internal = access_control_allow_internal

    @property
    def access_control_allow_external(self):
        r"""Gets the access_control_allow_external of this ShowChannelStatisticRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-External访问服务。

        :return: The access_control_allow_external of this ShowChannelStatisticRequest.
        :rtype: str
        """
        return self._access_control_allow_external

    @access_control_allow_external.setter
    def access_control_allow_external(self, access_control_allow_external):
        r"""Sets the access_control_allow_external of this ShowChannelStatisticRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-External访问服务。

        :param access_control_allow_external: The access_control_allow_external of this ShowChannelStatisticRequest.
        :type access_control_allow_external: str
        """
        self._access_control_allow_external = access_control_allow_external

    @property
    def limit(self):
        r"""Gets the limit of this ShowChannelStatisticRequest.

        每页记录数，取值范围[1,100]，默认值10。

        :return: The limit of this ShowChannelStatisticRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowChannelStatisticRequest.

        每页记录数，取值范围[1,100]，默认值10。

        :param limit: The limit of this ShowChannelStatisticRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowChannelStatisticRequest.

        偏移量。表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ShowChannelStatisticRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowChannelStatisticRequest.

        偏移量。表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ShowChannelStatisticRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def body(self):
        r"""Gets the body of this ShowChannelStatisticRequest.

        :return: The body of this ShowChannelStatisticRequest.
        :rtype: :class:`huaweicloudsdklive.v1.ShowChannelStatisticReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ShowChannelStatisticRequest.

        :param body: The body of this ShowChannelStatisticRequest.
        :type body: :class:`huaweicloudsdklive.v1.ShowChannelStatisticReq`
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
        if not isinstance(other, ShowChannelStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
