# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAccessAgentLatestVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latest_version': 'str'
    }

    attribute_map = {
        'latest_version': 'latest_version'
    }

    def __init__(self, latest_version=None):
        """ShowAccessAgentLatestVersionResponse

        The model defined in huaweicloud sdk

        :param latest_version: 租户的HDA最新版本。
        :type latest_version: str
        """
        
        super(ShowAccessAgentLatestVersionResponse, self).__init__()

        self._latest_version = None
        self.discriminator = None

        if latest_version is not None:
            self.latest_version = latest_version

    @property
    def latest_version(self):
        """Gets the latest_version of this ShowAccessAgentLatestVersionResponse.

        租户的HDA最新版本。

        :return: The latest_version of this ShowAccessAgentLatestVersionResponse.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this ShowAccessAgentLatestVersionResponse.

        租户的HDA最新版本。

        :param latest_version: The latest_version of this ShowAccessAgentLatestVersionResponse.
        :type latest_version: str
        """
        self._latest_version = latest_version

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
        if not isinstance(other, ShowAccessAgentLatestVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
