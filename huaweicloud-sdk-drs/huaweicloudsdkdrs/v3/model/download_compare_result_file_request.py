# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadCompareResultFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'job_id': 'str',
        'compare_type': 'str',
        'compare_job_id': 'str',
        'region': 'str',
        'body': 'ExportCompareResultReq'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_id': 'job_id',
        'compare_type': 'compare_type',
        'compare_job_id': 'compare_job_id',
        'region': 'Region',
        'body': 'body'
    }

    def __init__(self, x_language=None, job_id=None, compare_type=None, compare_job_id=None, region=None, body=None):
        r"""DownloadCompareResultFileRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param job_id: 任务ID。
        :type job_id: str
        :param compare_type: 对比任务类型： - contents： 内容对比。 - lines：行数对比。 - random：抽样对比。 - objects_comparison：对象对比。 - repair_data：数据修复。
        :type compare_type: str
        :param compare_job_id: 对比任务的ID，内容对比、抽样对比、行数对比场景必填。
        :type compare_job_id: str
        :param region: 区域ID，例如：cn-north-4。
        :type region: str
        :param body: Body of the DownloadCompareResultFileRequest
        :type body: :class:`huaweicloudsdkdrs.v3.ExportCompareResultReq`
        """
        
        

        self._x_language = None
        self._job_id = None
        self._compare_type = None
        self._compare_job_id = None
        self._region = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_id = job_id
        if compare_type is not None:
            self.compare_type = compare_type
        if compare_job_id is not None:
            self.compare_job_id = compare_job_id
        if region is not None:
            self.region = region
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this DownloadCompareResultFileRequest.

        请求语言类型。

        :return: The x_language of this DownloadCompareResultFileRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this DownloadCompareResultFileRequest.

        请求语言类型。

        :param x_language: The x_language of this DownloadCompareResultFileRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_id(self):
        r"""Gets the job_id of this DownloadCompareResultFileRequest.

        任务ID。

        :return: The job_id of this DownloadCompareResultFileRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DownloadCompareResultFileRequest.

        任务ID。

        :param job_id: The job_id of this DownloadCompareResultFileRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def compare_type(self):
        r"""Gets the compare_type of this DownloadCompareResultFileRequest.

        对比任务类型： - contents： 内容对比。 - lines：行数对比。 - random：抽样对比。 - objects_comparison：对象对比。 - repair_data：数据修复。

        :return: The compare_type of this DownloadCompareResultFileRequest.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this DownloadCompareResultFileRequest.

        对比任务类型： - contents： 内容对比。 - lines：行数对比。 - random：抽样对比。 - objects_comparison：对象对比。 - repair_data：数据修复。

        :param compare_type: The compare_type of this DownloadCompareResultFileRequest.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def compare_job_id(self):
        r"""Gets the compare_job_id of this DownloadCompareResultFileRequest.

        对比任务的ID，内容对比、抽样对比、行数对比场景必填。

        :return: The compare_job_id of this DownloadCompareResultFileRequest.
        :rtype: str
        """
        return self._compare_job_id

    @compare_job_id.setter
    def compare_job_id(self, compare_job_id):
        r"""Sets the compare_job_id of this DownloadCompareResultFileRequest.

        对比任务的ID，内容对比、抽样对比、行数对比场景必填。

        :param compare_job_id: The compare_job_id of this DownloadCompareResultFileRequest.
        :type compare_job_id: str
        """
        self._compare_job_id = compare_job_id

    @property
    def region(self):
        r"""Gets the region of this DownloadCompareResultFileRequest.

        区域ID，例如：cn-north-4。

        :return: The region of this DownloadCompareResultFileRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DownloadCompareResultFileRequest.

        区域ID，例如：cn-north-4。

        :param region: The region of this DownloadCompareResultFileRequest.
        :type region: str
        """
        self._region = region

    @property
    def body(self):
        r"""Gets the body of this DownloadCompareResultFileRequest.

        :return: The body of this DownloadCompareResultFileRequest.
        :rtype: :class:`huaweicloudsdkdrs.v3.ExportCompareResultReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DownloadCompareResultFileRequest.

        :param body: The body of this DownloadCompareResultFileRequest.
        :type body: :class:`huaweicloudsdkdrs.v3.ExportCompareResultReq`
        """
        self._body = body

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
        if not isinstance(other, DownloadCompareResultFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
