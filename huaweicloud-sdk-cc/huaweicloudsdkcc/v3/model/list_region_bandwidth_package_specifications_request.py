# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRegionBandwidthPackageSpecificationsRequest:

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
        'local_region_id': 'str',
        'remote_region_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'local_region_id': 'local_region_id',
        'remote_region_id': 'remote_region_id'
    }

    def __init__(self, limit=None, marker=None, local_region_id=None, remote_region_id=None):
        r"""ListRegionBandwidthPackageSpecificationsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        :param local_region_id: 根据城域带宽包本端区域ID过滤租户城域带宽配置列表。
        :type local_region_id: str
        :param remote_region_id: 根据城域带宽包对端区域ID过滤租户城域带宽配置列表。
        :type remote_region_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._local_region_id = None
        self._remote_region_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if local_region_id is not None:
            self.local_region_id = local_region_id
        if remote_region_id is not None:
            self.remote_region_id = remote_region_id

    @property
    def limit(self):
        r"""Gets the limit of this ListRegionBandwidthPackageSpecificationsRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ListRegionBandwidthPackageSpecificationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRegionBandwidthPackageSpecificationsRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ListRegionBandwidthPackageSpecificationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListRegionBandwidthPackageSpecificationsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListRegionBandwidthPackageSpecificationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRegionBandwidthPackageSpecificationsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListRegionBandwidthPackageSpecificationsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def local_region_id(self):
        r"""Gets the local_region_id of this ListRegionBandwidthPackageSpecificationsRequest.

        根据城域带宽包本端区域ID过滤租户城域带宽配置列表。

        :return: The local_region_id of this ListRegionBandwidthPackageSpecificationsRequest.
        :rtype: str
        """
        return self._local_region_id

    @local_region_id.setter
    def local_region_id(self, local_region_id):
        r"""Sets the local_region_id of this ListRegionBandwidthPackageSpecificationsRequest.

        根据城域带宽包本端区域ID过滤租户城域带宽配置列表。

        :param local_region_id: The local_region_id of this ListRegionBandwidthPackageSpecificationsRequest.
        :type local_region_id: str
        """
        self._local_region_id = local_region_id

    @property
    def remote_region_id(self):
        r"""Gets the remote_region_id of this ListRegionBandwidthPackageSpecificationsRequest.

        根据城域带宽包对端区域ID过滤租户城域带宽配置列表。

        :return: The remote_region_id of this ListRegionBandwidthPackageSpecificationsRequest.
        :rtype: str
        """
        return self._remote_region_id

    @remote_region_id.setter
    def remote_region_id(self, remote_region_id):
        r"""Sets the remote_region_id of this ListRegionBandwidthPackageSpecificationsRequest.

        根据城域带宽包对端区域ID过滤租户城域带宽配置列表。

        :param remote_region_id: The remote_region_id of this ListRegionBandwidthPackageSpecificationsRequest.
        :type remote_region_id: str
        """
        self._remote_region_id = remote_region_id

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
        if not isinstance(other, ListRegionBandwidthPackageSpecificationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
