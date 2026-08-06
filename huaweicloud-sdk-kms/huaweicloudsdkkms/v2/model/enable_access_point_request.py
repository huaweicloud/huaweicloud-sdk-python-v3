# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableAccessPointRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_point_id': 'str'
    }

    attribute_map = {
        'access_point_id': 'access_point_id'
    }

    def __init__(self, access_point_id=None):
        r"""EnableAccessPointRequest

        The model defined in huaweicloud sdk

        :param access_point_id: **参数解释：** 接入点ID。 **约束限制：** 不涉及 **取值范围：** UUID格式，字符长度36-36。 **默认取值：** 不涉及
        :type access_point_id: str
        """
        
        

        self._access_point_id = None
        self.discriminator = None

        self.access_point_id = access_point_id

    @property
    def access_point_id(self):
        r"""Gets the access_point_id of this EnableAccessPointRequest.

        **参数解释：** 接入点ID。 **约束限制：** 不涉及 **取值范围：** UUID格式，字符长度36-36。 **默认取值：** 不涉及

        :return: The access_point_id of this EnableAccessPointRequest.
        :rtype: str
        """
        return self._access_point_id

    @access_point_id.setter
    def access_point_id(self, access_point_id):
        r"""Sets the access_point_id of this EnableAccessPointRequest.

        **参数解释：** 接入点ID。 **约束限制：** 不涉及 **取值范围：** UUID格式，字符长度36-36。 **默认取值：** 不涉及

        :param access_point_id: The access_point_id of this EnableAccessPointRequest.
        :type access_point_id: str
        """
        self._access_point_id = access_point_id

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
        if not isinstance(other, EnableAccessPointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
