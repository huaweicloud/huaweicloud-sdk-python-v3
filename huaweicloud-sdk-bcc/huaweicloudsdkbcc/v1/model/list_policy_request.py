# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyRequest:

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
        'region_id': 'str',
        'operation_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'operation_type': 'operation_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, domain_id=None, region_id=None, operation_type=None, limit=None, offset=None):
        r"""ListPolicyRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param operation_type: 策略类型，备份 backup, 复制 replication
        :type operation_type: str
        :param limit: 分页参数limit
        :type limit: int
        :param offset: 分页参数offset
        :type offset: int
        """
        
        

        self._domain_id = None
        self._region_id = None
        self._operation_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if operation_type is not None:
            self.operation_type = operation_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListPolicyRequest.

        账号ID

        :return: The domain_id of this ListPolicyRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListPolicyRequest.

        账号ID

        :param domain_id: The domain_id of this ListPolicyRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListPolicyRequest.

        区域ID

        :return: The region_id of this ListPolicyRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListPolicyRequest.

        区域ID

        :param region_id: The region_id of this ListPolicyRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def operation_type(self):
        r"""Gets the operation_type of this ListPolicyRequest.

        策略类型，备份 backup, 复制 replication

        :return: The operation_type of this ListPolicyRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this ListPolicyRequest.

        策略类型，备份 backup, 复制 replication

        :param operation_type: The operation_type of this ListPolicyRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def limit(self):
        r"""Gets the limit of this ListPolicyRequest.

        分页参数limit

        :return: The limit of this ListPolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPolicyRequest.

        分页参数limit

        :param limit: The limit of this ListPolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPolicyRequest.

        分页参数offset

        :return: The offset of this ListPolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPolicyRequest.

        分页参数offset

        :param offset: The offset of this ListPolicyRequest.
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
        if not isinstance(other, ListPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
