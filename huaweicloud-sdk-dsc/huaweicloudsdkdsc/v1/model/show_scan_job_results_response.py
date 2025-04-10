# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScanJobResultsResponse(SdkResponse):

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
        'job_name': 'str',
        'type': 'str',
        'db_scan_result': 'DbScanResult',
        'obs_scan_result': 'ObsScanResult',
        'es_scan_result': 'EsScanResult'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'type': 'type',
        'db_scan_result': 'db_scan_result',
        'obs_scan_result': 'obs_scan_result',
        'es_scan_result': 'es_scan_result'
    }

    def __init__(self, job_id=None, job_name=None, type=None, db_scan_result=None, obs_scan_result=None, es_scan_result=None):
        r"""ShowScanJobResultsResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param job_name: 任务名
        :type job_name: str
        :param type: 查询资产类型
        :type type: str
        :param db_scan_result: 
        :type db_scan_result: :class:`huaweicloudsdkdsc.v1.DbScanResult`
        :param obs_scan_result: 
        :type obs_scan_result: :class:`huaweicloudsdkdsc.v1.ObsScanResult`
        :param es_scan_result: 
        :type es_scan_result: :class:`huaweicloudsdkdsc.v1.EsScanResult`
        """
        
        super(ShowScanJobResultsResponse, self).__init__()

        self._job_id = None
        self._job_name = None
        self._type = None
        self._db_scan_result = None
        self._obs_scan_result = None
        self._es_scan_result = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if type is not None:
            self.type = type
        if db_scan_result is not None:
            self.db_scan_result = db_scan_result
        if obs_scan_result is not None:
            self.obs_scan_result = obs_scan_result
        if es_scan_result is not None:
            self.es_scan_result = es_scan_result

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowScanJobResultsResponse.

        任务ID

        :return: The job_id of this ShowScanJobResultsResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowScanJobResultsResponse.

        任务ID

        :param job_id: The job_id of this ShowScanJobResultsResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowScanJobResultsResponse.

        任务名

        :return: The job_name of this ShowScanJobResultsResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowScanJobResultsResponse.

        任务名

        :param job_name: The job_name of this ShowScanJobResultsResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def type(self):
        r"""Gets the type of this ShowScanJobResultsResponse.

        查询资产类型

        :return: The type of this ShowScanJobResultsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowScanJobResultsResponse.

        查询资产类型

        :param type: The type of this ShowScanJobResultsResponse.
        :type type: str
        """
        self._type = type

    @property
    def db_scan_result(self):
        r"""Gets the db_scan_result of this ShowScanJobResultsResponse.

        :return: The db_scan_result of this ShowScanJobResultsResponse.
        :rtype: :class:`huaweicloudsdkdsc.v1.DbScanResult`
        """
        return self._db_scan_result

    @db_scan_result.setter
    def db_scan_result(self, db_scan_result):
        r"""Sets the db_scan_result of this ShowScanJobResultsResponse.

        :param db_scan_result: The db_scan_result of this ShowScanJobResultsResponse.
        :type db_scan_result: :class:`huaweicloudsdkdsc.v1.DbScanResult`
        """
        self._db_scan_result = db_scan_result

    @property
    def obs_scan_result(self):
        r"""Gets the obs_scan_result of this ShowScanJobResultsResponse.

        :return: The obs_scan_result of this ShowScanJobResultsResponse.
        :rtype: :class:`huaweicloudsdkdsc.v1.ObsScanResult`
        """
        return self._obs_scan_result

    @obs_scan_result.setter
    def obs_scan_result(self, obs_scan_result):
        r"""Sets the obs_scan_result of this ShowScanJobResultsResponse.

        :param obs_scan_result: The obs_scan_result of this ShowScanJobResultsResponse.
        :type obs_scan_result: :class:`huaweicloudsdkdsc.v1.ObsScanResult`
        """
        self._obs_scan_result = obs_scan_result

    @property
    def es_scan_result(self):
        r"""Gets the es_scan_result of this ShowScanJobResultsResponse.

        :return: The es_scan_result of this ShowScanJobResultsResponse.
        :rtype: :class:`huaweicloudsdkdsc.v1.EsScanResult`
        """
        return self._es_scan_result

    @es_scan_result.setter
    def es_scan_result(self, es_scan_result):
        r"""Sets the es_scan_result of this ShowScanJobResultsResponse.

        :param es_scan_result: The es_scan_result of this ShowScanJobResultsResponse.
        :type es_scan_result: :class:`huaweicloudsdkdsc.v1.EsScanResult`
        """
        self._es_scan_result = es_scan_result

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
        if not isinstance(other, ShowScanJobResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
