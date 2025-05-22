# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMemberHealthCheckJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'member_check': 'MemberCheckJob',
        'request_id': 'str'
    }

    attribute_map = {
        'member_check': 'member_check',
        'request_id': 'request_id'
    }

    def __init__(self, member_check=None, request_id=None):
        r"""CreateMemberHealthCheckJobResponse

        The model defined in huaweicloud sdk

        :param member_check: 
        :type member_check: :class:`huaweicloudsdkelb.v3.MemberCheckJob`
        :param request_id: 参数解释：请求ID。  注：自动生成 。
        :type request_id: str
        """
        
        super(CreateMemberHealthCheckJobResponse, self).__init__()

        self._member_check = None
        self._request_id = None
        self.discriminator = None

        if member_check is not None:
            self.member_check = member_check
        if request_id is not None:
            self.request_id = request_id

    @property
    def member_check(self):
        r"""Gets the member_check of this CreateMemberHealthCheckJobResponse.

        :return: The member_check of this CreateMemberHealthCheckJobResponse.
        :rtype: :class:`huaweicloudsdkelb.v3.MemberCheckJob`
        """
        return self._member_check

    @member_check.setter
    def member_check(self, member_check):
        r"""Sets the member_check of this CreateMemberHealthCheckJobResponse.

        :param member_check: The member_check of this CreateMemberHealthCheckJobResponse.
        :type member_check: :class:`huaweicloudsdkelb.v3.MemberCheckJob`
        """
        self._member_check = member_check

    @property
    def request_id(self):
        r"""Gets the request_id of this CreateMemberHealthCheckJobResponse.

        参数解释：请求ID。  注：自动生成 。

        :return: The request_id of this CreateMemberHealthCheckJobResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CreateMemberHealthCheckJobResponse.

        参数解释：请求ID。  注：自动生成 。

        :param request_id: The request_id of this CreateMemberHealthCheckJobResponse.
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
        if not isinstance(other, CreateMemberHealthCheckJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
