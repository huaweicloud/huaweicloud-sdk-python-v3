# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubResourceInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_id': 'str',
        'sub_resource_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'body': 'ListResourceInstancesRequestBody'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'sub_resource_type': 'sub_resource_type',
        'offset': 'offset',
        'limit': 'limit',
        'body': 'body'
    }

    def __init__(self, resource_type=None, resource_id=None, sub_resource_type=None, offset=None, limit=None, body=None):
        r"""ListSubResourceInstancesRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型，支持的资源类型为：instances
        :type resource_type: str
        :param resource_id: 资源id
        :type resource_id: str
        :param sub_resource_type: 子资源类型，支持的子资源类型为：namespaces
        :type sub_resource_type: str
        :param offset: 起始索引，默认值为0。**注意：offset和limit参数需要配套使用。**
        :type offset: int
        :param limit: 返回条数，默认为200，最小值为1，最大值为200。**注意：offset和limit参数需要配套使用。**
        :type limit: int
        :param body: Body of the ListSubResourceInstancesRequest
        :type body: :class:`huaweicloudsdkswr.v2.ListResourceInstancesRequestBody`
        """
        
        

        self._resource_type = None
        self._resource_id = None
        self._sub_resource_type = None
        self._offset = None
        self._limit = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_id = resource_id
        self.sub_resource_type = sub_resource_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListSubResourceInstancesRequest.

        资源类型，支持的资源类型为：instances

        :return: The resource_type of this ListSubResourceInstancesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListSubResourceInstancesRequest.

        资源类型，支持的资源类型为：instances

        :param resource_type: The resource_type of this ListSubResourceInstancesRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListSubResourceInstancesRequest.

        资源id

        :return: The resource_id of this ListSubResourceInstancesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListSubResourceInstancesRequest.

        资源id

        :param resource_id: The resource_id of this ListSubResourceInstancesRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def sub_resource_type(self):
        r"""Gets the sub_resource_type of this ListSubResourceInstancesRequest.

        子资源类型，支持的子资源类型为：namespaces

        :return: The sub_resource_type of this ListSubResourceInstancesRequest.
        :rtype: str
        """
        return self._sub_resource_type

    @sub_resource_type.setter
    def sub_resource_type(self, sub_resource_type):
        r"""Sets the sub_resource_type of this ListSubResourceInstancesRequest.

        子资源类型，支持的子资源类型为：namespaces

        :param sub_resource_type: The sub_resource_type of this ListSubResourceInstancesRequest.
        :type sub_resource_type: str
        """
        self._sub_resource_type = sub_resource_type

    @property
    def offset(self):
        r"""Gets the offset of this ListSubResourceInstancesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用。**

        :return: The offset of this ListSubResourceInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubResourceInstancesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用。**

        :param offset: The offset of this ListSubResourceInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubResourceInstancesRequest.

        返回条数，默认为200，最小值为1，最大值为200。**注意：offset和limit参数需要配套使用。**

        :return: The limit of this ListSubResourceInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubResourceInstancesRequest.

        返回条数，默认为200，最小值为1，最大值为200。**注意：offset和limit参数需要配套使用。**

        :param limit: The limit of this ListSubResourceInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def body(self):
        r"""Gets the body of this ListSubResourceInstancesRequest.

        :return: The body of this ListSubResourceInstancesRequest.
        :rtype: :class:`huaweicloudsdkswr.v2.ListResourceInstancesRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListSubResourceInstancesRequest.

        :param body: The body of this ListSubResourceInstancesRequest.
        :type body: :class:`huaweicloudsdkswr.v2.ListResourceInstancesRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ListSubResourceInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
