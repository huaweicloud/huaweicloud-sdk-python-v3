# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHtapFlavorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_name': 'str',
        'availability_zone_mode': 'str',
        'spec_code': 'str',
        'x_language': 'str',
        'version_name': 'str'
    }

    attribute_map = {
        'engine_name': 'engine_name',
        'availability_zone_mode': 'availability_zone_mode',
        'spec_code': 'spec_code',
        'x_language': 'X-Language',
        'version_name': 'version_name'
    }

    def __init__(self, engine_name=None, availability_zone_mode=None, spec_code=None, x_language=None, version_name=None):
        r"""ListHtapFlavorRequest

        The model defined in huaweicloud sdk

        :param engine_name: HTAP引擎名。 取值范围： - star-rocks - click-house
        :type engine_name: str
        :param availability_zone_mode: 可用区模式，当前仅支持single。
        :type availability_zone_mode: str
        :param spec_code: 规格码，提供后仅查询指定规格码规格信息。
        :type spec_code: str
        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param version_name: 数据库版本号，不填默认3.1.6.0。
        :type version_name: str
        """
        
        

        self._engine_name = None
        self._availability_zone_mode = None
        self._spec_code = None
        self._x_language = None
        self._version_name = None
        self.discriminator = None

        self.engine_name = engine_name
        if availability_zone_mode is not None:
            self.availability_zone_mode = availability_zone_mode
        if spec_code is not None:
            self.spec_code = spec_code
        if x_language is not None:
            self.x_language = x_language
        if version_name is not None:
            self.version_name = version_name

    @property
    def engine_name(self):
        r"""Gets the engine_name of this ListHtapFlavorRequest.

        HTAP引擎名。 取值范围： - star-rocks - click-house

        :return: The engine_name of this ListHtapFlavorRequest.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this ListHtapFlavorRequest.

        HTAP引擎名。 取值范围： - star-rocks - click-house

        :param engine_name: The engine_name of this ListHtapFlavorRequest.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def availability_zone_mode(self):
        r"""Gets the availability_zone_mode of this ListHtapFlavorRequest.

        可用区模式，当前仅支持single。

        :return: The availability_zone_mode of this ListHtapFlavorRequest.
        :rtype: str
        """
        return self._availability_zone_mode

    @availability_zone_mode.setter
    def availability_zone_mode(self, availability_zone_mode):
        r"""Sets the availability_zone_mode of this ListHtapFlavorRequest.

        可用区模式，当前仅支持single。

        :param availability_zone_mode: The availability_zone_mode of this ListHtapFlavorRequest.
        :type availability_zone_mode: str
        """
        self._availability_zone_mode = availability_zone_mode

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ListHtapFlavorRequest.

        规格码，提供后仅查询指定规格码规格信息。

        :return: The spec_code of this ListHtapFlavorRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ListHtapFlavorRequest.

        规格码，提供后仅查询指定规格码规格信息。

        :param spec_code: The spec_code of this ListHtapFlavorRequest.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def x_language(self):
        r"""Gets the x_language of this ListHtapFlavorRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ListHtapFlavorRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListHtapFlavorRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ListHtapFlavorRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def version_name(self):
        r"""Gets the version_name of this ListHtapFlavorRequest.

        数据库版本号，不填默认3.1.6.0。

        :return: The version_name of this ListHtapFlavorRequest.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this ListHtapFlavorRequest.

        数据库版本号，不填默认3.1.6.0。

        :param version_name: The version_name of this ListHtapFlavorRequest.
        :type version_name: str
        """
        self._version_name = version_name

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
        if not isinstance(other, ListHtapFlavorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
