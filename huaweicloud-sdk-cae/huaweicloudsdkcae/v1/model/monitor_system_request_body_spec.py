# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MonitorSystemRequestBodySpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'instrumentation': 'str',
        'access_key': 'str',
        'access_value': 'str',
        'access_token': 'str',
        'apm_application': 'str',
        'version': 'str',
        'image_pull_policy': 'str'
    }

    attribute_map = {
        'type': 'type',
        'instrumentation': 'instrumentation',
        'access_key': 'access_key',
        'access_value': 'access_value',
        'access_token': 'access_token',
        'apm_application': 'apm_application',
        'version': 'version',
        'image_pull_policy': 'image_pull_policy'
    }

    def __init__(self, type=None, instrumentation=None, access_key=None, access_value=None, access_token=None, apm_application=None, version=None, image_pull_policy=None):
        """MonitorSystemRequestBodySpec

        The model defined in huaweicloud sdk

        :param type: 采集方式，包括apm2和opentelemetry。
        :type type: str
        :param instrumentation: 探针注入方式，包括automatic和manual。
        :type instrumentation: str
        :param access_key: apm2 access_key。
        :type access_key: str
        :param access_value: apm2 access_value。
        :type access_value: str
        :param access_token: apm opentelemetry接入token。
        :type access_token: str
        :param apm_application: apm应用名。
        :type apm_application: str
        :param version: apm-agent/opentelemetry-agent探针版本。
        :type version: str
        :param image_pull_policy: 探针镜像更新策略。
        :type image_pull_policy: str
        """
        
        

        self._type = None
        self._instrumentation = None
        self._access_key = None
        self._access_value = None
        self._access_token = None
        self._apm_application = None
        self._version = None
        self._image_pull_policy = None
        self.discriminator = None

        self.type = type
        self.instrumentation = instrumentation
        if access_key is not None:
            self.access_key = access_key
        if access_value is not None:
            self.access_value = access_value
        if access_token is not None:
            self.access_token = access_token
        self.apm_application = apm_application
        self.version = version
        self.image_pull_policy = image_pull_policy

    @property
    def type(self):
        """Gets the type of this MonitorSystemRequestBodySpec.

        采集方式，包括apm2和opentelemetry。

        :return: The type of this MonitorSystemRequestBodySpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MonitorSystemRequestBodySpec.

        采集方式，包括apm2和opentelemetry。

        :param type: The type of this MonitorSystemRequestBodySpec.
        :type type: str
        """
        self._type = type

    @property
    def instrumentation(self):
        """Gets the instrumentation of this MonitorSystemRequestBodySpec.

        探针注入方式，包括automatic和manual。

        :return: The instrumentation of this MonitorSystemRequestBodySpec.
        :rtype: str
        """
        return self._instrumentation

    @instrumentation.setter
    def instrumentation(self, instrumentation):
        """Sets the instrumentation of this MonitorSystemRequestBodySpec.

        探针注入方式，包括automatic和manual。

        :param instrumentation: The instrumentation of this MonitorSystemRequestBodySpec.
        :type instrumentation: str
        """
        self._instrumentation = instrumentation

    @property
    def access_key(self):
        """Gets the access_key of this MonitorSystemRequestBodySpec.

        apm2 access_key。

        :return: The access_key of this MonitorSystemRequestBodySpec.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this MonitorSystemRequestBodySpec.

        apm2 access_key。

        :param access_key: The access_key of this MonitorSystemRequestBodySpec.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def access_value(self):
        """Gets the access_value of this MonitorSystemRequestBodySpec.

        apm2 access_value。

        :return: The access_value of this MonitorSystemRequestBodySpec.
        :rtype: str
        """
        return self._access_value

    @access_value.setter
    def access_value(self, access_value):
        """Sets the access_value of this MonitorSystemRequestBodySpec.

        apm2 access_value。

        :param access_value: The access_value of this MonitorSystemRequestBodySpec.
        :type access_value: str
        """
        self._access_value = access_value

    @property
    def access_token(self):
        """Gets the access_token of this MonitorSystemRequestBodySpec.

        apm opentelemetry接入token。

        :return: The access_token of this MonitorSystemRequestBodySpec.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this MonitorSystemRequestBodySpec.

        apm opentelemetry接入token。

        :param access_token: The access_token of this MonitorSystemRequestBodySpec.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def apm_application(self):
        """Gets the apm_application of this MonitorSystemRequestBodySpec.

        apm应用名。

        :return: The apm_application of this MonitorSystemRequestBodySpec.
        :rtype: str
        """
        return self._apm_application

    @apm_application.setter
    def apm_application(self, apm_application):
        """Sets the apm_application of this MonitorSystemRequestBodySpec.

        apm应用名。

        :param apm_application: The apm_application of this MonitorSystemRequestBodySpec.
        :type apm_application: str
        """
        self._apm_application = apm_application

    @property
    def version(self):
        """Gets the version of this MonitorSystemRequestBodySpec.

        apm-agent/opentelemetry-agent探针版本。

        :return: The version of this MonitorSystemRequestBodySpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MonitorSystemRequestBodySpec.

        apm-agent/opentelemetry-agent探针版本。

        :param version: The version of this MonitorSystemRequestBodySpec.
        :type version: str
        """
        self._version = version

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this MonitorSystemRequestBodySpec.

        探针镜像更新策略。

        :return: The image_pull_policy of this MonitorSystemRequestBodySpec.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this MonitorSystemRequestBodySpec.

        探针镜像更新策略。

        :param image_pull_policy: The image_pull_policy of this MonitorSystemRequestBodySpec.
        :type image_pull_policy: str
        """
        self._image_pull_policy = image_pull_policy

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
        if not isinstance(other, MonitorSystemRequestBodySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
