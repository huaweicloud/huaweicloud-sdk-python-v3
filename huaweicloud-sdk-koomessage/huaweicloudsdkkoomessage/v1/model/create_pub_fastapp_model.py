# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePubFastappModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'logo_img': 'str',
        'description': 'str',
        'deeplink': 'str',
        'depend_engine_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'logo_img': 'logo_img',
        'description': 'description',
        'deeplink': 'deeplink',
        'depend_engine_version': 'depend_engine_version'
    }

    def __init__(self, name=None, logo_img=None, description=None, deeplink=None, depend_engine_version=None):
        """CreatePubFastappModel

        The model defined in huaweicloud sdk

        :param name: 快应用名。  &gt; 长度范围为1-30个字符，中文占2个字符，英文占1个字符。 
        :type name: str
        :param logo_img: 快应用LOGO图片资源ID。  &gt; 图片格式为jpg、bmp、jpeg，分辨率大于等于192*192，大小不超过4M。参数值为上传智能信息服务号图片资源API返回的resource_id。 
        :type logo_img: str
        :param description: 快应用描述。  &gt; 长度范围为1-38个字符，中文占2个字符，英文占1个字符。 
        :type description: str
        :param deeplink: 快应用跳转链接。
        :type deeplink: str
        :param depend_engine_version: 快应用依赖引擎版本。  &gt; 长度范围为1-50个字符，中文占2个字符，英文占1个字符。 
        :type depend_engine_version: str
        """
        
        

        self._name = None
        self._logo_img = None
        self._description = None
        self._deeplink = None
        self._depend_engine_version = None
        self.discriminator = None

        self.name = name
        self.logo_img = logo_img
        if description is not None:
            self.description = description
        self.deeplink = deeplink
        self.depend_engine_version = depend_engine_version

    @property
    def name(self):
        """Gets the name of this CreatePubFastappModel.

        快应用名。  > 长度范围为1-30个字符，中文占2个字符，英文占1个字符。 

        :return: The name of this CreatePubFastappModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePubFastappModel.

        快应用名。  > 长度范围为1-30个字符，中文占2个字符，英文占1个字符。 

        :param name: The name of this CreatePubFastappModel.
        :type name: str
        """
        self._name = name

    @property
    def logo_img(self):
        """Gets the logo_img of this CreatePubFastappModel.

        快应用LOGO图片资源ID。  > 图片格式为jpg、bmp、jpeg，分辨率大于等于192*192，大小不超过4M。参数值为上传智能信息服务号图片资源API返回的resource_id。 

        :return: The logo_img of this CreatePubFastappModel.
        :rtype: str
        """
        return self._logo_img

    @logo_img.setter
    def logo_img(self, logo_img):
        """Sets the logo_img of this CreatePubFastappModel.

        快应用LOGO图片资源ID。  > 图片格式为jpg、bmp、jpeg，分辨率大于等于192*192，大小不超过4M。参数值为上传智能信息服务号图片资源API返回的resource_id。 

        :param logo_img: The logo_img of this CreatePubFastappModel.
        :type logo_img: str
        """
        self._logo_img = logo_img

    @property
    def description(self):
        """Gets the description of this CreatePubFastappModel.

        快应用描述。  > 长度范围为1-38个字符，中文占2个字符，英文占1个字符。 

        :return: The description of this CreatePubFastappModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePubFastappModel.

        快应用描述。  > 长度范围为1-38个字符，中文占2个字符，英文占1个字符。 

        :param description: The description of this CreatePubFastappModel.
        :type description: str
        """
        self._description = description

    @property
    def deeplink(self):
        """Gets the deeplink of this CreatePubFastappModel.

        快应用跳转链接。

        :return: The deeplink of this CreatePubFastappModel.
        :rtype: str
        """
        return self._deeplink

    @deeplink.setter
    def deeplink(self, deeplink):
        """Sets the deeplink of this CreatePubFastappModel.

        快应用跳转链接。

        :param deeplink: The deeplink of this CreatePubFastappModel.
        :type deeplink: str
        """
        self._deeplink = deeplink

    @property
    def depend_engine_version(self):
        """Gets the depend_engine_version of this CreatePubFastappModel.

        快应用依赖引擎版本。  > 长度范围为1-50个字符，中文占2个字符，英文占1个字符。 

        :return: The depend_engine_version of this CreatePubFastappModel.
        :rtype: str
        """
        return self._depend_engine_version

    @depend_engine_version.setter
    def depend_engine_version(self, depend_engine_version):
        """Sets the depend_engine_version of this CreatePubFastappModel.

        快应用依赖引擎版本。  > 长度范围为1-50个字符，中文占2个字符，英文占1个字符。 

        :param depend_engine_version: The depend_engine_version of this CreatePubFastappModel.
        :type depend_engine_version: str
        """
        self._depend_engine_version = depend_engine_version

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
        if not isinstance(other, CreatePubFastappModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
