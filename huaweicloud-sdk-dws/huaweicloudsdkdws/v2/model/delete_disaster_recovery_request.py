# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDisasterRecoveryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disaster_recovery_id': 'str',
        'need_send_request': 'int'
    }

    attribute_map = {
        'disaster_recovery_id': 'disaster_recovery_id',
        'need_send_request': 'need_send_request'
    }

    def __init__(self, disaster_recovery_id=None, need_send_request=None):
        r"""DeleteDisasterRecoveryRequest

        The model defined in huaweicloud sdk

        :param disaster_recovery_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type disaster_recovery_id: str
        :param need_send_request: **参数解释**： 跨region时是否需要向另一个集群发请求。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type need_send_request: int
        """
        
        

        self._disaster_recovery_id = None
        self._need_send_request = None
        self.discriminator = None

        self.disaster_recovery_id = disaster_recovery_id
        if need_send_request is not None:
            self.need_send_request = need_send_request

    @property
    def disaster_recovery_id(self):
        r"""Gets the disaster_recovery_id of this DeleteDisasterRecoveryRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The disaster_recovery_id of this DeleteDisasterRecoveryRequest.
        :rtype: str
        """
        return self._disaster_recovery_id

    @disaster_recovery_id.setter
    def disaster_recovery_id(self, disaster_recovery_id):
        r"""Sets the disaster_recovery_id of this DeleteDisasterRecoveryRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param disaster_recovery_id: The disaster_recovery_id of this DeleteDisasterRecoveryRequest.
        :type disaster_recovery_id: str
        """
        self._disaster_recovery_id = disaster_recovery_id

    @property
    def need_send_request(self):
        r"""Gets the need_send_request of this DeleteDisasterRecoveryRequest.

        **参数解释**： 跨region时是否需要向另一个集群发请求。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The need_send_request of this DeleteDisasterRecoveryRequest.
        :rtype: int
        """
        return self._need_send_request

    @need_send_request.setter
    def need_send_request(self, need_send_request):
        r"""Sets the need_send_request of this DeleteDisasterRecoveryRequest.

        **参数解释**： 跨region时是否需要向另一个集群发请求。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param need_send_request: The need_send_request of this DeleteDisasterRecoveryRequest.
        :type need_send_request: int
        """
        self._need_send_request = need_send_request

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
        if not isinstance(other, DeleteDisasterRecoveryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
