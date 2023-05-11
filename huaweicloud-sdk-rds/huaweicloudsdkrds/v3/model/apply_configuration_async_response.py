# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyConfigurationAsyncResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_id': 'str',
        'configuration_name': 'str',
        'success': 'bool',
        'job_id': 'str'
    }

    attribute_map = {
        'configuration_id': 'configuration_id',
        'configuration_name': 'configuration_name',
        'success': 'success',
        'job_id': 'job_id'
    }

    def __init__(self, configuration_id=None, configuration_name=None, success=None, job_id=None):
        """ApplyConfigurationAsyncResponse

        The model defined in huaweicloud sdk

        :param configuration_id: 参数组ID。
        :type configuration_id: str
        :param configuration_name: 参数组名称。
        :type configuration_name: str
        :param success: 参数模板是否都应用成功。 - “true”表示参数模板都应用成功。 - “false”表示存在应用失败的参数模板。
        :type success: bool
        :param job_id: 任务流id
        :type job_id: str
        """
        
        super(ApplyConfigurationAsyncResponse, self).__init__()

        self._configuration_id = None
        self._configuration_name = None
        self._success = None
        self._job_id = None
        self.discriminator = None

        if configuration_id is not None:
            self.configuration_id = configuration_id
        if configuration_name is not None:
            self.configuration_name = configuration_name
        if success is not None:
            self.success = success
        if job_id is not None:
            self.job_id = job_id

    @property
    def configuration_id(self):
        """Gets the configuration_id of this ApplyConfigurationAsyncResponse.

        参数组ID。

        :return: The configuration_id of this ApplyConfigurationAsyncResponse.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this ApplyConfigurationAsyncResponse.

        参数组ID。

        :param configuration_id: The configuration_id of this ApplyConfigurationAsyncResponse.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def configuration_name(self):
        """Gets the configuration_name of this ApplyConfigurationAsyncResponse.

        参数组名称。

        :return: The configuration_name of this ApplyConfigurationAsyncResponse.
        :rtype: str
        """
        return self._configuration_name

    @configuration_name.setter
    def configuration_name(self, configuration_name):
        """Sets the configuration_name of this ApplyConfigurationAsyncResponse.

        参数组名称。

        :param configuration_name: The configuration_name of this ApplyConfigurationAsyncResponse.
        :type configuration_name: str
        """
        self._configuration_name = configuration_name

    @property
    def success(self):
        """Gets the success of this ApplyConfigurationAsyncResponse.

        参数模板是否都应用成功。 - “true”表示参数模板都应用成功。 - “false”表示存在应用失败的参数模板。

        :return: The success of this ApplyConfigurationAsyncResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ApplyConfigurationAsyncResponse.

        参数模板是否都应用成功。 - “true”表示参数模板都应用成功。 - “false”表示存在应用失败的参数模板。

        :param success: The success of this ApplyConfigurationAsyncResponse.
        :type success: bool
        """
        self._success = success

    @property
    def job_id(self):
        """Gets the job_id of this ApplyConfigurationAsyncResponse.

        任务流id

        :return: The job_id of this ApplyConfigurationAsyncResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ApplyConfigurationAsyncResponse.

        任务流id

        :param job_id: The job_id of this ApplyConfigurationAsyncResponse.
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
        if not isinstance(other, ApplyConfigurationAsyncResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
