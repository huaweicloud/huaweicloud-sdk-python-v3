# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncJobResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'async_job_id': 'str',
        'status': 'str',
        'domain_name': 'str',
        'user_name': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'async_job_id': 'async_job_id',
        'status': 'status',
        'domain_name': 'domain_name',
        'user_name': 'user_name',
        'create_time': 'create_time'
    }

    def __init__(self, async_job_id=None, status=None, domain_name=None, user_name=None, create_time=None):
        """AsyncJobResp

        The model defined in huaweicloud sdk

        :param async_job_id: 批量异步创建的任务ID。
        :type async_job_id: str
        :param status: 批量异步创建的任务状态。取值： - ASYNC_JOB_VALIDATING：批量异步任务参数校验中。 - ASYNC_JOB_VALIDATE_FAILED：批量异步任务参数校验失败。 - AUTO_PARAM_VALIDATE_SUCCESS：批量异步任务参数校验成功。 - COMMIT_SUCCESS：批量异步任务提交成功。
        :type status: str
        :param domain_name: 批量异步创建的任务的租户名。
        :type domain_name: str
        :param user_name: 批量异步创建的任务的用户名。
        :type user_name: str
        :param create_time: 批量异步创建的任务的创建时间。
        :type create_time: str
        """
        
        

        self._async_job_id = None
        self._status = None
        self._domain_name = None
        self._user_name = None
        self._create_time = None
        self.discriminator = None

        self.async_job_id = async_job_id
        self.status = status
        self.domain_name = domain_name
        self.user_name = user_name
        self.create_time = create_time

    @property
    def async_job_id(self):
        """Gets the async_job_id of this AsyncJobResp.

        批量异步创建的任务ID。

        :return: The async_job_id of this AsyncJobResp.
        :rtype: str
        """
        return self._async_job_id

    @async_job_id.setter
    def async_job_id(self, async_job_id):
        """Sets the async_job_id of this AsyncJobResp.

        批量异步创建的任务ID。

        :param async_job_id: The async_job_id of this AsyncJobResp.
        :type async_job_id: str
        """
        self._async_job_id = async_job_id

    @property
    def status(self):
        """Gets the status of this AsyncJobResp.

        批量异步创建的任务状态。取值： - ASYNC_JOB_VALIDATING：批量异步任务参数校验中。 - ASYNC_JOB_VALIDATE_FAILED：批量异步任务参数校验失败。 - AUTO_PARAM_VALIDATE_SUCCESS：批量异步任务参数校验成功。 - COMMIT_SUCCESS：批量异步任务提交成功。

        :return: The status of this AsyncJobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AsyncJobResp.

        批量异步创建的任务状态。取值： - ASYNC_JOB_VALIDATING：批量异步任务参数校验中。 - ASYNC_JOB_VALIDATE_FAILED：批量异步任务参数校验失败。 - AUTO_PARAM_VALIDATE_SUCCESS：批量异步任务参数校验成功。 - COMMIT_SUCCESS：批量异步任务提交成功。

        :param status: The status of this AsyncJobResp.
        :type status: str
        """
        self._status = status

    @property
    def domain_name(self):
        """Gets the domain_name of this AsyncJobResp.

        批量异步创建的任务的租户名。

        :return: The domain_name of this AsyncJobResp.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this AsyncJobResp.

        批量异步创建的任务的租户名。

        :param domain_name: The domain_name of this AsyncJobResp.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def user_name(self):
        """Gets the user_name of this AsyncJobResp.

        批量异步创建的任务的用户名。

        :return: The user_name of this AsyncJobResp.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AsyncJobResp.

        批量异步创建的任务的用户名。

        :param user_name: The user_name of this AsyncJobResp.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def create_time(self):
        """Gets the create_time of this AsyncJobResp.

        批量异步创建的任务的创建时间。

        :return: The create_time of this AsyncJobResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AsyncJobResp.

        批量异步创建的任务的创建时间。

        :param create_time: The create_time of this AsyncJobResp.
        :type create_time: str
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
        if not isinstance(other, AsyncJobResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
