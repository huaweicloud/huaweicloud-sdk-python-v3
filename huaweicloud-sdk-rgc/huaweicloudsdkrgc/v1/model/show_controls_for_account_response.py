# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowControlsForAccountResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'control': 'EnabledControl',
        'regions': 'list[RegionConfigurationList]',
        'state': 'str',
        'message': 'str',
        'version': 'str'
    }

    attribute_map = {
        'control': 'control',
        'regions': 'regions',
        'state': 'state',
        'message': 'message',
        'version': 'version'
    }

    def __init__(self, control=None, regions=None, state=None, message=None, version=None):
        r"""ShowControlsForAccountResponse

        The model defined in huaweicloud sdk

        :param control: 
        :type control: :class:`huaweicloudsdkrgc.v1.EnabledControl`
        :param regions: 区域信息。
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        :param state: 状态。
        :type state: str
        :param message: 状态说明。
        :type message: str
        :param version: 控制策略当前版本。
        :type version: str
        """
        
        super(ShowControlsForAccountResponse, self).__init__()

        self._control = None
        self._regions = None
        self._state = None
        self._message = None
        self._version = None
        self.discriminator = None

        if control is not None:
            self.control = control
        if regions is not None:
            self.regions = regions
        if state is not None:
            self.state = state
        if message is not None:
            self.message = message
        if version is not None:
            self.version = version

    @property
    def control(self):
        r"""Gets the control of this ShowControlsForAccountResponse.

        :return: The control of this ShowControlsForAccountResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.EnabledControl`
        """
        return self._control

    @control.setter
    def control(self, control):
        r"""Sets the control of this ShowControlsForAccountResponse.

        :param control: The control of this ShowControlsForAccountResponse.
        :type control: :class:`huaweicloudsdkrgc.v1.EnabledControl`
        """
        self._control = control

    @property
    def regions(self):
        r"""Gets the regions of this ShowControlsForAccountResponse.

        区域信息。

        :return: The regions of this ShowControlsForAccountResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this ShowControlsForAccountResponse.

        区域信息。

        :param regions: The regions of this ShowControlsForAccountResponse.
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        self._regions = regions

    @property
    def state(self):
        r"""Gets the state of this ShowControlsForAccountResponse.

        状态。

        :return: The state of this ShowControlsForAccountResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowControlsForAccountResponse.

        状态。

        :param state: The state of this ShowControlsForAccountResponse.
        :type state: str
        """
        self._state = state

    @property
    def message(self):
        r"""Gets the message of this ShowControlsForAccountResponse.

        状态说明。

        :return: The message of this ShowControlsForAccountResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowControlsForAccountResponse.

        状态说明。

        :param message: The message of this ShowControlsForAccountResponse.
        :type message: str
        """
        self._message = message

    @property
    def version(self):
        r"""Gets the version of this ShowControlsForAccountResponse.

        控制策略当前版本。

        :return: The version of this ShowControlsForAccountResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowControlsForAccountResponse.

        控制策略当前版本。

        :param version: The version of this ShowControlsForAccountResponse.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ShowControlsForAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
