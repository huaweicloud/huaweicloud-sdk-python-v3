# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFuncSnapshotStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'code': 'str'
    }

    attribute_map = {
        'state': 'state',
        'code': 'code'
    }

    def __init__(self, state=None, code=None):
        r"""ShowFuncSnapshotStateResponse

        The model defined in huaweicloud sdk

        :param state: 快照制作状态
        :type state: str
        :param code: 快照制作响应码
        :type code: str
        """
        
        super(ShowFuncSnapshotStateResponse, self).__init__()

        self._state = None
        self._code = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if code is not None:
            self.code = code

    @property
    def state(self):
        r"""Gets the state of this ShowFuncSnapshotStateResponse.

        快照制作状态

        :return: The state of this ShowFuncSnapshotStateResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowFuncSnapshotStateResponse.

        快照制作状态

        :param state: The state of this ShowFuncSnapshotStateResponse.
        :type state: str
        """
        self._state = state

    @property
    def code(self):
        r"""Gets the code of this ShowFuncSnapshotStateResponse.

        快照制作响应码

        :return: The code of this ShowFuncSnapshotStateResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowFuncSnapshotStateResponse.

        快照制作响应码

        :param code: The code of this ShowFuncSnapshotStateResponse.
        :type code: str
        """
        self._code = code

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
        if not isinstance(other, ShowFuncSnapshotStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
