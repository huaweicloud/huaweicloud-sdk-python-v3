# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceConsumerGroupMembersRequest:

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
        'group': 'str',
        'offset': 'int',
        'limit': 'int',
        'host': 'str',
        'member_id': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'group': 'group',
        'offset': 'offset',
        'limit': 'limit',
        'host': 'host',
        'member_id': 'member_id'
    }

    def __init__(self, engine=None, instance_id=None, group=None, offset=None, limit=None, host=None, member_id=None):
        r"""ListInstanceConsumerGroupMembersRequest

        The model defined in huaweicloud sdk

        :param engine: 引擎。
        :type engine: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param group: 消费组ID。
        :type group: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        :param limit: 当次查询返回的最大消费组成员个数，默认值为10，取值范围为1~50。
        :type limit: int
        :param host: 消费者地址。
        :type host: str
        :param member_id: 消费者ID。
        :type member_id: str
        """
        
        

        self._engine = None
        self._instance_id = None
        self._group = None
        self._offset = None
        self._limit = None
        self._host = None
        self._member_id = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        self.group = group
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if host is not None:
            self.host = host
        if member_id is not None:
            self.member_id = member_id

    @property
    def engine(self):
        r"""Gets the engine of this ListInstanceConsumerGroupMembersRequest.

        引擎。

        :return: The engine of this ListInstanceConsumerGroupMembersRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListInstanceConsumerGroupMembersRequest.

        引擎。

        :param engine: The engine of this ListInstanceConsumerGroupMembersRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceConsumerGroupMembersRequest.

        实例ID。

        :return: The instance_id of this ListInstanceConsumerGroupMembersRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceConsumerGroupMembersRequest.

        实例ID。

        :param instance_id: The instance_id of this ListInstanceConsumerGroupMembersRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        r"""Gets the group of this ListInstanceConsumerGroupMembersRequest.

        消费组ID。

        :return: The group of this ListInstanceConsumerGroupMembersRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ListInstanceConsumerGroupMembersRequest.

        消费组ID。

        :param group: The group of this ListInstanceConsumerGroupMembersRequest.
        :type group: str
        """
        self._group = group

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceConsumerGroupMembersRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListInstanceConsumerGroupMembersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceConsumerGroupMembersRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListInstanceConsumerGroupMembersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceConsumerGroupMembersRequest.

        当次查询返回的最大消费组成员个数，默认值为10，取值范围为1~50。

        :return: The limit of this ListInstanceConsumerGroupMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceConsumerGroupMembersRequest.

        当次查询返回的最大消费组成员个数，默认值为10，取值范围为1~50。

        :param limit: The limit of this ListInstanceConsumerGroupMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host(self):
        r"""Gets the host of this ListInstanceConsumerGroupMembersRequest.

        消费者地址。

        :return: The host of this ListInstanceConsumerGroupMembersRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ListInstanceConsumerGroupMembersRequest.

        消费者地址。

        :param host: The host of this ListInstanceConsumerGroupMembersRequest.
        :type host: str
        """
        self._host = host

    @property
    def member_id(self):
        r"""Gets the member_id of this ListInstanceConsumerGroupMembersRequest.

        消费者ID。

        :return: The member_id of this ListInstanceConsumerGroupMembersRequest.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this ListInstanceConsumerGroupMembersRequest.

        消费者ID。

        :param member_id: The member_id of this ListInstanceConsumerGroupMembersRequest.
        :type member_id: str
        """
        self._member_id = member_id

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
        if not isinstance(other, ListInstanceConsumerGroupMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
