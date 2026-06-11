# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRawIconReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'icon_content': 'str'
    }

    attribute_map = {
        'icon_content': 'icon_content'
    }

    def __init__(self, icon_content=None):
        r"""UpdateRawIconReq

        The model defined in huaweicloud sdk

        :param icon_content: 待更新的应用图标
        :type icon_content: str
        """
        
        

        self._icon_content = None
        self.discriminator = None

        self.icon_content = icon_content

    @property
    def icon_content(self):
        r"""Gets the icon_content of this UpdateRawIconReq.

        待更新的应用图标

        :return: The icon_content of this UpdateRawIconReq.
        :rtype: str
        """
        return self._icon_content

    @icon_content.setter
    def icon_content(self, icon_content):
        r"""Sets the icon_content of this UpdateRawIconReq.

        待更新的应用图标

        :param icon_content: The icon_content of this UpdateRawIconReq.
        :type icon_content: str
        """
        self._icon_content = icon_content

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
        if not isinstance(other, UpdateRawIconReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
