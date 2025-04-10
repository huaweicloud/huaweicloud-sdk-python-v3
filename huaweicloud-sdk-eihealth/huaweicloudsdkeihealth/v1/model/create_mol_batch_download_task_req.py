# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMolBatchDownloadTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'job_result_url': 'str',
        'mode': 'str',
        'selected': 'list[int]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_result_url': 'job_result_url',
        'mode': 'mode',
        'selected': 'selected'
    }

    def __init__(self, job_id=None, job_result_url=None, mode=None, selected=None):
        r"""CreateMolBatchDownloadTaskReq

        The model defined in huaweicloud sdk

        :param job_id: 作业ID
        :type job_id: str
        :param job_result_url: 作业结果文件url
        :type job_result_url: str
        :param mode: 下载类型：MOL（小分子）、COMPLEX（复合物）
        :type mode: str
        :param selected: 选中下载的分子下标
        :type selected: list[int]
        """
        
        

        self._job_id = None
        self._job_result_url = None
        self._mode = None
        self._selected = None
        self.discriminator = None

        self.job_id = job_id
        self.job_result_url = job_result_url
        self.mode = mode
        self.selected = selected

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateMolBatchDownloadTaskReq.

        作业ID

        :return: The job_id of this CreateMolBatchDownloadTaskReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateMolBatchDownloadTaskReq.

        作业ID

        :param job_id: The job_id of this CreateMolBatchDownloadTaskReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_result_url(self):
        r"""Gets the job_result_url of this CreateMolBatchDownloadTaskReq.

        作业结果文件url

        :return: The job_result_url of this CreateMolBatchDownloadTaskReq.
        :rtype: str
        """
        return self._job_result_url

    @job_result_url.setter
    def job_result_url(self, job_result_url):
        r"""Sets the job_result_url of this CreateMolBatchDownloadTaskReq.

        作业结果文件url

        :param job_result_url: The job_result_url of this CreateMolBatchDownloadTaskReq.
        :type job_result_url: str
        """
        self._job_result_url = job_result_url

    @property
    def mode(self):
        r"""Gets the mode of this CreateMolBatchDownloadTaskReq.

        下载类型：MOL（小分子）、COMPLEX（复合物）

        :return: The mode of this CreateMolBatchDownloadTaskReq.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateMolBatchDownloadTaskReq.

        下载类型：MOL（小分子）、COMPLEX（复合物）

        :param mode: The mode of this CreateMolBatchDownloadTaskReq.
        :type mode: str
        """
        self._mode = mode

    @property
    def selected(self):
        r"""Gets the selected of this CreateMolBatchDownloadTaskReq.

        选中下载的分子下标

        :return: The selected of this CreateMolBatchDownloadTaskReq.
        :rtype: list[int]
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        r"""Sets the selected of this CreateMolBatchDownloadTaskReq.

        选中下载的分子下标

        :param selected: The selected of this CreateMolBatchDownloadTaskReq.
        :type selected: list[int]
        """
        self._selected = selected

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
        if not isinstance(other, CreateMolBatchDownloadTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
