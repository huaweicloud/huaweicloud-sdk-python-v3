# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccessPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_policy_id': 'str',
        'body': 'UpdateAccessPolicyReq'
    }

    attribute_map = {
        'access_policy_id': 'access_policy_id',
        'body': 'body'
    }

    def __init__(self, access_policy_id=None, body=None):
        r"""UpdateAccessPolicyRequest

        The model defined in huaweicloud sdk

        :param access_policy_id: 接入策略id。
        :type access_policy_id: str
        :param body: Body of the UpdateAccessPolicyRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyReq`
        """
        
        

        self._access_policy_id = None
        self._body = None
        self.discriminator = None

        self.access_policy_id = access_policy_id
        if body is not None:
            self.body = body

    @property
    def access_policy_id(self):
        r"""Gets the access_policy_id of this UpdateAccessPolicyRequest.

        接入策略id。

        :return: The access_policy_id of this UpdateAccessPolicyRequest.
        :rtype: str
        """
        return self._access_policy_id

    @access_policy_id.setter
    def access_policy_id(self, access_policy_id):
        r"""Sets the access_policy_id of this UpdateAccessPolicyRequest.

        接入策略id。

        :param access_policy_id: The access_policy_id of this UpdateAccessPolicyRequest.
        :type access_policy_id: str
        """
        self._access_policy_id = access_policy_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAccessPolicyRequest.

        :return: The body of this UpdateAccessPolicyRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAccessPolicyRequest.

        :param body: The body of this UpdateAccessPolicyRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateAccessPolicyReq`
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
        if not isinstance(other, UpdateAccessPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
