# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDisasterRecoverRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'primary_cluster_id': 'str',
        'standby_cluster_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'primary_cluster_id': 'primary_cluster_id',
        'standby_cluster_id': 'standby_cluster_id',
        'id': 'id'
    }

    def __init__(self, primary_cluster_id=None, standby_cluster_id=None, id=None):
        r"""ListDisasterRecoverRequest

        The model defined in huaweicloud sdk

        :param primary_cluster_id: **参数解释**： 主集群ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type primary_cluster_id: str
        :param standby_cluster_id: **参数解释**： 备集群ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type standby_cluster_id: str
        :param id: **参数解释**： 容灾ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type id: str
        """
        
        

        self._primary_cluster_id = None
        self._standby_cluster_id = None
        self._id = None
        self.discriminator = None

        if primary_cluster_id is not None:
            self.primary_cluster_id = primary_cluster_id
        if standby_cluster_id is not None:
            self.standby_cluster_id = standby_cluster_id
        if id is not None:
            self.id = id

    @property
    def primary_cluster_id(self):
        r"""Gets the primary_cluster_id of this ListDisasterRecoverRequest.

        **参数解释**： 主集群ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The primary_cluster_id of this ListDisasterRecoverRequest.
        :rtype: str
        """
        return self._primary_cluster_id

    @primary_cluster_id.setter
    def primary_cluster_id(self, primary_cluster_id):
        r"""Sets the primary_cluster_id of this ListDisasterRecoverRequest.

        **参数解释**： 主集群ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param primary_cluster_id: The primary_cluster_id of this ListDisasterRecoverRequest.
        :type primary_cluster_id: str
        """
        self._primary_cluster_id = primary_cluster_id

    @property
    def standby_cluster_id(self):
        r"""Gets the standby_cluster_id of this ListDisasterRecoverRequest.

        **参数解释**： 备集群ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The standby_cluster_id of this ListDisasterRecoverRequest.
        :rtype: str
        """
        return self._standby_cluster_id

    @standby_cluster_id.setter
    def standby_cluster_id(self, standby_cluster_id):
        r"""Sets the standby_cluster_id of this ListDisasterRecoverRequest.

        **参数解释**： 备集群ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param standby_cluster_id: The standby_cluster_id of this ListDisasterRecoverRequest.
        :type standby_cluster_id: str
        """
        self._standby_cluster_id = standby_cluster_id

    @property
    def id(self):
        r"""Gets the id of this ListDisasterRecoverRequest.

        **参数解释**： 容灾ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The id of this ListDisasterRecoverRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListDisasterRecoverRequest.

        **参数解释**： 容灾ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param id: The id of this ListDisasterRecoverRequest.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ListDisasterRecoverRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
