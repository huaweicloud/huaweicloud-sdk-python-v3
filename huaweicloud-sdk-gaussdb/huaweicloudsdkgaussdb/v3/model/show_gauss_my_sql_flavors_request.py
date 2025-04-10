# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGaussMySqlFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'database_name': 'str',
        'version_name': 'str',
        'availability_zone_mode': 'str',
        'spec_code': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'database_name': 'database_name',
        'version_name': 'version_name',
        'availability_zone_mode': 'availability_zone_mode',
        'spec_code': 'spec_code'
    }

    def __init__(self, x_language=None, database_name=None, version_name=None, availability_zone_mode=None, spec_code=None):
        r"""ShowGaussMySqlFlavorsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param database_name: 数据库引擎名称。
        :type database_name: str
        :param version_name: 数据库版本号，目前仅支持兼容MySQL 8.0。
        :type version_name: str
        :param availability_zone_mode: 规格的可用区模式，现在仅支持\&quot;single\&quot;、\&quot;multi\&quot;，不区分大小写。
        :type availability_zone_mode: str
        :param spec_code: 规格编码。
        :type spec_code: str
        """
        
        

        self._x_language = None
        self._database_name = None
        self._version_name = None
        self._availability_zone_mode = None
        self._spec_code = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.database_name = database_name
        if version_name is not None:
            self.version_name = version_name
        self.availability_zone_mode = availability_zone_mode
        if spec_code is not None:
            self.spec_code = spec_code

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowGaussMySqlFlavorsRequest.

        语言。

        :return: The x_language of this ShowGaussMySqlFlavorsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowGaussMySqlFlavorsRequest.

        语言。

        :param x_language: The x_language of this ShowGaussMySqlFlavorsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowGaussMySqlFlavorsRequest.

        数据库引擎名称。

        :return: The database_name of this ShowGaussMySqlFlavorsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowGaussMySqlFlavorsRequest.

        数据库引擎名称。

        :param database_name: The database_name of this ShowGaussMySqlFlavorsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def version_name(self):
        r"""Gets the version_name of this ShowGaussMySqlFlavorsRequest.

        数据库版本号，目前仅支持兼容MySQL 8.0。

        :return: The version_name of this ShowGaussMySqlFlavorsRequest.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this ShowGaussMySqlFlavorsRequest.

        数据库版本号，目前仅支持兼容MySQL 8.0。

        :param version_name: The version_name of this ShowGaussMySqlFlavorsRequest.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def availability_zone_mode(self):
        r"""Gets the availability_zone_mode of this ShowGaussMySqlFlavorsRequest.

        规格的可用区模式，现在仅支持\"single\"、\"multi\"，不区分大小写。

        :return: The availability_zone_mode of this ShowGaussMySqlFlavorsRequest.
        :rtype: str
        """
        return self._availability_zone_mode

    @availability_zone_mode.setter
    def availability_zone_mode(self, availability_zone_mode):
        r"""Sets the availability_zone_mode of this ShowGaussMySqlFlavorsRequest.

        规格的可用区模式，现在仅支持\"single\"、\"multi\"，不区分大小写。

        :param availability_zone_mode: The availability_zone_mode of this ShowGaussMySqlFlavorsRequest.
        :type availability_zone_mode: str
        """
        self._availability_zone_mode = availability_zone_mode

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ShowGaussMySqlFlavorsRequest.

        规格编码。

        :return: The spec_code of this ShowGaussMySqlFlavorsRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ShowGaussMySqlFlavorsRequest.

        规格编码。

        :param spec_code: The spec_code of this ShowGaussMySqlFlavorsRequest.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, ShowGaussMySqlFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
