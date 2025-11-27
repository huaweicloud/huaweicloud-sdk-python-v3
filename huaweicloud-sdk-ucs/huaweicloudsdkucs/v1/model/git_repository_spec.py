# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GitRepositorySpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'ref': 'GitRepositoryRef',
        'secret_ref': 'LocalObjectReference',
        'interval': 'str',
        'timeout': 'str'
    }

    attribute_map = {
        'url': 'url',
        'ref': 'ref',
        'secret_ref': 'secretRef',
        'interval': 'interval',
        'timeout': 'timeout'
    }

    def __init__(self, url=None, ref=None, secret_ref=None, interval=None, timeout=None):
        r"""GitRepositorySpec

        The model defined in huaweicloud sdk

        :param url: Git仓库地址
        :type url: str
        :param ref: 
        :type ref: :class:`huaweicloudsdkucs.v1.GitRepositoryRef`
        :param secret_ref: 
        :type secret_ref: :class:`huaweicloudsdkucs.v1.LocalObjectReference`
        :param interval: 周期性检查仓库更新的时间间隔，格式如 \&quot;1m\&quot; 表示1分钟
        :type interval: str
        :param timeout: Git 操作（如克隆）的超时时间，默认60秒
        :type timeout: str
        """
        
        

        self._url = None
        self._ref = None
        self._secret_ref = None
        self._interval = None
        self._timeout = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if ref is not None:
            self.ref = ref
        if secret_ref is not None:
            self.secret_ref = secret_ref
        if interval is not None:
            self.interval = interval
        if timeout is not None:
            self.timeout = timeout

    @property
    def url(self):
        r"""Gets the url of this GitRepositorySpec.

        Git仓库地址

        :return: The url of this GitRepositorySpec.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this GitRepositorySpec.

        Git仓库地址

        :param url: The url of this GitRepositorySpec.
        :type url: str
        """
        self._url = url

    @property
    def ref(self):
        r"""Gets the ref of this GitRepositorySpec.

        :return: The ref of this GitRepositorySpec.
        :rtype: :class:`huaweicloudsdkucs.v1.GitRepositoryRef`
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this GitRepositorySpec.

        :param ref: The ref of this GitRepositorySpec.
        :type ref: :class:`huaweicloudsdkucs.v1.GitRepositoryRef`
        """
        self._ref = ref

    @property
    def secret_ref(self):
        r"""Gets the secret_ref of this GitRepositorySpec.

        :return: The secret_ref of this GitRepositorySpec.
        :rtype: :class:`huaweicloudsdkucs.v1.LocalObjectReference`
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        r"""Sets the secret_ref of this GitRepositorySpec.

        :param secret_ref: The secret_ref of this GitRepositorySpec.
        :type secret_ref: :class:`huaweicloudsdkucs.v1.LocalObjectReference`
        """
        self._secret_ref = secret_ref

    @property
    def interval(self):
        r"""Gets the interval of this GitRepositorySpec.

        周期性检查仓库更新的时间间隔，格式如 \"1m\" 表示1分钟

        :return: The interval of this GitRepositorySpec.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this GitRepositorySpec.

        周期性检查仓库更新的时间间隔，格式如 \"1m\" 表示1分钟

        :param interval: The interval of this GitRepositorySpec.
        :type interval: str
        """
        self._interval = interval

    @property
    def timeout(self):
        r"""Gets the timeout of this GitRepositorySpec.

        Git 操作（如克隆）的超时时间，默认60秒

        :return: The timeout of this GitRepositorySpec.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this GitRepositorySpec.

        Git 操作（如克隆）的超时时间，默认60秒

        :param timeout: The timeout of this GitRepositorySpec.
        :type timeout: str
        """
        self._timeout = timeout

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GitRepositorySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
