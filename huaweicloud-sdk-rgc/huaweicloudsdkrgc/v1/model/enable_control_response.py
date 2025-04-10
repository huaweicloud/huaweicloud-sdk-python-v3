# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableControlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'control_operate_request_id': 'str'
    }

    attribute_map = {
        'control_operate_request_id': 'control_operate_request_id'
    }

    def __init__(self, control_operate_request_id=None):
        r"""EnableControlResponse

        The model defined in huaweicloud sdk

        :param control_operate_request_id: 控制策略的操作ID。
        :type control_operate_request_id: str
        """
        
        super(EnableControlResponse, self).__init__()

        self._control_operate_request_id = None
        self.discriminator = None

        if control_operate_request_id is not None:
            self.control_operate_request_id = control_operate_request_id

    @property
    def control_operate_request_id(self):
        r"""Gets the control_operate_request_id of this EnableControlResponse.

        控制策略的操作ID。

        :return: The control_operate_request_id of this EnableControlResponse.
        :rtype: str
        """
        return self._control_operate_request_id

    @control_operate_request_id.setter
    def control_operate_request_id(self, control_operate_request_id):
        r"""Sets the control_operate_request_id of this EnableControlResponse.

        控制策略的操作ID。

        :param control_operate_request_id: The control_operate_request_id of this EnableControlResponse.
        :type control_operate_request_id: str
        """
        self._control_operate_request_id = control_operate_request_id

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
        if not isinstance(other, EnableControlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
