# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIpListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ipgroup_id': 'str',
        'body': 'UpdateIpListRequestBody'
    }

    attribute_map = {
        'ipgroup_id': 'ipgroup_id',
        'body': 'body'
    }

    def __init__(self, ipgroup_id=None, body=None):
        r"""UpdateIpListRequest

        The model defined in huaweicloud sdk

        :param ipgroup_id: 参数解释：IP地址组ID。
        :type ipgroup_id: str
        :param body: Body of the UpdateIpListRequest
        :type body: :class:`huaweicloudsdkelb.v3.UpdateIpListRequestBody`
        """
        
        

        self._ipgroup_id = None
        self._body = None
        self.discriminator = None

        self.ipgroup_id = ipgroup_id
        if body is not None:
            self.body = body

    @property
    def ipgroup_id(self):
        r"""Gets the ipgroup_id of this UpdateIpListRequest.

        参数解释：IP地址组ID。

        :return: The ipgroup_id of this UpdateIpListRequest.
        :rtype: str
        """
        return self._ipgroup_id

    @ipgroup_id.setter
    def ipgroup_id(self, ipgroup_id):
        r"""Sets the ipgroup_id of this UpdateIpListRequest.

        参数解释：IP地址组ID。

        :param ipgroup_id: The ipgroup_id of this UpdateIpListRequest.
        :type ipgroup_id: str
        """
        self._ipgroup_id = ipgroup_id

    @property
    def body(self):
        r"""Gets the body of this UpdateIpListRequest.

        :return: The body of this UpdateIpListRequest.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateIpListRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateIpListRequest.

        :param body: The body of this UpdateIpListRequest.
        :type body: :class:`huaweicloudsdkelb.v3.UpdateIpListRequestBody`
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
        if not isinstance(other, UpdateIpListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
