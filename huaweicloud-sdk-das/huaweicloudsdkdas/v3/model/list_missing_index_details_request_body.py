# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMissingIndexDetailsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conditions': 'list[MissingIndexCondition]',
        'object_name': 'str',
        'sort_field': 'str',
        'sort_asc': 'bool',
        'cur_page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'conditions': 'conditions',
        'object_name': 'object_name',
        'sort_field': 'sort_field',
        'sort_asc': 'sort_asc',
        'cur_page': 'cur_page',
        'per_page': 'per_page'
    }

    def __init__(self, conditions=None, object_name=None, sort_field=None, sort_asc=None, cur_page=None, per_page=None):
        r"""ListMissingIndexDetailsRequestBody

        The model defined in huaweicloud sdk

        :param conditions: 过滤条件
        :type conditions: list[:class:`huaweicloudsdkdas.v3.MissingIndexCondition`]
        :param object_name: 表名称
        :type object_name: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_asc: 排序是否升序
        :type sort_asc: bool
        :param cur_page: 当前页
        :type cur_page: int
        :param per_page: 页大小
        :type per_page: int
        """
        
        

        self._conditions = None
        self._object_name = None
        self._sort_field = None
        self._sort_asc = None
        self._cur_page = None
        self._per_page = None
        self.discriminator = None

        self.conditions = conditions
        if object_name is not None:
            self.object_name = object_name
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_asc is not None:
            self.sort_asc = sort_asc
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page

    @property
    def conditions(self):
        r"""Gets the conditions of this ListMissingIndexDetailsRequestBody.

        过滤条件

        :return: The conditions of this ListMissingIndexDetailsRequestBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.MissingIndexCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this ListMissingIndexDetailsRequestBody.

        过滤条件

        :param conditions: The conditions of this ListMissingIndexDetailsRequestBody.
        :type conditions: list[:class:`huaweicloudsdkdas.v3.MissingIndexCondition`]
        """
        self._conditions = conditions

    @property
    def object_name(self):
        r"""Gets the object_name of this ListMissingIndexDetailsRequestBody.

        表名称

        :return: The object_name of this ListMissingIndexDetailsRequestBody.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ListMissingIndexDetailsRequestBody.

        表名称

        :param object_name: The object_name of this ListMissingIndexDetailsRequestBody.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListMissingIndexDetailsRequestBody.

        排序字段

        :return: The sort_field of this ListMissingIndexDetailsRequestBody.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListMissingIndexDetailsRequestBody.

        排序字段

        :param sort_field: The sort_field of this ListMissingIndexDetailsRequestBody.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_asc(self):
        r"""Gets the sort_asc of this ListMissingIndexDetailsRequestBody.

        排序是否升序

        :return: The sort_asc of this ListMissingIndexDetailsRequestBody.
        :rtype: bool
        """
        return self._sort_asc

    @sort_asc.setter
    def sort_asc(self, sort_asc):
        r"""Sets the sort_asc of this ListMissingIndexDetailsRequestBody.

        排序是否升序

        :param sort_asc: The sort_asc of this ListMissingIndexDetailsRequestBody.
        :type sort_asc: bool
        """
        self._sort_asc = sort_asc

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListMissingIndexDetailsRequestBody.

        当前页

        :return: The cur_page of this ListMissingIndexDetailsRequestBody.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListMissingIndexDetailsRequestBody.

        当前页

        :param cur_page: The cur_page of this ListMissingIndexDetailsRequestBody.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListMissingIndexDetailsRequestBody.

        页大小

        :return: The per_page of this ListMissingIndexDetailsRequestBody.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListMissingIndexDetailsRequestBody.

        页大小

        :param per_page: The per_page of this ListMissingIndexDetailsRequestBody.
        :type per_page: int
        """
        self._per_page = per_page

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListMissingIndexDetailsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
