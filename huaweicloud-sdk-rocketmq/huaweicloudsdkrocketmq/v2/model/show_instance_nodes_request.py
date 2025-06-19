# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceNodesRequest:

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
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, engine=None, instance_id=None, limit=None, offset=None):
        r"""ShowInstanceNodesRequest

        The model defined in huaweicloud sdk

        :param engine: 消息引擎类型。
        :type engine: str
        :param instance_id: 实例id。
        :type instance_id: str
        :param limit: 查询数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        """
        
        

        self._engine = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def engine(self):
        r"""Gets the engine of this ShowInstanceNodesRequest.

        消息引擎类型。

        :return: The engine of this ShowInstanceNodesRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ShowInstanceNodesRequest.

        消息引擎类型。

        :param engine: The engine of this ShowInstanceNodesRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceNodesRequest.

        实例id。

        :return: The instance_id of this ShowInstanceNodesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceNodesRequest.

        实例id。

        :param instance_id: The instance_id of this ShowInstanceNodesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstanceNodesRequest.

        查询数量。

        :return: The limit of this ShowInstanceNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstanceNodesRequest.

        查询数量。

        :param limit: The limit of this ShowInstanceNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowInstanceNodesRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ShowInstanceNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowInstanceNodesRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ShowInstanceNodesRequest.
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
        if not isinstance(other, ShowInstanceNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
