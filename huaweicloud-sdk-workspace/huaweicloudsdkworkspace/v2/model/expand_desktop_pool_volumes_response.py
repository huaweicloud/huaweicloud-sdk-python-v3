# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandDesktopPoolVolumesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'cbc_job_id': 'str',
        'get_job_endpoint': 'str',
        'max_provision_time': 'int',
        'min_provision_time': 'int',
        'periodic_query_time': 'int',
        'job_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'cbc_job_id': 'cbcJobId',
        'get_job_endpoint': 'getJobEndpoint',
        'max_provision_time': 'maxProvisionTime',
        'min_provision_time': 'minProvisionTime',
        'periodic_query_time': 'periodicQueryTime',
        'job_id': 'job_id'
    }

    def __init__(self, error_code=None, error_msg=None, cbc_job_id=None, get_job_endpoint=None, max_provision_time=None, min_provision_time=None, periodic_query_time=None, job_id=None):
        """ExpandDesktopPoolVolumesResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码，失败时返回。
        :type error_code: str
        :param error_msg: 错误描述。
        :type error_msg: str
        :param cbc_job_id: 创建云桌面总任务ID，CBC根据此ID定期查询任务是否成功
        :type cbc_job_id: str
        :param get_job_endpoint: 云运营平台CBC获取到JobId后，会使用getJobEndpoint当做URL，调用云服务，查询获取Job结果
        :type get_job_endpoint: str
        :param max_provision_time: 在线开通最大时间 在maxProvisionTime时间范围内，CBC会周期性的查询云服务开通结果；超过maxProvisionTime还没有开通成功，CBC会发失败工单，人工去分析处理。 单位：分钟。 如果为空，CBC默认为6小时。 取值范围（0,43200]，即30天。
        :type max_provision_time: int
        :param min_provision_time: 开通最小时间（云服务最快开通时长，或一般开通时长） 获取到JobId后，经过minProvisionTime时间后，才来查询获取云服务开通结果。如果为空，云运营平台获取到JobId后，就去查询云服务开通结果。 单位：分钟。 取值范围：(0, 43200)
        :type min_provision_time: int
        :param periodic_query_time: Job周期性查询时间，默认2分钟查询一次 云运营平台会使用getJobEndpoint(Job查询接口)、每隔periodicQueryTime时间去查询云服务开通结果。 单位：分钟。 如果为空，则使用CBC默认的间隔时间（1分钟，2分钟，4分钟……15分钟）来查询云服务开通结果。 取值范围：(0, 43200)
        :type periodic_query_time: int
        :param job_id: 任务ID
        :type job_id: str
        """
        
        super(ExpandDesktopPoolVolumesResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._cbc_job_id = None
        self._get_job_endpoint = None
        self._max_provision_time = None
        self._min_provision_time = None
        self._periodic_query_time = None
        self._job_id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if cbc_job_id is not None:
            self.cbc_job_id = cbc_job_id
        if get_job_endpoint is not None:
            self.get_job_endpoint = get_job_endpoint
        if max_provision_time is not None:
            self.max_provision_time = max_provision_time
        if min_provision_time is not None:
            self.min_provision_time = min_provision_time
        if periodic_query_time is not None:
            self.periodic_query_time = periodic_query_time
        if job_id is not None:
            self.job_id = job_id

    @property
    def error_code(self):
        """Gets the error_code of this ExpandDesktopPoolVolumesResponse.

        错误码，失败时返回。

        :return: The error_code of this ExpandDesktopPoolVolumesResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ExpandDesktopPoolVolumesResponse.

        错误码，失败时返回。

        :param error_code: The error_code of this ExpandDesktopPoolVolumesResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ExpandDesktopPoolVolumesResponse.

        错误描述。

        :return: The error_msg of this ExpandDesktopPoolVolumesResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ExpandDesktopPoolVolumesResponse.

        错误描述。

        :param error_msg: The error_msg of this ExpandDesktopPoolVolumesResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def cbc_job_id(self):
        """Gets the cbc_job_id of this ExpandDesktopPoolVolumesResponse.

        创建云桌面总任务ID，CBC根据此ID定期查询任务是否成功

        :return: The cbc_job_id of this ExpandDesktopPoolVolumesResponse.
        :rtype: str
        """
        return self._cbc_job_id

    @cbc_job_id.setter
    def cbc_job_id(self, cbc_job_id):
        """Sets the cbc_job_id of this ExpandDesktopPoolVolumesResponse.

        创建云桌面总任务ID，CBC根据此ID定期查询任务是否成功

        :param cbc_job_id: The cbc_job_id of this ExpandDesktopPoolVolumesResponse.
        :type cbc_job_id: str
        """
        self._cbc_job_id = cbc_job_id

    @property
    def get_job_endpoint(self):
        """Gets the get_job_endpoint of this ExpandDesktopPoolVolumesResponse.

        云运营平台CBC获取到JobId后，会使用getJobEndpoint当做URL，调用云服务，查询获取Job结果

        :return: The get_job_endpoint of this ExpandDesktopPoolVolumesResponse.
        :rtype: str
        """
        return self._get_job_endpoint

    @get_job_endpoint.setter
    def get_job_endpoint(self, get_job_endpoint):
        """Sets the get_job_endpoint of this ExpandDesktopPoolVolumesResponse.

        云运营平台CBC获取到JobId后，会使用getJobEndpoint当做URL，调用云服务，查询获取Job结果

        :param get_job_endpoint: The get_job_endpoint of this ExpandDesktopPoolVolumesResponse.
        :type get_job_endpoint: str
        """
        self._get_job_endpoint = get_job_endpoint

    @property
    def max_provision_time(self):
        """Gets the max_provision_time of this ExpandDesktopPoolVolumesResponse.

        在线开通最大时间 在maxProvisionTime时间范围内，CBC会周期性的查询云服务开通结果；超过maxProvisionTime还没有开通成功，CBC会发失败工单，人工去分析处理。 单位：分钟。 如果为空，CBC默认为6小时。 取值范围（0,43200]，即30天。

        :return: The max_provision_time of this ExpandDesktopPoolVolumesResponse.
        :rtype: int
        """
        return self._max_provision_time

    @max_provision_time.setter
    def max_provision_time(self, max_provision_time):
        """Sets the max_provision_time of this ExpandDesktopPoolVolumesResponse.

        在线开通最大时间 在maxProvisionTime时间范围内，CBC会周期性的查询云服务开通结果；超过maxProvisionTime还没有开通成功，CBC会发失败工单，人工去分析处理。 单位：分钟。 如果为空，CBC默认为6小时。 取值范围（0,43200]，即30天。

        :param max_provision_time: The max_provision_time of this ExpandDesktopPoolVolumesResponse.
        :type max_provision_time: int
        """
        self._max_provision_time = max_provision_time

    @property
    def min_provision_time(self):
        """Gets the min_provision_time of this ExpandDesktopPoolVolumesResponse.

        开通最小时间（云服务最快开通时长，或一般开通时长） 获取到JobId后，经过minProvisionTime时间后，才来查询获取云服务开通结果。如果为空，云运营平台获取到JobId后，就去查询云服务开通结果。 单位：分钟。 取值范围：(0, 43200)

        :return: The min_provision_time of this ExpandDesktopPoolVolumesResponse.
        :rtype: int
        """
        return self._min_provision_time

    @min_provision_time.setter
    def min_provision_time(self, min_provision_time):
        """Sets the min_provision_time of this ExpandDesktopPoolVolumesResponse.

        开通最小时间（云服务最快开通时长，或一般开通时长） 获取到JobId后，经过minProvisionTime时间后，才来查询获取云服务开通结果。如果为空，云运营平台获取到JobId后，就去查询云服务开通结果。 单位：分钟。 取值范围：(0, 43200)

        :param min_provision_time: The min_provision_time of this ExpandDesktopPoolVolumesResponse.
        :type min_provision_time: int
        """
        self._min_provision_time = min_provision_time

    @property
    def periodic_query_time(self):
        """Gets the periodic_query_time of this ExpandDesktopPoolVolumesResponse.

        Job周期性查询时间，默认2分钟查询一次 云运营平台会使用getJobEndpoint(Job查询接口)、每隔periodicQueryTime时间去查询云服务开通结果。 单位：分钟。 如果为空，则使用CBC默认的间隔时间（1分钟，2分钟，4分钟……15分钟）来查询云服务开通结果。 取值范围：(0, 43200)

        :return: The periodic_query_time of this ExpandDesktopPoolVolumesResponse.
        :rtype: int
        """
        return self._periodic_query_time

    @periodic_query_time.setter
    def periodic_query_time(self, periodic_query_time):
        """Sets the periodic_query_time of this ExpandDesktopPoolVolumesResponse.

        Job周期性查询时间，默认2分钟查询一次 云运营平台会使用getJobEndpoint(Job查询接口)、每隔periodicQueryTime时间去查询云服务开通结果。 单位：分钟。 如果为空，则使用CBC默认的间隔时间（1分钟，2分钟，4分钟……15分钟）来查询云服务开通结果。 取值范围：(0, 43200)

        :param periodic_query_time: The periodic_query_time of this ExpandDesktopPoolVolumesResponse.
        :type periodic_query_time: int
        """
        self._periodic_query_time = periodic_query_time

    @property
    def job_id(self):
        """Gets the job_id of this ExpandDesktopPoolVolumesResponse.

        任务ID

        :return: The job_id of this ExpandDesktopPoolVolumesResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ExpandDesktopPoolVolumesResponse.

        任务ID

        :param job_id: The job_id of this ExpandDesktopPoolVolumesResponse.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ExpandDesktopPoolVolumesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
