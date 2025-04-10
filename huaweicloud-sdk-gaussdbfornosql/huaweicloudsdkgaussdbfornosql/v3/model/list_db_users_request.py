# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbUsersRequest:

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
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, name=None, offset=None, limit=None):
        r"""ListDbUsersRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param name: 数据库账号名。若传此参数，则查询指定账号的信息，否则返回所有数据库账号信息。
        :type name: str
        :param offset: 索引位置，偏移量。    - 从第一条数据偏移offset条数据后开始查询，默认为0。   - 取值必须为数字，且不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。  - 取值范围：1~100。 - 不传该参数时，默认查询前100条信息。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDbUsersRequest.

        实例ID。

        :return: The instance_id of this ListDbUsersRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDbUsersRequest.

        实例ID。

        :param instance_id: The instance_id of this ListDbUsersRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this ListDbUsersRequest.

        数据库账号名。若传此参数，则查询指定账号的信息，否则返回所有数据库账号信息。

        :return: The name of this ListDbUsersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDbUsersRequest.

        数据库账号名。若传此参数，则查询指定账号的信息，否则返回所有数据库账号信息。

        :param name: The name of this ListDbUsersRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListDbUsersRequest.

        索引位置，偏移量。    - 从第一条数据偏移offset条数据后开始查询，默认为0。   - 取值必须为数字，且不能为负数。

        :return: The offset of this ListDbUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDbUsersRequest.

        索引位置，偏移量。    - 从第一条数据偏移offset条数据后开始查询，默认为0。   - 取值必须为数字，且不能为负数。

        :param offset: The offset of this ListDbUsersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDbUsersRequest.

        查询个数上限值。  - 取值范围：1~100。 - 不传该参数时，默认查询前100条信息。

        :return: The limit of this ListDbUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDbUsersRequest.

        查询个数上限值。  - 取值范围：1~100。 - 不传该参数时，默认查询前100条信息。

        :param limit: The limit of this ListDbUsersRequest.
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
        if not isinstance(other, ListDbUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
