# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMolBatchDownloadTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'filename': 'str',
        'out_dir': 'str'
    }

    attribute_map = {
        'status': 'status',
        'filename': 'filename',
        'out_dir': 'out_dir'
    }

    def __init__(self, status=None, filename=None, out_dir=None):
        """ShowMolBatchDownloadTaskResponse

        The model defined in huaweicloud sdk

        :param status: 任务状态：WAITING、RUNNING、FINISHED、CANCELLED、ABNORMAL、FAILED
        :type status: str
        :param filename: 下载文件名
        :type filename: str
        :param out_dir: 下载路径
        :type out_dir: str
        """
        
        super(ShowMolBatchDownloadTaskResponse, self).__init__()

        self._status = None
        self._filename = None
        self._out_dir = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if filename is not None:
            self.filename = filename
        if out_dir is not None:
            self.out_dir = out_dir

    @property
    def status(self):
        """Gets the status of this ShowMolBatchDownloadTaskResponse.

        任务状态：WAITING、RUNNING、FINISHED、CANCELLED、ABNORMAL、FAILED

        :return: The status of this ShowMolBatchDownloadTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowMolBatchDownloadTaskResponse.

        任务状态：WAITING、RUNNING、FINISHED、CANCELLED、ABNORMAL、FAILED

        :param status: The status of this ShowMolBatchDownloadTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def filename(self):
        """Gets the filename of this ShowMolBatchDownloadTaskResponse.

        下载文件名

        :return: The filename of this ShowMolBatchDownloadTaskResponse.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ShowMolBatchDownloadTaskResponse.

        下载文件名

        :param filename: The filename of this ShowMolBatchDownloadTaskResponse.
        :type filename: str
        """
        self._filename = filename

    @property
    def out_dir(self):
        """Gets the out_dir of this ShowMolBatchDownloadTaskResponse.

        下载路径

        :return: The out_dir of this ShowMolBatchDownloadTaskResponse.
        :rtype: str
        """
        return self._out_dir

    @out_dir.setter
    def out_dir(self, out_dir):
        """Sets the out_dir of this ShowMolBatchDownloadTaskResponse.

        下载路径

        :param out_dir: The out_dir of this ShowMolBatchDownloadTaskResponse.
        :type out_dir: str
        """
        self._out_dir = out_dir

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
        if not isinstance(other, ShowMolBatchDownloadTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
