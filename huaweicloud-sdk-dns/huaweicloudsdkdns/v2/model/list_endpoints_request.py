# coding: utf-8

import re
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
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'direction': 'direction',
        'vpc_id': 'vpc_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, direction=None, vpc_id=None, limit=None, offset=None):
        """ListEndpointsRequest

        The model defined in huaweicloud sdk

        :param direction: 待查询的endpoint的方向。 取值：inbound，表示入站规则。
        :type direction: str
        :param vpc_id: 待查询的endpoint所属vpc的id。
        :type vpc_id: str
        :param limit: 每页返回的资源个数。 取值范围：0~500，取值一般为10，20，50。
        :type limit: int
        :param offset: 分页查询起始页码，起始值为0。 当前设置marker不为空时，以marker为分页起始标识。取值范围：0~2147483647。
        :type offset: int
        """
        
        

        self._direction = None
        self._vpc_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.direction = direction
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def direction(self):
        """Gets the direction of this ListEndpointsRequest.

        待查询的endpoint的方向。 取值：inbound，表示入站规则。

        :return: The direction of this ListEndpointsRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ListEndpointsRequest.

        待查询的endpoint的方向。 取值：inbound，表示入站规则。

        :param direction: The direction of this ListEndpointsRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListEndpointsRequest.

        待查询的endpoint所属vpc的id。

        :return: The vpc_id of this ListEndpointsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListEndpointsRequest.

        待查询的endpoint所属vpc的id。

        :param vpc_id: The vpc_id of this ListEndpointsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def limit(self):
        """Gets the limit of this ListEndpointsRequest.

        每页返回的资源个数。 取值范围：0~500，取值一般为10，20，50。

        :return: The limit of this ListEndpointsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEndpointsRequest.

        每页返回的资源个数。 取值范围：0~500，取值一般为10，20，50。

        :param limit: The limit of this ListEndpointsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListEndpointsRequest.

        分页查询起始页码，起始值为0。 当前设置marker不为空时，以marker为分页起始标识。取值范围：0~2147483647。

        :return: The offset of this ListEndpointsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEndpointsRequest.

        分页查询起始页码，起始值为0。 当前设置marker不为空时，以marker为分页起始标识。取值范围：0~2147483647。

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
