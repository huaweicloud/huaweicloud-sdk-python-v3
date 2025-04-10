# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateComponentRequestSpec:

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
        'source': 'Source',
        'build': 'Build',
        'resource_limit': 'ResourceLimit',
        'replica': 'int'
    }

    attribute_map = {
        'runtime': 'runtime',
        'source': 'source',
        'build': 'build',
        'resource_limit': 'resource_limit',
        'replica': 'replica'
    }

    def __init__(self, runtime=None, source=None, build=None, resource_limit=None, replica=None):
        r"""UpdateComponentRequestSpec

        The model defined in huaweicloud sdk

        :param runtime: 语言/运行时。
        :type runtime: str
        :param source: 
        :type source: :class:`huaweicloudsdkcae.v1.Source`
        :param build: 
        :type build: :class:`huaweicloudsdkcae.v1.Build`
        :param resource_limit: 
        :type resource_limit: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        :param replica: 实例个数。
        :type replica: int
        """
        
        

        self._runtime = None
        self._source = None
        self._build = None
        self._resource_limit = None
        self._replica = None
        self.discriminator = None

        if runtime is not None:
            self.runtime = runtime
        if source is not None:
            self.source = source
        if build is not None:
            self.build = build
        self.resource_limit = resource_limit
        if replica is not None:
            self.replica = replica

    @property
    def runtime(self):
        r"""Gets the runtime of this UpdateComponentRequestSpec.

        语言/运行时。

        :return: The runtime of this UpdateComponentRequestSpec.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this UpdateComponentRequestSpec.

        语言/运行时。

        :param runtime: The runtime of this UpdateComponentRequestSpec.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def source(self):
        r"""Gets the source of this UpdateComponentRequestSpec.

        :return: The source of this UpdateComponentRequestSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.Source`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this UpdateComponentRequestSpec.

        :param source: The source of this UpdateComponentRequestSpec.
        :type source: :class:`huaweicloudsdkcae.v1.Source`
        """
        self._source = source

    @property
    def build(self):
        r"""Gets the build of this UpdateComponentRequestSpec.

        :return: The build of this UpdateComponentRequestSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.Build`
        """
        return self._build

    @build.setter
    def build(self, build):
        r"""Sets the build of this UpdateComponentRequestSpec.

        :param build: The build of this UpdateComponentRequestSpec.
        :type build: :class:`huaweicloudsdkcae.v1.Build`
        """
        self._build = build

    @property
    def resource_limit(self):
        r"""Gets the resource_limit of this UpdateComponentRequestSpec.

        :return: The resource_limit of this UpdateComponentRequestSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        """
        return self._resource_limit

    @resource_limit.setter
    def resource_limit(self, resource_limit):
        r"""Sets the resource_limit of this UpdateComponentRequestSpec.

        :param resource_limit: The resource_limit of this UpdateComponentRequestSpec.
        :type resource_limit: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        """
        self._resource_limit = resource_limit

    @property
    def replica(self):
        r"""Gets the replica of this UpdateComponentRequestSpec.

        实例个数。

        :return: The replica of this UpdateComponentRequestSpec.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        r"""Sets the replica of this UpdateComponentRequestSpec.

        实例个数。

        :param replica: The replica of this UpdateComponentRequestSpec.
        :type replica: int
        """
        self._replica = replica

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
        if not isinstance(other, UpdateComponentRequestSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
