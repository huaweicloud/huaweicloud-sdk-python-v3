# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAttributesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cust_attr_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'status': 'int'
    }

    attribute_map = {
        'cust_attr_name': 'cust_attr_name',
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status'
    }

    def __init__(self, cust_attr_name=None, limit=None, offset=None, status=None):
        r"""ListAttributesRequest

        The model defined in huaweicloud sdk

        :param cust_attr_name: 自定义属性名称
        :type cust_attr_name: str
        :param limit: 分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数
        :type limit: int
        :param offset: 分页查询时的页码数，默认值为1，取值范围为1-1000000的整数
        :type offset: int
        :param status: 自定义属性状态：0 未启用，1 已启用。
        :type status: int
        """
        
        

        self._cust_attr_name = None
        self._limit = None
        self._offset = None
        self._status = None
        self.discriminator = None

        if cust_attr_name is not None:
            self.cust_attr_name = cust_attr_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status

    @property
    def cust_attr_name(self):
        r"""Gets the cust_attr_name of this ListAttributesRequest.

        自定义属性名称

        :return: The cust_attr_name of this ListAttributesRequest.
        :rtype: str
        """
        return self._cust_attr_name

    @cust_attr_name.setter
    def cust_attr_name(self, cust_attr_name):
        r"""Sets the cust_attr_name of this ListAttributesRequest.

        自定义属性名称

        :param cust_attr_name: The cust_attr_name of this ListAttributesRequest.
        :type cust_attr_name: str
        """
        self._cust_attr_name = cust_attr_name

    @property
    def limit(self):
        r"""Gets the limit of this ListAttributesRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :return: The limit of this ListAttributesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAttributesRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :param limit: The limit of this ListAttributesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAttributesRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :return: The offset of this ListAttributesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAttributesRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :param offset: The offset of this ListAttributesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListAttributesRequest.

        自定义属性状态：0 未启用，1 已启用。

        :return: The status of this ListAttributesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAttributesRequest.

        自定义属性状态：0 未启用，1 已启用。

        :param status: The status of this ListAttributesRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ListAttributesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
