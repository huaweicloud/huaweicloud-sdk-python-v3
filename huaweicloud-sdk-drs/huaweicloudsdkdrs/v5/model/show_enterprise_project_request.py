# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEnterpriseProjectRequest:

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
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'domain_id': 'domain_id'
    }

    def __init__(self, x_language=None, offset=None, limit=None, name=None, domain_id=None):
        r"""ShowEnterpriseProjectRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0
        :type offset: int
        :param limit: 每页显示的条目数量。默认为10，取值范围【1-1000】
        :type limit: int
        :param name: 企业项目名称，支持模糊搜索。
        :type name: str
        :param domain_id: IAM用户所属帐号ID。op_service权限必须携带此参数，非op_service权限可不携带此参数。
        :type domain_id: str
        """
        
        

        self._x_language = None
        self._offset = None
        self._limit = None
        self._name = None
        self._domain_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowEnterpriseProjectRequest.

        请求语言类型。

        :return: The x_language of this ShowEnterpriseProjectRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowEnterpriseProjectRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowEnterpriseProjectRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        r"""Gets the offset of this ShowEnterpriseProjectRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :return: The offset of this ShowEnterpriseProjectRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowEnterpriseProjectRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :param offset: The offset of this ShowEnterpriseProjectRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowEnterpriseProjectRequest.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :return: The limit of this ShowEnterpriseProjectRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowEnterpriseProjectRequest.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :param limit: The limit of this ShowEnterpriseProjectRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ShowEnterpriseProjectRequest.

        企业项目名称，支持模糊搜索。

        :return: The name of this ShowEnterpriseProjectRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowEnterpriseProjectRequest.

        企业项目名称，支持模糊搜索。

        :param name: The name of this ShowEnterpriseProjectRequest.
        :type name: str
        """
        self._name = name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowEnterpriseProjectRequest.

        IAM用户所属帐号ID。op_service权限必须携带此参数，非op_service权限可不携带此参数。

        :return: The domain_id of this ShowEnterpriseProjectRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowEnterpriseProjectRequest.

        IAM用户所属帐号ID。op_service权限必须携带此参数，非op_service权限可不携带此参数。

        :param domain_id: The domain_id of this ShowEnterpriseProjectRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, ShowEnterpriseProjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
