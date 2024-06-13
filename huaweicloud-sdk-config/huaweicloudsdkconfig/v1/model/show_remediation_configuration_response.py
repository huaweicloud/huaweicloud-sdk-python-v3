# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRemediationConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'automatic': 'bool',
        'target_type': 'str',
        'target_id': 'str',
        'static_parameter': 'list[RemediationStaticParameter]',
        'resource_parameter': 'RemediationResourceParameter',
        'maximum_attempts': 'int',
        'retry_attempt_seconds': 'int',
        'auth_type': 'str',
        'auth_value': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'created_by': 'str'
    }

    attribute_map = {
        'automatic': 'automatic',
        'target_type': 'target_type',
        'target_id': 'target_id',
        'static_parameter': 'static_parameter',
        'resource_parameter': 'resource_parameter',
        'maximum_attempts': 'maximum_attempts',
        'retry_attempt_seconds': 'retry_attempt_seconds',
        'auth_type': 'auth_type',
        'auth_value': 'auth_value',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'created_by': 'created_by'
    }

    def __init__(self, automatic=None, target_type=None, target_id=None, static_parameter=None, resource_parameter=None, maximum_attempts=None, retry_attempt_seconds=None, auth_type=None, auth_value=None, created_at=None, updated_at=None, created_by=None):
        """ShowRemediationConfigurationResponse

        The model defined in huaweicloud sdk

        :param automatic: 是否为自动修正。
        :type automatic: bool
        :param target_type: 合规规则修正执行的方式。
        :type target_type: str
        :param target_id: 修正执行的目标ID。如果修正方式为fgs，则该值为函数工作流的函数urn；如果修正方式为rfs，则该值为资源编排服务的模板name与版本号，两者以/分割，如果没有指定默认V1。
        :type target_id: str
        :param static_parameter: 修正执行的参数。
        :type static_parameter: list[:class:`huaweicloudsdkconfig.v1.RemediationStaticParameter`]
        :param resource_parameter: 
        :type resource_parameter: :class:`huaweicloudsdkconfig.v1.RemediationResourceParameter`
        :param maximum_attempts: 指定时间内自动修正的最大尝试次数。
        :type maximum_attempts: int
        :param retry_attempt_seconds: 用于防止循环修正的时间窗口，如果在指定时间内进行了自动修正的最大尝试次数，则将资源添加至修正例外。
        :type retry_attempt_seconds: int
        :param auth_type: 合规规则修正配置的权限方式。
        :type auth_type: str
        :param auth_value: 合规规则修正配置的权限信息。
        :type auth_value: str
        :param created_at: 修正配置的创建时间。
        :type created_at: str
        :param updated_at: 修正配置的更新时间。
        :type updated_at: str
        :param created_by: 创建者。
        :type created_by: str
        """
        
        super(ShowRemediationConfigurationResponse, self).__init__()

        self._automatic = None
        self._target_type = None
        self._target_id = None
        self._static_parameter = None
        self._resource_parameter = None
        self._maximum_attempts = None
        self._retry_attempt_seconds = None
        self._auth_type = None
        self._auth_value = None
        self._created_at = None
        self._updated_at = None
        self._created_by = None
        self.discriminator = None

        if automatic is not None:
            self.automatic = automatic
        if target_type is not None:
            self.target_type = target_type
        if target_id is not None:
            self.target_id = target_id
        if static_parameter is not None:
            self.static_parameter = static_parameter
        if resource_parameter is not None:
            self.resource_parameter = resource_parameter
        if maximum_attempts is not None:
            self.maximum_attempts = maximum_attempts
        if retry_attempt_seconds is not None:
            self.retry_attempt_seconds = retry_attempt_seconds
        if auth_type is not None:
            self.auth_type = auth_type
        if auth_value is not None:
            self.auth_value = auth_value
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if created_by is not None:
            self.created_by = created_by

    @property
    def automatic(self):
        """Gets the automatic of this ShowRemediationConfigurationResponse.

        是否为自动修正。

        :return: The automatic of this ShowRemediationConfigurationResponse.
        :rtype: bool
        """
        return self._automatic

    @automatic.setter
    def automatic(self, automatic):
        """Sets the automatic of this ShowRemediationConfigurationResponse.

        是否为自动修正。

        :param automatic: The automatic of this ShowRemediationConfigurationResponse.
        :type automatic: bool
        """
        self._automatic = automatic

    @property
    def target_type(self):
        """Gets the target_type of this ShowRemediationConfigurationResponse.

        合规规则修正执行的方式。

        :return: The target_type of this ShowRemediationConfigurationResponse.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this ShowRemediationConfigurationResponse.

        合规规则修正执行的方式。

        :param target_type: The target_type of this ShowRemediationConfigurationResponse.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_id(self):
        """Gets the target_id of this ShowRemediationConfigurationResponse.

        修正执行的目标ID。如果修正方式为fgs，则该值为函数工作流的函数urn；如果修正方式为rfs，则该值为资源编排服务的模板name与版本号，两者以/分割，如果没有指定默认V1。

        :return: The target_id of this ShowRemediationConfigurationResponse.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this ShowRemediationConfigurationResponse.

        修正执行的目标ID。如果修正方式为fgs，则该值为函数工作流的函数urn；如果修正方式为rfs，则该值为资源编排服务的模板name与版本号，两者以/分割，如果没有指定默认V1。

        :param target_id: The target_id of this ShowRemediationConfigurationResponse.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def static_parameter(self):
        """Gets the static_parameter of this ShowRemediationConfigurationResponse.

        修正执行的参数。

        :return: The static_parameter of this ShowRemediationConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.RemediationStaticParameter`]
        """
        return self._static_parameter

    @static_parameter.setter
    def static_parameter(self, static_parameter):
        """Sets the static_parameter of this ShowRemediationConfigurationResponse.

        修正执行的参数。

        :param static_parameter: The static_parameter of this ShowRemediationConfigurationResponse.
        :type static_parameter: list[:class:`huaweicloudsdkconfig.v1.RemediationStaticParameter`]
        """
        self._static_parameter = static_parameter

    @property
    def resource_parameter(self):
        """Gets the resource_parameter of this ShowRemediationConfigurationResponse.

        :return: The resource_parameter of this ShowRemediationConfigurationResponse.
        :rtype: :class:`huaweicloudsdkconfig.v1.RemediationResourceParameter`
        """
        return self._resource_parameter

    @resource_parameter.setter
    def resource_parameter(self, resource_parameter):
        """Sets the resource_parameter of this ShowRemediationConfigurationResponse.

        :param resource_parameter: The resource_parameter of this ShowRemediationConfigurationResponse.
        :type resource_parameter: :class:`huaweicloudsdkconfig.v1.RemediationResourceParameter`
        """
        self._resource_parameter = resource_parameter

    @property
    def maximum_attempts(self):
        """Gets the maximum_attempts of this ShowRemediationConfigurationResponse.

        指定时间内自动修正的最大尝试次数。

        :return: The maximum_attempts of this ShowRemediationConfigurationResponse.
        :rtype: int
        """
        return self._maximum_attempts

    @maximum_attempts.setter
    def maximum_attempts(self, maximum_attempts):
        """Sets the maximum_attempts of this ShowRemediationConfigurationResponse.

        指定时间内自动修正的最大尝试次数。

        :param maximum_attempts: The maximum_attempts of this ShowRemediationConfigurationResponse.
        :type maximum_attempts: int
        """
        self._maximum_attempts = maximum_attempts

    @property
    def retry_attempt_seconds(self):
        """Gets the retry_attempt_seconds of this ShowRemediationConfigurationResponse.

        用于防止循环修正的时间窗口，如果在指定时间内进行了自动修正的最大尝试次数，则将资源添加至修正例外。

        :return: The retry_attempt_seconds of this ShowRemediationConfigurationResponse.
        :rtype: int
        """
        return self._retry_attempt_seconds

    @retry_attempt_seconds.setter
    def retry_attempt_seconds(self, retry_attempt_seconds):
        """Sets the retry_attempt_seconds of this ShowRemediationConfigurationResponse.

        用于防止循环修正的时间窗口，如果在指定时间内进行了自动修正的最大尝试次数，则将资源添加至修正例外。

        :param retry_attempt_seconds: The retry_attempt_seconds of this ShowRemediationConfigurationResponse.
        :type retry_attempt_seconds: int
        """
        self._retry_attempt_seconds = retry_attempt_seconds

    @property
    def auth_type(self):
        """Gets the auth_type of this ShowRemediationConfigurationResponse.

        合规规则修正配置的权限方式。

        :return: The auth_type of this ShowRemediationConfigurationResponse.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ShowRemediationConfigurationResponse.

        合规规则修正配置的权限方式。

        :param auth_type: The auth_type of this ShowRemediationConfigurationResponse.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def auth_value(self):
        """Gets the auth_value of this ShowRemediationConfigurationResponse.

        合规规则修正配置的权限信息。

        :return: The auth_value of this ShowRemediationConfigurationResponse.
        :rtype: str
        """
        return self._auth_value

    @auth_value.setter
    def auth_value(self, auth_value):
        """Sets the auth_value of this ShowRemediationConfigurationResponse.

        合规规则修正配置的权限信息。

        :param auth_value: The auth_value of this ShowRemediationConfigurationResponse.
        :type auth_value: str
        """
        self._auth_value = auth_value

    @property
    def created_at(self):
        """Gets the created_at of this ShowRemediationConfigurationResponse.

        修正配置的创建时间。

        :return: The created_at of this ShowRemediationConfigurationResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowRemediationConfigurationResponse.

        修正配置的创建时间。

        :param created_at: The created_at of this ShowRemediationConfigurationResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowRemediationConfigurationResponse.

        修正配置的更新时间。

        :return: The updated_at of this ShowRemediationConfigurationResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowRemediationConfigurationResponse.

        修正配置的更新时间。

        :param updated_at: The updated_at of this ShowRemediationConfigurationResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def created_by(self):
        """Gets the created_by of this ShowRemediationConfigurationResponse.

        创建者。

        :return: The created_by of this ShowRemediationConfigurationResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ShowRemediationConfigurationResponse.

        创建者。

        :param created_by: The created_by of this ShowRemediationConfigurationResponse.
        :type created_by: str
        """
        self._created_by = created_by

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
        if not isinstance(other, ShowRemediationConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
