# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CapacityOrderResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'rank_list': 'CapacityOrderResponseRankList'
    }

    attribute_map = {
        'type': 'type',
        'rank_list': 'rank_list'
    }

    def __init__(self, type=None, rank_list=None):
        r"""CapacityOrderResponseData

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 容量的种类。 **取值范围：** 根据云服务容量数据显示具体容量类型，一般种类 - cpu：CPU核数。 - mem：内存。 - size：云盘大小。
        :type type: str
        :param rank_list: 
        :type rank_list: :class:`huaweicloudsdkcoc.v1.CapacityOrderResponseRankList`
        """
        
        

        self._type = None
        self._rank_list = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if rank_list is not None:
            self.rank_list = rank_list

    @property
    def type(self):
        r"""Gets the type of this CapacityOrderResponseData.

        **参数解释：** 容量的种类。 **取值范围：** 根据云服务容量数据显示具体容量类型，一般种类 - cpu：CPU核数。 - mem：内存。 - size：云盘大小。

        :return: The type of this CapacityOrderResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CapacityOrderResponseData.

        **参数解释：** 容量的种类。 **取值范围：** 根据云服务容量数据显示具体容量类型，一般种类 - cpu：CPU核数。 - mem：内存。 - size：云盘大小。

        :param type: The type of this CapacityOrderResponseData.
        :type type: str
        """
        self._type = type

    @property
    def rank_list(self):
        r"""Gets the rank_list of this CapacityOrderResponseData.

        :return: The rank_list of this CapacityOrderResponseData.
        :rtype: :class:`huaweicloudsdkcoc.v1.CapacityOrderResponseRankList`
        """
        return self._rank_list

    @rank_list.setter
    def rank_list(self, rank_list):
        r"""Sets the rank_list of this CapacityOrderResponseData.

        :param rank_list: The rank_list of this CapacityOrderResponseData.
        :type rank_list: :class:`huaweicloudsdkcoc.v1.CapacityOrderResponseRankList`
        """
        self._rank_list = rank_list

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
        if not isinstance(other, CapacityOrderResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
