# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociatedResourceSettingsRequest:

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
        'region_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'region_id': 'region_id'
    }

    def __init__(self, limit=None, marker=None, region_id=None):
        r"""ListAssociatedResourceSettingsRequest

        The model defined in huaweicloud sdk

        :param limit: 查询记录数。
        :type limit: int
        :param marker: 分页位置标识（索引）。从marker指定索引的下一条数据开始查询。
        :type marker: str
        :param region_id: 规则的区域ID
        :type region_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._region_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if region_id is not None:
            self.region_id = region_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAssociatedResourceSettingsRequest.

        查询记录数。

        :return: The limit of this ListAssociatedResourceSettingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAssociatedResourceSettingsRequest.

        查询记录数。

        :param limit: The limit of this ListAssociatedResourceSettingsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListAssociatedResourceSettingsRequest.

        分页位置标识（索引）。从marker指定索引的下一条数据开始查询。

        :return: The marker of this ListAssociatedResourceSettingsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAssociatedResourceSettingsRequest.

        分页位置标识（索引）。从marker指定索引的下一条数据开始查询。

        :param marker: The marker of this ListAssociatedResourceSettingsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def region_id(self):
        r"""Gets the region_id of this ListAssociatedResourceSettingsRequest.

        规则的区域ID

        :return: The region_id of this ListAssociatedResourceSettingsRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListAssociatedResourceSettingsRequest.

        规则的区域ID

        :param region_id: The region_id of this ListAssociatedResourceSettingsRequest.
        :type region_id: str
        """
        self._region_id = region_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAssociatedResourceSettingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
