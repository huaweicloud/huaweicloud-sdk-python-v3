# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGaussMySqlQuotasRequest:

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
        'offset': 'str',
        'limit': 'str',
        'enterprise_project_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit',
        'enterprise_project_name': 'enterprise_project_name'
    }

    def __init__(self, x_language=None, offset=None, limit=None, enterprise_project_name=None):
        """ShowGaussMySqlQuotasRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。 取值范围：0 - 10000
        :type offset: str
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        """
        
        

        self._x_language = None
        self._offset = None
        self._limit = None
        self._enterprise_project_name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name

    @property
    def x_language(self):
        """Gets the x_language of this ShowGaussMySqlQuotasRequest.

        语言

        :return: The x_language of this ShowGaussMySqlQuotasRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowGaussMySqlQuotasRequest.

        语言

        :param x_language: The x_language of this ShowGaussMySqlQuotasRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        """Gets the offset of this ShowGaussMySqlQuotasRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。 取值范围：0 - 10000

        :return: The offset of this ShowGaussMySqlQuotasRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowGaussMySqlQuotasRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。 取值范围：0 - 10000

        :param offset: The offset of this ShowGaussMySqlQuotasRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowGaussMySqlQuotasRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ShowGaussMySqlQuotasRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowGaussMySqlQuotasRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ShowGaussMySqlQuotasRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this ShowGaussMySqlQuotasRequest.

        企业项目名称。

        :return: The enterprise_project_name of this ShowGaussMySqlQuotasRequest.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this ShowGaussMySqlQuotasRequest.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this ShowGaussMySqlQuotasRequest.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

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
        if not isinstance(other, ShowGaussMySqlQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
