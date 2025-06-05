# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterInstallStepResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'installs': 'list[InstallStep]',
        'uninstalls': 'list[InstallStep]'
    }

    attribute_map = {
        'installs': 'installs',
        'uninstalls': 'uninstalls'
    }

    def __init__(self, installs=None, uninstalls=None):
        r"""ListClusterInstallStepResponse

        The model defined in huaweicloud sdk

        :param installs: 安装步骤详情列表。
        :type installs: list[:class:`huaweicloudsdkeihealth.v1.InstallStep`]
        :param uninstalls: 卸载步骤详情列表。
        :type uninstalls: list[:class:`huaweicloudsdkeihealth.v1.InstallStep`]
        """
        
        super(ListClusterInstallStepResponse, self).__init__()

        self._installs = None
        self._uninstalls = None
        self.discriminator = None

        if installs is not None:
            self.installs = installs
        if uninstalls is not None:
            self.uninstalls = uninstalls

    @property
    def installs(self):
        r"""Gets the installs of this ListClusterInstallStepResponse.

        安装步骤详情列表。

        :return: The installs of this ListClusterInstallStepResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.InstallStep`]
        """
        return self._installs

    @installs.setter
    def installs(self, installs):
        r"""Sets the installs of this ListClusterInstallStepResponse.

        安装步骤详情列表。

        :param installs: The installs of this ListClusterInstallStepResponse.
        :type installs: list[:class:`huaweicloudsdkeihealth.v1.InstallStep`]
        """
        self._installs = installs

    @property
    def uninstalls(self):
        r"""Gets the uninstalls of this ListClusterInstallStepResponse.

        卸载步骤详情列表。

        :return: The uninstalls of this ListClusterInstallStepResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.InstallStep`]
        """
        return self._uninstalls

    @uninstalls.setter
    def uninstalls(self, uninstalls):
        r"""Sets the uninstalls of this ListClusterInstallStepResponse.

        卸载步骤详情列表。

        :param uninstalls: The uninstalls of this ListClusterInstallStepResponse.
        :type uninstalls: list[:class:`huaweicloudsdkeihealth.v1.InstallStep`]
        """
        self._uninstalls = uninstalls

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
        if not isinstance(other, ListClusterInstallStepResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
