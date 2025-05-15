# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudConnectionRoutesRequest:

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
        'cloud_connection_id': 'list[str]',
        'instance_id': 'list[str]',
        'region_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'cloud_connection_id': 'cloud_connection_id',
        'instance_id': 'instance_id',
        'region_id': 'region_id',
        'id': 'id'
    }

    def __init__(self, limit=None, marker=None, cloud_connection_id=None, instance_id=None, region_id=None, id=None):
        r"""ListCloudConnectionRoutesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        :param cloud_connection_id: 根据云连接的ID过滤列表。
        :type cloud_connection_id: list[str]
        :param instance_id: 根据网络实例ID过滤云连接路由条目列表。
        :type instance_id: list[str]
        :param region_id: 根据Region ID过滤云连接路由条目列表。
        :type region_id: str
        :param id: 根据id查询。
        :type id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._cloud_connection_id = None
        self._instance_id = None
        self._region_id = None
        self._id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if instance_id is not None:
            self.instance_id = instance_id
        if region_id is not None:
            self.region_id = region_id
        if id is not None:
            self.id = id

    @property
    def limit(self):
        r"""Gets the limit of this ListCloudConnectionRoutesRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListCloudConnectionRoutesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCloudConnectionRoutesRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListCloudConnectionRoutesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListCloudConnectionRoutesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListCloudConnectionRoutesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCloudConnectionRoutesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListCloudConnectionRoutesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def cloud_connection_id(self):
        r"""Gets the cloud_connection_id of this ListCloudConnectionRoutesRequest.

        根据云连接的ID过滤列表。

        :return: The cloud_connection_id of this ListCloudConnectionRoutesRequest.
        :rtype: list[str]
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        r"""Sets the cloud_connection_id of this ListCloudConnectionRoutesRequest.

        根据云连接的ID过滤列表。

        :param cloud_connection_id: The cloud_connection_id of this ListCloudConnectionRoutesRequest.
        :type cloud_connection_id: list[str]
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListCloudConnectionRoutesRequest.

        根据网络实例ID过滤云连接路由条目列表。

        :return: The instance_id of this ListCloudConnectionRoutesRequest.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListCloudConnectionRoutesRequest.

        根据网络实例ID过滤云连接路由条目列表。

        :param instance_id: The instance_id of this ListCloudConnectionRoutesRequest.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListCloudConnectionRoutesRequest.

        根据Region ID过滤云连接路由条目列表。

        :return: The region_id of this ListCloudConnectionRoutesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListCloudConnectionRoutesRequest.

        根据Region ID过滤云连接路由条目列表。

        :param region_id: The region_id of this ListCloudConnectionRoutesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def id(self):
        r"""Gets the id of this ListCloudConnectionRoutesRequest.

        根据id查询。

        :return: The id of this ListCloudConnectionRoutesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListCloudConnectionRoutesRequest.

        根据id查询。

        :param id: The id of this ListCloudConnectionRoutesRequest.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ListCloudConnectionRoutesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
