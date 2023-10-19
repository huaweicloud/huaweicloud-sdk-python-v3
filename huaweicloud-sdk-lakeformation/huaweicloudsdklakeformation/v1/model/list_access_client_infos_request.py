# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessClientInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'id': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'id': 'id',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, id=None, name=None, offset=None, limit=None):
        """ListAccessClientInfosRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param id: ID搜索。根据ID进行搜索。
        :type id: str
        :param name: 名称关键字搜索。只能包含字母、数字、下划线和中划线，且最大长度为32个字符。
        :type name: str
        :param offset: 分页查询时的偏移量。默认值为0。最小值为0，最大值为1000。
        :type offset: int
        :param limit: 分页一页显示数。默认值为10。最小值为1，最大值为1000。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._id = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ListAccessClientInfosRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this ListAccessClientInfosRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListAccessClientInfosRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this ListAccessClientInfosRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def id(self):
        """Gets the id of this ListAccessClientInfosRequest.

        ID搜索。根据ID进行搜索。

        :return: The id of this ListAccessClientInfosRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAccessClientInfosRequest.

        ID搜索。根据ID进行搜索。

        :param id: The id of this ListAccessClientInfosRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListAccessClientInfosRequest.

        名称关键字搜索。只能包含字母、数字、下划线和中划线，且最大长度为32个字符。

        :return: The name of this ListAccessClientInfosRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAccessClientInfosRequest.

        名称关键字搜索。只能包含字母、数字、下划线和中划线，且最大长度为32个字符。

        :param name: The name of this ListAccessClientInfosRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListAccessClientInfosRequest.

        分页查询时的偏移量。默认值为0。最小值为0，最大值为1000。

        :return: The offset of this ListAccessClientInfosRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAccessClientInfosRequest.

        分页查询时的偏移量。默认值为0。最小值为0，最大值为1000。

        :param offset: The offset of this ListAccessClientInfosRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAccessClientInfosRequest.

        分页一页显示数。默认值为10。最小值为1，最大值为1000。

        :return: The limit of this ListAccessClientInfosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAccessClientInfosRequest.

        分页一页显示数。默认值为10。最小值为1，最大值为1000。

        :param limit: The limit of this ListAccessClientInfosRequest.
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
        if not isinstance(other, ListAccessClientInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
