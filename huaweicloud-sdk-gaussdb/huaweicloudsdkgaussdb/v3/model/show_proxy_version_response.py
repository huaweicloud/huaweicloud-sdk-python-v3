# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProxyVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_version': 'str',
        'latest_version': 'str',
        'can_upgrade': 'bool'
    }

    attribute_map = {
        'current_version': 'current_version',
        'latest_version': 'latest_version',
        'can_upgrade': 'can_upgrade'
    }

    def __init__(self, current_version=None, latest_version=None, can_upgrade=None):
        """ShowProxyVersionResponse

        The model defined in huaweicloud sdk

        :param current_version: 当前代理版本
        :type current_version: str
        :param latest_version: 最新代理版本
        :type latest_version: str
        :param can_upgrade: 是否能升级
        :type can_upgrade: bool
        """
        
        super(ShowProxyVersionResponse, self).__init__()

        self._current_version = None
        self._latest_version = None
        self._can_upgrade = None
        self.discriminator = None

        if current_version is not None:
            self.current_version = current_version
        if latest_version is not None:
            self.latest_version = latest_version
        if can_upgrade is not None:
            self.can_upgrade = can_upgrade

    @property
    def current_version(self):
        """Gets the current_version of this ShowProxyVersionResponse.

        当前代理版本

        :return: The current_version of this ShowProxyVersionResponse.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this ShowProxyVersionResponse.

        当前代理版本

        :param current_version: The current_version of this ShowProxyVersionResponse.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def latest_version(self):
        """Gets the latest_version of this ShowProxyVersionResponse.

        最新代理版本

        :return: The latest_version of this ShowProxyVersionResponse.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this ShowProxyVersionResponse.

        最新代理版本

        :param latest_version: The latest_version of this ShowProxyVersionResponse.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def can_upgrade(self):
        """Gets the can_upgrade of this ShowProxyVersionResponse.

        是否能升级

        :return: The can_upgrade of this ShowProxyVersionResponse.
        :rtype: bool
        """
        return self._can_upgrade

    @can_upgrade.setter
    def can_upgrade(self, can_upgrade):
        """Sets the can_upgrade of this ShowProxyVersionResponse.

        是否能升级

        :param can_upgrade: The can_upgrade of this ShowProxyVersionResponse.
        :type can_upgrade: bool
        """
        self._can_upgrade = can_upgrade

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
        if not isinstance(other, ShowProxyVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
