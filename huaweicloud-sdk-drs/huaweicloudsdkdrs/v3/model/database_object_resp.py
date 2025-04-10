# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseObjectResp:

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
        'status': 'bool',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, job_id=None, status=None, error_code=None, error_msg=None):
        r"""DatabaseObjectResp

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param status: 选择对象任务成功标志
        :type status: bool
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        

        self._job_id = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def job_id(self):
        r"""Gets the job_id of this DatabaseObjectResp.

        任务ID

        :return: The job_id of this DatabaseObjectResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DatabaseObjectResp.

        任务ID

        :param job_id: The job_id of this DatabaseObjectResp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this DatabaseObjectResp.

        选择对象任务成功标志

        :return: The status of this DatabaseObjectResp.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DatabaseObjectResp.

        选择对象任务成功标志

        :param status: The status of this DatabaseObjectResp.
        :type status: bool
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this DatabaseObjectResp.

        错误码

        :return: The error_code of this DatabaseObjectResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this DatabaseObjectResp.

        错误码

        :param error_code: The error_code of this DatabaseObjectResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this DatabaseObjectResp.

        错误信息

        :return: The error_msg of this DatabaseObjectResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this DatabaseObjectResp.

        错误信息

        :param error_msg: The error_msg of this DatabaseObjectResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, DatabaseObjectResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
