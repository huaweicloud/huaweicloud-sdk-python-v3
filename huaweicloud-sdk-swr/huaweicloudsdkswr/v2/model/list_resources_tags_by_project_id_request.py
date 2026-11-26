# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourcesTagsByProjectIdRequest:

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
        'offset': 'int',
        'limit': 'int',
        'instance_id': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'offset': 'offset',
        'limit': 'limit',
        'instance_id': 'instance_id'
    }

    def __init__(self, resource_type=None, offset=None, limit=None, instance_id=None):
        r"""ListResourcesTagsByProjectIdRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型 取值范围： - instances：Instance实例 - namespaces：命名空间 - repositories：仓库
        :type resource_type: str
        :param offset: 起始索引，默认值为0。**注意：offset和limit参数需要配套使用。**
        :type offset: int
        :param limit: 返回条数，默认为200，最小值为1，最大值为200。**注意：offset和limit参数需要配套使用。**
        :type limit: int
        :param instance_id: 当resource_type为repositories或namespaces时，支持通过instance_id进行过滤查询，用于获取指定注册表实例下对应资源类型的标签列表。
        :type instance_id: str
        """
        
        

        self._resource_type = None
        self._offset = None
        self._limit = None
        self._instance_id = None
        self.discriminator = None

        self.resource_type = resource_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListResourcesTagsByProjectIdRequest.

        资源类型 取值范围： - instances：Instance实例 - namespaces：命名空间 - repositories：仓库

        :return: The resource_type of this ListResourcesTagsByProjectIdRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListResourcesTagsByProjectIdRequest.

        资源类型 取值范围： - instances：Instance实例 - namespaces：命名空间 - repositories：仓库

        :param resource_type: The resource_type of this ListResourcesTagsByProjectIdRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def offset(self):
        r"""Gets the offset of this ListResourcesTagsByProjectIdRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用。**

        :return: The offset of this ListResourcesTagsByProjectIdRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResourcesTagsByProjectIdRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用。**

        :param offset: The offset of this ListResourcesTagsByProjectIdRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListResourcesTagsByProjectIdRequest.

        返回条数，默认为200，最小值为1，最大值为200。**注意：offset和limit参数需要配套使用。**

        :return: The limit of this ListResourcesTagsByProjectIdRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourcesTagsByProjectIdRequest.

        返回条数，默认为200，最小值为1，最大值为200。**注意：offset和limit参数需要配套使用。**

        :param limit: The limit of this ListResourcesTagsByProjectIdRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListResourcesTagsByProjectIdRequest.

        当resource_type为repositories或namespaces时，支持通过instance_id进行过滤查询，用于获取指定注册表实例下对应资源类型的标签列表。

        :return: The instance_id of this ListResourcesTagsByProjectIdRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListResourcesTagsByProjectIdRequest.

        当resource_type为repositories或namespaces时，支持通过instance_id进行过滤查询，用于获取指定注册表实例下对应资源类型的标签列表。

        :param instance_id: The instance_id of this ListResourcesTagsByProjectIdRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListResourcesTagsByProjectIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
