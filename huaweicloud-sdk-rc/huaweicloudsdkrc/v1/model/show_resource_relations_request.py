# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceRelationsRequest:

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
        'related_resource_id': 'str',
        'related_resource_type': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'related_resource_id': 'related_resource_id',
        'related_resource_type': 'related_resource_type',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, resource_id=None, related_resource_id=None, related_resource_type=None, limit=None, marker=None):
        r"""ShowResourceRelationsRequest

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param related_resource_id: 资源ID
        :type related_resource_id: str
        :param related_resource_type: 关联资源类型
        :type related_resource_type: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._resource_id = None
        self._related_resource_id = None
        self._related_resource_type = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.resource_id = resource_id
        if related_resource_id is not None:
            self.related_resource_id = related_resource_id
        if related_resource_type is not None:
            self.related_resource_type = related_resource_type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowResourceRelationsRequest.

        资源ID

        :return: The resource_id of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowResourceRelationsRequest.

        资源ID

        :param resource_id: The resource_id of this ShowResourceRelationsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def related_resource_id(self):
        r"""Gets the related_resource_id of this ShowResourceRelationsRequest.

        资源ID

        :return: The related_resource_id of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._related_resource_id

    @related_resource_id.setter
    def related_resource_id(self, related_resource_id):
        r"""Sets the related_resource_id of this ShowResourceRelationsRequest.

        资源ID

        :param related_resource_id: The related_resource_id of this ShowResourceRelationsRequest.
        :type related_resource_id: str
        """
        self._related_resource_id = related_resource_id

    @property
    def related_resource_type(self):
        r"""Gets the related_resource_type of this ShowResourceRelationsRequest.

        关联资源类型

        :return: The related_resource_type of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._related_resource_type

    @related_resource_type.setter
    def related_resource_type(self, related_resource_type):
        r"""Sets the related_resource_type of this ShowResourceRelationsRequest.

        关联资源类型

        :param related_resource_type: The related_resource_type of this ShowResourceRelationsRequest.
        :type related_resource_type: str
        """
        self._related_resource_type = related_resource_type

    @property
    def limit(self):
        r"""Gets the limit of this ShowResourceRelationsRequest.

        最大的返回数量

        :return: The limit of this ShowResourceRelationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowResourceRelationsRequest.

        最大的返回数量

        :param limit: The limit of this ShowResourceRelationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ShowResourceRelationsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ShowResourceRelationsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ShowResourceRelationsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ShowResourceRelationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
