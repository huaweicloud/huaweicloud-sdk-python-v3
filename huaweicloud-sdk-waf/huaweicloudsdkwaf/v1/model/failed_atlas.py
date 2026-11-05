# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedAtlas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'atlas_id': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'atlas_id': 'atlas_id',
        'reason': 'reason'
    }

    def __init__(self, atlas_id=None, reason=None):
        r"""FailedAtlas

        The model defined in huaweicloud sdk

        :param atlas_id: 图库ID
        :type atlas_id: str
        :param reason: 失败原因
        :type reason: str
        """
        
        

        self._atlas_id = None
        self._reason = None
        self.discriminator = None

        if atlas_id is not None:
            self.atlas_id = atlas_id
        if reason is not None:
            self.reason = reason

    @property
    def atlas_id(self):
        r"""Gets the atlas_id of this FailedAtlas.

        图库ID

        :return: The atlas_id of this FailedAtlas.
        :rtype: str
        """
        return self._atlas_id

    @atlas_id.setter
    def atlas_id(self, atlas_id):
        r"""Sets the atlas_id of this FailedAtlas.

        图库ID

        :param atlas_id: The atlas_id of this FailedAtlas.
        :type atlas_id: str
        """
        self._atlas_id = atlas_id

    @property
    def reason(self):
        r"""Gets the reason of this FailedAtlas.

        失败原因

        :return: The reason of this FailedAtlas.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this FailedAtlas.

        失败原因

        :param reason: The reason of this FailedAtlas.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, FailedAtlas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
