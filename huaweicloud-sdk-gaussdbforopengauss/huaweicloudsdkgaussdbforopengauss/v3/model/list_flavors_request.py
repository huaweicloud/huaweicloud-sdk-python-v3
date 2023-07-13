# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsRequest:

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
        'version': 'str',
        'spec_code': 'str',
        'ha_mode': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'version': 'version',
        'spec_code': 'spec_code',
        'ha_mode': 'ha_mode',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, version=None, spec_code=None, ha_mode=None, limit=None, offset=None):
        """ListFlavorsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param version: 数据库版本号。
        :type version: str
        :param spec_code: 规格编码
        :type spec_code: str
        :param ha_mode: 实例类型  集中式centralization_standard  分布式enterprise
        :type ha_mode: str
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        """
        
        

        self._x_language = None
        self._version = None
        self._spec_code = None
        self._ha_mode = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if version is not None:
            self.version = version
        if spec_code is not None:
            self.spec_code = spec_code
        if ha_mode is not None:
            self.ha_mode = ha_mode
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        """Gets the x_language of this ListFlavorsRequest.

        语言

        :return: The x_language of this ListFlavorsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListFlavorsRequest.

        语言

        :param x_language: The x_language of this ListFlavorsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def version(self):
        """Gets the version of this ListFlavorsRequest.

        数据库版本号。

        :return: The version of this ListFlavorsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListFlavorsRequest.

        数据库版本号。

        :param version: The version of this ListFlavorsRequest.
        :type version: str
        """
        self._version = version

    @property
    def spec_code(self):
        """Gets the spec_code of this ListFlavorsRequest.

        规格编码

        :return: The spec_code of this ListFlavorsRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ListFlavorsRequest.

        规格编码

        :param spec_code: The spec_code of this ListFlavorsRequest.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def ha_mode(self):
        """Gets the ha_mode of this ListFlavorsRequest.

        实例类型  集中式centralization_standard  分布式enterprise

        :return: The ha_mode of this ListFlavorsRequest.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this ListFlavorsRequest.

        实例类型  集中式centralization_standard  分布式enterprise

        :param ha_mode: The ha_mode of this ListFlavorsRequest.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def limit(self):
        """Gets the limit of this ListFlavorsRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFlavorsRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListFlavorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListFlavorsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListFlavorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFlavorsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListFlavorsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
