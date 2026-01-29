# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtsResponseVoLogTypes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secm_lts_': 'list[str]'
    }

    attribute_map = {
        'secm_lts_': 'secm_lts_'
    }

    def __init__(self, secm_lts_=None):
        r"""LtsResponseVoLogTypes

        The model defined in huaweicloud sdk

        :param secm_lts_: 类型前缀
        :type secm_lts_: list[str]
        """
        
        

        self._secm_lts_ = None
        self.discriminator = None

        if secm_lts_ is not None:
            self.secm_lts_ = secm_lts_

    @property
    def secm_lts_(self):
        r"""Gets the secm_lts_ of this LtsResponseVoLogTypes.

        类型前缀

        :return: The secm_lts_ of this LtsResponseVoLogTypes.
        :rtype: list[str]
        """
        return self._secm_lts_

    @secm_lts_.setter
    def secm_lts_(self, secm_lts_):
        r"""Sets the secm_lts_ of this LtsResponseVoLogTypes.

        类型前缀

        :param secm_lts_: The secm_lts_ of this LtsResponseVoLogTypes.
        :type secm_lts_: list[str]
        """
        self._secm_lts_ = secm_lts_

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
        if not isinstance(other, LtsResponseVoLogTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
