# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInterfacesRequest:

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
        'filter': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'principal_source': 'str',
        'principal_type': 'str',
        'principal_name': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'filter': 'filter',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'principal_source': 'principal_source',
        'principal_type': 'principal_type',
        'principal_name': 'principal_name',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, instance_id=None, filter=None, resource_name=None, resource_type=None, principal_source=None, principal_type=None, principal_name=None, limit=None, marker=None):
        """ListInterfacesRequest

        The model defined in huaweicloud sdk

        :param instance_id: instance id
        :type instance_id: str
        :param filter: expression
        :type filter: str
        :param resource_name: 元数据资源全名
        :type resource_name: str
        :param resource_type: 元数据资源类型
        :type resource_type: str
        :param principal_source: 授权主体来源
        :type principal_source: str
        :param principal_type: 授权主体类型
        :type principal_type: str
        :param principal_name: 授权主体名称
        :type principal_name: str
        :param limit: limit
        :type limit: int
        :param marker: page token
        :type marker: str
        """
        
        

        self._instance_id = None
        self._filter = None
        self._resource_name = None
        self._resource_type = None
        self._principal_source = None
        self._principal_type = None
        self._principal_name = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.instance_id = instance_id
        if filter is not None:
            self.filter = filter
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if principal_source is not None:
            self.principal_source = principal_source
        if principal_type is not None:
            self.principal_type = principal_type
        if principal_name is not None:
            self.principal_name = principal_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def instance_id(self):
        """Gets the instance_id of this ListInterfacesRequest.

        instance id

        :return: The instance_id of this ListInterfacesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListInterfacesRequest.

        instance id

        :param instance_id: The instance_id of this ListInterfacesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def filter(self):
        """Gets the filter of this ListInterfacesRequest.

        expression

        :return: The filter of this ListInterfacesRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListInterfacesRequest.

        expression

        :param filter: The filter of this ListInterfacesRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def resource_name(self):
        """Gets the resource_name of this ListInterfacesRequest.

        元数据资源全名

        :return: The resource_name of this ListInterfacesRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListInterfacesRequest.

        元数据资源全名

        :param resource_name: The resource_name of this ListInterfacesRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this ListInterfacesRequest.

        元数据资源类型

        :return: The resource_type of this ListInterfacesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListInterfacesRequest.

        元数据资源类型

        :param resource_type: The resource_type of this ListInterfacesRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def principal_source(self):
        """Gets the principal_source of this ListInterfacesRequest.

        授权主体来源

        :return: The principal_source of this ListInterfacesRequest.
        :rtype: str
        """
        return self._principal_source

    @principal_source.setter
    def principal_source(self, principal_source):
        """Sets the principal_source of this ListInterfacesRequest.

        授权主体来源

        :param principal_source: The principal_source of this ListInterfacesRequest.
        :type principal_source: str
        """
        self._principal_source = principal_source

    @property
    def principal_type(self):
        """Gets the principal_type of this ListInterfacesRequest.

        授权主体类型

        :return: The principal_type of this ListInterfacesRequest.
        :rtype: str
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        """Sets the principal_type of this ListInterfacesRequest.

        授权主体类型

        :param principal_type: The principal_type of this ListInterfacesRequest.
        :type principal_type: str
        """
        self._principal_type = principal_type

    @property
    def principal_name(self):
        """Gets the principal_name of this ListInterfacesRequest.

        授权主体名称

        :return: The principal_name of this ListInterfacesRequest.
        :rtype: str
        """
        return self._principal_name

    @principal_name.setter
    def principal_name(self, principal_name):
        """Sets the principal_name of this ListInterfacesRequest.

        授权主体名称

        :param principal_name: The principal_name of this ListInterfacesRequest.
        :type principal_name: str
        """
        self._principal_name = principal_name

    @property
    def limit(self):
        """Gets the limit of this ListInterfacesRequest.

        limit

        :return: The limit of this ListInterfacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInterfacesRequest.

        limit

        :param limit: The limit of this ListInterfacesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListInterfacesRequest.

        page token

        :return: The marker of this ListInterfacesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListInterfacesRequest.

        page token

        :param marker: The marker of this ListInterfacesRequest.
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
        if not isinstance(other, ListInterfacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
