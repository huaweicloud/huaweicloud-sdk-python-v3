# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityGroupResponse(SdkResponse):

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
        'security_group': 'SecurityGroupInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'security_group': 'security_group'
    }

    def __init__(self, request_id=None, security_group=None):
        """UpdateSecurityGroupResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param security_group: 
        :type security_group: :class:`huaweicloudsdkvpc.v3.SecurityGroupInfo`
        """
        
        super(UpdateSecurityGroupResponse, self).__init__()

        self._request_id = None
        self._security_group = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if security_group is not None:
            self.security_group = security_group

    @property
    def request_id(self):
        """Gets the request_id of this UpdateSecurityGroupResponse.

        请求ID

        :return: The request_id of this UpdateSecurityGroupResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateSecurityGroupResponse.

        请求ID

        :param request_id: The request_id of this UpdateSecurityGroupResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def security_group(self):
        """Gets the security_group of this UpdateSecurityGroupResponse.


        :return: The security_group of this UpdateSecurityGroupResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.SecurityGroupInfo`
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        """Sets the security_group of this UpdateSecurityGroupResponse.


        :param security_group: The security_group of this UpdateSecurityGroupResponse.
        :type security_group: :class:`huaweicloudsdkvpc.v3.SecurityGroupInfo`
        """
        self._security_group = security_group

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
        if not isinstance(other, UpdateSecurityGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
