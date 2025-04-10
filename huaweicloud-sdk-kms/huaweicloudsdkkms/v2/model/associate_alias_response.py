# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateAliasResponse(SdkResponse):

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
        'key_id': 'str',
        'alias': 'str',
        'alias_urn': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'key_id': 'key_id',
        'alias': 'alias',
        'alias_urn': 'alias_urn',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, domain_id=None, key_id=None, alias=None, alias_urn=None, create_time=None, update_time=None):
        r"""AssociateAliasResponse

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param key_id: 密钥ID
        :type key_id: str
        :param alias: 别名
        :type alias: str
        :param alias_urn: 别名资源定位符
        :type alias_urn: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        super(AssociateAliasResponse, self).__init__()

        self._domain_id = None
        self._key_id = None
        self._alias = None
        self._alias_urn = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if key_id is not None:
            self.key_id = key_id
        if alias is not None:
            self.alias = alias
        if alias_urn is not None:
            self.alias_urn = alias_urn
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this AssociateAliasResponse.

        账号ID

        :return: The domain_id of this AssociateAliasResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this AssociateAliasResponse.

        账号ID

        :param domain_id: The domain_id of this AssociateAliasResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def key_id(self):
        r"""Gets the key_id of this AssociateAliasResponse.

        密钥ID

        :return: The key_id of this AssociateAliasResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this AssociateAliasResponse.

        密钥ID

        :param key_id: The key_id of this AssociateAliasResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def alias(self):
        r"""Gets the alias of this AssociateAliasResponse.

        别名

        :return: The alias of this AssociateAliasResponse.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this AssociateAliasResponse.

        别名

        :param alias: The alias of this AssociateAliasResponse.
        :type alias: str
        """
        self._alias = alias

    @property
    def alias_urn(self):
        r"""Gets the alias_urn of this AssociateAliasResponse.

        别名资源定位符

        :return: The alias_urn of this AssociateAliasResponse.
        :rtype: str
        """
        return self._alias_urn

    @alias_urn.setter
    def alias_urn(self, alias_urn):
        r"""Sets the alias_urn of this AssociateAliasResponse.

        别名资源定位符

        :param alias_urn: The alias_urn of this AssociateAliasResponse.
        :type alias_urn: str
        """
        self._alias_urn = alias_urn

    @property
    def create_time(self):
        r"""Gets the create_time of this AssociateAliasResponse.

        创建时间

        :return: The create_time of this AssociateAliasResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AssociateAliasResponse.

        创建时间

        :param create_time: The create_time of this AssociateAliasResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AssociateAliasResponse.

        更新时间

        :return: The update_time of this AssociateAliasResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AssociateAliasResponse.

        更新时间

        :param update_time: The update_time of this AssociateAliasResponse.
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
        if not isinstance(other, AssociateAliasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
