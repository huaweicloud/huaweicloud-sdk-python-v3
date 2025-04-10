# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rules': 'list[RecordRule]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'rules': 'rules',
        'x_request_id': 'X-request-Id'
    }

    def __init__(self, rules=None, x_request_id=None):
        r"""ListRecordRulesResponse

        The model defined in huaweicloud sdk

        :param rules: 录制规则列表
        :type rules: list[:class:`huaweicloudsdkcloudrtc.v2.RecordRule`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRecordRulesResponse, self).__init__()

        self._rules = None
        self._x_request_id = None
        self.discriminator = None

        if rules is not None:
            self.rules = rules
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def rules(self):
        r"""Gets the rules of this ListRecordRulesResponse.

        录制规则列表

        :return: The rules of this ListRecordRulesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v2.RecordRule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ListRecordRulesResponse.

        录制规则列表

        :param rules: The rules of this ListRecordRulesResponse.
        :type rules: list[:class:`huaweicloudsdkcloudrtc.v2.RecordRule`]
        """
        self._rules = rules

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListRecordRulesResponse.

        :return: The x_request_id of this ListRecordRulesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListRecordRulesResponse.

        :param x_request_id: The x_request_id of this ListRecordRulesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListRecordRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
