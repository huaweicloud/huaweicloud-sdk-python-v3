# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteMembersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'members': 'list[BatchDeleteMembersState]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'members': 'members'
    }

    def __init__(self, request_id=None, members=None):
        r"""BatchDeleteMembersResponse

        The model defined in huaweicloud sdk

        :param request_id: **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        :param members: **参数解释**：后端服务器对象列表。
        :type members: list[:class:`huaweicloudsdkelb.v3.BatchDeleteMembersState`]
        """
        
        super(BatchDeleteMembersResponse, self).__init__()

        self._request_id = None
        self._members = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if members is not None:
            self.members = members

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchDeleteMembersResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this BatchDeleteMembersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchDeleteMembersResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this BatchDeleteMembersResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def members(self):
        r"""Gets the members of this BatchDeleteMembersResponse.

        **参数解释**：后端服务器对象列表。

        :return: The members of this BatchDeleteMembersResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.BatchDeleteMembersState`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this BatchDeleteMembersResponse.

        **参数解释**：后端服务器对象列表。

        :param members: The members of this BatchDeleteMembersResponse.
        :type members: list[:class:`huaweicloudsdkelb.v3.BatchDeleteMembersState`]
        """
        self._members = members

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
        if not isinstance(other, BatchDeleteMembersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
