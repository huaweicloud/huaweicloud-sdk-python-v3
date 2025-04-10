# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReleasePackagesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_word': 'str',
        'apply_user_name': 'str',
        'deploy_user_name': 'str',
        'apply_begin_time': 'int',
        'apply_end_time': 'int',
        'deploy_begin_time': 'int',
        'deploy_end_time': 'int',
        'apply_user_name_filter': 'list[str]',
        'deploy_user_name_filter': 'list[str]',
        'deploy_status_filter': 'list[int]',
        'sorted_direction': 'str',
        'order_column': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'key_word': 'key_word',
        'apply_user_name': 'apply_user_name',
        'deploy_user_name': 'deploy_user_name',
        'apply_begin_time': 'apply_begin_time',
        'apply_end_time': 'apply_end_time',
        'deploy_begin_time': 'deploy_begin_time',
        'deploy_end_time': 'deploy_end_time',
        'apply_user_name_filter': 'apply_user_name_filter',
        'deploy_user_name_filter': 'deploy_user_name_filter',
        'deploy_status_filter': 'deploy_status_filter',
        'sorted_direction': 'sorted_direction',
        'order_column': 'order_column',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, key_word=None, apply_user_name=None, deploy_user_name=None, apply_begin_time=None, apply_end_time=None, deploy_begin_time=None, deploy_end_time=None, apply_user_name_filter=None, deploy_user_name_filter=None, deploy_status_filter=None, sorted_direction=None, order_column=None, limit=None, offset=None):
        r"""ListReleasePackagesRequestBody

        The model defined in huaweicloud sdk

        :param key_word: 包名package_name关键字
        :type key_word: str
        :param apply_user_name: 申请人名称
        :type apply_user_name: str
        :param deploy_user_name: 发布人名称
        :type deploy_user_name: str
        :param apply_begin_time: 申请开始时间，13位时间戳
        :type apply_begin_time: int
        :param apply_end_time: 申请结束时间，13位时间戳
        :type apply_end_time: int
        :param deploy_begin_time: 发布开始时间，13位时间戳
        :type deploy_begin_time: int
        :param deploy_end_time: 发布结束时间，13位时间戳
        :type deploy_end_time: int
        :param apply_user_name_filter: 申请人名称集合，根据该字段筛选，如果选择了apply_user_name，则该名称必须包含在集合内
        :type apply_user_name_filter: list[str]
        :param deploy_user_name_filter: 发布人名称集合，根据该字段筛选，如果选择了apply_user_name，则该名称必须包含在集合内
        :type deploy_user_name_filter: list[str]
        :param deploy_status_filter: 发布状态集合: 1:待审批,2:成功,3:失败, 5:发布中
        :type deploy_status_filter: list[int]
        :param sorted_direction: 排序方向，默认是desc
        :type sorted_direction: str
        :param order_column: 排序字段，默认是apply_timestamp
        :type order_column: str
        :param limit: 分页返回结果，默认是10
        :type limit: int
        :param offset: 分页的起始页，默认值位0，取值范围大于等于0
        :type offset: int
        """
        
        

        self._key_word = None
        self._apply_user_name = None
        self._deploy_user_name = None
        self._apply_begin_time = None
        self._apply_end_time = None
        self._deploy_begin_time = None
        self._deploy_end_time = None
        self._apply_user_name_filter = None
        self._deploy_user_name_filter = None
        self._deploy_status_filter = None
        self._sorted_direction = None
        self._order_column = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if key_word is not None:
            self.key_word = key_word
        if apply_user_name is not None:
            self.apply_user_name = apply_user_name
        if deploy_user_name is not None:
            self.deploy_user_name = deploy_user_name
        if apply_begin_time is not None:
            self.apply_begin_time = apply_begin_time
        if apply_end_time is not None:
            self.apply_end_time = apply_end_time
        if deploy_begin_time is not None:
            self.deploy_begin_time = deploy_begin_time
        if deploy_end_time is not None:
            self.deploy_end_time = deploy_end_time
        if apply_user_name_filter is not None:
            self.apply_user_name_filter = apply_user_name_filter
        if deploy_user_name_filter is not None:
            self.deploy_user_name_filter = deploy_user_name_filter
        if deploy_status_filter is not None:
            self.deploy_status_filter = deploy_status_filter
        if sorted_direction is not None:
            self.sorted_direction = sorted_direction
        if order_column is not None:
            self.order_column = order_column
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def key_word(self):
        r"""Gets the key_word of this ListReleasePackagesRequestBody.

        包名package_name关键字

        :return: The key_word of this ListReleasePackagesRequestBody.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this ListReleasePackagesRequestBody.

        包名package_name关键字

        :param key_word: The key_word of this ListReleasePackagesRequestBody.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def apply_user_name(self):
        r"""Gets the apply_user_name of this ListReleasePackagesRequestBody.

        申请人名称

        :return: The apply_user_name of this ListReleasePackagesRequestBody.
        :rtype: str
        """
        return self._apply_user_name

    @apply_user_name.setter
    def apply_user_name(self, apply_user_name):
        r"""Sets the apply_user_name of this ListReleasePackagesRequestBody.

        申请人名称

        :param apply_user_name: The apply_user_name of this ListReleasePackagesRequestBody.
        :type apply_user_name: str
        """
        self._apply_user_name = apply_user_name

    @property
    def deploy_user_name(self):
        r"""Gets the deploy_user_name of this ListReleasePackagesRequestBody.

        发布人名称

        :return: The deploy_user_name of this ListReleasePackagesRequestBody.
        :rtype: str
        """
        return self._deploy_user_name

    @deploy_user_name.setter
    def deploy_user_name(self, deploy_user_name):
        r"""Sets the deploy_user_name of this ListReleasePackagesRequestBody.

        发布人名称

        :param deploy_user_name: The deploy_user_name of this ListReleasePackagesRequestBody.
        :type deploy_user_name: str
        """
        self._deploy_user_name = deploy_user_name

    @property
    def apply_begin_time(self):
        r"""Gets the apply_begin_time of this ListReleasePackagesRequestBody.

        申请开始时间，13位时间戳

        :return: The apply_begin_time of this ListReleasePackagesRequestBody.
        :rtype: int
        """
        return self._apply_begin_time

    @apply_begin_time.setter
    def apply_begin_time(self, apply_begin_time):
        r"""Sets the apply_begin_time of this ListReleasePackagesRequestBody.

        申请开始时间，13位时间戳

        :param apply_begin_time: The apply_begin_time of this ListReleasePackagesRequestBody.
        :type apply_begin_time: int
        """
        self._apply_begin_time = apply_begin_time

    @property
    def apply_end_time(self):
        r"""Gets the apply_end_time of this ListReleasePackagesRequestBody.

        申请结束时间，13位时间戳

        :return: The apply_end_time of this ListReleasePackagesRequestBody.
        :rtype: int
        """
        return self._apply_end_time

    @apply_end_time.setter
    def apply_end_time(self, apply_end_time):
        r"""Sets the apply_end_time of this ListReleasePackagesRequestBody.

        申请结束时间，13位时间戳

        :param apply_end_time: The apply_end_time of this ListReleasePackagesRequestBody.
        :type apply_end_time: int
        """
        self._apply_end_time = apply_end_time

    @property
    def deploy_begin_time(self):
        r"""Gets the deploy_begin_time of this ListReleasePackagesRequestBody.

        发布开始时间，13位时间戳

        :return: The deploy_begin_time of this ListReleasePackagesRequestBody.
        :rtype: int
        """
        return self._deploy_begin_time

    @deploy_begin_time.setter
    def deploy_begin_time(self, deploy_begin_time):
        r"""Sets the deploy_begin_time of this ListReleasePackagesRequestBody.

        发布开始时间，13位时间戳

        :param deploy_begin_time: The deploy_begin_time of this ListReleasePackagesRequestBody.
        :type deploy_begin_time: int
        """
        self._deploy_begin_time = deploy_begin_time

    @property
    def deploy_end_time(self):
        r"""Gets the deploy_end_time of this ListReleasePackagesRequestBody.

        发布结束时间，13位时间戳

        :return: The deploy_end_time of this ListReleasePackagesRequestBody.
        :rtype: int
        """
        return self._deploy_end_time

    @deploy_end_time.setter
    def deploy_end_time(self, deploy_end_time):
        r"""Sets the deploy_end_time of this ListReleasePackagesRequestBody.

        发布结束时间，13位时间戳

        :param deploy_end_time: The deploy_end_time of this ListReleasePackagesRequestBody.
        :type deploy_end_time: int
        """
        self._deploy_end_time = deploy_end_time

    @property
    def apply_user_name_filter(self):
        r"""Gets the apply_user_name_filter of this ListReleasePackagesRequestBody.

        申请人名称集合，根据该字段筛选，如果选择了apply_user_name，则该名称必须包含在集合内

        :return: The apply_user_name_filter of this ListReleasePackagesRequestBody.
        :rtype: list[str]
        """
        return self._apply_user_name_filter

    @apply_user_name_filter.setter
    def apply_user_name_filter(self, apply_user_name_filter):
        r"""Sets the apply_user_name_filter of this ListReleasePackagesRequestBody.

        申请人名称集合，根据该字段筛选，如果选择了apply_user_name，则该名称必须包含在集合内

        :param apply_user_name_filter: The apply_user_name_filter of this ListReleasePackagesRequestBody.
        :type apply_user_name_filter: list[str]
        """
        self._apply_user_name_filter = apply_user_name_filter

    @property
    def deploy_user_name_filter(self):
        r"""Gets the deploy_user_name_filter of this ListReleasePackagesRequestBody.

        发布人名称集合，根据该字段筛选，如果选择了apply_user_name，则该名称必须包含在集合内

        :return: The deploy_user_name_filter of this ListReleasePackagesRequestBody.
        :rtype: list[str]
        """
        return self._deploy_user_name_filter

    @deploy_user_name_filter.setter
    def deploy_user_name_filter(self, deploy_user_name_filter):
        r"""Sets the deploy_user_name_filter of this ListReleasePackagesRequestBody.

        发布人名称集合，根据该字段筛选，如果选择了apply_user_name，则该名称必须包含在集合内

        :param deploy_user_name_filter: The deploy_user_name_filter of this ListReleasePackagesRequestBody.
        :type deploy_user_name_filter: list[str]
        """
        self._deploy_user_name_filter = deploy_user_name_filter

    @property
    def deploy_status_filter(self):
        r"""Gets the deploy_status_filter of this ListReleasePackagesRequestBody.

        发布状态集合: 1:待审批,2:成功,3:失败, 5:发布中

        :return: The deploy_status_filter of this ListReleasePackagesRequestBody.
        :rtype: list[int]
        """
        return self._deploy_status_filter

    @deploy_status_filter.setter
    def deploy_status_filter(self, deploy_status_filter):
        r"""Sets the deploy_status_filter of this ListReleasePackagesRequestBody.

        发布状态集合: 1:待审批,2:成功,3:失败, 5:发布中

        :param deploy_status_filter: The deploy_status_filter of this ListReleasePackagesRequestBody.
        :type deploy_status_filter: list[int]
        """
        self._deploy_status_filter = deploy_status_filter

    @property
    def sorted_direction(self):
        r"""Gets the sorted_direction of this ListReleasePackagesRequestBody.

        排序方向，默认是desc

        :return: The sorted_direction of this ListReleasePackagesRequestBody.
        :rtype: str
        """
        return self._sorted_direction

    @sorted_direction.setter
    def sorted_direction(self, sorted_direction):
        r"""Sets the sorted_direction of this ListReleasePackagesRequestBody.

        排序方向，默认是desc

        :param sorted_direction: The sorted_direction of this ListReleasePackagesRequestBody.
        :type sorted_direction: str
        """
        self._sorted_direction = sorted_direction

    @property
    def order_column(self):
        r"""Gets the order_column of this ListReleasePackagesRequestBody.

        排序字段，默认是apply_timestamp

        :return: The order_column of this ListReleasePackagesRequestBody.
        :rtype: str
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        r"""Sets the order_column of this ListReleasePackagesRequestBody.

        排序字段，默认是apply_timestamp

        :param order_column: The order_column of this ListReleasePackagesRequestBody.
        :type order_column: str
        """
        self._order_column = order_column

    @property
    def limit(self):
        r"""Gets the limit of this ListReleasePackagesRequestBody.

        分页返回结果，默认是10

        :return: The limit of this ListReleasePackagesRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListReleasePackagesRequestBody.

        分页返回结果，默认是10

        :param limit: The limit of this ListReleasePackagesRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListReleasePackagesRequestBody.

        分页的起始页，默认值位0，取值范围大于等于0

        :return: The offset of this ListReleasePackagesRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListReleasePackagesRequestBody.

        分页的起始页，默认值位0，取值范围大于等于0

        :param offset: The offset of this ListReleasePackagesRequestBody.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListReleasePackagesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
