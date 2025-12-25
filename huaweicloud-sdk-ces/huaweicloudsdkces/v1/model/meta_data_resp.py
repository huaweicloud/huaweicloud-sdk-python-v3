# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaDataResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'total': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'count': 'count',
        'total': 'total',
        'marker': 'marker'
    }

    def __init__(self, count=None, total=None, marker=None):
        r"""MetaDataResp

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 当前返回结果条数。 **取值范围**: 0 - 2147483647 
        :type count: int
        :param total: **参数解释**： 结果总条数。 **取值范围**： 0 - 2147483647 
        :type total: int
        :param marker: **参数解释**： 下一个开始的标记，用于分页。如本次查询10条数据，第十条alarm_id为al1441967036681YkazZ0deN，下次start配置为al1441967036681YkazZ0deN可从该alarm_id开始查询。 **取值范围**： 1 - 9999 
        :type marker: str
        """
        
        

        self._count = None
        self._total = None
        self._marker = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if total is not None:
            self.total = total
        if marker is not None:
            self.marker = marker

    @property
    def count(self):
        r"""Gets the count of this MetaDataResp.

        **参数解释**： 当前返回结果条数。 **取值范围**: 0 - 2147483647 

        :return: The count of this MetaDataResp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this MetaDataResp.

        **参数解释**： 当前返回结果条数。 **取值范围**: 0 - 2147483647 

        :param count: The count of this MetaDataResp.
        :type count: int
        """
        self._count = count

    @property
    def total(self):
        r"""Gets the total of this MetaDataResp.

        **参数解释**： 结果总条数。 **取值范围**： 0 - 2147483647 

        :return: The total of this MetaDataResp.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this MetaDataResp.

        **参数解释**： 结果总条数。 **取值范围**： 0 - 2147483647 

        :param total: The total of this MetaDataResp.
        :type total: int
        """
        self._total = total

    @property
    def marker(self):
        r"""Gets the marker of this MetaDataResp.

        **参数解释**： 下一个开始的标记，用于分页。如本次查询10条数据，第十条alarm_id为al1441967036681YkazZ0deN，下次start配置为al1441967036681YkazZ0deN可从该alarm_id开始查询。 **取值范围**： 1 - 9999 

        :return: The marker of this MetaDataResp.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this MetaDataResp.

        **参数解释**： 下一个开始的标记，用于分页。如本次查询10条数据，第十条alarm_id为al1441967036681YkazZ0deN，下次start配置为al1441967036681YkazZ0deN可从该alarm_id开始查询。 **取值范围**： 1 - 9999 

        :param marker: The marker of this MetaDataResp.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, MetaDataResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
