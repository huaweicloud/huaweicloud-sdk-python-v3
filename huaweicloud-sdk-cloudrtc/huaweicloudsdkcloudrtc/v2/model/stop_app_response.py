# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'state': 'AppState',
        'x_request_id': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'state': 'state',
        'x_request_id': 'X-request-Id'
    }

    def __init__(self, app_id=None, state=None, x_request_id=None):
        r"""StopAppResponse

        The model defined in huaweicloud sdk

        :param app_id: 应用id
        :type app_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkcloudrtc.v2.AppState`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(StopAppResponse, self).__init__()

        self._app_id = None
        self._state = None
        self._x_request_id = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if state is not None:
            self.state = state
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def app_id(self):
        r"""Gets the app_id of this StopAppResponse.

        应用id

        :return: The app_id of this StopAppResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this StopAppResponse.

        应用id

        :param app_id: The app_id of this StopAppResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def state(self):
        r"""Gets the state of this StopAppResponse.

        :return: The state of this StopAppResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.AppState`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this StopAppResponse.

        :param state: The state of this StopAppResponse.
        :type state: :class:`huaweicloudsdkcloudrtc.v2.AppState`
        """
        self._state = state

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this StopAppResponse.

        :return: The x_request_id of this StopAppResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this StopAppResponse.

        :param x_request_id: The x_request_id of this StopAppResponse.
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
        if not isinstance(other, StopAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
