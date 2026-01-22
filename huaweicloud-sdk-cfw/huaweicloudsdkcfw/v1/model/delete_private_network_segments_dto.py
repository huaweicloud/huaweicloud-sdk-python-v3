# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePrivateNetworkSegmentsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conf_ids': 'list[str]'
    }

    attribute_map = {
        'conf_ids': 'conf_ids'
    }

    def __init__(self, conf_ids=None):
        r"""DeletePrivateNetworkSegmentsDto

        The model defined in huaweicloud sdk

        :param conf_ids: **参数解释**： 删除的私网网段ID列表，可以通过调用[获取私网网段的信息]获得，通过返回值中的data.private_network_list.conf_id获得 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type conf_ids: list[str]
        """
        
        

        self._conf_ids = None
        self.discriminator = None

        self.conf_ids = conf_ids

    @property
    def conf_ids(self):
        r"""Gets the conf_ids of this DeletePrivateNetworkSegmentsDto.

        **参数解释**： 删除的私网网段ID列表，可以通过调用[获取私网网段的信息]获得，通过返回值中的data.private_network_list.conf_id获得 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The conf_ids of this DeletePrivateNetworkSegmentsDto.
        :rtype: list[str]
        """
        return self._conf_ids

    @conf_ids.setter
    def conf_ids(self, conf_ids):
        r"""Sets the conf_ids of this DeletePrivateNetworkSegmentsDto.

        **参数解释**： 删除的私网网段ID列表，可以通过调用[获取私网网段的信息]获得，通过返回值中的data.private_network_list.conf_id获得 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param conf_ids: The conf_ids of this DeletePrivateNetworkSegmentsDto.
        :type conf_ids: list[str]
        """
        self._conf_ids = conf_ids

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
        if not isinstance(other, DeletePrivateNetworkSegmentsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
