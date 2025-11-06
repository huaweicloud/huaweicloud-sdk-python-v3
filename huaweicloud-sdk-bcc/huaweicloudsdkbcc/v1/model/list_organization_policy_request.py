# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationPolicyRequest:

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
        'limit': 'int',
        'offset': 'int',
        'operation_type': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'limit': 'limit',
        'offset': 'offset',
        'operation_type': 'operation_type'
    }

    def __init__(self, domain_id=None, limit=None, offset=None, operation_type=None):
        r"""ListOrganizationPolicyRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param limit: 分页limit
        :type limit: int
        :param offset: 分页offset
        :type offset: int
        :param operation_type: 组织策略类型，取值范围：backup：备份，replication：复制
        :type operation_type: str
        """
        
        

        self._domain_id = None
        self._limit = None
        self._offset = None
        self._operation_type = None
        self.discriminator = None

        self.domain_id = domain_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if operation_type is not None:
            self.operation_type = operation_type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListOrganizationPolicyRequest.

        账号ID

        :return: The domain_id of this ListOrganizationPolicyRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListOrganizationPolicyRequest.

        账号ID

        :param domain_id: The domain_id of this ListOrganizationPolicyRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def limit(self):
        r"""Gets the limit of this ListOrganizationPolicyRequest.

        分页limit

        :return: The limit of this ListOrganizationPolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOrganizationPolicyRequest.

        分页limit

        :param limit: The limit of this ListOrganizationPolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListOrganizationPolicyRequest.

        分页offset

        :return: The offset of this ListOrganizationPolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOrganizationPolicyRequest.

        分页offset

        :param offset: The offset of this ListOrganizationPolicyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def operation_type(self):
        r"""Gets the operation_type of this ListOrganizationPolicyRequest.

        组织策略类型，取值范围：backup：备份，replication：复制

        :return: The operation_type of this ListOrganizationPolicyRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this ListOrganizationPolicyRequest.

        组织策略类型，取值范围：backup：备份，replication：复制

        :param operation_type: The operation_type of this ListOrganizationPolicyRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

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
        if not isinstance(other, ListOrganizationPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
