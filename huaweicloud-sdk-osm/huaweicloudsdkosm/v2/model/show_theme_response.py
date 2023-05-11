# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowThemeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'themes': 'list[RelationTheme]',
        'error_code': 'str',
        'error_msg': 'str',
        'product_type_id': 'str',
        'theme_name': 'str'
    }

    attribute_map = {
        'themes': 'themes',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'product_type_id': 'product_type_id',
        'theme_name': 'theme_name'
    }

    def __init__(self, themes=None, error_code=None, error_msg=None, product_type_id=None, theme_name=None):
        """ShowThemeResponse

        The model defined in huaweicloud sdk

        :param themes: 关联主题列表
        :type themes: list[:class:`huaweicloudsdkosm.v2.RelationTheme`]
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误描述
        :type error_msg: str
        :param product_type_id: 产品类型Id
        :type product_type_id: str
        :param theme_name: 主题名称
        :type theme_name: str
        """
        
        super(ShowThemeResponse, self).__init__()

        self._themes = None
        self._error_code = None
        self._error_msg = None
        self._product_type_id = None
        self._theme_name = None
        self.discriminator = None

        if themes is not None:
            self.themes = themes
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if product_type_id is not None:
            self.product_type_id = product_type_id
        if theme_name is not None:
            self.theme_name = theme_name

    @property
    def themes(self):
        """Gets the themes of this ShowThemeResponse.

        关联主题列表

        :return: The themes of this ShowThemeResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.RelationTheme`]
        """
        return self._themes

    @themes.setter
    def themes(self, themes):
        """Sets the themes of this ShowThemeResponse.

        关联主题列表

        :param themes: The themes of this ShowThemeResponse.
        :type themes: list[:class:`huaweicloudsdkosm.v2.RelationTheme`]
        """
        self._themes = themes

    @property
    def error_code(self):
        """Gets the error_code of this ShowThemeResponse.

        错误码

        :return: The error_code of this ShowThemeResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ShowThemeResponse.

        错误码

        :param error_code: The error_code of this ShowThemeResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ShowThemeResponse.

        错误描述

        :return: The error_msg of this ShowThemeResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ShowThemeResponse.

        错误描述

        :param error_msg: The error_msg of this ShowThemeResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def product_type_id(self):
        """Gets the product_type_id of this ShowThemeResponse.

        产品类型Id

        :return: The product_type_id of this ShowThemeResponse.
        :rtype: str
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this ShowThemeResponse.

        产品类型Id

        :param product_type_id: The product_type_id of this ShowThemeResponse.
        :type product_type_id: str
        """
        self._product_type_id = product_type_id

    @property
    def theme_name(self):
        """Gets the theme_name of this ShowThemeResponse.

        主题名称

        :return: The theme_name of this ShowThemeResponse.
        :rtype: str
        """
        return self._theme_name

    @theme_name.setter
    def theme_name(self, theme_name):
        """Sets the theme_name of this ShowThemeResponse.

        主题名称

        :param theme_name: The theme_name of this ShowThemeResponse.
        :type theme_name: str
        """
        self._theme_name = theme_name

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
        if not isinstance(other, ShowThemeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
