# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceNamespacesRequest:

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
        'offset': 'int',
        'limit': 'int',
        'order_column': 'str',
        'order_type': 'str',
        'name': 'str',
        'public': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'order_column': 'order_column',
        'order_type': 'order_type',
        'name': 'name',
        'public': 'public'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, order_column=None, order_type=None, name=None, public=None):
        r"""ListInstanceNamespacesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param offset: 起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type offset: int
        :param limit: 返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type limit: int
        :param order_column: 按列排序，可设置为updated_at（按更新时间排序）
        :type order_column: str
        :param order_type: 排序类型，可设置为desc（降序）、asc（升序），与order_column配合使用
        :type order_type: str
        :param name: 命名空间名称，小写字母或数字开头，后面跟小写字母、数字、点、下划线或中划线（其中点、下划线、中划线不能直接连续），小写字母或数字结尾，1-64个字符。
        :type name: str
        :param public: 是否公开，非空且非true默认返回false
        :type public: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._order_column = None
        self._order_type = None
        self._name = None
        self._public = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_column is not None:
            self.order_column = order_column
        if order_type is not None:
            self.order_type = order_type
        if name is not None:
            self.name = name
        if public is not None:
            self.public = public

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceNamespacesRequest.

        企业仓库实例ID

        :return: The instance_id of this ListInstanceNamespacesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceNamespacesRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListInstanceNamespacesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceNamespacesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The offset of this ListInstanceNamespacesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceNamespacesRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param offset: The offset of this ListInstanceNamespacesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceNamespacesRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The limit of this ListInstanceNamespacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceNamespacesRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param limit: The limit of this ListInstanceNamespacesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_column(self):
        r"""Gets the order_column of this ListInstanceNamespacesRequest.

        按列排序，可设置为updated_at（按更新时间排序）

        :return: The order_column of this ListInstanceNamespacesRequest.
        :rtype: str
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        r"""Sets the order_column of this ListInstanceNamespacesRequest.

        按列排序，可设置为updated_at（按更新时间排序）

        :param order_column: The order_column of this ListInstanceNamespacesRequest.
        :type order_column: str
        """
        self._order_column = order_column

    @property
    def order_type(self):
        r"""Gets the order_type of this ListInstanceNamespacesRequest.

        排序类型，可设置为desc（降序）、asc（升序），与order_column配合使用

        :return: The order_type of this ListInstanceNamespacesRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        r"""Sets the order_type of this ListInstanceNamespacesRequest.

        排序类型，可设置为desc（降序）、asc（升序），与order_column配合使用

        :param order_type: The order_type of this ListInstanceNamespacesRequest.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def name(self):
        r"""Gets the name of this ListInstanceNamespacesRequest.

        命名空间名称，小写字母或数字开头，后面跟小写字母、数字、点、下划线或中划线（其中点、下划线、中划线不能直接连续），小写字母或数字结尾，1-64个字符。

        :return: The name of this ListInstanceNamespacesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstanceNamespacesRequest.

        命名空间名称，小写字母或数字开头，后面跟小写字母、数字、点、下划线或中划线（其中点、下划线、中划线不能直接连续），小写字母或数字结尾，1-64个字符。

        :param name: The name of this ListInstanceNamespacesRequest.
        :type name: str
        """
        self._name = name

    @property
    def public(self):
        r"""Gets the public of this ListInstanceNamespacesRequest.

        是否公开，非空且非true默认返回false

        :return: The public of this ListInstanceNamespacesRequest.
        :rtype: str
        """
        return self._public

    @public.setter
    def public(self, public):
        r"""Sets the public of this ListInstanceNamespacesRequest.

        是否公开，非空且非true默认返回false

        :param public: The public of this ListInstanceNamespacesRequest.
        :type public: str
        """
        self._public = public

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
        if not isinstance(other, ListInstanceNamespacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
