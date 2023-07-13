# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNextflowResponse(SdkResponse):

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
        'workspace': 'int',
        'status': 'str',
        'progress': 'float',
        'failed_reason': 'str',
        'cache_status': 'str'
    }

    attribute_map = {
        'version': 'version',
        'workspace': 'workspace',
        'status': 'status',
        'progress': 'progress',
        'failed_reason': 'failed_reason',
        'cache_status': 'cache_status'
    }

    def __init__(self, version=None, workspace=None, status=None, progress=None, failed_reason=None, cache_status=None):
        """ShowNextflowResponse

        The model defined in huaweicloud sdk

        :param version: 引擎版本号
        :type version: str
        :param workspace: 用作路径用量，单位：byte
        :type workspace: int
        :param status: 状态
        :type status: str
        :param progress: 进度
        :type progress: float
        :param failed_reason: 失败原因
        :type failed_reason: str
        :param cache_status: 缓存清理状态
        :type cache_status: str
        """
        
        super(ShowNextflowResponse, self).__init__()

        self._version = None
        self._workspace = None
        self._status = None
        self._progress = None
        self._failed_reason = None
        self._cache_status = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if workspace is not None:
            self.workspace = workspace
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if cache_status is not None:
            self.cache_status = cache_status

    @property
    def version(self):
        """Gets the version of this ShowNextflowResponse.

        引擎版本号

        :return: The version of this ShowNextflowResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowNextflowResponse.

        引擎版本号

        :param version: The version of this ShowNextflowResponse.
        :type version: str
        """
        self._version = version

    @property
    def workspace(self):
        """Gets the workspace of this ShowNextflowResponse.

        用作路径用量，单位：byte

        :return: The workspace of this ShowNextflowResponse.
        :rtype: int
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowNextflowResponse.

        用作路径用量，单位：byte

        :param workspace: The workspace of this ShowNextflowResponse.
        :type workspace: int
        """
        self._workspace = workspace

    @property
    def status(self):
        """Gets the status of this ShowNextflowResponse.

        状态

        :return: The status of this ShowNextflowResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowNextflowResponse.

        状态

        :param status: The status of this ShowNextflowResponse.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        """Gets the progress of this ShowNextflowResponse.

        进度

        :return: The progress of this ShowNextflowResponse.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowNextflowResponse.

        进度

        :param progress: The progress of this ShowNextflowResponse.
        :type progress: float
        """
        self._progress = progress

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ShowNextflowResponse.

        失败原因

        :return: The failed_reason of this ShowNextflowResponse.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ShowNextflowResponse.

        失败原因

        :param failed_reason: The failed_reason of this ShowNextflowResponse.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def cache_status(self):
        """Gets the cache_status of this ShowNextflowResponse.

        缓存清理状态

        :return: The cache_status of this ShowNextflowResponse.
        :rtype: str
        """
        return self._cache_status

    @cache_status.setter
    def cache_status(self, cache_status):
        """Sets the cache_status of this ShowNextflowResponse.

        缓存清理状态

        :param cache_status: The cache_status of this ShowNextflowResponse.
        :type cache_status: str
        """
        self._cache_status = cache_status

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
        if not isinstance(other, ShowNextflowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
