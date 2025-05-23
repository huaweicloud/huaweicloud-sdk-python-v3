# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComponentWithConfigurationRequestBodySpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime': 'str',
        'replica': 'int',
        'build': 'Build',
        'source': 'Source',
        'resource_limit': 'ResourceLimit',
        'image_url': 'str'
    }

    attribute_map = {
        'runtime': 'runtime',
        'replica': 'replica',
        'build': 'build',
        'source': 'source',
        'resource_limit': 'resource_limit',
        'image_url': 'image_url'
    }

    def __init__(self, runtime=None, replica=None, build=None, source=None, resource_limit=None, image_url=None):
        r"""CreateComponentWithConfigurationRequestBodySpec

        The model defined in huaweicloud sdk

        :param runtime: 语言/运行时。
        :type runtime: str
        :param replica: 实例个数。
        :type replica: int
        :param build: 
        :type build: :class:`huaweicloudsdkcae.v1.Build`
        :param source: 
        :type source: :class:`huaweicloudsdkcae.v1.Source`
        :param resource_limit: 
        :type resource_limit: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        :param image_url: 镜像地址。
        :type image_url: str
        """
        
        

        self._runtime = None
        self._replica = None
        self._build = None
        self._source = None
        self._resource_limit = None
        self._image_url = None
        self.discriminator = None

        self.runtime = runtime
        self.replica = replica
        if build is not None:
            self.build = build
        self.source = source
        self.resource_limit = resource_limit
        if image_url is not None:
            self.image_url = image_url

    @property
    def runtime(self):
        r"""Gets the runtime of this CreateComponentWithConfigurationRequestBodySpec.

        语言/运行时。

        :return: The runtime of this CreateComponentWithConfigurationRequestBodySpec.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this CreateComponentWithConfigurationRequestBodySpec.

        语言/运行时。

        :param runtime: The runtime of this CreateComponentWithConfigurationRequestBodySpec.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def replica(self):
        r"""Gets the replica of this CreateComponentWithConfigurationRequestBodySpec.

        实例个数。

        :return: The replica of this CreateComponentWithConfigurationRequestBodySpec.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        r"""Sets the replica of this CreateComponentWithConfigurationRequestBodySpec.

        实例个数。

        :param replica: The replica of this CreateComponentWithConfigurationRequestBodySpec.
        :type replica: int
        """
        self._replica = replica

    @property
    def build(self):
        r"""Gets the build of this CreateComponentWithConfigurationRequestBodySpec.

        :return: The build of this CreateComponentWithConfigurationRequestBodySpec.
        :rtype: :class:`huaweicloudsdkcae.v1.Build`
        """
        return self._build

    @build.setter
    def build(self, build):
        r"""Sets the build of this CreateComponentWithConfigurationRequestBodySpec.

        :param build: The build of this CreateComponentWithConfigurationRequestBodySpec.
        :type build: :class:`huaweicloudsdkcae.v1.Build`
        """
        self._build = build

    @property
    def source(self):
        r"""Gets the source of this CreateComponentWithConfigurationRequestBodySpec.

        :return: The source of this CreateComponentWithConfigurationRequestBodySpec.
        :rtype: :class:`huaweicloudsdkcae.v1.Source`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateComponentWithConfigurationRequestBodySpec.

        :param source: The source of this CreateComponentWithConfigurationRequestBodySpec.
        :type source: :class:`huaweicloudsdkcae.v1.Source`
        """
        self._source = source

    @property
    def resource_limit(self):
        r"""Gets the resource_limit of this CreateComponentWithConfigurationRequestBodySpec.

        :return: The resource_limit of this CreateComponentWithConfigurationRequestBodySpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        """
        return self._resource_limit

    @resource_limit.setter
    def resource_limit(self, resource_limit):
        r"""Sets the resource_limit of this CreateComponentWithConfigurationRequestBodySpec.

        :param resource_limit: The resource_limit of this CreateComponentWithConfigurationRequestBodySpec.
        :type resource_limit: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        """
        self._resource_limit = resource_limit

    @property
    def image_url(self):
        r"""Gets the image_url of this CreateComponentWithConfigurationRequestBodySpec.

        镜像地址。

        :return: The image_url of this CreateComponentWithConfigurationRequestBodySpec.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this CreateComponentWithConfigurationRequestBodySpec.

        镜像地址。

        :param image_url: The image_url of this CreateComponentWithConfigurationRequestBodySpec.
        :type image_url: str
        """
        self._image_url = image_url

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
        if not isinstance(other, CreateComponentWithConfigurationRequestBodySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
