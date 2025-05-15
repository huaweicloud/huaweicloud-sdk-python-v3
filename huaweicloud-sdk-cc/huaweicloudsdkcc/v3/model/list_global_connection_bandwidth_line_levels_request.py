# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalConnectionBandwidthLineLevelsRequest:

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
        'local_area': 'str',
        'remote_area': 'str',
        'levels': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'local_area': 'local_area',
        'remote_area': 'remote_area',
        'levels': 'levels'
    }

    def __init__(self, limit=None, marker=None, id=None, local_area=None, remote_area=None, levels=None):
        r"""ListGlobalConnectionBandwidthLineLevelsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        :param id: 根据ID查询，可查询多个ID。
        :type id: list[str]
        :param local_area: 线路规格本端接入点编码信息。
        :type local_area: str
        :param remote_area: 线路规格远端接入点编码信息。
        :type remote_area: str
        :param levels: 带宽等级信息： - Pt: 铂金 - Ag: 银
        :type levels: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._local_area = None
        self._remote_area = None
        self._levels = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if local_area is not None:
            self.local_area = local_area
        if remote_area is not None:
            self.remote_area = remote_area
        if levels is not None:
            self.levels = levels

    @property
    def limit(self):
        r"""Gets the limit of this ListGlobalConnectionBandwidthLineLevelsRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGlobalConnectionBandwidthLineLevelsRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListGlobalConnectionBandwidthLineLevelsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListGlobalConnectionBandwidthLineLevelsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListGlobalConnectionBandwidthLineLevelsRequest.

        根据ID查询，可查询多个ID。

        :return: The id of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListGlobalConnectionBandwidthLineLevelsRequest.

        根据ID查询，可查询多个ID。

        :param id: The id of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def local_area(self):
        r"""Gets the local_area of this ListGlobalConnectionBandwidthLineLevelsRequest.

        线路规格本端接入点编码信息。

        :return: The local_area of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :rtype: str
        """
        return self._local_area

    @local_area.setter
    def local_area(self, local_area):
        r"""Sets the local_area of this ListGlobalConnectionBandwidthLineLevelsRequest.

        线路规格本端接入点编码信息。

        :param local_area: The local_area of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :type local_area: str
        """
        self._local_area = local_area

    @property
    def remote_area(self):
        r"""Gets the remote_area of this ListGlobalConnectionBandwidthLineLevelsRequest.

        线路规格远端接入点编码信息。

        :return: The remote_area of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :rtype: str
        """
        return self._remote_area

    @remote_area.setter
    def remote_area(self, remote_area):
        r"""Sets the remote_area of this ListGlobalConnectionBandwidthLineLevelsRequest.

        线路规格远端接入点编码信息。

        :param remote_area: The remote_area of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :type remote_area: str
        """
        self._remote_area = remote_area

    @property
    def levels(self):
        r"""Gets the levels of this ListGlobalConnectionBandwidthLineLevelsRequest.

        带宽等级信息： - Pt: 铂金 - Ag: 银

        :return: The levels of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :rtype: list[str]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        r"""Sets the levels of this ListGlobalConnectionBandwidthLineLevelsRequest.

        带宽等级信息： - Pt: 铂金 - Ag: 银

        :param levels: The levels of this ListGlobalConnectionBandwidthLineLevelsRequest.
        :type levels: list[str]
        """
        self._levels = levels

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
        if not isinstance(other, ListGlobalConnectionBandwidthLineLevelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
