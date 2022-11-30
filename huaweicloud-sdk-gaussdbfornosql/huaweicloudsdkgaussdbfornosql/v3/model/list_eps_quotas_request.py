# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEpsQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'enterprise_project_name': 'enterprise_project_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, enterprise_project_name=None, offset=None, limit=None):
        """ListEpsQuotasRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_name: 企业项目名称。支持模糊搜索，若不指定则返回所有企业项目配额。
        :type enterprise_project_name: str
        :param offset: 索引位置，偏移量。    - 从第一条数据偏移offset条数据后开始查询，默认为0。   - 取值必须为数字，且不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。  - 取值范围：1~100。 - 不传该参数时，默认查询前100条信息。
        :type limit: int
        """
        
        

        self._enterprise_project_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this ListEpsQuotasRequest.

        企业项目名称。支持模糊搜索，若不指定则返回所有企业项目配额。

        :return: The enterprise_project_name of this ListEpsQuotasRequest.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this ListEpsQuotasRequest.

        企业项目名称。支持模糊搜索，若不指定则返回所有企业项目配额。

        :param enterprise_project_name: The enterprise_project_name of this ListEpsQuotasRequest.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def offset(self):
        """Gets the offset of this ListEpsQuotasRequest.

        索引位置，偏移量。    - 从第一条数据偏移offset条数据后开始查询，默认为0。   - 取值必须为数字，且不能为负数。

        :return: The offset of this ListEpsQuotasRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEpsQuotasRequest.

        索引位置，偏移量。    - 从第一条数据偏移offset条数据后开始查询，默认为0。   - 取值必须为数字，且不能为负数。

        :param offset: The offset of this ListEpsQuotasRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEpsQuotasRequest.

        查询个数上限值。  - 取值范围：1~100。 - 不传该参数时，默认查询前100条信息。

        :return: The limit of this ListEpsQuotasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEpsQuotasRequest.

        查询个数上限值。  - 取值范围：1~100。 - 不传该参数时，默认查询前100条信息。

        :param limit: The limit of this ListEpsQuotasRequest.
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
        if not isinstance(other, ListEpsQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
