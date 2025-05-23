# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRebuildDesktopsSystemDiskResponse(SdkResponse):

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
        'encoded_authorization_message': 'str',
        'job_id': 'str',
        'get_job_endpoint': 'str',
        'max_provision_time': 'int',
        'min_provision_time': 'int',
        'periodic_query_time': 'int'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'encoded_authorization_message': 'encoded_authorization_message',
        'job_id': 'job_id',
        'get_job_endpoint': 'get_job_endpoint',
        'max_provision_time': 'max_provision_time',
        'min_provision_time': 'min_provision_time',
        'periodic_query_time': 'periodic_query_time'
    }

    def __init__(self, error_code=None, error_msg=None, encoded_authorization_message=None, job_id=None, get_job_endpoint=None, max_provision_time=None, min_provision_time=None, periodic_query_time=None):
        r"""BatchRebuildDesktopsSystemDiskResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误描述。
        :type error_msg: str
        :param encoded_authorization_message: 加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。
        :type encoded_authorization_message: str
        :param job_id: 重建系统盘总任务id。
        :type job_id: str
        :param get_job_endpoint: 云运营平台CBC获取到JobId后，会使用getJobEndpoint当做URL，调用云服务，查询获取Job结果。
        :type get_job_endpoint: str
        :param max_provision_time: 在线开通最大时间。
        :type max_provision_time: int
        :param min_provision_time: 开通最小时间（云服务最快开通时长，或一般开通时长）。
        :type min_provision_time: int
        :param periodic_query_time: Job周期性查询时间。
        :type periodic_query_time: int
        """
        
        super(BatchRebuildDesktopsSystemDiskResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._encoded_authorization_message = None
        self._job_id = None
        self._get_job_endpoint = None
        self._max_provision_time = None
        self._min_provision_time = None
        self._periodic_query_time = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if encoded_authorization_message is not None:
            self.encoded_authorization_message = encoded_authorization_message
        if job_id is not None:
            self.job_id = job_id
        if get_job_endpoint is not None:
            self.get_job_endpoint = get_job_endpoint
        if max_provision_time is not None:
            self.max_provision_time = max_provision_time
        if min_provision_time is not None:
            self.min_provision_time = min_provision_time
        if periodic_query_time is not None:
            self.periodic_query_time = periodic_query_time

    @property
    def error_code(self):
        r"""Gets the error_code of this BatchRebuildDesktopsSystemDiskResponse.

        错误码。

        :return: The error_code of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this BatchRebuildDesktopsSystemDiskResponse.

        错误码。

        :param error_code: The error_code of this BatchRebuildDesktopsSystemDiskResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this BatchRebuildDesktopsSystemDiskResponse.

        错误描述。

        :return: The error_msg of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this BatchRebuildDesktopsSystemDiskResponse.

        错误描述。

        :param error_msg: The error_msg of this BatchRebuildDesktopsSystemDiskResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def encoded_authorization_message(self):
        r"""Gets the encoded_authorization_message of this BatchRebuildDesktopsSystemDiskResponse.

        加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。

        :return: The encoded_authorization_message of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: str
        """
        return self._encoded_authorization_message

    @encoded_authorization_message.setter
    def encoded_authorization_message(self, encoded_authorization_message):
        r"""Sets the encoded_authorization_message of this BatchRebuildDesktopsSystemDiskResponse.

        加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。

        :param encoded_authorization_message: The encoded_authorization_message of this BatchRebuildDesktopsSystemDiskResponse.
        :type encoded_authorization_message: str
        """
        self._encoded_authorization_message = encoded_authorization_message

    @property
    def job_id(self):
        r"""Gets the job_id of this BatchRebuildDesktopsSystemDiskResponse.

        重建系统盘总任务id。

        :return: The job_id of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this BatchRebuildDesktopsSystemDiskResponse.

        重建系统盘总任务id。

        :param job_id: The job_id of this BatchRebuildDesktopsSystemDiskResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def get_job_endpoint(self):
        r"""Gets the get_job_endpoint of this BatchRebuildDesktopsSystemDiskResponse.

        云运营平台CBC获取到JobId后，会使用getJobEndpoint当做URL，调用云服务，查询获取Job结果。

        :return: The get_job_endpoint of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: str
        """
        return self._get_job_endpoint

    @get_job_endpoint.setter
    def get_job_endpoint(self, get_job_endpoint):
        r"""Sets the get_job_endpoint of this BatchRebuildDesktopsSystemDiskResponse.

        云运营平台CBC获取到JobId后，会使用getJobEndpoint当做URL，调用云服务，查询获取Job结果。

        :param get_job_endpoint: The get_job_endpoint of this BatchRebuildDesktopsSystemDiskResponse.
        :type get_job_endpoint: str
        """
        self._get_job_endpoint = get_job_endpoint

    @property
    def max_provision_time(self):
        r"""Gets the max_provision_time of this BatchRebuildDesktopsSystemDiskResponse.

        在线开通最大时间。

        :return: The max_provision_time of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: int
        """
        return self._max_provision_time

    @max_provision_time.setter
    def max_provision_time(self, max_provision_time):
        r"""Sets the max_provision_time of this BatchRebuildDesktopsSystemDiskResponse.

        在线开通最大时间。

        :param max_provision_time: The max_provision_time of this BatchRebuildDesktopsSystemDiskResponse.
        :type max_provision_time: int
        """
        self._max_provision_time = max_provision_time

    @property
    def min_provision_time(self):
        r"""Gets the min_provision_time of this BatchRebuildDesktopsSystemDiskResponse.

        开通最小时间（云服务最快开通时长，或一般开通时长）。

        :return: The min_provision_time of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: int
        """
        return self._min_provision_time

    @min_provision_time.setter
    def min_provision_time(self, min_provision_time):
        r"""Sets the min_provision_time of this BatchRebuildDesktopsSystemDiskResponse.

        开通最小时间（云服务最快开通时长，或一般开通时长）。

        :param min_provision_time: The min_provision_time of this BatchRebuildDesktopsSystemDiskResponse.
        :type min_provision_time: int
        """
        self._min_provision_time = min_provision_time

    @property
    def periodic_query_time(self):
        r"""Gets the periodic_query_time of this BatchRebuildDesktopsSystemDiskResponse.

        Job周期性查询时间。

        :return: The periodic_query_time of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: int
        """
        return self._periodic_query_time

    @periodic_query_time.setter
    def periodic_query_time(self, periodic_query_time):
        r"""Sets the periodic_query_time of this BatchRebuildDesktopsSystemDiskResponse.

        Job周期性查询时间。

        :param periodic_query_time: The periodic_query_time of this BatchRebuildDesktopsSystemDiskResponse.
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
        if not isinstance(other, BatchRebuildDesktopsSystemDiskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
