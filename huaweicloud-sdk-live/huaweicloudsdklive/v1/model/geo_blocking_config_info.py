# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeoBlockingConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app': 'str',
        'area_whitelist': 'list[str]'
    }

    attribute_map = {
        'app': 'app',
        'area_whitelist': 'area_whitelist'
    }

    def __init__(self, app=None, area_whitelist=None):
        r"""GeoBlockingConfigInfo

        The model defined in huaweicloud sdk

        :param app: 应用名
        :type app: str
        :param area_whitelist: 限制区域列表, 空列表表示不限制。 除中国以外，其他地区代码，2位字母大写。代码格式参阅[ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#search/code/) 包含如下部分取值： - CN-IN：中国大陆 - CN-HK：中国香港 - CN-MO：中国澳门 - CN-TW：中国台湾 - BR：巴西
        :type area_whitelist: list[str]
        """
        
        

        self._app = None
        self._area_whitelist = None
        self.discriminator = None

        self.app = app
        if area_whitelist is not None:
            self.area_whitelist = area_whitelist

    @property
    def app(self):
        r"""Gets the app of this GeoBlockingConfigInfo.

        应用名

        :return: The app of this GeoBlockingConfigInfo.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this GeoBlockingConfigInfo.

        应用名

        :param app: The app of this GeoBlockingConfigInfo.
        :type app: str
        """
        self._app = app

    @property
    def area_whitelist(self):
        r"""Gets the area_whitelist of this GeoBlockingConfigInfo.

        限制区域列表, 空列表表示不限制。 除中国以外，其他地区代码，2位字母大写。代码格式参阅[ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#search/code/) 包含如下部分取值： - CN-IN：中国大陆 - CN-HK：中国香港 - CN-MO：中国澳门 - CN-TW：中国台湾 - BR：巴西

        :return: The area_whitelist of this GeoBlockingConfigInfo.
        :rtype: list[str]
        """
        return self._area_whitelist

    @area_whitelist.setter
    def area_whitelist(self, area_whitelist):
        r"""Sets the area_whitelist of this GeoBlockingConfigInfo.

        限制区域列表, 空列表表示不限制。 除中国以外，其他地区代码，2位字母大写。代码格式参阅[ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#search/code/) 包含如下部分取值： - CN-IN：中国大陆 - CN-HK：中国香港 - CN-MO：中国澳门 - CN-TW：中国台湾 - BR：巴西

        :param area_whitelist: The area_whitelist of this GeoBlockingConfigInfo.
        :type area_whitelist: list[str]
        """
        self._area_whitelist = area_whitelist

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
        if not isinstance(other, GeoBlockingConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
