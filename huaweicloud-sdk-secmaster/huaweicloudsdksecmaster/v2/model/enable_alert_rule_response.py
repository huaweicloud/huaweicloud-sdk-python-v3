# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableAlertRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fail_list': 'list[AlertRule]',
        'success_list': 'list[AlertRule]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'fail_list': 'fail_list',
        'success_list': 'success_list',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, fail_list=None, success_list=None, x_request_id=None):
        r"""EnableAlertRuleResponse

        The model defined in huaweicloud sdk

        :param fail_list: Alert rule ID.
        :type fail_list: list[:class:`huaweicloudsdksecmaster.v2.AlertRule`]
        :param success_list: Alert rule ID.
        :type success_list: list[:class:`huaweicloudsdksecmaster.v2.AlertRule`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(EnableAlertRuleResponse, self).__init__()

        self._fail_list = None
        self._success_list = None
        self._x_request_id = None
        self.discriminator = None

        if fail_list is not None:
            self.fail_list = fail_list
        if success_list is not None:
            self.success_list = success_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def fail_list(self):
        r"""Gets the fail_list of this EnableAlertRuleResponse.

        Alert rule ID.

        :return: The fail_list of this EnableAlertRuleResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AlertRule`]
        """
        return self._fail_list

    @fail_list.setter
    def fail_list(self, fail_list):
        r"""Sets the fail_list of this EnableAlertRuleResponse.

        Alert rule ID.

        :param fail_list: The fail_list of this EnableAlertRuleResponse.
        :type fail_list: list[:class:`huaweicloudsdksecmaster.v2.AlertRule`]
        """
        self._fail_list = fail_list

    @property
    def success_list(self):
        r"""Gets the success_list of this EnableAlertRuleResponse.

        Alert rule ID.

        :return: The success_list of this EnableAlertRuleResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AlertRule`]
        """
        return self._success_list

    @success_list.setter
    def success_list(self, success_list):
        r"""Sets the success_list of this EnableAlertRuleResponse.

        Alert rule ID.

        :param success_list: The success_list of this EnableAlertRuleResponse.
        :type success_list: list[:class:`huaweicloudsdksecmaster.v2.AlertRule`]
        """
        self._success_list = success_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this EnableAlertRuleResponse.

        :return: The x_request_id of this EnableAlertRuleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this EnableAlertRuleResponse.

        :param x_request_id: The x_request_id of this EnableAlertRuleResponse.
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
        if not isinstance(other, EnableAlertRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
