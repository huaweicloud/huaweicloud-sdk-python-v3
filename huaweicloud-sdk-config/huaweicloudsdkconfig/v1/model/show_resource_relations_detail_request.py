# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceRelationsDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'direction': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'direction': 'direction',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, resource_id=None, direction=None, limit=None, marker=None):
        r"""ShowResourceRelationsDetailRequest

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param direction: 资源关系的指向。
        :type direction: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._resource_id = None
        self._direction = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.resource_id = resource_id
        self.direction = direction
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowResourceRelationsDetailRequest.

        资源ID

        :return: The resource_id of this ShowResourceRelationsDetailRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowResourceRelationsDetailRequest.

        资源ID

        :param resource_id: The resource_id of this ShowResourceRelationsDetailRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def direction(self):
        r"""Gets the direction of this ShowResourceRelationsDetailRequest.

        资源关系的指向。

        :return: The direction of this ShowResourceRelationsDetailRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this ShowResourceRelationsDetailRequest.

        资源关系的指向。

        :param direction: The direction of this ShowResourceRelationsDetailRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def limit(self):
        r"""Gets the limit of this ShowResourceRelationsDetailRequest.

        最大的返回数量

        :return: The limit of this ShowResourceRelationsDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowResourceRelationsDetailRequest.

        最大的返回数量

        :param limit: The limit of this ShowResourceRelationsDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ShowResourceRelationsDetailRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ShowResourceRelationsDetailRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ShowResourceRelationsDetailRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ShowResourceRelationsDetailRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ShowResourceRelationsDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
