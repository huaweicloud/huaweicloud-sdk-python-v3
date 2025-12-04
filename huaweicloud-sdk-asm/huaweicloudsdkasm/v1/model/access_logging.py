# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessLogging:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lts': 'list[LtsConfig]'
    }

    attribute_map = {
        'lts': 'lts'
    }

    def __init__(self, lts=None):
        r"""AccessLogging

        The model defined in huaweicloud sdk

        :param lts: LTS配置
        :type lts: list[:class:`huaweicloudsdkasm.v1.LtsConfig`]
        """
        
        

        self._lts = None
        self.discriminator = None

        if lts is not None:
            self.lts = lts

    @property
    def lts(self):
        r"""Gets the lts of this AccessLogging.

        LTS配置

        :return: The lts of this AccessLogging.
        :rtype: list[:class:`huaweicloudsdkasm.v1.LtsConfig`]
        """
        return self._lts

    @lts.setter
    def lts(self, lts):
        r"""Sets the lts of this AccessLogging.

        LTS配置

        :param lts: The lts of this AccessLogging.
        :type lts: list[:class:`huaweicloudsdkasm.v1.LtsConfig`]
        """
        self._lts = lts

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
        if not isinstance(other, AccessLogging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
