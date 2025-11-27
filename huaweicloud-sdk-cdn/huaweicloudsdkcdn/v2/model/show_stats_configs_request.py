# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatsConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_type': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'config_type': 'config_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, config_type=None, limit=None, offset=None):
        r"""ShowStatsConfigsRequest

        The model defined in huaweicloud sdk

        :param config_type: - 配置类型 - 目前支持0：热点统计，1：ces上报
        :type config_type: int
        :param limit: **参数解释：** 分页查询每页的数量 **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 10
        :type limit: int
        :param offset: **参数解释：** 查询偏移量，表示跳过多少个数据开始查询 **约束限制：** 不涉及 **取值范围：** 0-65535 **默认取值：** 0
        :type offset: int
        """
        
        

        self._config_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.config_type = config_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def config_type(self):
        r"""Gets the config_type of this ShowStatsConfigsRequest.

        - 配置类型 - 目前支持0：热点统计，1：ces上报

        :return: The config_type of this ShowStatsConfigsRequest.
        :rtype: int
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        r"""Sets the config_type of this ShowStatsConfigsRequest.

        - 配置类型 - 目前支持0：热点统计，1：ces上报

        :param config_type: The config_type of this ShowStatsConfigsRequest.
        :type config_type: int
        """
        self._config_type = config_type

    @property
    def limit(self):
        r"""Gets the limit of this ShowStatsConfigsRequest.

        **参数解释：** 分页查询每页的数量 **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 10

        :return: The limit of this ShowStatsConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowStatsConfigsRequest.

        **参数解释：** 分页查询每页的数量 **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 10

        :param limit: The limit of this ShowStatsConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowStatsConfigsRequest.

        **参数解释：** 查询偏移量，表示跳过多少个数据开始查询 **约束限制：** 不涉及 **取值范围：** 0-65535 **默认取值：** 0

        :return: The offset of this ShowStatsConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowStatsConfigsRequest.

        **参数解释：** 查询偏移量，表示跳过多少个数据开始查询 **约束限制：** 不涉及 **取值范围：** 0-65535 **默认取值：** 0

        :param offset: The offset of this ShowStatsConfigsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowStatsConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
