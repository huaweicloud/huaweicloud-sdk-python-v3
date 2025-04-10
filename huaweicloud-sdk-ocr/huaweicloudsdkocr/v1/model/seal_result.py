# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SealResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'seal_list': 'list[SealList]',
        'erased_seal_image': 'str'
    }

    attribute_map = {
        'seal_list': 'seal_list',
        'erased_seal_image': 'erased_seal_image'
    }

    def __init__(self, seal_list=None, erased_seal_image=None):
        r"""SealResult

        The model defined in huaweicloud sdk

        :param seal_list: 印章信息列表。 
        :type seal_list: list[:class:`huaweicloudsdkocr.v1.SealList`]
        :param erased_seal_image: 在输入图片基础上进行印章擦除后的base64编码图片。 
        :type erased_seal_image: str
        """
        
        

        self._seal_list = None
        self._erased_seal_image = None
        self.discriminator = None

        if seal_list is not None:
            self.seal_list = seal_list
        if erased_seal_image is not None:
            self.erased_seal_image = erased_seal_image

    @property
    def seal_list(self):
        r"""Gets the seal_list of this SealResult.

        印章信息列表。 

        :return: The seal_list of this SealResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SealList`]
        """
        return self._seal_list

    @seal_list.setter
    def seal_list(self, seal_list):
        r"""Sets the seal_list of this SealResult.

        印章信息列表。 

        :param seal_list: The seal_list of this SealResult.
        :type seal_list: list[:class:`huaweicloudsdkocr.v1.SealList`]
        """
        self._seal_list = seal_list

    @property
    def erased_seal_image(self):
        r"""Gets the erased_seal_image of this SealResult.

        在输入图片基础上进行印章擦除后的base64编码图片。 

        :return: The erased_seal_image of this SealResult.
        :rtype: str
        """
        return self._erased_seal_image

    @erased_seal_image.setter
    def erased_seal_image(self, erased_seal_image):
        r"""Sets the erased_seal_image of this SealResult.

        在输入图片基础上进行印章擦除后的base64编码图片。 

        :param erased_seal_image: The erased_seal_image of this SealResult.
        :type erased_seal_image: str
        """
        self._erased_seal_image = erased_seal_image

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SealResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
