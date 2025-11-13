# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdatePublicRecordsetsTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_names': 'list[str]',
        'filter': 'BatchUpdatePublicRecordsetsFilter',
        'update_info': 'BatchUpdatePublicRecordsetsUpdateValue'
    }

    attribute_map = {
        'zone_names': 'zone_names',
        'filter': 'filter',
        'update_info': 'update_info'
    }

    def __init__(self, zone_names=None, filter=None, update_info=None):
        r"""BatchUpdatePublicRecordsetsTaskRequestBody

        The model defined in huaweicloud sdk

        :param zone_names: **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type zone_names: list[str]
        :param filter: 
        :type filter: :class:`huaweicloudsdkdns.v2.BatchUpdatePublicRecordsetsFilter`
        :param update_info: 
        :type update_info: :class:`huaweicloudsdkdns.v2.BatchUpdatePublicRecordsetsUpdateValue`
        """
        
        

        self._zone_names = None
        self._filter = None
        self._update_info = None
        self.discriminator = None

        self.zone_names = zone_names
        self.filter = filter
        self.update_info = update_info

    @property
    def zone_names(self):
        r"""Gets the zone_names of this BatchUpdatePublicRecordsetsTaskRequestBody.

        **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The zone_names of this BatchUpdatePublicRecordsetsTaskRequestBody.
        :rtype: list[str]
        """
        return self._zone_names

    @zone_names.setter
    def zone_names(self, zone_names):
        r"""Sets the zone_names of this BatchUpdatePublicRecordsetsTaskRequestBody.

        **参数解释：** 托管该记录的域名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param zone_names: The zone_names of this BatchUpdatePublicRecordsetsTaskRequestBody.
        :type zone_names: list[str]
        """
        self._zone_names = zone_names

    @property
    def filter(self):
        r"""Gets the filter of this BatchUpdatePublicRecordsetsTaskRequestBody.

        :return: The filter of this BatchUpdatePublicRecordsetsTaskRequestBody.
        :rtype: :class:`huaweicloudsdkdns.v2.BatchUpdatePublicRecordsetsFilter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this BatchUpdatePublicRecordsetsTaskRequestBody.

        :param filter: The filter of this BatchUpdatePublicRecordsetsTaskRequestBody.
        :type filter: :class:`huaweicloudsdkdns.v2.BatchUpdatePublicRecordsetsFilter`
        """
        self._filter = filter

    @property
    def update_info(self):
        r"""Gets the update_info of this BatchUpdatePublicRecordsetsTaskRequestBody.

        :return: The update_info of this BatchUpdatePublicRecordsetsTaskRequestBody.
        :rtype: :class:`huaweicloudsdkdns.v2.BatchUpdatePublicRecordsetsUpdateValue`
        """
        return self._update_info

    @update_info.setter
    def update_info(self, update_info):
        r"""Sets the update_info of this BatchUpdatePublicRecordsetsTaskRequestBody.

        :param update_info: The update_info of this BatchUpdatePublicRecordsetsTaskRequestBody.
        :type update_info: :class:`huaweicloudsdkdns.v2.BatchUpdatePublicRecordsetsUpdateValue`
        """
        self._update_info = update_info

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
        if not isinstance(other, BatchUpdatePublicRecordsetsTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
