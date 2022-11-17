# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyConfigurationResponse(SdkResponse):

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
        'success': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'success': 'success'
    }

    def __init__(self, job_id=None, success=None):
        """ApplyConfigurationResponse

        The model defined in huaweicloud sdk

        :param job_id: 应用参数模板的异步任务ID。
        :type job_id: str
        :param success: 应用参数模板任务是否提交成功。 - 取值为“true”，表示任务提交成功。 - 取值为“false”，表示任务提交失败。
        :type success: bool
        """
        
        super(ApplyConfigurationResponse, self).__init__()

        self._job_id = None
        self._success = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if success is not None:
            self.success = success

    @property
    def job_id(self):
        """Gets the job_id of this ApplyConfigurationResponse.

        应用参数模板的异步任务ID。

        :return: The job_id of this ApplyConfigurationResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ApplyConfigurationResponse.

        应用参数模板的异步任务ID。

        :param job_id: The job_id of this ApplyConfigurationResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def success(self):
        """Gets the success of this ApplyConfigurationResponse.

        应用参数模板任务是否提交成功。 - 取值为“true”，表示任务提交成功。 - 取值为“false”，表示任务提交失败。

        :return: The success of this ApplyConfigurationResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ApplyConfigurationResponse.

        应用参数模板任务是否提交成功。 - 取值为“true”，表示任务提交成功。 - 取值为“false”，表示任务提交失败。

        :param success: The success of this ApplyConfigurationResponse.
        :type success: bool
        """
        self._success = success

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
        if not isinstance(other, ApplyConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
