# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportUsersTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'active_type': 'str'
    }

    attribute_map = {
        'language': 'language',
        'active_type': 'active_type'
    }

    def __init__(self, language=None, active_type=None):
        r"""ExportUsersTemplateRequest

        The model defined in huaweicloud sdk

        :param language: 语言 * zh_CN：中文。 * en_US：英文。
        :type language: str
        :param active_type: 激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活
        :type active_type: str
        """
        
        

        self._language = None
        self._active_type = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if active_type is not None:
            self.active_type = active_type

    @property
    def language(self):
        r"""Gets the language of this ExportUsersTemplateRequest.

        语言 * zh_CN：中文。 * en_US：英文。

        :return: The language of this ExportUsersTemplateRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportUsersTemplateRequest.

        语言 * zh_CN：中文。 * en_US：英文。

        :param language: The language of this ExportUsersTemplateRequest.
        :type language: str
        """
        self._language = language

    @property
    def active_type(self):
        r"""Gets the active_type of this ExportUsersTemplateRequest.

        激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活

        :return: The active_type of this ExportUsersTemplateRequest.
        :rtype: str
        """
        return self._active_type

    @active_type.setter
    def active_type(self, active_type):
        r"""Sets the active_type of this ExportUsersTemplateRequest.

        激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活

        :param active_type: The active_type of this ExportUsersTemplateRequest.
        :type active_type: str
        """
        self._active_type = active_type

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
        if not isinstance(other, ExportUsersTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
