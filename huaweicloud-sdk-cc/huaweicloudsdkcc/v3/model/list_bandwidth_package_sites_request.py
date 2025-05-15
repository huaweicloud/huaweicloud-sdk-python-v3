# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthPackageSitesRequest:

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
        'site_code': 'str',
        'region_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'site_code': 'site_code',
        'region_id': 'region_id',
        'name': 'name'
    }

    def __init__(self, limit=None, marker=None, site_code=None, region_id=None, name=None):
        r"""ListBandwidthPackageSitesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        :param site_code: 根据站点编码进行查询。
        :type site_code: str
        :param region_id: 根据区域ID进行查询。
        :type region_id: str
        :param name: 根据名称模糊查询。
        :type name: str
        """
        
        

        self._limit = None
        self._marker = None
        self._site_code = None
        self._region_id = None
        self._name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if site_code is not None:
            self.site_code = site_code
        if region_id is not None:
            self.region_id = region_id
        if name is not None:
            self.name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListBandwidthPackageSitesRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListBandwidthPackageSitesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBandwidthPackageSitesRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListBandwidthPackageSitesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListBandwidthPackageSitesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListBandwidthPackageSitesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListBandwidthPackageSitesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListBandwidthPackageSitesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def site_code(self):
        r"""Gets the site_code of this ListBandwidthPackageSitesRequest.

        根据站点编码进行查询。

        :return: The site_code of this ListBandwidthPackageSitesRequest.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this ListBandwidthPackageSitesRequest.

        根据站点编码进行查询。

        :param site_code: The site_code of this ListBandwidthPackageSitesRequest.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def region_id(self):
        r"""Gets the region_id of this ListBandwidthPackageSitesRequest.

        根据区域ID进行查询。

        :return: The region_id of this ListBandwidthPackageSitesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListBandwidthPackageSitesRequest.

        根据区域ID进行查询。

        :param region_id: The region_id of this ListBandwidthPackageSitesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def name(self):
        r"""Gets the name of this ListBandwidthPackageSitesRequest.

        根据名称模糊查询。

        :return: The name of this ListBandwidthPackageSitesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListBandwidthPackageSitesRequest.

        根据名称模糊查询。

        :param name: The name of this ListBandwidthPackageSitesRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListBandwidthPackageSitesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
