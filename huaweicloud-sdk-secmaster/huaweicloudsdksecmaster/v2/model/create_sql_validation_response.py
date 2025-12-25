# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlValidationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sources': 'list[TableItem]',
        'modes': 'list[str]'
    }

    attribute_map = {
        'sources': 'sources',
        'modes': 'modes'
    }

    def __init__(self, sources=None, modes=None):
        r"""CreateSqlValidationResponse

        The model defined in huaweicloud sdk

        :param sources: 源表
        :type sources: list[:class:`huaweicloudsdksecmaster.v2.TableItem`]
        :param modes: 模式
        :type modes: list[str]
        """
        
        super().__init__()

        self._sources = None
        self._modes = None
        self.discriminator = None

        if sources is not None:
            self.sources = sources
        if modes is not None:
            self.modes = modes

    @property
    def sources(self):
        r"""Gets the sources of this CreateSqlValidationResponse.

        源表

        :return: The sources of this CreateSqlValidationResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.TableItem`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this CreateSqlValidationResponse.

        源表

        :param sources: The sources of this CreateSqlValidationResponse.
        :type sources: list[:class:`huaweicloudsdksecmaster.v2.TableItem`]
        """
        self._sources = sources

    @property
    def modes(self):
        r"""Gets the modes of this CreateSqlValidationResponse.

        模式

        :return: The modes of this CreateSqlValidationResponse.
        :rtype: list[str]
        """
        return self._modes

    @modes.setter
    def modes(self, modes):
        r"""Sets the modes of this CreateSqlValidationResponse.

        模式

        :param modes: The modes of this CreateSqlValidationResponse.
        :type modes: list[str]
        """
        self._modes = modes

    def to_dict(self):
        import warnings
        warnings.warn("CreateSqlValidationResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateSqlValidationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
