# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePluginResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_pull_policy': 'str',
        'image_pull_secret': 'str',
        'phase': 'str',
        'plugin_config': 'object',
        'plugin_name': 'str',
        'priority': 'int',
        'sha256': 'str',
        'url': 'str',
        'verification_key': 'str'
    }

    attribute_map = {
        'image_pull_policy': 'imagePullPolicy',
        'image_pull_secret': 'imagePullSecret',
        'phase': 'phase',
        'plugin_config': 'pluginConfig',
        'plugin_name': 'pluginName',
        'priority': 'priority',
        'sha256': 'sha256',
        'url': 'url',
        'verification_key': 'verificationKey'
    }

    def __init__(self, image_pull_policy=None, image_pull_secret=None, phase=None, plugin_config=None, plugin_name=None, priority=None, sha256=None, url=None, verification_key=None):
        r"""CreatePluginResponse

        The model defined in huaweicloud sdk

        :param image_pull_policy: 拉取OCI镜像的行为
        :type image_pull_policy: str
        :param image_pull_secret: 拉取OCI 镜像的凭据
        :type image_pull_secret: str
        :param phase: 确定插件将在过滤器链中的何处注入。
        :type phase: str
        :param plugin_config: 传递给插件的配置。
        :type plugin_config: object
        :param plugin_name: 插件名。
        :type plugin_name: str
        :param priority: 插件的调用优先级。
        :type priority: int
        :param sha256: 用于校验插件和容器的校验和。
        :type sha256: str
        :param url: 插件或容器的下载地址。
        :type url: str
        :param verification_key: 校验值。
        :type verification_key: str
        """
        
        super(CreatePluginResponse, self).__init__()

        self._image_pull_policy = None
        self._image_pull_secret = None
        self._phase = None
        self._plugin_config = None
        self._plugin_name = None
        self._priority = None
        self._sha256 = None
        self._url = None
        self._verification_key = None
        self.discriminator = None

        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_pull_secret is not None:
            self.image_pull_secret = image_pull_secret
        if phase is not None:
            self.phase = phase
        if plugin_config is not None:
            self.plugin_config = plugin_config
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if priority is not None:
            self.priority = priority
        if sha256 is not None:
            self.sha256 = sha256
        if url is not None:
            self.url = url
        if verification_key is not None:
            self.verification_key = verification_key

    @property
    def image_pull_policy(self):
        r"""Gets the image_pull_policy of this CreatePluginResponse.

        拉取OCI镜像的行为

        :return: The image_pull_policy of this CreatePluginResponse.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        r"""Sets the image_pull_policy of this CreatePluginResponse.

        拉取OCI镜像的行为

        :param image_pull_policy: The image_pull_policy of this CreatePluginResponse.
        :type image_pull_policy: str
        """
        self._image_pull_policy = image_pull_policy

    @property
    def image_pull_secret(self):
        r"""Gets the image_pull_secret of this CreatePluginResponse.

        拉取OCI 镜像的凭据

        :return: The image_pull_secret of this CreatePluginResponse.
        :rtype: str
        """
        return self._image_pull_secret

    @image_pull_secret.setter
    def image_pull_secret(self, image_pull_secret):
        r"""Sets the image_pull_secret of this CreatePluginResponse.

        拉取OCI 镜像的凭据

        :param image_pull_secret: The image_pull_secret of this CreatePluginResponse.
        :type image_pull_secret: str
        """
        self._image_pull_secret = image_pull_secret

    @property
    def phase(self):
        r"""Gets the phase of this CreatePluginResponse.

        确定插件将在过滤器链中的何处注入。

        :return: The phase of this CreatePluginResponse.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this CreatePluginResponse.

        确定插件将在过滤器链中的何处注入。

        :param phase: The phase of this CreatePluginResponse.
        :type phase: str
        """
        self._phase = phase

    @property
    def plugin_config(self):
        r"""Gets the plugin_config of this CreatePluginResponse.

        传递给插件的配置。

        :return: The plugin_config of this CreatePluginResponse.
        :rtype: object
        """
        return self._plugin_config

    @plugin_config.setter
    def plugin_config(self, plugin_config):
        r"""Sets the plugin_config of this CreatePluginResponse.

        传递给插件的配置。

        :param plugin_config: The plugin_config of this CreatePluginResponse.
        :type plugin_config: object
        """
        self._plugin_config = plugin_config

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this CreatePluginResponse.

        插件名。

        :return: The plugin_name of this CreatePluginResponse.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this CreatePluginResponse.

        插件名。

        :param plugin_name: The plugin_name of this CreatePluginResponse.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def priority(self):
        r"""Gets the priority of this CreatePluginResponse.

        插件的调用优先级。

        :return: The priority of this CreatePluginResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreatePluginResponse.

        插件的调用优先级。

        :param priority: The priority of this CreatePluginResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def sha256(self):
        r"""Gets the sha256 of this CreatePluginResponse.

        用于校验插件和容器的校验和。

        :return: The sha256 of this CreatePluginResponse.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        r"""Sets the sha256 of this CreatePluginResponse.

        用于校验插件和容器的校验和。

        :param sha256: The sha256 of this CreatePluginResponse.
        :type sha256: str
        """
        self._sha256 = sha256

    @property
    def url(self):
        r"""Gets the url of this CreatePluginResponse.

        插件或容器的下载地址。

        :return: The url of this CreatePluginResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreatePluginResponse.

        插件或容器的下载地址。

        :param url: The url of this CreatePluginResponse.
        :type url: str
        """
        self._url = url

    @property
    def verification_key(self):
        r"""Gets the verification_key of this CreatePluginResponse.

        校验值。

        :return: The verification_key of this CreatePluginResponse.
        :rtype: str
        """
        return self._verification_key

    @verification_key.setter
    def verification_key(self, verification_key):
        r"""Sets the verification_key of this CreatePluginResponse.

        校验值。

        :param verification_key: The verification_key of this CreatePluginResponse.
        :type verification_key: str
        """
        self._verification_key = verification_key

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
        if not isinstance(other, CreatePluginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
