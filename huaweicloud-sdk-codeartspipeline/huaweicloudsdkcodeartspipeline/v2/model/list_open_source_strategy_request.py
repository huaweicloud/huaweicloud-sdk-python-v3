# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpenSourceStrategyRequest:

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
        'name': 'str',
        'creator_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'name': 'name',
        'creator_name': 'creator_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, domain_id=None, name=None, creator_name=None, limit=None, offset=None):
        """ListOpenSourceStrategyRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param name: 策略名称
        :type name: str
        :param creator_name: 策略创建人名称
        :type creator_name: str
        :param limit: 分页参数，默认15
        :type limit: int
        :param offset: 分页参数，默认0
        :type offset: int
        """
        
        

        self._domain_id = None
        self._name = None
        self._creator_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.domain_id = domain_id
        if name is not None:
            self.name = name
        if creator_name is not None:
            self.creator_name = creator_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def domain_id(self):
        """Gets the domain_id of this ListOpenSourceStrategyRequest.

        租户ID

        :return: The domain_id of this ListOpenSourceStrategyRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListOpenSourceStrategyRequest.

        租户ID

        :param domain_id: The domain_id of this ListOpenSourceStrategyRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this ListOpenSourceStrategyRequest.

        策略名称

        :return: The name of this ListOpenSourceStrategyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListOpenSourceStrategyRequest.

        策略名称

        :param name: The name of this ListOpenSourceStrategyRequest.
        :type name: str
        """
        self._name = name

    @property
    def creator_name(self):
        """Gets the creator_name of this ListOpenSourceStrategyRequest.

        策略创建人名称

        :return: The creator_name of this ListOpenSourceStrategyRequest.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ListOpenSourceStrategyRequest.

        策略创建人名称

        :param creator_name: The creator_name of this ListOpenSourceStrategyRequest.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def limit(self):
        """Gets the limit of this ListOpenSourceStrategyRequest.

        分页参数，默认15

        :return: The limit of this ListOpenSourceStrategyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListOpenSourceStrategyRequest.

        分页参数，默认15

        :param limit: The limit of this ListOpenSourceStrategyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListOpenSourceStrategyRequest.

        分页参数，默认0

        :return: The offset of this ListOpenSourceStrategyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListOpenSourceStrategyRequest.

        分页参数，默认0

        :param offset: The offset of this ListOpenSourceStrategyRequest.
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
        if not isinstance(other, ListOpenSourceStrategyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
