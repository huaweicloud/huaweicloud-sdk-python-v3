# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageVulResponseInfo:

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
        'image_name': 'str',
        'vul_id': 'str',
        'vul_name': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_name': 'image_name',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name'
    }

    def __init__(self, image_id=None, image_name=None, vul_id=None, vul_name=None):
        r"""ImageVulResponseInfo

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-512 
        :type image_id: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-512 
        :type image_name: str
        :param vul_id: **参数解释**: 漏洞id **取值范围**: 字符长度0-512 
        :type vul_id: str
        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符长度0-512 
        :type vul_name: str
        """
        
        

        self._image_id = None
        self._image_name = None
        self._vul_id = None
        self._vul_name = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name

    @property
    def image_id(self):
        r"""Gets the image_id of this ImageVulResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-512 

        :return: The image_id of this ImageVulResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ImageVulResponseInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-512 

        :param image_id: The image_id of this ImageVulResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageVulResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-512 

        :return: The image_name of this ImageVulResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageVulResponseInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-512 

        :param image_name: The image_name of this ImageVulResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ImageVulResponseInfo.

        **参数解释**: 漏洞id **取值范围**: 字符长度0-512 

        :return: The vul_id of this ImageVulResponseInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ImageVulResponseInfo.

        **参数解释**: 漏洞id **取值范围**: 字符长度0-512 

        :param vul_id: The vul_id of this ImageVulResponseInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ImageVulResponseInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-512 

        :return: The vul_name of this ImageVulResponseInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ImageVulResponseInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-512 

        :param vul_name: The vul_name of this ImageVulResponseInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

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
        if not isinstance(other, ImageVulResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
