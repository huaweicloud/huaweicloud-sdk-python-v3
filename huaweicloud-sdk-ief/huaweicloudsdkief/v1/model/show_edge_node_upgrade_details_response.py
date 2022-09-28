# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEdgeNodeUpgradeDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'upgrade_enable': 'bool',
        'reason': 'str',
        'version': 'str'
    }

    attribute_map = {
        'upgrade_enable': 'upgrade_enable',
        'reason': 'reason',
        'version': 'version'
    }

    def __init__(self, upgrade_enable=None, reason=None, version=None):
        """ShowEdgeNodeUpgradeDetailsResponse

        The model defined in huaweicloud sdk

        :param upgrade_enable: 是否升级成功
        :type upgrade_enable: bool
        :param reason: 未升级成功的原因，若升级成功，返回值为空字符串
        :type reason: str
        :param version: 升级成功后，当前边缘节点的版本
        :type version: str
        """
        
        super(ShowEdgeNodeUpgradeDetailsResponse, self).__init__()

        self._upgrade_enable = None
        self._reason = None
        self._version = None
        self.discriminator = None

        if upgrade_enable is not None:
            self.upgrade_enable = upgrade_enable
        if reason is not None:
            self.reason = reason
        if version is not None:
            self.version = version

    @property
    def upgrade_enable(self):
        """Gets the upgrade_enable of this ShowEdgeNodeUpgradeDetailsResponse.

        是否升级成功

        :return: The upgrade_enable of this ShowEdgeNodeUpgradeDetailsResponse.
        :rtype: bool
        """
        return self._upgrade_enable

    @upgrade_enable.setter
    def upgrade_enable(self, upgrade_enable):
        """Sets the upgrade_enable of this ShowEdgeNodeUpgradeDetailsResponse.

        是否升级成功

        :param upgrade_enable: The upgrade_enable of this ShowEdgeNodeUpgradeDetailsResponse.
        :type upgrade_enable: bool
        """
        self._upgrade_enable = upgrade_enable

    @property
    def reason(self):
        """Gets the reason of this ShowEdgeNodeUpgradeDetailsResponse.

        未升级成功的原因，若升级成功，返回值为空字符串

        :return: The reason of this ShowEdgeNodeUpgradeDetailsResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ShowEdgeNodeUpgradeDetailsResponse.

        未升级成功的原因，若升级成功，返回值为空字符串

        :param reason: The reason of this ShowEdgeNodeUpgradeDetailsResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def version(self):
        """Gets the version of this ShowEdgeNodeUpgradeDetailsResponse.

        升级成功后，当前边缘节点的版本

        :return: The version of this ShowEdgeNodeUpgradeDetailsResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowEdgeNodeUpgradeDetailsResponse.

        升级成功后，当前边缘节点的版本

        :param version: The version of this ShowEdgeNodeUpgradeDetailsResponse.
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
        if not isinstance(other, ShowEdgeNodeUpgradeDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
