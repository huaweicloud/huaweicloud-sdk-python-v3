# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePrivateProviderVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_request_id': 'str',
        'provider_name': 'str',
        'provider_version': 'str',
        'provider_id': 'str'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'provider_name': 'provider_name',
        'provider_version': 'provider_version',
        'provider_id': 'provider_id'
    }

    def __init__(self, client_request_id=None, provider_name=None, provider_version=None, provider_id=None):
        r"""DeletePrivateProviderVersionRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一Id，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param provider_name: 私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。
        :type provider_name: str
        :param provider_version: provider的版本号。版本号遵循语义化版本号（Semantic Version），为用户自定义
        :type provider_version: str
        :param provider_id: 私有provider的唯一Id，由资源编排服务随机生成，为UUID。  由于私有provider名称仅仅在同一时间下唯一，即用户允许先生成一个叫helloword的私有provider，删除，再重新创建一个同名私有provider。  对于团队并行开发，用户可能希望确保，当前我操作的私有provider就是我以为的那个，而不是由其他队友删除后创建的同名私有provider。  因此，使用ID就可以做到强匹配。资源编排服务保证每次创建私有provider所对应的Id都不相同。  如果给予的provider_id和当前私有provider的Id不一致，则返回400。
        :type provider_id: str
        """
        
        

        self._client_request_id = None
        self._provider_name = None
        self._provider_version = None
        self._provider_id = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.provider_name = provider_name
        self.provider_version = provider_version
        if provider_id is not None:
            self.provider_id = provider_id

    @property
    def client_request_id(self):
        r"""Gets the client_request_id of this DeletePrivateProviderVersionRequest.

        用户指定的，对于此请求的唯一Id，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this DeletePrivateProviderVersionRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        r"""Sets the client_request_id of this DeletePrivateProviderVersionRequest.

        用户指定的，对于此请求的唯一Id，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this DeletePrivateProviderVersionRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def provider_name(self):
        r"""Gets the provider_name of this DeletePrivateProviderVersionRequest.

        私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。

        :return: The provider_name of this DeletePrivateProviderVersionRequest.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this DeletePrivateProviderVersionRequest.

        私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。

        :param provider_name: The provider_name of this DeletePrivateProviderVersionRequest.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def provider_version(self):
        r"""Gets the provider_version of this DeletePrivateProviderVersionRequest.

        provider的版本号。版本号遵循语义化版本号（Semantic Version），为用户自定义

        :return: The provider_version of this DeletePrivateProviderVersionRequest.
        :rtype: str
        """
        return self._provider_version

    @provider_version.setter
    def provider_version(self, provider_version):
        r"""Sets the provider_version of this DeletePrivateProviderVersionRequest.

        provider的版本号。版本号遵循语义化版本号（Semantic Version），为用户自定义

        :param provider_version: The provider_version of this DeletePrivateProviderVersionRequest.
        :type provider_version: str
        """
        self._provider_version = provider_version

    @property
    def provider_id(self):
        r"""Gets the provider_id of this DeletePrivateProviderVersionRequest.

        私有provider的唯一Id，由资源编排服务随机生成，为UUID。  由于私有provider名称仅仅在同一时间下唯一，即用户允许先生成一个叫helloword的私有provider，删除，再重新创建一个同名私有provider。  对于团队并行开发，用户可能希望确保，当前我操作的私有provider就是我以为的那个，而不是由其他队友删除后创建的同名私有provider。  因此，使用ID就可以做到强匹配。资源编排服务保证每次创建私有provider所对应的Id都不相同。  如果给予的provider_id和当前私有provider的Id不一致，则返回400。

        :return: The provider_id of this DeletePrivateProviderVersionRequest.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this DeletePrivateProviderVersionRequest.

        私有provider的唯一Id，由资源编排服务随机生成，为UUID。  由于私有provider名称仅仅在同一时间下唯一，即用户允许先生成一个叫helloword的私有provider，删除，再重新创建一个同名私有provider。  对于团队并行开发，用户可能希望确保，当前我操作的私有provider就是我以为的那个，而不是由其他队友删除后创建的同名私有provider。  因此，使用ID就可以做到强匹配。资源编排服务保证每次创建私有provider所对应的Id都不相同。  如果给予的provider_id和当前私有provider的Id不一致，则返回400。

        :param provider_id: The provider_id of this DeletePrivateProviderVersionRequest.
        :type provider_id: str
        """
        self._provider_id = provider_id

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
        if not isinstance(other, DeletePrivateProviderVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
