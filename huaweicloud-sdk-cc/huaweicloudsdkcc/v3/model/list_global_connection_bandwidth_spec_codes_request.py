# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalConnectionBandwidthSpecCodesRequest:

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
        'level': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'local_area': 'local_area',
        'remote_area': 'remote_area',
        'level': 'level'
    }

    def __init__(self, limit=None, marker=None, id=None, local_area=None, remote_area=None, level=None):
        """ListGlobalConnectionBandwidthSpecCodesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。
        :type marker: str
        :param id: 根据id查询，可查询多个id。
        :type id: list[str]
        :param local_area: 线路规格本端接入点编码信息。
        :type local_area: str
        :param remote_area: 线路规格远端接入点编码信息。
        :type remote_area: str
        :param level: 带宽等级： - Pt: 铂金 - Au: 金 - Ag: 银
        :type level: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._local_area = None
        self._remote_area = None
        self._level = None
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
        if level is not None:
            self.level = level

    @property
    def limit(self):
        """Gets the limit of this ListGlobalConnectionBandwidthSpecCodesRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGlobalConnectionBandwidthSpecCodesRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListGlobalConnectionBandwidthSpecCodesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :return: The marker of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListGlobalConnectionBandwidthSpecCodesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :param marker: The marker of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListGlobalConnectionBandwidthSpecCodesRequest.

        根据id查询，可查询多个id。

        :return: The id of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListGlobalConnectionBandwidthSpecCodesRequest.

        根据id查询，可查询多个id。

        :param id: The id of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def local_area(self):
        """Gets the local_area of this ListGlobalConnectionBandwidthSpecCodesRequest.

        线路规格本端接入点编码信息。

        :return: The local_area of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :rtype: str
        """
        return self._local_area

    @local_area.setter
    def local_area(self, local_area):
        """Sets the local_area of this ListGlobalConnectionBandwidthSpecCodesRequest.

        线路规格本端接入点编码信息。

        :param local_area: The local_area of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :type local_area: str
        """
        self._local_area = local_area

    @property
    def remote_area(self):
        """Gets the remote_area of this ListGlobalConnectionBandwidthSpecCodesRequest.

        线路规格远端接入点编码信息。

        :return: The remote_area of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :rtype: str
        """
        return self._remote_area

    @remote_area.setter
    def remote_area(self, remote_area):
        """Sets the remote_area of this ListGlobalConnectionBandwidthSpecCodesRequest.

        线路规格远端接入点编码信息。

        :param remote_area: The remote_area of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :type remote_area: str
        """
        self._remote_area = remote_area

    @property
    def level(self):
        """Gets the level of this ListGlobalConnectionBandwidthSpecCodesRequest.

        带宽等级： - Pt: 铂金 - Au: 金 - Ag: 银

        :return: The level of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :rtype: list[str]
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ListGlobalConnectionBandwidthSpecCodesRequest.

        带宽等级： - Pt: 铂金 - Au: 金 - Ag: 银

        :param level: The level of this ListGlobalConnectionBandwidthSpecCodesRequest.
        :type level: list[str]
        """
        self._level = level

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
        if not isinstance(other, ListGlobalConnectionBandwidthSpecCodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
