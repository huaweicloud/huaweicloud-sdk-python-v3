# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDrugModelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_key': 'str',
        'creator_list': 'list[str]',
        'type_list': 'list[str]',
        'status_list': 'list[str]',
        'sort_key': 'str',
        'sort_dir': 'str',
        'create_start_time': 'int',
        'create_end_time': 'int',
        'finish_start_time': 'int',
        'finish_end_time': 'int',
        'limit': 'int',
        'offset': 'int',
        'base_model_list': 'list[str]'
    }

    attribute_map = {
        'search_key': 'search_key',
        'creator_list': 'creator_list',
        'type_list': 'type_list',
        'status_list': 'status_list',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'create_start_time': 'create_start_time',
        'create_end_time': 'create_end_time',
        'finish_start_time': 'finish_start_time',
        'finish_end_time': 'finish_end_time',
        'limit': 'limit',
        'offset': 'offset',
        'base_model_list': 'base_model_list'
    }

    def __init__(self, search_key=None, creator_list=None, type_list=None, status_list=None, sort_key=None, sort_dir=None, create_start_time=None, create_end_time=None, finish_start_time=None, finish_end_time=None, limit=None, offset=None, base_model_list=None):
        r"""ListDrugModelRequest

        The model defined in huaweicloud sdk

        :param search_key: 模糊搜索值
        :type search_key: str
        :param creator_list: 创建者列表
        :type creator_list: list[str]
        :param type_list: 模型类型列表
        :type type_list: list[str]
        :param status_list: 模型状态列表
        :type status_list: list[str]
        :param sort_key: 排序规则 目前默认时间降序，支持根据create_time|finish_time|base_model_name
        :type sort_key: str
        :param sort_dir: 排序规则 目前默认时间降序
        :type sort_dir: str
        :param create_start_time: 最小创建时间
        :type create_start_time: int
        :param create_end_time: 最大创建时间
        :type create_end_time: int
        :param finish_start_time: 最小结束时间
        :type finish_start_time: int
        :param finish_end_time: 最大结束时间
        :type finish_end_time: int
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]
        :type offset: int
        :param base_model_list: 基模型id列表
        :type base_model_list: list[str]
        """
        
        

        self._search_key = None
        self._creator_list = None
        self._type_list = None
        self._status_list = None
        self._sort_key = None
        self._sort_dir = None
        self._create_start_time = None
        self._create_end_time = None
        self._finish_start_time = None
        self._finish_end_time = None
        self._limit = None
        self._offset = None
        self._base_model_list = None
        self.discriminator = None

        if search_key is not None:
            self.search_key = search_key
        if creator_list is not None:
            self.creator_list = creator_list
        if type_list is not None:
            self.type_list = type_list
        if status_list is not None:
            self.status_list = status_list
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if create_start_time is not None:
            self.create_start_time = create_start_time
        if create_end_time is not None:
            self.create_end_time = create_end_time
        if finish_start_time is not None:
            self.finish_start_time = finish_start_time
        if finish_end_time is not None:
            self.finish_end_time = finish_end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if base_model_list is not None:
            self.base_model_list = base_model_list

    @property
    def search_key(self):
        r"""Gets the search_key of this ListDrugModelRequest.

        模糊搜索值

        :return: The search_key of this ListDrugModelRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        r"""Sets the search_key of this ListDrugModelRequest.

        模糊搜索值

        :param search_key: The search_key of this ListDrugModelRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def creator_list(self):
        r"""Gets the creator_list of this ListDrugModelRequest.

        创建者列表

        :return: The creator_list of this ListDrugModelRequest.
        :rtype: list[str]
        """
        return self._creator_list

    @creator_list.setter
    def creator_list(self, creator_list):
        r"""Sets the creator_list of this ListDrugModelRequest.

        创建者列表

        :param creator_list: The creator_list of this ListDrugModelRequest.
        :type creator_list: list[str]
        """
        self._creator_list = creator_list

    @property
    def type_list(self):
        r"""Gets the type_list of this ListDrugModelRequest.

        模型类型列表

        :return: The type_list of this ListDrugModelRequest.
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        r"""Sets the type_list of this ListDrugModelRequest.

        模型类型列表

        :param type_list: The type_list of this ListDrugModelRequest.
        :type type_list: list[str]
        """
        self._type_list = type_list

    @property
    def status_list(self):
        r"""Gets the status_list of this ListDrugModelRequest.

        模型状态列表

        :return: The status_list of this ListDrugModelRequest.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this ListDrugModelRequest.

        模型状态列表

        :param status_list: The status_list of this ListDrugModelRequest.
        :type status_list: list[str]
        """
        self._status_list = status_list

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListDrugModelRequest.

        排序规则 目前默认时间降序，支持根据create_time|finish_time|base_model_name

        :return: The sort_key of this ListDrugModelRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListDrugModelRequest.

        排序规则 目前默认时间降序，支持根据create_time|finish_time|base_model_name

        :param sort_key: The sort_key of this ListDrugModelRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListDrugModelRequest.

        排序规则 目前默认时间降序

        :return: The sort_dir of this ListDrugModelRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListDrugModelRequest.

        排序规则 目前默认时间降序

        :param sort_dir: The sort_dir of this ListDrugModelRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def create_start_time(self):
        r"""Gets the create_start_time of this ListDrugModelRequest.

        最小创建时间

        :return: The create_start_time of this ListDrugModelRequest.
        :rtype: int
        """
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, create_start_time):
        r"""Sets the create_start_time of this ListDrugModelRequest.

        最小创建时间

        :param create_start_time: The create_start_time of this ListDrugModelRequest.
        :type create_start_time: int
        """
        self._create_start_time = create_start_time

    @property
    def create_end_time(self):
        r"""Gets the create_end_time of this ListDrugModelRequest.

        最大创建时间

        :return: The create_end_time of this ListDrugModelRequest.
        :rtype: int
        """
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, create_end_time):
        r"""Sets the create_end_time of this ListDrugModelRequest.

        最大创建时间

        :param create_end_time: The create_end_time of this ListDrugModelRequest.
        :type create_end_time: int
        """
        self._create_end_time = create_end_time

    @property
    def finish_start_time(self):
        r"""Gets the finish_start_time of this ListDrugModelRequest.

        最小结束时间

        :return: The finish_start_time of this ListDrugModelRequest.
        :rtype: int
        """
        return self._finish_start_time

    @finish_start_time.setter
    def finish_start_time(self, finish_start_time):
        r"""Sets the finish_start_time of this ListDrugModelRequest.

        最小结束时间

        :param finish_start_time: The finish_start_time of this ListDrugModelRequest.
        :type finish_start_time: int
        """
        self._finish_start_time = finish_start_time

    @property
    def finish_end_time(self):
        r"""Gets the finish_end_time of this ListDrugModelRequest.

        最大结束时间

        :return: The finish_end_time of this ListDrugModelRequest.
        :rtype: int
        """
        return self._finish_end_time

    @finish_end_time.setter
    def finish_end_time(self, finish_end_time):
        r"""Sets the finish_end_time of this ListDrugModelRequest.

        最大结束时间

        :param finish_end_time: The finish_end_time of this ListDrugModelRequest.
        :type finish_end_time: int
        """
        self._finish_end_time = finish_end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListDrugModelRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :return: The limit of this ListDrugModelRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDrugModelRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :param limit: The limit of this ListDrugModelRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListDrugModelRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :return: The offset of this ListDrugModelRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDrugModelRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :param offset: The offset of this ListDrugModelRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def base_model_list(self):
        r"""Gets the base_model_list of this ListDrugModelRequest.

        基模型id列表

        :return: The base_model_list of this ListDrugModelRequest.
        :rtype: list[str]
        """
        return self._base_model_list

    @base_model_list.setter
    def base_model_list(self, base_model_list):
        r"""Sets the base_model_list of this ListDrugModelRequest.

        基模型id列表

        :param base_model_list: The base_model_list of this ListDrugModelRequest.
        :type base_model_list: list[str]
        """
        self._base_model_list = base_model_list

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
        if not isinstance(other, ListDrugModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
