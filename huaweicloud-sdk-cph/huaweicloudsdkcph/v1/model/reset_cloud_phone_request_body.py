# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetCloudPhoneRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'phones': 'list[PhoneProperty]'
    }

    attribute_map = {
        'image_id': 'image_id',
        'phones': 'phones'
    }

    def __init__(self, image_id=None, phones=None):
        r"""ResetCloudPhoneRequestBody

        The model defined in huaweicloud sdk

        :param image_id: 云手机镜像。
        :type image_id: str
        :param phones: 云手机列表。
        :type phones: list[:class:`huaweicloudsdkcph.v1.PhoneProperty`]
        """
        
        

        self._image_id = None
        self._phones = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        self.phones = phones

    @property
    def image_id(self):
        r"""Gets the image_id of this ResetCloudPhoneRequestBody.

        云手机镜像。

        :return: The image_id of this ResetCloudPhoneRequestBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ResetCloudPhoneRequestBody.

        云手机镜像。

        :param image_id: The image_id of this ResetCloudPhoneRequestBody.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def phones(self):
        r"""Gets the phones of this ResetCloudPhoneRequestBody.

        云手机列表。

        :return: The phones of this ResetCloudPhoneRequestBody.
        :rtype: list[:class:`huaweicloudsdkcph.v1.PhoneProperty`]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        r"""Sets the phones of this ResetCloudPhoneRequestBody.

        云手机列表。

        :param phones: The phones of this ResetCloudPhoneRequestBody.
        :type phones: list[:class:`huaweicloudsdkcph.v1.PhoneProperty`]
        """
        self._phones = phones

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
        if not isinstance(other, ResetCloudPhoneRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
