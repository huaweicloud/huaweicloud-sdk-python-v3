# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceLtCredentialsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'self_only': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'self_only': 'self_only'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, self_only=None):
        r"""ListInstanceLtCredentialsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param offset: 起始索引，默认为0。**注意：offset和limit参数需要配套使用。**
        :type offset: int
        :param limit: 返回条数，默认为100，最大值为100。**注意：offset和limit参数需要配套使用。**
        :type limit: int
        :param self_only: 值为false的时候，拥有te_admin角色的用户可以查询实例下所有的长期登录凭证，默认情况下只查询自己创建的长期登录凭证
        :type self_only: bool
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._self_only = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if self_only is not None:
            self.self_only = self_only

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceLtCredentialsRequest.

        企业仓库实例ID

        :return: The instance_id of this ListInstanceLtCredentialsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceLtCredentialsRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListInstanceLtCredentialsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceLtCredentialsRequest.

        起始索引，默认为0。**注意：offset和limit参数需要配套使用。**

        :return: The offset of this ListInstanceLtCredentialsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceLtCredentialsRequest.

        起始索引，默认为0。**注意：offset和limit参数需要配套使用。**

        :param offset: The offset of this ListInstanceLtCredentialsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceLtCredentialsRequest.

        返回条数，默认为100，最大值为100。**注意：offset和limit参数需要配套使用。**

        :return: The limit of this ListInstanceLtCredentialsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceLtCredentialsRequest.

        返回条数，默认为100，最大值为100。**注意：offset和limit参数需要配套使用。**

        :param limit: The limit of this ListInstanceLtCredentialsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def self_only(self):
        r"""Gets the self_only of this ListInstanceLtCredentialsRequest.

        值为false的时候，拥有te_admin角色的用户可以查询实例下所有的长期登录凭证，默认情况下只查询自己创建的长期登录凭证

        :return: The self_only of this ListInstanceLtCredentialsRequest.
        :rtype: bool
        """
        return self._self_only

    @self_only.setter
    def self_only(self, self_only):
        r"""Sets the self_only of this ListInstanceLtCredentialsRequest.

        值为false的时候，拥有te_admin角色的用户可以查询实例下所有的长期登录凭证，默认情况下只查询自己创建的长期登录凭证

        :param self_only: The self_only of this ListInstanceLtCredentialsRequest.
        :type self_only: bool
        """
        self._self_only = self_only

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
        if not isinstance(other, ListInstanceLtCredentialsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
