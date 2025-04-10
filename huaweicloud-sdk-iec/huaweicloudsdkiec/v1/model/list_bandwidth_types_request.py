# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthTypesRequest:

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
        'offset': 'int',
        'site_id': 'str',
        'bandwidth_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'site_id': 'site_id',
        'bandwidth_type': 'bandwidth_type'
    }

    def __init__(self, limit=None, offset=None, site_id=None, bandwidth_type=None):
        r"""ListBandwidthTypesRequest

        The model defined in huaweicloud sdk

        :param limit: 查询的数目，取值范围：0~1000。
        :type limit: int
        :param offset: 查询的偏移量。
        :type offset: int
        :param site_id: 边缘站点ID。
        :type site_id: str
        :param bandwidth_type: 带宽支持类型。
        :type bandwidth_type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._site_id = None
        self._bandwidth_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if site_id is not None:
            self.site_id = site_id
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type

    @property
    def limit(self):
        r"""Gets the limit of this ListBandwidthTypesRequest.

        查询的数目，取值范围：0~1000。

        :return: The limit of this ListBandwidthTypesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBandwidthTypesRequest.

        查询的数目，取值范围：0~1000。

        :param limit: The limit of this ListBandwidthTypesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListBandwidthTypesRequest.

        查询的偏移量。

        :return: The offset of this ListBandwidthTypesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBandwidthTypesRequest.

        查询的偏移量。

        :param offset: The offset of this ListBandwidthTypesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def site_id(self):
        r"""Gets the site_id of this ListBandwidthTypesRequest.

        边缘站点ID。

        :return: The site_id of this ListBandwidthTypesRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this ListBandwidthTypesRequest.

        边缘站点ID。

        :param site_id: The site_id of this ListBandwidthTypesRequest.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def bandwidth_type(self):
        r"""Gets the bandwidth_type of this ListBandwidthTypesRequest.

        带宽支持类型。

        :return: The bandwidth_type of this ListBandwidthTypesRequest.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        r"""Sets the bandwidth_type of this ListBandwidthTypesRequest.

        带宽支持类型。

        :param bandwidth_type: The bandwidth_type of this ListBandwidthTypesRequest.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

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
        if not isinstance(other, ListBandwidthTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
