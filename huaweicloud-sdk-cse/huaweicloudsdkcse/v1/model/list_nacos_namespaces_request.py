# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNacosNamespacesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_engine_id': 'str',
        'x_enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_engine_id': 'x-engine-id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_engine_id=None, x_enterprise_project_id=None, offset=None, limit=None):
        r"""ListNacosNamespacesRequest

        The model defined in huaweicloud sdk

        :param x_engine_id: 微服务引擎的实例ID
        :type x_engine_id: str
        :param x_enterprise_project_id: 企业项目ID
        :type x_enterprise_project_id: str
        :param offset: 分页参数，偏移量，从0开始
        :type offset: int
        :param limit: 分页参数，分页大小，0表示不分页
        :type limit: int
        """
        
        

        self._x_engine_id = None
        self._x_enterprise_project_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.x_engine_id = x_engine_id
        self.x_enterprise_project_id = x_enterprise_project_id
        self.offset = offset
        self.limit = limit

    @property
    def x_engine_id(self):
        r"""Gets the x_engine_id of this ListNacosNamespacesRequest.

        微服务引擎的实例ID

        :return: The x_engine_id of this ListNacosNamespacesRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        r"""Sets the x_engine_id of this ListNacosNamespacesRequest.

        微服务引擎的实例ID

        :param x_engine_id: The x_engine_id of this ListNacosNamespacesRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def x_enterprise_project_id(self):
        r"""Gets the x_enterprise_project_id of this ListNacosNamespacesRequest.

        企业项目ID

        :return: The x_enterprise_project_id of this ListNacosNamespacesRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        r"""Sets the x_enterprise_project_id of this ListNacosNamespacesRequest.

        企业项目ID

        :param x_enterprise_project_id: The x_enterprise_project_id of this ListNacosNamespacesRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListNacosNamespacesRequest.

        分页参数，偏移量，从0开始

        :return: The offset of this ListNacosNamespacesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNacosNamespacesRequest.

        分页参数，偏移量，从0开始

        :param offset: The offset of this ListNacosNamespacesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListNacosNamespacesRequest.

        分页参数，分页大小，0表示不分页

        :return: The limit of this ListNacosNamespacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNacosNamespacesRequest.

        分页参数，分页大小，0表示不分页

        :param limit: The limit of this ListNacosNamespacesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListNacosNamespacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
