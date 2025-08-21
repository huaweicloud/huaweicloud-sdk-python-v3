# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAvailableUpdatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'baseline_update_available': 'bool',
        'control_update_available': 'bool',
        'landing_zone_update_available': 'bool',
        'service_landing_zone_version': 'str',
        'user_landing_zone_version': 'str'
    }

    attribute_map = {
        'baseline_update_available': 'baseline_update_available',
        'control_update_available': 'control_update_available',
        'landing_zone_update_available': 'landing_zone_update_available',
        'service_landing_zone_version': 'service_landing_zone_version',
        'user_landing_zone_version': 'user_landing_zone_version'
    }

    def __init__(self, baseline_update_available=None, control_update_available=None, landing_zone_update_available=None, service_landing_zone_version=None, user_landing_zone_version=None):
        r"""ShowAvailableUpdatesResponse

        The model defined in huaweicloud sdk

        :param baseline_update_available: 用户当前的Landing Zone版本是否为最新版本。
        :type baseline_update_available: bool
        :param control_update_available: 当前账号下是否有新的控制策略。
        :type control_update_available: bool
        :param landing_zone_update_available: Landing Zone是否可更新。
        :type landing_zone_update_available: bool
        :param service_landing_zone_version: Landing Zone当前最新的版本号。
        :type service_landing_zone_version: str
        :param user_landing_zone_version: 用户当前的Landing Zone版本。
        :type user_landing_zone_version: str
        """
        
        super(ShowAvailableUpdatesResponse, self).__init__()

        self._baseline_update_available = None
        self._control_update_available = None
        self._landing_zone_update_available = None
        self._service_landing_zone_version = None
        self._user_landing_zone_version = None
        self.discriminator = None

        if baseline_update_available is not None:
            self.baseline_update_available = baseline_update_available
        if control_update_available is not None:
            self.control_update_available = control_update_available
        if landing_zone_update_available is not None:
            self.landing_zone_update_available = landing_zone_update_available
        if service_landing_zone_version is not None:
            self.service_landing_zone_version = service_landing_zone_version
        if user_landing_zone_version is not None:
            self.user_landing_zone_version = user_landing_zone_version

    @property
    def baseline_update_available(self):
        r"""Gets the baseline_update_available of this ShowAvailableUpdatesResponse.

        用户当前的Landing Zone版本是否为最新版本。

        :return: The baseline_update_available of this ShowAvailableUpdatesResponse.
        :rtype: bool
        """
        return self._baseline_update_available

    @baseline_update_available.setter
    def baseline_update_available(self, baseline_update_available):
        r"""Sets the baseline_update_available of this ShowAvailableUpdatesResponse.

        用户当前的Landing Zone版本是否为最新版本。

        :param baseline_update_available: The baseline_update_available of this ShowAvailableUpdatesResponse.
        :type baseline_update_available: bool
        """
        self._baseline_update_available = baseline_update_available

    @property
    def control_update_available(self):
        r"""Gets the control_update_available of this ShowAvailableUpdatesResponse.

        当前账号下是否有新的控制策略。

        :return: The control_update_available of this ShowAvailableUpdatesResponse.
        :rtype: bool
        """
        return self._control_update_available

    @control_update_available.setter
    def control_update_available(self, control_update_available):
        r"""Sets the control_update_available of this ShowAvailableUpdatesResponse.

        当前账号下是否有新的控制策略。

        :param control_update_available: The control_update_available of this ShowAvailableUpdatesResponse.
        :type control_update_available: bool
        """
        self._control_update_available = control_update_available

    @property
    def landing_zone_update_available(self):
        r"""Gets the landing_zone_update_available of this ShowAvailableUpdatesResponse.

        Landing Zone是否可更新。

        :return: The landing_zone_update_available of this ShowAvailableUpdatesResponse.
        :rtype: bool
        """
        return self._landing_zone_update_available

    @landing_zone_update_available.setter
    def landing_zone_update_available(self, landing_zone_update_available):
        r"""Sets the landing_zone_update_available of this ShowAvailableUpdatesResponse.

        Landing Zone是否可更新。

        :param landing_zone_update_available: The landing_zone_update_available of this ShowAvailableUpdatesResponse.
        :type landing_zone_update_available: bool
        """
        self._landing_zone_update_available = landing_zone_update_available

    @property
    def service_landing_zone_version(self):
        r"""Gets the service_landing_zone_version of this ShowAvailableUpdatesResponse.

        Landing Zone当前最新的版本号。

        :return: The service_landing_zone_version of this ShowAvailableUpdatesResponse.
        :rtype: str
        """
        return self._service_landing_zone_version

    @service_landing_zone_version.setter
    def service_landing_zone_version(self, service_landing_zone_version):
        r"""Sets the service_landing_zone_version of this ShowAvailableUpdatesResponse.

        Landing Zone当前最新的版本号。

        :param service_landing_zone_version: The service_landing_zone_version of this ShowAvailableUpdatesResponse.
        :type service_landing_zone_version: str
        """
        self._service_landing_zone_version = service_landing_zone_version

    @property
    def user_landing_zone_version(self):
        r"""Gets the user_landing_zone_version of this ShowAvailableUpdatesResponse.

        用户当前的Landing Zone版本。

        :return: The user_landing_zone_version of this ShowAvailableUpdatesResponse.
        :rtype: str
        """
        return self._user_landing_zone_version

    @user_landing_zone_version.setter
    def user_landing_zone_version(self, user_landing_zone_version):
        r"""Sets the user_landing_zone_version of this ShowAvailableUpdatesResponse.

        用户当前的Landing Zone版本。

        :param user_landing_zone_version: The user_landing_zone_version of this ShowAvailableUpdatesResponse.
        :type user_landing_zone_version: str
        """
        self._user_landing_zone_version = user_landing_zone_version

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
        if not isinstance(other, ShowAvailableUpdatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
