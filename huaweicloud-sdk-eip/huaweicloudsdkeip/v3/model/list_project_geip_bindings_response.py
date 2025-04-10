# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectGeipBindingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'geip_bindings': 'list[GeipBindingsInternalResp]',
        'request_id': 'str'
    }

    attribute_map = {
        'geip_bindings': 'geip_bindings',
        'request_id': 'request_id'
    }

    def __init__(self, geip_bindings=None, request_id=None):
        r"""ListProjectGeipBindingsResponse

        The model defined in huaweicloud sdk

        :param geip_bindings: geip绑定关系对象
        :type geip_bindings: list[:class:`huaweicloudsdkeip.v3.GeipBindingsInternalResp`]
        :param request_id: 本次请求编号
        :type request_id: str
        """
        
        super(ListProjectGeipBindingsResponse, self).__init__()

        self._geip_bindings = None
        self._request_id = None
        self.discriminator = None

        if geip_bindings is not None:
            self.geip_bindings = geip_bindings
        if request_id is not None:
            self.request_id = request_id

    @property
    def geip_bindings(self):
        r"""Gets the geip_bindings of this ListProjectGeipBindingsResponse.

        geip绑定关系对象

        :return: The geip_bindings of this ListProjectGeipBindingsResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v3.GeipBindingsInternalResp`]
        """
        return self._geip_bindings

    @geip_bindings.setter
    def geip_bindings(self, geip_bindings):
        r"""Sets the geip_bindings of this ListProjectGeipBindingsResponse.

        geip绑定关系对象

        :param geip_bindings: The geip_bindings of this ListProjectGeipBindingsResponse.
        :type geip_bindings: list[:class:`huaweicloudsdkeip.v3.GeipBindingsInternalResp`]
        """
        self._geip_bindings = geip_bindings

    @property
    def request_id(self):
        r"""Gets the request_id of this ListProjectGeipBindingsResponse.

        本次请求编号

        :return: The request_id of this ListProjectGeipBindingsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListProjectGeipBindingsResponse.

        本次请求编号

        :param request_id: The request_id of this ListProjectGeipBindingsResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListProjectGeipBindingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
