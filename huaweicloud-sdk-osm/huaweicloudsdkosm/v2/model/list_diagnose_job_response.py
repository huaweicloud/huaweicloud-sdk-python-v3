# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiagnoseJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'error_code': 'str',
        'error_msg': 'str',
        'job_id': 'int',
        'domain_id': 'str',
        'items_result': 'list[ItemResultVo]',
        'create_time': 'int'
    }

    attribute_map = {
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'job_id': 'job_id',
        'domain_id': 'domain_id',
        'items_result': 'items_result',
        'create_time': 'create_time'
    }

    def __init__(self, status=None, error_code=None, error_msg=None, job_id=None, domain_id=None, items_result=None, create_time=None):
        """ListDiagnoseJobResponse

        The model defined in huaweicloud sdk

        :param status:  任务执行的状态 0：准备中，2：执行中，3：完成，4：失败，7：未执行，8：不可用；用于判断任务的是否执行结束，3就是结束了，4,7,8说明是TSC诊断脚本有问题，OSM这边无法处理
        :type status: int
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误描述
        :type error_msg: str
        :param job_id: 任务ID
        :type job_id: int
        :param domain_id: 租户ID
        :type domain_id: str
        :param items_result: 任务的检查项结果
        :type items_result: list[:class:`huaweicloudsdkosm.v2.ItemResultVo`]
        :param create_time: 任务创建时间
        :type create_time: int
        """
        
        super(ListDiagnoseJobResponse, self).__init__()

        self._status = None
        self._error_code = None
        self._error_msg = None
        self._job_id = None
        self._domain_id = None
        self._items_result = None
        self._create_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if job_id is not None:
            self.job_id = job_id
        if domain_id is not None:
            self.domain_id = domain_id
        if items_result is not None:
            self.items_result = items_result
        if create_time is not None:
            self.create_time = create_time

    @property
    def status(self):
        """Gets the status of this ListDiagnoseJobResponse.

         任务执行的状态 0：准备中，2：执行中，3：完成，4：失败，7：未执行，8：不可用；用于判断任务的是否执行结束，3就是结束了，4,7,8说明是TSC诊断脚本有问题，OSM这边无法处理

        :return: The status of this ListDiagnoseJobResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDiagnoseJobResponse.

         任务执行的状态 0：准备中，2：执行中，3：完成，4：失败，7：未执行，8：不可用；用于判断任务的是否执行结束，3就是结束了，4,7,8说明是TSC诊断脚本有问题，OSM这边无法处理

        :param status: The status of this ListDiagnoseJobResponse.
        :type status: int
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this ListDiagnoseJobResponse.

        错误码

        :return: The error_code of this ListDiagnoseJobResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListDiagnoseJobResponse.

        错误码

        :param error_code: The error_code of this ListDiagnoseJobResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ListDiagnoseJobResponse.

        错误描述

        :return: The error_msg of this ListDiagnoseJobResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ListDiagnoseJobResponse.

        错误描述

        :param error_msg: The error_msg of this ListDiagnoseJobResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def job_id(self):
        """Gets the job_id of this ListDiagnoseJobResponse.

        任务ID

        :return: The job_id of this ListDiagnoseJobResponse.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListDiagnoseJobResponse.

        任务ID

        :param job_id: The job_id of this ListDiagnoseJobResponse.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def domain_id(self):
        """Gets the domain_id of this ListDiagnoseJobResponse.

        租户ID

        :return: The domain_id of this ListDiagnoseJobResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListDiagnoseJobResponse.

        租户ID

        :param domain_id: The domain_id of this ListDiagnoseJobResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def items_result(self):
        """Gets the items_result of this ListDiagnoseJobResponse.

        任务的检查项结果

        :return: The items_result of this ListDiagnoseJobResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.ItemResultVo`]
        """
        return self._items_result

    @items_result.setter
    def items_result(self, items_result):
        """Sets the items_result of this ListDiagnoseJobResponse.

        任务的检查项结果

        :param items_result: The items_result of this ListDiagnoseJobResponse.
        :type items_result: list[:class:`huaweicloudsdkosm.v2.ItemResultVo`]
        """
        self._items_result = items_result

    @property
    def create_time(self):
        """Gets the create_time of this ListDiagnoseJobResponse.

        任务创建时间

        :return: The create_time of this ListDiagnoseJobResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListDiagnoseJobResponse.

        任务创建时间

        :param create_time: The create_time of this ListDiagnoseJobResponse.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ListDiagnoseJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
