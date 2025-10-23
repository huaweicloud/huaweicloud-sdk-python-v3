# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourcesLevelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'provider': 'str',
        'compliance_rule_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'provider': 'provider',
        'compliance_rule_id': 'compliance_rule_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, domain_id=None, provider=None, compliance_rule_id=None, limit=None, offset=None):
        r"""ListResourcesLevelRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param provider: 云服务类型：ecs-云服务器，evs-云硬盘，sfsturbo-高性能文件存储，workspace-云桌面，rds-关系型数据库，gaussdb-高斯数据库
        :type provider: str
        :param compliance_rule_id: 合规规则ID
        :type compliance_rule_id: str
        :param limit: 本次请求返回的最大记录条数。
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        

        self._domain_id = None
        self._provider = None
        self._compliance_rule_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.domain_id = domain_id
        if provider is not None:
            self.provider = provider
        if compliance_rule_id is not None:
            self.compliance_rule_id = compliance_rule_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListResourcesLevelRequest.

        账号ID

        :return: The domain_id of this ListResourcesLevelRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListResourcesLevelRequest.

        账号ID

        :param domain_id: The domain_id of this ListResourcesLevelRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def provider(self):
        r"""Gets the provider of this ListResourcesLevelRequest.

        云服务类型：ecs-云服务器，evs-云硬盘，sfsturbo-高性能文件存储，workspace-云桌面，rds-关系型数据库，gaussdb-高斯数据库

        :return: The provider of this ListResourcesLevelRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ListResourcesLevelRequest.

        云服务类型：ecs-云服务器，evs-云硬盘，sfsturbo-高性能文件存储，workspace-云桌面，rds-关系型数据库，gaussdb-高斯数据库

        :param provider: The provider of this ListResourcesLevelRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def compliance_rule_id(self):
        r"""Gets the compliance_rule_id of this ListResourcesLevelRequest.

        合规规则ID

        :return: The compliance_rule_id of this ListResourcesLevelRequest.
        :rtype: str
        """
        return self._compliance_rule_id

    @compliance_rule_id.setter
    def compliance_rule_id(self, compliance_rule_id):
        r"""Sets the compliance_rule_id of this ListResourcesLevelRequest.

        合规规则ID

        :param compliance_rule_id: The compliance_rule_id of this ListResourcesLevelRequest.
        :type compliance_rule_id: str
        """
        self._compliance_rule_id = compliance_rule_id

    @property
    def limit(self):
        r"""Gets the limit of this ListResourcesLevelRequest.

        本次请求返回的最大记录条数。

        :return: The limit of this ListResourcesLevelRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourcesLevelRequest.

        本次请求返回的最大记录条数。

        :param limit: The limit of this ListResourcesLevelRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListResourcesLevelRequest.

        偏移量

        :return: The offset of this ListResourcesLevelRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResourcesLevelRequest.

        偏移量

        :param offset: The offset of this ListResourcesLevelRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListResourcesLevelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
