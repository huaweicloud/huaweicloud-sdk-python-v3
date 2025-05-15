# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInterRegionBandwidthsRequest:

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
        'enterprise_project_id': 'list[str]',
        'cloud_connection_id': 'list[str]',
        'bandwidth_package_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'cloud_connection_id': 'cloud_connection_id',
        'bandwidth_package_id': 'bandwidth_package_id'
    }

    def __init__(self, limit=None, marker=None, id=None, enterprise_project_id=None, cloud_connection_id=None, bandwidth_package_id=None):
        r"""ListInterRegionBandwidthsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        :param id: 根据ID查询，可查询多个ID。
        :type id: list[str]
        :param enterprise_project_id: 根据企业项目ID过滤列表。
        :type enterprise_project_id: list[str]
        :param cloud_connection_id: 根据云连接的ID过滤列表。
        :type cloud_connection_id: list[str]
        :param bandwidth_package_id: 根据带宽包列表过滤域间带宽实例列表。
        :type bandwidth_package_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._enterprise_project_id = None
        self._cloud_connection_id = None
        self._bandwidth_package_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if bandwidth_package_id is not None:
            self.bandwidth_package_id = bandwidth_package_id

    @property
    def limit(self):
        r"""Gets the limit of this ListInterRegionBandwidthsRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListInterRegionBandwidthsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInterRegionBandwidthsRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListInterRegionBandwidthsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListInterRegionBandwidthsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListInterRegionBandwidthsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListInterRegionBandwidthsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListInterRegionBandwidthsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListInterRegionBandwidthsRequest.

        根据ID查询，可查询多个ID。

        :return: The id of this ListInterRegionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInterRegionBandwidthsRequest.

        根据ID查询，可查询多个ID。

        :param id: The id of this ListInterRegionBandwidthsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListInterRegionBandwidthsRequest.

        根据企业项目ID过滤列表。

        :return: The enterprise_project_id of this ListInterRegionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListInterRegionBandwidthsRequest.

        根据企业项目ID过滤列表。

        :param enterprise_project_id: The enterprise_project_id of this ListInterRegionBandwidthsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cloud_connection_id(self):
        r"""Gets the cloud_connection_id of this ListInterRegionBandwidthsRequest.

        根据云连接的ID过滤列表。

        :return: The cloud_connection_id of this ListInterRegionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        r"""Sets the cloud_connection_id of this ListInterRegionBandwidthsRequest.

        根据云连接的ID过滤列表。

        :param cloud_connection_id: The cloud_connection_id of this ListInterRegionBandwidthsRequest.
        :type cloud_connection_id: list[str]
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def bandwidth_package_id(self):
        r"""Gets the bandwidth_package_id of this ListInterRegionBandwidthsRequest.

        根据带宽包列表过滤域间带宽实例列表。

        :return: The bandwidth_package_id of this ListInterRegionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        r"""Sets the bandwidth_package_id of this ListInterRegionBandwidthsRequest.

        根据带宽包列表过滤域间带宽实例列表。

        :param bandwidth_package_id: The bandwidth_package_id of this ListInterRegionBandwidthsRequest.
        :type bandwidth_package_id: list[str]
        """
        self._bandwidth_package_id = bandwidth_package_id

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
        if not isinstance(other, ListInterRegionBandwidthsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
