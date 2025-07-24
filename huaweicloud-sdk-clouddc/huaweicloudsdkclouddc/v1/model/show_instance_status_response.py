# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'InstanceState',
        'error': 'ErrorStatus'
    }

    attribute_map = {
        'state': 'state',
        'error': 'error'
    }

    def __init__(self, state=None, error=None):
        r"""ShowInstanceStatusResponse

        The model defined in huaweicloud sdk

        :param state: 
        :type state: :class:`huaweicloudsdkclouddc.v1.InstanceState`
        :param error: 
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        
        super(ShowInstanceStatusResponse, self).__init__()

        self._state = None
        self._error = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if error is not None:
            self.error = error

    @property
    def state(self):
        r"""Gets the state of this ShowInstanceStatusResponse.

        :return: The state of this ShowInstanceStatusResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.InstanceState`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowInstanceStatusResponse.

        :param state: The state of this ShowInstanceStatusResponse.
        :type state: :class:`huaweicloudsdkclouddc.v1.InstanceState`
        """
        self._state = state

    @property
    def error(self):
        r"""Gets the error of this ShowInstanceStatusResponse.

        :return: The error of this ShowInstanceStatusResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ShowInstanceStatusResponse.

        :param error: The error of this ShowInstanceStatusResponse.
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        self._error = error

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
        if not isinstance(other, ShowInstanceStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
