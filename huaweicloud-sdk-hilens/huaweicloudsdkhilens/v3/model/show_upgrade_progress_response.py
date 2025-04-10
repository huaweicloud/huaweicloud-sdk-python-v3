# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUpgradeProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'status': 'int',
        'progress': 'str',
        'cause': 'str'
    }

    attribute_map = {
        'version': 'version',
        'status': 'status',
        'progress': 'progress',
        'cause': 'cause'
    }

    def __init__(self, version=None, status=None, progress=None, cause=None):
        r"""ShowUpgradeProgressResponse

        The model defined in huaweicloud sdk

        :param version: 升级的固件版本
        :type version: str
        :param status: 固件升级状态，1:升级中 2:升级失败 3:升级成功
        :type status: int
        :param progress: 固件升级进度，用数字0-100表示
        :type progress: str
        :param cause: 固件升级失败原因
        :type cause: str
        """
        
        super(ShowUpgradeProgressResponse, self).__init__()

        self._version = None
        self._status = None
        self._progress = None
        self._cause = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if cause is not None:
            self.cause = cause

    @property
    def version(self):
        r"""Gets the version of this ShowUpgradeProgressResponse.

        升级的固件版本

        :return: The version of this ShowUpgradeProgressResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowUpgradeProgressResponse.

        升级的固件版本

        :param version: The version of this ShowUpgradeProgressResponse.
        :type version: str
        """
        self._version = version

    @property
    def status(self):
        r"""Gets the status of this ShowUpgradeProgressResponse.

        固件升级状态，1:升级中 2:升级失败 3:升级成功

        :return: The status of this ShowUpgradeProgressResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowUpgradeProgressResponse.

        固件升级状态，1:升级中 2:升级失败 3:升级成功

        :param status: The status of this ShowUpgradeProgressResponse.
        :type status: int
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this ShowUpgradeProgressResponse.

        固件升级进度，用数字0-100表示

        :return: The progress of this ShowUpgradeProgressResponse.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ShowUpgradeProgressResponse.

        固件升级进度，用数字0-100表示

        :param progress: The progress of this ShowUpgradeProgressResponse.
        :type progress: str
        """
        self._progress = progress

    @property
    def cause(self):
        r"""Gets the cause of this ShowUpgradeProgressResponse.

        固件升级失败原因

        :return: The cause of this ShowUpgradeProgressResponse.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        r"""Sets the cause of this ShowUpgradeProgressResponse.

        固件升级失败原因

        :param cause: The cause of this ShowUpgradeProgressResponse.
        :type cause: str
        """
        self._cause = cause

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
        if not isinstance(other, ShowUpgradeProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
