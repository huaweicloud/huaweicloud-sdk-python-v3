# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'enterprise_project_id': 'str',
        'name': 'str',
        'fuzzy_name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'fuzzy_name': 'fuzzy_name'
    }

    def __init__(self, offset=None, limit=None, enterprise_project_id=None, name=None, fuzzy_name=None):
        """ListTopicsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。
        :type offset: int
        :param limit:  查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。
        :type limit: int
        :param enterprise_project_id: 企业项目id，默认企业项目id为0。
        :type enterprise_project_id: str
        :param name: 检索的主题名称，完全匹配。
        :type name: str
        :param fuzzy_name: 检索的主题名称，模糊匹配，按照startwith模式进行匹配。
        :type fuzzy_name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._enterprise_project_id = None
        self._name = None
        self._fuzzy_name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
        if fuzzy_name is not None:
            self.fuzzy_name = fuzzy_name

    @property
    def offset(self):
        """Gets the offset of this ListTopicsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :return: The offset of this ListTopicsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTopicsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :param offset: The offset of this ListTopicsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTopicsRequest.

         查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :return: The limit of this ListTopicsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTopicsRequest.

         查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :param limit: The limit of this ListTopicsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListTopicsRequest.

        企业项目id，默认企业项目id为0。

        :return: The enterprise_project_id of this ListTopicsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListTopicsRequest.

        企业项目id，默认企业项目id为0。

        :param enterprise_project_id: The enterprise_project_id of this ListTopicsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this ListTopicsRequest.

        检索的主题名称，完全匹配。

        :return: The name of this ListTopicsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTopicsRequest.

        检索的主题名称，完全匹配。

        :param name: The name of this ListTopicsRequest.
        :type name: str
        """
        self._name = name

    @property
    def fuzzy_name(self):
        """Gets the fuzzy_name of this ListTopicsRequest.

        检索的主题名称，模糊匹配，按照startwith模式进行匹配。

        :return: The fuzzy_name of this ListTopicsRequest.
        :rtype: str
        """
        return self._fuzzy_name

    @fuzzy_name.setter
    def fuzzy_name(self, fuzzy_name):
        """Sets the fuzzy_name of this ListTopicsRequest.

        检索的主题名称，模糊匹配，按照startwith模式进行匹配。

        :param fuzzy_name: The fuzzy_name of this ListTopicsRequest.
        :type fuzzy_name: str
        """
        self._fuzzy_name = fuzzy_name

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
        if not isinstance(other, ListTopicsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
