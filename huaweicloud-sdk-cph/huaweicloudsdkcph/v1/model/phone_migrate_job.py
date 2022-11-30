# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PhoneMigrateJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_phone_id': 'str',
        'target_phone_id': 'str',
        'job_id': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'source_phone_id': 'source_phone_id',
        'target_phone_id': 'target_phone_id',
        'job_id': 'job_id',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, source_phone_id=None, target_phone_id=None, job_id=None, error_code=None, error_msg=None):
        """PhoneMigrateJob

        The model defined in huaweicloud sdk

        :param source_phone_id: 源云手机id。
        :type source_phone_id: str
        :param target_phone_id: 目标云手机id。
        :type target_phone_id: str
        :param job_id: 任务的唯一标识。
        :type job_id: str
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误说明。
        :type error_msg: str
        """
        
        

        self._source_phone_id = None
        self._target_phone_id = None
        self._job_id = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if source_phone_id is not None:
            self.source_phone_id = source_phone_id
        if target_phone_id is not None:
            self.target_phone_id = target_phone_id
        if job_id is not None:
            self.job_id = job_id
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def source_phone_id(self):
        """Gets the source_phone_id of this PhoneMigrateJob.

        源云手机id。

        :return: The source_phone_id of this PhoneMigrateJob.
        :rtype: str
        """
        return self._source_phone_id

    @source_phone_id.setter
    def source_phone_id(self, source_phone_id):
        """Sets the source_phone_id of this PhoneMigrateJob.

        源云手机id。

        :param source_phone_id: The source_phone_id of this PhoneMigrateJob.
        :type source_phone_id: str
        """
        self._source_phone_id = source_phone_id

    @property
    def target_phone_id(self):
        """Gets the target_phone_id of this PhoneMigrateJob.

        目标云手机id。

        :return: The target_phone_id of this PhoneMigrateJob.
        :rtype: str
        """
        return self._target_phone_id

    @target_phone_id.setter
    def target_phone_id(self, target_phone_id):
        """Sets the target_phone_id of this PhoneMigrateJob.

        目标云手机id。

        :param target_phone_id: The target_phone_id of this PhoneMigrateJob.
        :type target_phone_id: str
        """
        self._target_phone_id = target_phone_id

    @property
    def job_id(self):
        """Gets the job_id of this PhoneMigrateJob.

        任务的唯一标识。

        :return: The job_id of this PhoneMigrateJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this PhoneMigrateJob.

        任务的唯一标识。

        :param job_id: The job_id of this PhoneMigrateJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def error_code(self):
        """Gets the error_code of this PhoneMigrateJob.

        错误码。

        :return: The error_code of this PhoneMigrateJob.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this PhoneMigrateJob.

        错误码。

        :param error_code: The error_code of this PhoneMigrateJob.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this PhoneMigrateJob.

        错误说明。

        :return: The error_msg of this PhoneMigrateJob.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this PhoneMigrateJob.

        错误说明。

        :param error_msg: The error_msg of this PhoneMigrateJob.
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
        if not isinstance(other, PhoneMigrateJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
