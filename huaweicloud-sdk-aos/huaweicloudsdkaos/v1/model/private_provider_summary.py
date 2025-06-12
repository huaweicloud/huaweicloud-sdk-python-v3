# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateProviderSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_id': 'str',
        'provider_name': 'str',
        'provider_description': 'str',
        'provider_source': 'str',
        'provider_agency_urn': 'str',
        'provider_agency_name': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'provider_id': 'provider_id',
        'provider_name': 'provider_name',
        'provider_description': 'provider_description',
        'provider_source': 'provider_source',
        'provider_agency_urn': 'provider_agency_urn',
        'provider_agency_name': 'provider_agency_name',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, provider_id=None, provider_name=None, provider_description=None, provider_source=None, provider_agency_urn=None, provider_agency_name=None, create_time=None, update_time=None):
        r"""PrivateProviderSummary

        The model defined in huaweicloud sdk

        :param provider_id: 私有provider（private-provider）的唯一Id。  此Id由资源编排服务在生成provider的时候生成，为UUID。  由于私有provider名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有provider，删除，再重新创建一个同名私有provider。  对于团队并行开发，用户可能希望确保，当前我操作的私有provider就是我以为的那个，而不是其他队友删除后创建的同名私有provider。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有provider所对应的Id都不相同，更新不会影响Id。如果给予的provider_id和当前provider的Id不一致，则返回400
        :type provider_id: str
        :param provider_name: 私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。  按照HCL最佳实践，该名称推荐为在模板中定义的provider的本地名称（local_name）。  创建私有Provider（CreatePrivateProvider）API 还会以 “huawei.com/private-provider”为固定前缀，并以“huawei.com/private-provider/{provider_name}”的形式返回provider_source字段。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。
        :type provider_name: str
        :param provider_description: 私有provider（private-provider）的描述。可用于客户识别被管理的私有provider。
        :type provider_description: str
        :param provider_source: 用户使用私有provider，在Terraform模板中定义required_providers信息时，需要指明的source参数。  该参数按照“huawei.com/private-provider/{provider_name}”的形式拼接。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。
        :type provider_source: str
        :param provider_agency_urn: 自定义provider所绑定的IAM委托URN，provider_agency_name和provider_agency_urn最多只能提供一个。
        :type provider_agency_urn: str
        :param provider_agency_name: 自定义provider所绑定的IAM委托名称，provider_agency_name和provider_agency_urn最多只能提供一个。
        :type provider_agency_name: str
        :param create_time: 私有provider（private-provider）的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        :param update_time: 私有provider（private-provider）的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type update_time: str
        """
        
        

        self._provider_id = None
        self._provider_name = None
        self._provider_description = None
        self._provider_source = None
        self._provider_agency_urn = None
        self._provider_agency_name = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if provider_id is not None:
            self.provider_id = provider_id
        self.provider_name = provider_name
        if provider_description is not None:
            self.provider_description = provider_description
        if provider_source is not None:
            self.provider_source = provider_source
        if provider_agency_urn is not None:
            self.provider_agency_urn = provider_agency_urn
        if provider_agency_name is not None:
            self.provider_agency_name = provider_agency_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def provider_id(self):
        r"""Gets the provider_id of this PrivateProviderSummary.

        私有provider（private-provider）的唯一Id。  此Id由资源编排服务在生成provider的时候生成，为UUID。  由于私有provider名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有provider，删除，再重新创建一个同名私有provider。  对于团队并行开发，用户可能希望确保，当前我操作的私有provider就是我以为的那个，而不是其他队友删除后创建的同名私有provider。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有provider所对应的Id都不相同，更新不会影响Id。如果给予的provider_id和当前provider的Id不一致，则返回400

        :return: The provider_id of this PrivateProviderSummary.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this PrivateProviderSummary.

        私有provider（private-provider）的唯一Id。  此Id由资源编排服务在生成provider的时候生成，为UUID。  由于私有provider名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有provider，删除，再重新创建一个同名私有provider。  对于团队并行开发，用户可能希望确保，当前我操作的私有provider就是我以为的那个，而不是其他队友删除后创建的同名私有provider。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有provider所对应的Id都不相同，更新不会影响Id。如果给予的provider_id和当前provider的Id不一致，则返回400

        :param provider_id: The provider_id of this PrivateProviderSummary.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def provider_name(self):
        r"""Gets the provider_name of this PrivateProviderSummary.

        私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。  按照HCL最佳实践，该名称推荐为在模板中定义的provider的本地名称（local_name）。  创建私有Provider（CreatePrivateProvider）API 还会以 “huawei.com/private-provider”为固定前缀，并以“huawei.com/private-provider/{provider_name}”的形式返回provider_source字段。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。

        :return: The provider_name of this PrivateProviderSummary.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this PrivateProviderSummary.

        私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。  按照HCL最佳实践，该名称推荐为在模板中定义的provider的本地名称（local_name）。  创建私有Provider（CreatePrivateProvider）API 还会以 “huawei.com/private-provider”为固定前缀，并以“huawei.com/private-provider/{provider_name}”的形式返回provider_source字段。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。

        :param provider_name: The provider_name of this PrivateProviderSummary.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def provider_description(self):
        r"""Gets the provider_description of this PrivateProviderSummary.

        私有provider（private-provider）的描述。可用于客户识别被管理的私有provider。

        :return: The provider_description of this PrivateProviderSummary.
        :rtype: str
        """
        return self._provider_description

    @provider_description.setter
    def provider_description(self, provider_description):
        r"""Sets the provider_description of this PrivateProviderSummary.

        私有provider（private-provider）的描述。可用于客户识别被管理的私有provider。

        :param provider_description: The provider_description of this PrivateProviderSummary.
        :type provider_description: str
        """
        self._provider_description = provider_description

    @property
    def provider_source(self):
        r"""Gets the provider_source of this PrivateProviderSummary.

        用户使用私有provider，在Terraform模板中定义required_providers信息时，需要指明的source参数。  该参数按照“huawei.com/private-provider/{provider_name}”的形式拼接。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。

        :return: The provider_source of this PrivateProviderSummary.
        :rtype: str
        """
        return self._provider_source

    @provider_source.setter
    def provider_source(self, provider_source):
        r"""Sets the provider_source of this PrivateProviderSummary.

        用户使用私有provider，在Terraform模板中定义required_providers信息时，需要指明的source参数。  该参数按照“huawei.com/private-provider/{provider_name}”的形式拼接。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。

        :param provider_source: The provider_source of this PrivateProviderSummary.
        :type provider_source: str
        """
        self._provider_source = provider_source

    @property
    def provider_agency_urn(self):
        r"""Gets the provider_agency_urn of this PrivateProviderSummary.

        自定义provider所绑定的IAM委托URN，provider_agency_name和provider_agency_urn最多只能提供一个。

        :return: The provider_agency_urn of this PrivateProviderSummary.
        :rtype: str
        """
        return self._provider_agency_urn

    @provider_agency_urn.setter
    def provider_agency_urn(self, provider_agency_urn):
        r"""Sets the provider_agency_urn of this PrivateProviderSummary.

        自定义provider所绑定的IAM委托URN，provider_agency_name和provider_agency_urn最多只能提供一个。

        :param provider_agency_urn: The provider_agency_urn of this PrivateProviderSummary.
        :type provider_agency_urn: str
        """
        self._provider_agency_urn = provider_agency_urn

    @property
    def provider_agency_name(self):
        r"""Gets the provider_agency_name of this PrivateProviderSummary.

        自定义provider所绑定的IAM委托名称，provider_agency_name和provider_agency_urn最多只能提供一个。

        :return: The provider_agency_name of this PrivateProviderSummary.
        :rtype: str
        """
        return self._provider_agency_name

    @provider_agency_name.setter
    def provider_agency_name(self, provider_agency_name):
        r"""Sets the provider_agency_name of this PrivateProviderSummary.

        自定义provider所绑定的IAM委托名称，provider_agency_name和provider_agency_urn最多只能提供一个。

        :param provider_agency_name: The provider_agency_name of this PrivateProviderSummary.
        :type provider_agency_name: str
        """
        self._provider_agency_name = provider_agency_name

    @property
    def create_time(self):
        r"""Gets the create_time of this PrivateProviderSummary.

        私有provider（private-provider）的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this PrivateProviderSummary.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PrivateProviderSummary.

        私有provider（private-provider）的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this PrivateProviderSummary.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this PrivateProviderSummary.

        私有provider（private-provider）的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The update_time of this PrivateProviderSummary.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PrivateProviderSummary.

        私有provider（private-provider）的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param update_time: The update_time of this PrivateProviderSummary.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, PrivateProviderSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
