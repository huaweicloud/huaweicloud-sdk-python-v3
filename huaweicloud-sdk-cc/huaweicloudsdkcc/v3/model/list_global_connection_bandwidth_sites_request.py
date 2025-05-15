# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalConnectionBandwidthSitesRequest:

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
        'name_en': 'str',
        'name_cn': 'str',
        'site_code': 'str',
        'site_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name_en': 'name_en',
        'name_cn': 'name_cn',
        'site_code': 'site_code',
        'site_type': 'site_type'
    }

    def __init__(self, limit=None, marker=None, id=None, name_en=None, name_cn=None, site_code=None, site_type=None):
        r"""ListGlobalConnectionBandwidthSitesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        :param id: 根据ID查询，可查询多个ID。
        :type id: list[str]
        :param name_en: 站点信息自定义英文名称。
        :type name_en: str
        :param name_cn: 站点信息自定义中文名称。
        :type name_cn: str
        :param site_code: 站点编码。
        :type site_code: str
        :param site_type: 站点类型： - Area: 大区 - SubArea: 区域 - Region: 城域
        :type site_type: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name_en = None
        self._name_cn = None
        self._site_code = None
        self._site_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name_en is not None:
            self.name_en = name_en
        if name_cn is not None:
            self.name_cn = name_cn
        if site_code is not None:
            self.site_code = site_code
        if site_type is not None:
            self.site_type = site_type

    @property
    def limit(self):
        r"""Gets the limit of this ListGlobalConnectionBandwidthSitesRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListGlobalConnectionBandwidthSitesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGlobalConnectionBandwidthSitesRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListGlobalConnectionBandwidthSitesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListGlobalConnectionBandwidthSitesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListGlobalConnectionBandwidthSitesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListGlobalConnectionBandwidthSitesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListGlobalConnectionBandwidthSitesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListGlobalConnectionBandwidthSitesRequest.

        根据ID查询，可查询多个ID。

        :return: The id of this ListGlobalConnectionBandwidthSitesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListGlobalConnectionBandwidthSitesRequest.

        根据ID查询，可查询多个ID。

        :param id: The id of this ListGlobalConnectionBandwidthSitesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name_en(self):
        r"""Gets the name_en of this ListGlobalConnectionBandwidthSitesRequest.

        站点信息自定义英文名称。

        :return: The name_en of this ListGlobalConnectionBandwidthSitesRequest.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this ListGlobalConnectionBandwidthSitesRequest.

        站点信息自定义英文名称。

        :param name_en: The name_en of this ListGlobalConnectionBandwidthSitesRequest.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_cn(self):
        r"""Gets the name_cn of this ListGlobalConnectionBandwidthSitesRequest.

        站点信息自定义中文名称。

        :return: The name_cn of this ListGlobalConnectionBandwidthSitesRequest.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this ListGlobalConnectionBandwidthSitesRequest.

        站点信息自定义中文名称。

        :param name_cn: The name_cn of this ListGlobalConnectionBandwidthSitesRequest.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def site_code(self):
        r"""Gets the site_code of this ListGlobalConnectionBandwidthSitesRequest.

        站点编码。

        :return: The site_code of this ListGlobalConnectionBandwidthSitesRequest.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this ListGlobalConnectionBandwidthSitesRequest.

        站点编码。

        :param site_code: The site_code of this ListGlobalConnectionBandwidthSitesRequest.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def site_type(self):
        r"""Gets the site_type of this ListGlobalConnectionBandwidthSitesRequest.

        站点类型： - Area: 大区 - SubArea: 区域 - Region: 城域

        :return: The site_type of this ListGlobalConnectionBandwidthSitesRequest.
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        r"""Sets the site_type of this ListGlobalConnectionBandwidthSitesRequest.

        站点类型： - Area: 大区 - SubArea: 区域 - Region: 城域

        :param site_type: The site_type of this ListGlobalConnectionBandwidthSitesRequest.
        :type site_type: str
        """
        self._site_type = site_type

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
        if not isinstance(other, ListGlobalConnectionBandwidthSitesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
