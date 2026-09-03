# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyEngineAttachmentSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entity_type': 'EntityType',
        'entity_id': 'str',
        'mode': 'PolicyEngineMode',
        'attached_at': 'datetime'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'entity_id': 'entity_id',
        'mode': 'mode',
        'attached_at': 'attached_at'
    }

    def __init__(self, entity_type=None, entity_id=None, mode=None, attached_at=None):
        r"""PolicyEngineAttachmentSummary

        The model defined in huaweicloud sdk

        :param entity_type: 
        :type entity_type: :class:`huaweicloudsdkagentidentity.v1.EntityType`
        :param entity_id: The unique identifier of the attached entity.
        :type entity_id: str
        :param mode: 
        :type mode: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineMode`
        :param attached_at: Timestamp in RFC 3339 format (UTC)
        :type attached_at: datetime
        """
        
        

        self._entity_type = None
        self._entity_id = None
        self._mode = None
        self._attached_at = None
        self.discriminator = None

        self.entity_type = entity_type
        self.entity_id = entity_id
        self.mode = mode
        self.attached_at = attached_at

    @property
    def entity_type(self):
        r"""Gets the entity_type of this PolicyEngineAttachmentSummary.

        :return: The entity_type of this PolicyEngineAttachmentSummary.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.EntityType`
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        r"""Sets the entity_type of this PolicyEngineAttachmentSummary.

        :param entity_type: The entity_type of this PolicyEngineAttachmentSummary.
        :type entity_type: :class:`huaweicloudsdkagentidentity.v1.EntityType`
        """
        self._entity_type = entity_type

    @property
    def entity_id(self):
        r"""Gets the entity_id of this PolicyEngineAttachmentSummary.

        The unique identifier of the attached entity.

        :return: The entity_id of this PolicyEngineAttachmentSummary.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this PolicyEngineAttachmentSummary.

        The unique identifier of the attached entity.

        :param entity_id: The entity_id of this PolicyEngineAttachmentSummary.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def mode(self):
        r"""Gets the mode of this PolicyEngineAttachmentSummary.

        :return: The mode of this PolicyEngineAttachmentSummary.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineMode`
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this PolicyEngineAttachmentSummary.

        :param mode: The mode of this PolicyEngineAttachmentSummary.
        :type mode: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineMode`
        """
        self._mode = mode

    @property
    def attached_at(self):
        r"""Gets the attached_at of this PolicyEngineAttachmentSummary.

        Timestamp in RFC 3339 format (UTC)

        :return: The attached_at of this PolicyEngineAttachmentSummary.
        :rtype: datetime
        """
        return self._attached_at

    @attached_at.setter
    def attached_at(self, attached_at):
        r"""Sets the attached_at of this PolicyEngineAttachmentSummary.

        Timestamp in RFC 3339 format (UTC)

        :param attached_at: The attached_at of this PolicyEngineAttachmentSummary.
        :type attached_at: datetime
        """
        self._attached_at = attached_at

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
        if not isinstance(other, PolicyEngineAttachmentSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
