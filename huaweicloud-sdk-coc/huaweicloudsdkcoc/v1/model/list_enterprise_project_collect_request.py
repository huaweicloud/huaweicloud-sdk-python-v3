# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseProjectCollectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'id': 'id',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, id=None, marker=None, limit=None):
        r"""ListEnterpriseProjectCollectRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 唯一标识id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param marker: **参数解释：** 分页参数，上一页请求最后一个id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type marker: str
        :param limit: **参数解释：** 分页查询每页显示的条目数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1~500范围。 **默认取值：** 不涉及。
        :type limit: int
        """
        
        

        self._id = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if marker is not None:
            self.marker = marker
        self.limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListEnterpriseProjectCollectRequest.

        **参数解释：** 唯一标识id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this ListEnterpriseProjectCollectRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListEnterpriseProjectCollectRequest.

        **参数解释：** 唯一标识id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this ListEnterpriseProjectCollectRequest.
        :type id: str
        """
        self._id = id

    @property
    def marker(self):
        r"""Gets the marker of this ListEnterpriseProjectCollectRequest.

        **参数解释：** 分页参数，上一页请求最后一个id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The marker of this ListEnterpriseProjectCollectRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListEnterpriseProjectCollectRequest.

        **参数解释：** 分页参数，上一页请求最后一个id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param marker: The marker of this ListEnterpriseProjectCollectRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListEnterpriseProjectCollectRequest.

        **参数解释：** 分页查询每页显示的条目数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1~500范围。 **默认取值：** 不涉及。

        :return: The limit of this ListEnterpriseProjectCollectRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEnterpriseProjectCollectRequest.

        **参数解释：** 分页查询每页显示的条目数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1~500范围。 **默认取值：** 不涉及。

        :param limit: The limit of this ListEnterpriseProjectCollectRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListEnterpriseProjectCollectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
