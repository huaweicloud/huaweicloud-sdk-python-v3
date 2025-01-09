# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDesktopResponse(SdkResponse):

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
        'cbc_job_id': 'str',
        'get_job_endpoint': 'str',
        'max_provision_time': 'int',
        'min_provision_time': 'int',
        'periodic_query_time': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'cbc_job_id': 'cbcJobId',
        'get_job_endpoint': 'getJobEndpoint',
        'max_provision_time': 'maxProvisionTime',
        'min_provision_time': 'minProvisionTime',
        'periodic_query_time': 'periodicQueryTime'
    }

    def __init__(self, job_id=None, cbc_job_id=None, get_job_endpoint=None, max_provision_time=None, min_provision_time=None, periodic_query_time=None):
        """CreateDesktopResponse

        The model defined in huaweicloud sdk

        :param job_id: 创建云桌面总任务id
        :type job_id: str
        :param cbc_job_id: 【CBC回调】包周期创建桌面的任务ID
        :type cbc_job_id: str
        :param get_job_endpoint: 【CBC回调】云运营平台CBC获取到JobId后，会使用getJobEndpoint当做URL，调用云服务，查询获取Job结果。
        :type get_job_endpoint: str
        :param max_provision_time: 【CBC回调】在线开通最大时间，在maxProvisionTime时间范围内，CBC会周期性的查询云服务开通结果；超过maxProvisionTime还没有开通成功，CBC会发失败工单，人工去分析处理。
        :type max_provision_time: int
        :param min_provision_time: 【CBC回调】开通最小时间（云服务最快开通时长，或一般开通时长）。获取到JobId后，经过minProvisionTime时间后，才来查询获取云服务开通结果。如果为空，云运营平台获取到JobId后，就去查询云服务开通结果。
        :type min_provision_time: int
        :param periodic_query_time: 【CBC回调】云运营平台会使用getJobEndpoint(Job查询接口)、每隔periodicQueryTime时间去查询云服务开通结果。
        :type periodic_query_time: int
        """
        
        super(CreateDesktopResponse, self).__init__()

        self._job_id = None
        self._cbc_job_id = None
        self._get_job_endpoint = None
        self._max_provision_time = None
        self._min_provision_time = None
        self._periodic_query_time = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
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

    @property
    def job_id(self):
        """Gets the job_id of this CreateDesktopResponse.

        创建云桌面总任务id

        :return: The job_id of this CreateDesktopResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateDesktopResponse.

        创建云桌面总任务id

        :param job_id: The job_id of this CreateDesktopResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def cbc_job_id(self):
        """Gets the cbc_job_id of this CreateDesktopResponse.

        【CBC回调】包周期创建桌面的任务ID

        :return: The cbc_job_id of this CreateDesktopResponse.
        :rtype: str
        """
        return self._cbc_job_id

    @cbc_job_id.setter
    def cbc_job_id(self, cbc_job_id):
        """Sets the cbc_job_id of this CreateDesktopResponse.

        【CBC回调】包周期创建桌面的任务ID

        :param cbc_job_id: The cbc_job_id of this CreateDesktopResponse.
        :type cbc_job_id: str
        """
        self._cbc_job_id = cbc_job_id

    @property
    def get_job_endpoint(self):
        """Gets the get_job_endpoint of this CreateDesktopResponse.

        【CBC回调】云运营平台CBC获取到JobId后，会使用getJobEndpoint当做URL，调用云服务，查询获取Job结果。

        :return: The get_job_endpoint of this CreateDesktopResponse.
        :rtype: str
        """
        return self._get_job_endpoint

    @get_job_endpoint.setter
    def get_job_endpoint(self, get_job_endpoint):
        """Sets the get_job_endpoint of this CreateDesktopResponse.

        【CBC回调】云运营平台CBC获取到JobId后，会使用getJobEndpoint当做URL，调用云服务，查询获取Job结果。

        :param get_job_endpoint: The get_job_endpoint of this CreateDesktopResponse.
        :type get_job_endpoint: str
        """
        self._get_job_endpoint = get_job_endpoint

    @property
    def max_provision_time(self):
        """Gets the max_provision_time of this CreateDesktopResponse.

        【CBC回调】在线开通最大时间，在maxProvisionTime时间范围内，CBC会周期性的查询云服务开通结果；超过maxProvisionTime还没有开通成功，CBC会发失败工单，人工去分析处理。

        :return: The max_provision_time of this CreateDesktopResponse.
        :rtype: int
        """
        return self._max_provision_time

    @max_provision_time.setter
    def max_provision_time(self, max_provision_time):
        """Sets the max_provision_time of this CreateDesktopResponse.

        【CBC回调】在线开通最大时间，在maxProvisionTime时间范围内，CBC会周期性的查询云服务开通结果；超过maxProvisionTime还没有开通成功，CBC会发失败工单，人工去分析处理。

        :param max_provision_time: The max_provision_time of this CreateDesktopResponse.
        :type max_provision_time: int
        """
        self._max_provision_time = max_provision_time

    @property
    def min_provision_time(self):
        """Gets the min_provision_time of this CreateDesktopResponse.

        【CBC回调】开通最小时间（云服务最快开通时长，或一般开通时长）。获取到JobId后，经过minProvisionTime时间后，才来查询获取云服务开通结果。如果为空，云运营平台获取到JobId后，就去查询云服务开通结果。

        :return: The min_provision_time of this CreateDesktopResponse.
        :rtype: int
        """
        return self._min_provision_time

    @min_provision_time.setter
    def min_provision_time(self, min_provision_time):
        """Sets the min_provision_time of this CreateDesktopResponse.

        【CBC回调】开通最小时间（云服务最快开通时长，或一般开通时长）。获取到JobId后，经过minProvisionTime时间后，才来查询获取云服务开通结果。如果为空，云运营平台获取到JobId后，就去查询云服务开通结果。

        :param min_provision_time: The min_provision_time of this CreateDesktopResponse.
        :type min_provision_time: int
        """
        self._min_provision_time = min_provision_time

    @property
    def periodic_query_time(self):
        """Gets the periodic_query_time of this CreateDesktopResponse.

        【CBC回调】云运营平台会使用getJobEndpoint(Job查询接口)、每隔periodicQueryTime时间去查询云服务开通结果。

        :return: The periodic_query_time of this CreateDesktopResponse.
        :rtype: int
        """
        return self._periodic_query_time

    @periodic_query_time.setter
    def periodic_query_time(self, periodic_query_time):
        """Sets the periodic_query_time of this CreateDesktopResponse.

        【CBC回调】云运营平台会使用getJobEndpoint(Job查询接口)、每隔periodicQueryTime时间去查询云服务开通结果。

        :param periodic_query_time: The periodic_query_time of this CreateDesktopResponse.
        :type periodic_query_time: int
        """
        self._periodic_query_time = periodic_query_time

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
        if not isinstance(other, CreateDesktopResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
