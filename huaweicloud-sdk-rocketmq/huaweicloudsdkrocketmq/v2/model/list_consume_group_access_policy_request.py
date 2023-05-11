# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConsumeGroupAccessPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'instance_id': 'str',
        'group_id': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'group_id': 'group_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, engine=None, instance_id=None, group_id=None, offset=None, limit=None):
        """ListConsumeGroupAccessPolicyRequest

        The model defined in huaweicloud sdk

        :param engine: 消息引擎。
        :type engine: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param group_id: 消费组。
        :type group_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: str
        :param limit: 查询数量。
        :type limit: str
        """
        
        

        self._engine = None
        self._instance_id = None
        self._group_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        self.group_id = group_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def engine(self):
        """Gets the engine of this ListConsumeGroupAccessPolicyRequest.

        消息引擎。

        :return: The engine of this ListConsumeGroupAccessPolicyRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ListConsumeGroupAccessPolicyRequest.

        消息引擎。

        :param engine: The engine of this ListConsumeGroupAccessPolicyRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        """Gets the instance_id of this ListConsumeGroupAccessPolicyRequest.

        实例ID。

        :return: The instance_id of this ListConsumeGroupAccessPolicyRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListConsumeGroupAccessPolicyRequest.

        实例ID。

        :param instance_id: The instance_id of this ListConsumeGroupAccessPolicyRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group_id(self):
        """Gets the group_id of this ListConsumeGroupAccessPolicyRequest.

        消费组。

        :return: The group_id of this ListConsumeGroupAccessPolicyRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListConsumeGroupAccessPolicyRequest.

        消费组。

        :param group_id: The group_id of this ListConsumeGroupAccessPolicyRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def offset(self):
        """Gets the offset of this ListConsumeGroupAccessPolicyRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListConsumeGroupAccessPolicyRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListConsumeGroupAccessPolicyRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListConsumeGroupAccessPolicyRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListConsumeGroupAccessPolicyRequest.

        查询数量。

        :return: The limit of this ListConsumeGroupAccessPolicyRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListConsumeGroupAccessPolicyRequest.

        查询数量。

        :param limit: The limit of this ListConsumeGroupAccessPolicyRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListConsumeGroupAccessPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
