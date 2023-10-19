# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'cloud_connection_id': 'list[str]',
        'instance_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'cloud_connection_id': 'cloud_connection_id',
        'instance_id': 'instance_id'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, description=None, cloud_connection_id=None, instance_id=None):
        """ListPermissionsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。
        :type marker: str
        :param id: 根据id查询，可查询多个id。
        :type id: list[str]
        :param name: 根据名字查询，可查询多个名字。
        :type name: list[str]
        :param description: 根据描述查询，可查询多个描述。
        :type description: list[str]
        :param cloud_connection_id: 根据云连接的ID过滤列表。
        :type cloud_connection_id: list[str]
        :param instance_id: 根据实例ID过滤授权列表。
        :type instance_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._description = None
        self._cloud_connection_id = None
        self._instance_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListPermissionsRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListPermissionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPermissionsRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListPermissionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPermissionsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :return: The marker of this ListPermissionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPermissionsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :param marker: The marker of this ListPermissionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListPermissionsRequest.

        根据id查询，可查询多个id。

        :return: The id of this ListPermissionsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPermissionsRequest.

        根据id查询，可查询多个id。

        :param id: The id of this ListPermissionsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListPermissionsRequest.

        根据名字查询，可查询多个名字。

        :return: The name of this ListPermissionsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPermissionsRequest.

        根据名字查询，可查询多个名字。

        :param name: The name of this ListPermissionsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListPermissionsRequest.

        根据描述查询，可查询多个描述。

        :return: The description of this ListPermissionsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPermissionsRequest.

        根据描述查询，可查询多个描述。

        :param description: The description of this ListPermissionsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this ListPermissionsRequest.

        根据云连接的ID过滤列表。

        :return: The cloud_connection_id of this ListPermissionsRequest.
        :rtype: list[str]
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this ListPermissionsRequest.

        根据云连接的ID过滤列表。

        :param cloud_connection_id: The cloud_connection_id of this ListPermissionsRequest.
        :type cloud_connection_id: list[str]
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListPermissionsRequest.

        根据实例ID过滤授权列表。

        :return: The instance_id of this ListPermissionsRequest.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListPermissionsRequest.

        根据实例ID过滤授权列表。

        :param instance_id: The instance_id of this ListPermissionsRequest.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListPermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
