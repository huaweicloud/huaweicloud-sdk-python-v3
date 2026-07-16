# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlgorithmVersionToGalleryBody:

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
        'content_info': 'ContentInfo',
        'algorithm': 'AlgorithmInfo'
    }

    attribute_map = {
        'content_id': 'content_id',
        'content_info': 'content_info',
        'algorithm': 'algorithm'
    }

    def __init__(self, content_id=None, content_info=None, algorithm=None):
        r"""CreateAlgorithmVersionToGalleryBody

        The model defined in huaweicloud sdk

        :param content_id: **参数解释**：资产id。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type content_id: str
        :param content_info: 
        :type content_info: :class:`huaweicloudsdkmodelarts.v1.ContentInfo`
        :param algorithm: 
        :type algorithm: :class:`huaweicloudsdkmodelarts.v1.AlgorithmInfo`
        """
        
        

        self._content_id = None
        self._content_info = None
        self._algorithm = None
        self.discriminator = None

        if content_id is not None:
            self.content_id = content_id
        if content_info is not None:
            self.content_info = content_info
        if algorithm is not None:
            self.algorithm = algorithm

    @property
    def content_id(self):
        r"""Gets the content_id of this CreateAlgorithmVersionToGalleryBody.

        **参数解释**：资产id。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The content_id of this CreateAlgorithmVersionToGalleryBody.
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        r"""Sets the content_id of this CreateAlgorithmVersionToGalleryBody.

        **参数解释**：资产id。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param content_id: The content_id of this CreateAlgorithmVersionToGalleryBody.
        :type content_id: str
        """
        self._content_id = content_id

    @property
    def content_info(self):
        r"""Gets the content_info of this CreateAlgorithmVersionToGalleryBody.

        :return: The content_info of this CreateAlgorithmVersionToGalleryBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ContentInfo`
        """
        return self._content_info

    @content_info.setter
    def content_info(self, content_info):
        r"""Sets the content_info of this CreateAlgorithmVersionToGalleryBody.

        :param content_info: The content_info of this CreateAlgorithmVersionToGalleryBody.
        :type content_info: :class:`huaweicloudsdkmodelarts.v1.ContentInfo`
        """
        self._content_info = content_info

    @property
    def algorithm(self):
        r"""Gets the algorithm of this CreateAlgorithmVersionToGalleryBody.

        :return: The algorithm of this CreateAlgorithmVersionToGalleryBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AlgorithmInfo`
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this CreateAlgorithmVersionToGalleryBody.

        :param algorithm: The algorithm of this CreateAlgorithmVersionToGalleryBody.
        :type algorithm: :class:`huaweicloudsdkmodelarts.v1.AlgorithmInfo`
        """
        self._algorithm = algorithm

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
        if not isinstance(other, CreateAlgorithmVersionToGalleryBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
