# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowControlOperateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'control_operation': 'ControlOperation'
    }

    attribute_map = {
        'control_operation': 'control_operation'
    }

    def __init__(self, control_operation=None):
        r"""ShowControlOperateResponse

        The model defined in huaweicloud sdk

        :param control_operation: 
        :type control_operation: :class:`huaweicloudsdkrgc.v1.ControlOperation`
        """
        
        super(ShowControlOperateResponse, self).__init__()

        self._control_operation = None
        self.discriminator = None

        if control_operation is not None:
            self.control_operation = control_operation

    @property
    def control_operation(self):
        r"""Gets the control_operation of this ShowControlOperateResponse.

        :return: The control_operation of this ShowControlOperateResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.ControlOperation`
        """
        return self._control_operation

    @control_operation.setter
    def control_operation(self, control_operation):
        r"""Sets the control_operation of this ShowControlOperateResponse.

        :param control_operation: The control_operation of this ShowControlOperateResponse.
        :type control_operation: :class:`huaweicloudsdkrgc.v1.ControlOperation`
        """
        self._control_operation = control_operation

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
        if not isinstance(other, ShowControlOperateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
