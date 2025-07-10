# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPolicyGeoipMapResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'continent': 'object',
        'geomap': 'object',
        'locale': 'object'
    }

    attribute_map = {
        'continent': 'continent',
        'geomap': 'geomap',
        'locale': 'locale'
    }

    def __init__(self, continent=None, geomap=None, locale=None):
        r"""ShowPolicyGeoipMapResponse

        The model defined in huaweicloud sdk

        :param continent: **参数解释：** 各个洲上的国家名称分布信息 **取值范围：** 不涉及
        :type continent: object
        :param geomap: **参数解释：** key值为各个国家的简称（AB和AB2除外，AB表示海外及港澳台，AB2表示海外），当key为CN时，里面是数组内容为各个省份的简称 **取值范围：** 不涉及
        :type geomap: object
        :param locale: **参数解释：** geomap中的值对应语言的显示名称 **取值范围：** 不涉及
        :type locale: object
        """
        
        super(ShowPolicyGeoipMapResponse, self).__init__()

        self._continent = None
        self._geomap = None
        self._locale = None
        self.discriminator = None

        if continent is not None:
            self.continent = continent
        if geomap is not None:
            self.geomap = geomap
        if locale is not None:
            self.locale = locale

    @property
    def continent(self):
        r"""Gets the continent of this ShowPolicyGeoipMapResponse.

        **参数解释：** 各个洲上的国家名称分布信息 **取值范围：** 不涉及

        :return: The continent of this ShowPolicyGeoipMapResponse.
        :rtype: object
        """
        return self._continent

    @continent.setter
    def continent(self, continent):
        r"""Sets the continent of this ShowPolicyGeoipMapResponse.

        **参数解释：** 各个洲上的国家名称分布信息 **取值范围：** 不涉及

        :param continent: The continent of this ShowPolicyGeoipMapResponse.
        :type continent: object
        """
        self._continent = continent

    @property
    def geomap(self):
        r"""Gets the geomap of this ShowPolicyGeoipMapResponse.

        **参数解释：** key值为各个国家的简称（AB和AB2除外，AB表示海外及港澳台，AB2表示海外），当key为CN时，里面是数组内容为各个省份的简称 **取值范围：** 不涉及

        :return: The geomap of this ShowPolicyGeoipMapResponse.
        :rtype: object
        """
        return self._geomap

    @geomap.setter
    def geomap(self, geomap):
        r"""Sets the geomap of this ShowPolicyGeoipMapResponse.

        **参数解释：** key值为各个国家的简称（AB和AB2除外，AB表示海外及港澳台，AB2表示海外），当key为CN时，里面是数组内容为各个省份的简称 **取值范围：** 不涉及

        :param geomap: The geomap of this ShowPolicyGeoipMapResponse.
        :type geomap: object
        """
        self._geomap = geomap

    @property
    def locale(self):
        r"""Gets the locale of this ShowPolicyGeoipMapResponse.

        **参数解释：** geomap中的值对应语言的显示名称 **取值范围：** 不涉及

        :return: The locale of this ShowPolicyGeoipMapResponse.
        :rtype: object
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this ShowPolicyGeoipMapResponse.

        **参数解释：** geomap中的值对应语言的显示名称 **取值范围：** 不涉及

        :param locale: The locale of this ShowPolicyGeoipMapResponse.
        :type locale: object
        """
        self._locale = locale

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
        if not isinstance(other, ShowPolicyGeoipMapResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
