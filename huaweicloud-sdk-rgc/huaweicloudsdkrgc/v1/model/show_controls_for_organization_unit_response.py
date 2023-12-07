# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowControlsForOrganizationUnitResponse(SdkResponse):

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
        'regions': 'list[str]',
        'state': 'str',
        'state_message': 'str',
        'version': 'str'
    }

    attribute_map = {
        'control': 'control',
        'regions': 'regions',
        'state': 'state',
        'state_message': 'state_message',
        'version': 'version'
    }

    def __init__(self, control=None, regions=None, state=None, state_message=None, version=None):
        """ShowControlsForOrganizationUnitResponse

        The model defined in huaweicloud sdk

        :param control: 
        :type control: :class:`huaweicloudsdkrgc.v1.EnabledControl`
        :param regions: 开启的区域。
        :type regions: list[str]
        :param state: 是否允许启用控制策略。
        :type state: str
        :param state_message: 状态说明。
        :type state_message: str
        :param version: 控制策略当前版本。
        :type version: str
        """
        
        super(ShowControlsForOrganizationUnitResponse, self).__init__()

        self._control = None
        self._regions = None
        self._state = None
        self._state_message = None
        self._version = None
        self.discriminator = None

        if control is not None:
            self.control = control
        if regions is not None:
            self.regions = regions
        if state is not None:
            self.state = state
        if state_message is not None:
            self.state_message = state_message
        if version is not None:
            self.version = version

    @property
    def control(self):
        """Gets the control of this ShowControlsForOrganizationUnitResponse.

        :return: The control of this ShowControlsForOrganizationUnitResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.EnabledControl`
        """
        return self._control

    @control.setter
    def control(self, control):
        """Sets the control of this ShowControlsForOrganizationUnitResponse.

        :param control: The control of this ShowControlsForOrganizationUnitResponse.
        :type control: :class:`huaweicloudsdkrgc.v1.EnabledControl`
        """
        self._control = control

    @property
    def regions(self):
        """Gets the regions of this ShowControlsForOrganizationUnitResponse.

        开启的区域。

        :return: The regions of this ShowControlsForOrganizationUnitResponse.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ShowControlsForOrganizationUnitResponse.

        开启的区域。

        :param regions: The regions of this ShowControlsForOrganizationUnitResponse.
        :type regions: list[str]
        """
        self._regions = regions

    @property
    def state(self):
        """Gets the state of this ShowControlsForOrganizationUnitResponse.

        是否允许启用控制策略。

        :return: The state of this ShowControlsForOrganizationUnitResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowControlsForOrganizationUnitResponse.

        是否允许启用控制策略。

        :param state: The state of this ShowControlsForOrganizationUnitResponse.
        :type state: str
        """
        self._state = state

    @property
    def state_message(self):
        """Gets the state_message of this ShowControlsForOrganizationUnitResponse.

        状态说明。

        :return: The state_message of this ShowControlsForOrganizationUnitResponse.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """Sets the state_message of this ShowControlsForOrganizationUnitResponse.

        状态说明。

        :param state_message: The state_message of this ShowControlsForOrganizationUnitResponse.
        :type state_message: str
        """
        self._state_message = state_message

    @property
    def version(self):
        """Gets the version of this ShowControlsForOrganizationUnitResponse.

        控制策略当前版本。

        :return: The version of this ShowControlsForOrganizationUnitResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowControlsForOrganizationUnitResponse.

        控制策略当前版本。

        :param version: The version of this ShowControlsForOrganizationUnitResponse.
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
        if not isinstance(other, ShowControlsForOrganizationUnitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
