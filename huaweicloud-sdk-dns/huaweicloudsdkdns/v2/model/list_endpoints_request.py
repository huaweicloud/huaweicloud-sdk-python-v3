# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'direction': 'str',
        'vpc_id': 'str',
        'name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'direction': 'direction',
        'vpc_id': 'vpc_id',
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, direction=None, vpc_id=None, name=None, limit=None, offset=None):
        r"""ListEndpointsRequest

        The model defined in huaweicloud sdk

        :param direction: 终端节点方向。 取值： inbound，表示入站终端节点。 outbound，表示出站终端节点。
        :type direction: str
        :param vpc_id: 待查询的终端节点所属VPC的ID。
        :type vpc_id: str
        :param name: 终端节点名称。
        :type name: str
        :param limit: **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500
        :type limit: int
        :param offset: **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0
        :type offset: int
        """
        
        

        self._direction = None
        self._vpc_id = None
        self._name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.direction = direction
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def direction(self):
        r"""Gets the direction of this ListEndpointsRequest.

        终端节点方向。 取值： inbound，表示入站终端节点。 outbound，表示出站终端节点。

        :return: The direction of this ListEndpointsRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this ListEndpointsRequest.

        终端节点方向。 取值： inbound，表示入站终端节点。 outbound，表示出站终端节点。

        :param direction: The direction of this ListEndpointsRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListEndpointsRequest.

        待查询的终端节点所属VPC的ID。

        :return: The vpc_id of this ListEndpointsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListEndpointsRequest.

        待查询的终端节点所属VPC的ID。

        :param vpc_id: The vpc_id of this ListEndpointsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def name(self):
        r"""Gets the name of this ListEndpointsRequest.

        终端节点名称。

        :return: The name of this ListEndpointsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListEndpointsRequest.

        终端节点名称。

        :param name: The name of this ListEndpointsRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListEndpointsRequest.

        **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500

        :return: The limit of this ListEndpointsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEndpointsRequest.

        **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500

        :param limit: The limit of this ListEndpointsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListEndpointsRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :return: The offset of this ListEndpointsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEndpointsRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :param offset: The offset of this ListEndpointsRequest.
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
        if not isinstance(other, ListEndpointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
