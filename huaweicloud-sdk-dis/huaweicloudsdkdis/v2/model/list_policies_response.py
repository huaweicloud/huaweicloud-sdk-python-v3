# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_id': 'str',
        'rules': 'list[PrincipalRule]'
    }

    attribute_map = {
        'stream_id': 'stream_id',
        'rules': 'rules'
    }

    def __init__(self, stream_id=None, rules=None):
        r"""ListPoliciesResponse

        The model defined in huaweicloud sdk

        :param stream_id: 通道唯一标识符。
        :type stream_id: str
        :param rules: 通道授权信息列表。
        :type rules: list[:class:`huaweicloudsdkdis.v2.PrincipalRule`]
        """
        
        super(ListPoliciesResponse, self).__init__()

        self._stream_id = None
        self._rules = None
        self.discriminator = None

        if stream_id is not None:
            self.stream_id = stream_id
        if rules is not None:
            self.rules = rules

    @property
    def stream_id(self):
        r"""Gets the stream_id of this ListPoliciesResponse.

        通道唯一标识符。

        :return: The stream_id of this ListPoliciesResponse.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this ListPoliciesResponse.

        通道唯一标识符。

        :param stream_id: The stream_id of this ListPoliciesResponse.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def rules(self):
        r"""Gets the rules of this ListPoliciesResponse.

        通道授权信息列表。

        :return: The rules of this ListPoliciesResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.PrincipalRule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ListPoliciesResponse.

        通道授权信息列表。

        :param rules: The rules of this ListPoliciesResponse.
        :type rules: list[:class:`huaweicloudsdkdis.v2.PrincipalRule`]
        """
        self._rules = rules

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
        if not isinstance(other, ListPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
