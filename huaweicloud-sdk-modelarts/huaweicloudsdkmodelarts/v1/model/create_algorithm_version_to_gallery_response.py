# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlgorithmVersionToGalleryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_id': 'str',
        'version_id': 'str',
        'version_num': 'str',
        'content_uri': 'str'
    }

    attribute_map = {
        'content_id': 'content_id',
        'version_id': 'version_id',
        'version_num': 'version_num',
        'content_uri': 'content_uri'
    }

    def __init__(self, content_id=None, version_id=None, version_num=None, content_uri=None):
        r"""CreateAlgorithmVersionToGalleryResponse

        The model defined in huaweicloud sdk

        :param content_id: **参数解释**：资产id。 **取值范围**：不涉及。
        :type content_id: str
        :param version_id: **参数解释**：版本号id。 **取值范围**：不涉及。
        :type version_id: str
        :param version_num: **参数解释**：版本数量。 **取值范围**：不涉及。
        :type version_num: str
        :param content_uri: **参数解释**：资产uri地址。 **取值范围**：不涉及。
        :type content_uri: str
        """
        
        super().__init__()

        self._content_id = None
        self._version_id = None
        self._version_num = None
        self._content_uri = None
        self.discriminator = None

        if content_id is not None:
            self.content_id = content_id
        if version_id is not None:
            self.version_id = version_id
        if version_num is not None:
            self.version_num = version_num
        if content_uri is not None:
            self.content_uri = content_uri

    @property
    def content_id(self):
        r"""Gets the content_id of this CreateAlgorithmVersionToGalleryResponse.

        **参数解释**：资产id。 **取值范围**：不涉及。

        :return: The content_id of this CreateAlgorithmVersionToGalleryResponse.
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        r"""Sets the content_id of this CreateAlgorithmVersionToGalleryResponse.

        **参数解释**：资产id。 **取值范围**：不涉及。

        :param content_id: The content_id of this CreateAlgorithmVersionToGalleryResponse.
        :type content_id: str
        """
        self._content_id = content_id

    @property
    def version_id(self):
        r"""Gets the version_id of this CreateAlgorithmVersionToGalleryResponse.

        **参数解释**：版本号id。 **取值范围**：不涉及。

        :return: The version_id of this CreateAlgorithmVersionToGalleryResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this CreateAlgorithmVersionToGalleryResponse.

        **参数解释**：版本号id。 **取值范围**：不涉及。

        :param version_id: The version_id of this CreateAlgorithmVersionToGalleryResponse.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def version_num(self):
        r"""Gets the version_num of this CreateAlgorithmVersionToGalleryResponse.

        **参数解释**：版本数量。 **取值范围**：不涉及。

        :return: The version_num of this CreateAlgorithmVersionToGalleryResponse.
        :rtype: str
        """
        return self._version_num

    @version_num.setter
    def version_num(self, version_num):
        r"""Sets the version_num of this CreateAlgorithmVersionToGalleryResponse.

        **参数解释**：版本数量。 **取值范围**：不涉及。

        :param version_num: The version_num of this CreateAlgorithmVersionToGalleryResponse.
        :type version_num: str
        """
        self._version_num = version_num

    @property
    def content_uri(self):
        r"""Gets the content_uri of this CreateAlgorithmVersionToGalleryResponse.

        **参数解释**：资产uri地址。 **取值范围**：不涉及。

        :return: The content_uri of this CreateAlgorithmVersionToGalleryResponse.
        :rtype: str
        """
        return self._content_uri

    @content_uri.setter
    def content_uri(self, content_uri):
        r"""Sets the content_uri of this CreateAlgorithmVersionToGalleryResponse.

        **参数解释**：资产uri地址。 **取值范围**：不涉及。

        :param content_uri: The content_uri of this CreateAlgorithmVersionToGalleryResponse.
        :type content_uri: str
        """
        self._content_uri = content_uri

    def to_dict(self):
        import warnings
        warnings.warn("CreateAlgorithmVersionToGalleryResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateAlgorithmVersionToGalleryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
