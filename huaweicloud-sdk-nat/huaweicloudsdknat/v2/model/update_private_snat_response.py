# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrivateSnatResponse(SdkResponse):

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
        'snat_rule': 'PrivateSnat'
    }

    attribute_map = {
        'request_id': 'request_id',
        'snat_rule': 'snat_rule'
    }

    def __init__(self, request_id=None, snat_rule=None):
        """UpdatePrivateSnatResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param snat_rule: 
        :type snat_rule: :class:`huaweicloudsdknat.v2.PrivateSnat`
        """
        
        super(UpdatePrivateSnatResponse, self).__init__()

        self._request_id = None
        self._snat_rule = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if snat_rule is not None:
            self.snat_rule = snat_rule

    @property
    def request_id(self):
        """Gets the request_id of this UpdatePrivateSnatResponse.

        请求ID。

        :return: The request_id of this UpdatePrivateSnatResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdatePrivateSnatResponse.

        请求ID。

        :param request_id: The request_id of this UpdatePrivateSnatResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def snat_rule(self):
        """Gets the snat_rule of this UpdatePrivateSnatResponse.

        :return: The snat_rule of this UpdatePrivateSnatResponse.
        :rtype: :class:`huaweicloudsdknat.v2.PrivateSnat`
        """
        return self._snat_rule

    @snat_rule.setter
    def snat_rule(self, snat_rule):
        """Sets the snat_rule of this UpdatePrivateSnatResponse.

        :param snat_rule: The snat_rule of this UpdatePrivateSnatResponse.
        :type snat_rule: :class:`huaweicloudsdknat.v2.PrivateSnat`
        """
        self._snat_rule = snat_rule

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
        if not isinstance(other, UpdatePrivateSnatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
