# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RawTableParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_row_id': 'str',
        'view_config': 'RawTableView',
        'page': 'int',
        'page_size': 'int',
        'order_by': 'str',
        'search_word': 'str',
        'instance_id': 'int',
        'monitor_item_id': 'int',
        'env_id': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'last_row_id': 'last_row_id',
        'view_config': 'view_config',
        'page': 'page',
        'page_size': 'page_size',
        'order_by': 'order_by',
        'search_word': 'search_word',
        'instance_id': 'instance_id',
        'monitor_item_id': 'monitor_item_id',
        'env_id': 'env_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, last_row_id=None, view_config=None, page=None, page_size=None, order_by=None, search_word=None, instance_id=None, monitor_item_id=None, env_id=None, start_time=None, end_time=None):
        r"""RawTableParam

        The model defined in huaweicloud sdk

        :param last_row_id: 上一次扫描的数据ID。
        :type last_row_id: str
        :param view_config: 
        :type view_config: :class:`huaweicloudsdkapm.v1.RawTableView`
        :param page: 当前页码。
        :type page: int
        :param page_size: 每页数据总数。
        :type page_size: int
        :param order_by: 排序。
        :type order_by: str
        :param search_word: 搜索关键字。
        :type search_word: str
        :param instance_id: 实例id。
        :type instance_id: int
        :param monitor_item_id: 监控项id。
        :type monitor_item_id: int
        :param env_id: 环境id。
        :type env_id: int
        :param start_time: 开始时间。
        :type start_time: str
        :param end_time: 结束时间。
        :type end_time: str
        """
        
        

        self._last_row_id = None
        self._view_config = None
        self._page = None
        self._page_size = None
        self._order_by = None
        self._search_word = None
        self._instance_id = None
        self._monitor_item_id = None
        self._env_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if last_row_id is not None:
            self.last_row_id = last_row_id
        self.view_config = view_config
        self.page = page
        self.page_size = page_size
        if order_by is not None:
            self.order_by = order_by
        if search_word is not None:
            self.search_word = search_word
        if instance_id is not None:
            self.instance_id = instance_id
        if monitor_item_id is not None:
            self.monitor_item_id = monitor_item_id
        self.env_id = env_id
        self.start_time = start_time
        self.end_time = end_time

    @property
    def last_row_id(self):
        r"""Gets the last_row_id of this RawTableParam.

        上一次扫描的数据ID。

        :return: The last_row_id of this RawTableParam.
        :rtype: str
        """
        return self._last_row_id

    @last_row_id.setter
    def last_row_id(self, last_row_id):
        r"""Sets the last_row_id of this RawTableParam.

        上一次扫描的数据ID。

        :param last_row_id: The last_row_id of this RawTableParam.
        :type last_row_id: str
        """
        self._last_row_id = last_row_id

    @property
    def view_config(self):
        r"""Gets the view_config of this RawTableParam.

        :return: The view_config of this RawTableParam.
        :rtype: :class:`huaweicloudsdkapm.v1.RawTableView`
        """
        return self._view_config

    @view_config.setter
    def view_config(self, view_config):
        r"""Sets the view_config of this RawTableParam.

        :param view_config: The view_config of this RawTableParam.
        :type view_config: :class:`huaweicloudsdkapm.v1.RawTableView`
        """
        self._view_config = view_config

    @property
    def page(self):
        r"""Gets the page of this RawTableParam.

        当前页码。

        :return: The page of this RawTableParam.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this RawTableParam.

        当前页码。

        :param page: The page of this RawTableParam.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        r"""Gets the page_size of this RawTableParam.

        每页数据总数。

        :return: The page_size of this RawTableParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this RawTableParam.

        每页数据总数。

        :param page_size: The page_size of this RawTableParam.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def order_by(self):
        r"""Gets the order_by of this RawTableParam.

        排序。

        :return: The order_by of this RawTableParam.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this RawTableParam.

        排序。

        :param order_by: The order_by of this RawTableParam.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def search_word(self):
        r"""Gets the search_word of this RawTableParam.

        搜索关键字。

        :return: The search_word of this RawTableParam.
        :rtype: str
        """
        return self._search_word

    @search_word.setter
    def search_word(self, search_word):
        r"""Sets the search_word of this RawTableParam.

        搜索关键字。

        :param search_word: The search_word of this RawTableParam.
        :type search_word: str
        """
        self._search_word = search_word

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RawTableParam.

        实例id。

        :return: The instance_id of this RawTableParam.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RawTableParam.

        实例id。

        :param instance_id: The instance_id of this RawTableParam.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def monitor_item_id(self):
        r"""Gets the monitor_item_id of this RawTableParam.

        监控项id。

        :return: The monitor_item_id of this RawTableParam.
        :rtype: int
        """
        return self._monitor_item_id

    @monitor_item_id.setter
    def monitor_item_id(self, monitor_item_id):
        r"""Sets the monitor_item_id of this RawTableParam.

        监控项id。

        :param monitor_item_id: The monitor_item_id of this RawTableParam.
        :type monitor_item_id: int
        """
        self._monitor_item_id = monitor_item_id

    @property
    def env_id(self):
        r"""Gets the env_id of this RawTableParam.

        环境id。

        :return: The env_id of this RawTableParam.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this RawTableParam.

        环境id。

        :param env_id: The env_id of this RawTableParam.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def start_time(self):
        r"""Gets the start_time of this RawTableParam.

        开始时间。

        :return: The start_time of this RawTableParam.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this RawTableParam.

        开始时间。

        :param start_time: The start_time of this RawTableParam.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RawTableParam.

        结束时间。

        :return: The end_time of this RawTableParam.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RawTableParam.

        结束时间。

        :param end_time: The end_time of this RawTableParam.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, RawTableParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
