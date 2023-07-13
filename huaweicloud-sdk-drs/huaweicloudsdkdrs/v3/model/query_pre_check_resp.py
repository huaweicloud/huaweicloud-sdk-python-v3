# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryPreCheckResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'precheck_id': 'str',
        'result': 'bool',
        'process': 'str',
        'total_passed_rate': 'str',
        'rds_instance_id': 'str',
        'job_direction': 'str',
        'precheck_result': 'list[PrecheckResult]',
        'error_msg': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'precheck_id': 'precheck_id',
        'result': 'result',
        'process': 'process',
        'total_passed_rate': 'total_passed_rate',
        'rds_instance_id': 'rds_instance_id',
        'job_direction': 'job_direction',
        'precheck_result': 'precheck_result',
        'error_msg': 'error_msg',
        'error_code': 'error_code'
    }

    def __init__(self, precheck_id=None, result=None, process=None, total_passed_rate=None, rds_instance_id=None, job_direction=None, precheck_result=None, error_msg=None, error_code=None):
        """QueryPreCheckResp

        The model defined in huaweicloud sdk

        :param precheck_id: 预检查id。
        :type precheck_id: str
        :param result: 返回的预检查结果是否通过。true表示预检查通过，通过后才可进行启动任务。
        :type result: bool
        :param process: 预检查进度百分比。
        :type process: str
        :param total_passed_rate: 预检查通过百分比。
        :type total_passed_rate: str
        :param rds_instance_id: RDS实例id。
        :type rds_instance_id: str
        :param job_direction: 迁移方向。 - up-入云 灾备场景时对应本云为备 - down-出云 灾备场景时对应本云为主 - non-dbs-自建
        :type job_direction: str
        :param precheck_result: 预检查各项结果。
        :type precheck_result: list[:class:`huaweicloudsdkdrs.v3.PrecheckResult`]
        :param error_msg: 错误信息
        :type error_msg: str
        :param error_code: 任务错误码。
        :type error_code: str
        """
        
        

        self._precheck_id = None
        self._result = None
        self._process = None
        self._total_passed_rate = None
        self._rds_instance_id = None
        self._job_direction = None
        self._precheck_result = None
        self._error_msg = None
        self._error_code = None
        self.discriminator = None

        if precheck_id is not None:
            self.precheck_id = precheck_id
        if result is not None:
            self.result = result
        if process is not None:
            self.process = process
        if total_passed_rate is not None:
            self.total_passed_rate = total_passed_rate
        if rds_instance_id is not None:
            self.rds_instance_id = rds_instance_id
        if job_direction is not None:
            self.job_direction = job_direction
        if precheck_result is not None:
            self.precheck_result = precheck_result
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code

    @property
    def precheck_id(self):
        """Gets the precheck_id of this QueryPreCheckResp.

        预检查id。

        :return: The precheck_id of this QueryPreCheckResp.
        :rtype: str
        """
        return self._precheck_id

    @precheck_id.setter
    def precheck_id(self, precheck_id):
        """Sets the precheck_id of this QueryPreCheckResp.

        预检查id。

        :param precheck_id: The precheck_id of this QueryPreCheckResp.
        :type precheck_id: str
        """
        self._precheck_id = precheck_id

    @property
    def result(self):
        """Gets the result of this QueryPreCheckResp.

        返回的预检查结果是否通过。true表示预检查通过，通过后才可进行启动任务。

        :return: The result of this QueryPreCheckResp.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this QueryPreCheckResp.

        返回的预检查结果是否通过。true表示预检查通过，通过后才可进行启动任务。

        :param result: The result of this QueryPreCheckResp.
        :type result: bool
        """
        self._result = result

    @property
    def process(self):
        """Gets the process of this QueryPreCheckResp.

        预检查进度百分比。

        :return: The process of this QueryPreCheckResp.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this QueryPreCheckResp.

        预检查进度百分比。

        :param process: The process of this QueryPreCheckResp.
        :type process: str
        """
        self._process = process

    @property
    def total_passed_rate(self):
        """Gets the total_passed_rate of this QueryPreCheckResp.

        预检查通过百分比。

        :return: The total_passed_rate of this QueryPreCheckResp.
        :rtype: str
        """
        return self._total_passed_rate

    @total_passed_rate.setter
    def total_passed_rate(self, total_passed_rate):
        """Sets the total_passed_rate of this QueryPreCheckResp.

        预检查通过百分比。

        :param total_passed_rate: The total_passed_rate of this QueryPreCheckResp.
        :type total_passed_rate: str
        """
        self._total_passed_rate = total_passed_rate

    @property
    def rds_instance_id(self):
        """Gets the rds_instance_id of this QueryPreCheckResp.

        RDS实例id。

        :return: The rds_instance_id of this QueryPreCheckResp.
        :rtype: str
        """
        return self._rds_instance_id

    @rds_instance_id.setter
    def rds_instance_id(self, rds_instance_id):
        """Sets the rds_instance_id of this QueryPreCheckResp.

        RDS实例id。

        :param rds_instance_id: The rds_instance_id of this QueryPreCheckResp.
        :type rds_instance_id: str
        """
        self._rds_instance_id = rds_instance_id

    @property
    def job_direction(self):
        """Gets the job_direction of this QueryPreCheckResp.

        迁移方向。 - up-入云 灾备场景时对应本云为备 - down-出云 灾备场景时对应本云为主 - non-dbs-自建

        :return: The job_direction of this QueryPreCheckResp.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this QueryPreCheckResp.

        迁移方向。 - up-入云 灾备场景时对应本云为备 - down-出云 灾备场景时对应本云为主 - non-dbs-自建

        :param job_direction: The job_direction of this QueryPreCheckResp.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def precheck_result(self):
        """Gets the precheck_result of this QueryPreCheckResp.

        预检查各项结果。

        :return: The precheck_result of this QueryPreCheckResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.PrecheckResult`]
        """
        return self._precheck_result

    @precheck_result.setter
    def precheck_result(self, precheck_result):
        """Sets the precheck_result of this QueryPreCheckResp.

        预检查各项结果。

        :param precheck_result: The precheck_result of this QueryPreCheckResp.
        :type precheck_result: list[:class:`huaweicloudsdkdrs.v3.PrecheckResult`]
        """
        self._precheck_result = precheck_result

    @property
    def error_msg(self):
        """Gets the error_msg of this QueryPreCheckResp.

        错误信息

        :return: The error_msg of this QueryPreCheckResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this QueryPreCheckResp.

        错误信息

        :param error_msg: The error_msg of this QueryPreCheckResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        """Gets the error_code of this QueryPreCheckResp.

        任务错误码。

        :return: The error_code of this QueryPreCheckResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this QueryPreCheckResp.

        任务错误码。

        :param error_code: The error_code of this QueryPreCheckResp.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, QueryPreCheckResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
