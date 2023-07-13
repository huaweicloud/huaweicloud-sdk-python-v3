# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsumerConnectionsRequest:

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
        'group': 'str',
        'limit': 'int',
        'offset': 'int',
        'is_detail': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group': 'group',
        'limit': 'limit',
        'offset': 'offset',
        'is_detail': 'is_detail'
    }

    def __init__(self, instance_id=None, group=None, limit=None, offset=None, is_detail=None):
        """ShowConsumerConnectionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param group: 消费组名称
        :type group: str
        :param limit: 查询数量，取值范围为1~50。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        :param is_detail: 是否查询消费者详细列表，参数为“true”则表示查询详细列表，否则表示查询简易列表。
        :type is_detail: bool
        """
        
        

        self._instance_id = None
        self._group = None
        self._limit = None
        self._offset = None
        self._is_detail = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group = group
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if is_detail is not None:
            self.is_detail = is_detail

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowConsumerConnectionsRequest.

        实例ID

        :return: The instance_id of this ShowConsumerConnectionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowConsumerConnectionsRequest.

        实例ID

        :param instance_id: The instance_id of this ShowConsumerConnectionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        """Gets the group of this ShowConsumerConnectionsRequest.

        消费组名称

        :return: The group of this ShowConsumerConnectionsRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ShowConsumerConnectionsRequest.

        消费组名称

        :param group: The group of this ShowConsumerConnectionsRequest.
        :type group: str
        """
        self._group = group

    @property
    def limit(self):
        """Gets the limit of this ShowConsumerConnectionsRequest.

        查询数量，取值范围为1~50。

        :return: The limit of this ShowConsumerConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowConsumerConnectionsRequest.

        查询数量，取值范围为1~50。

        :param limit: The limit of this ShowConsumerConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowConsumerConnectionsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ShowConsumerConnectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowConsumerConnectionsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ShowConsumerConnectionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def is_detail(self):
        """Gets the is_detail of this ShowConsumerConnectionsRequest.

        是否查询消费者详细列表，参数为“true”则表示查询详细列表，否则表示查询简易列表。

        :return: The is_detail of this ShowConsumerConnectionsRequest.
        :rtype: bool
        """
        return self._is_detail

    @is_detail.setter
    def is_detail(self, is_detail):
        """Sets the is_detail of this ShowConsumerConnectionsRequest.

        是否查询消费者详细列表，参数为“true”则表示查询详细列表，否则表示查询简易列表。

        :param is_detail: The is_detail of this ShowConsumerConnectionsRequest.
        :type is_detail: bool
        """
        self._is_detail = is_detail

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
        if not isinstance(other, ShowConsumerConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
