# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudConnectionQuotasRequest:

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
        'quota_type': 'str',
        'cloud_connection_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'quota_type': 'quota_type',
        'cloud_connection_id': 'cloud_connection_id',
        'region_id': 'region_id'
    }

    def __init__(self, limit=None, marker=None, quota_type=None, cloud_connection_id=None, region_id=None):
        r"""ListCloudConnectionQuotasRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        :param quota_type: 配额类型： - cloud_connection: 可加载的云连接实例数 - cloud_connection_region: 某云连接实例下可加载的Region数 - cloud_connection_route: 某云连接实例下可加载的路由数 - region_network_instance: 某云连接实例下某个Region下可加载的网络实例数
        :type quota_type: str
        :param cloud_connection_id: 云连接ID。当查询cloud_connection_region、cloud_connection_route、region_network_instance三种类型的配额时需要填写此参数。
        :type cloud_connection_id: str
        :param region_id: 区域ID。当查询region_network_instance类型的配额时需要填写此参数。
        :type region_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._quota_type = None
        self._cloud_connection_id = None
        self._region_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        self.quota_type = quota_type
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def limit(self):
        r"""Gets the limit of this ListCloudConnectionQuotasRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListCloudConnectionQuotasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCloudConnectionQuotasRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListCloudConnectionQuotasRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListCloudConnectionQuotasRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListCloudConnectionQuotasRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCloudConnectionQuotasRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListCloudConnectionQuotasRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def quota_type(self):
        r"""Gets the quota_type of this ListCloudConnectionQuotasRequest.

        配额类型： - cloud_connection: 可加载的云连接实例数 - cloud_connection_region: 某云连接实例下可加载的Region数 - cloud_connection_route: 某云连接实例下可加载的路由数 - region_network_instance: 某云连接实例下某个Region下可加载的网络实例数

        :return: The quota_type of this ListCloudConnectionQuotasRequest.
        :rtype: str
        """
        return self._quota_type

    @quota_type.setter
    def quota_type(self, quota_type):
        r"""Sets the quota_type of this ListCloudConnectionQuotasRequest.

        配额类型： - cloud_connection: 可加载的云连接实例数 - cloud_connection_region: 某云连接实例下可加载的Region数 - cloud_connection_route: 某云连接实例下可加载的路由数 - region_network_instance: 某云连接实例下某个Region下可加载的网络实例数

        :param quota_type: The quota_type of this ListCloudConnectionQuotasRequest.
        :type quota_type: str
        """
        self._quota_type = quota_type

    @property
    def cloud_connection_id(self):
        r"""Gets the cloud_connection_id of this ListCloudConnectionQuotasRequest.

        云连接ID。当查询cloud_connection_region、cloud_connection_route、region_network_instance三种类型的配额时需要填写此参数。

        :return: The cloud_connection_id of this ListCloudConnectionQuotasRequest.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        r"""Sets the cloud_connection_id of this ListCloudConnectionQuotasRequest.

        云连接ID。当查询cloud_connection_region、cloud_connection_route、region_network_instance三种类型的配额时需要填写此参数。

        :param cloud_connection_id: The cloud_connection_id of this ListCloudConnectionQuotasRequest.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListCloudConnectionQuotasRequest.

        区域ID。当查询region_network_instance类型的配额时需要填写此参数。

        :return: The region_id of this ListCloudConnectionQuotasRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListCloudConnectionQuotasRequest.

        区域ID。当查询region_network_instance类型的配额时需要填写此参数。

        :param region_id: The region_id of this ListCloudConnectionQuotasRequest.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, ListCloudConnectionQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
