# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTtscVocabularyConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'x_app_user_id': 'str',
        'type': 'str',
        'tts_service_name': 'str',
        'is_vocabulary_config_enable': 'str',
        'group_id': 'str',
        'asset_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'search_key': 'str'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'x_app_user_id': 'X-App-UserId',
        'type': 'type',
        'tts_service_name': 'tts_service_name',
        'is_vocabulary_config_enable': 'is_vocabulary_config_enable',
        'group_id': 'group_id',
        'asset_id': 'asset_id',
        'limit': 'limit',
        'offset': 'offset',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'search_key': 'search_key'
    }

    def __init__(self, x_request_id=None, x_app_user_id=None, type=None, tts_service_name=None, is_vocabulary_config_enable=None, group_id=None, asset_id=None, limit=None, offset=None, start_time=None, end_time=None, search_key=None):
        r"""ListTtscVocabularyConfigsRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成
        :type x_request_id: str
        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param type: 自定义读法类型。 - CHINESE_G2P：拼音 - PHONETIC_SYMBOL：音标 - CONTINUUM：连读 - ALIAS：别名 - SAY_AS：数字英文读法
        :type type: str
        :param tts_service_name: 声音模型名称
        :type tts_service_name: str
        :param is_vocabulary_config_enable: 是否应用词表配置，从周边服务传递
        :type is_vocabulary_config_enable: str
        :param group_id: 分组id
        :type group_id: str
        :param asset_id: 资产id
        :type asset_id: str
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param start_time: 起始时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type start_time: str
        :param end_time: 结束时间。格式遵循：RFC 3339 如\&quot;2021-01-10T10:43:17Z\&quot;。
        :type end_time: str
        :param search_key: 搜索条件
        :type search_key: str
        """
        
        

        self._x_request_id = None
        self._x_app_user_id = None
        self._type = None
        self._tts_service_name = None
        self._is_vocabulary_config_enable = None
        self._group_id = None
        self._asset_id = None
        self._limit = None
        self._offset = None
        self._start_time = None
        self._end_time = None
        self._search_key = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if type is not None:
            self.type = type
        if tts_service_name is not None:
            self.tts_service_name = tts_service_name
        if is_vocabulary_config_enable is not None:
            self.is_vocabulary_config_enable = is_vocabulary_config_enable
        if group_id is not None:
            self.group_id = group_id
        if asset_id is not None:
            self.asset_id = asset_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if search_key is not None:
            self.search_key = search_key

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListTtscVocabularyConfigsRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :return: The x_request_id of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListTtscVocabularyConfigsRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :param x_request_id: The x_request_id of this ListTtscVocabularyConfigsRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListTtscVocabularyConfigsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListTtscVocabularyConfigsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListTtscVocabularyConfigsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def type(self):
        r"""Gets the type of this ListTtscVocabularyConfigsRequest.

        自定义读法类型。 - CHINESE_G2P：拼音 - PHONETIC_SYMBOL：音标 - CONTINUUM：连读 - ALIAS：别名 - SAY_AS：数字英文读法

        :return: The type of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListTtscVocabularyConfigsRequest.

        自定义读法类型。 - CHINESE_G2P：拼音 - PHONETIC_SYMBOL：音标 - CONTINUUM：连读 - ALIAS：别名 - SAY_AS：数字英文读法

        :param type: The type of this ListTtscVocabularyConfigsRequest.
        :type type: str
        """
        self._type = type

    @property
    def tts_service_name(self):
        r"""Gets the tts_service_name of this ListTtscVocabularyConfigsRequest.

        声音模型名称

        :return: The tts_service_name of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._tts_service_name

    @tts_service_name.setter
    def tts_service_name(self, tts_service_name):
        r"""Sets the tts_service_name of this ListTtscVocabularyConfigsRequest.

        声音模型名称

        :param tts_service_name: The tts_service_name of this ListTtscVocabularyConfigsRequest.
        :type tts_service_name: str
        """
        self._tts_service_name = tts_service_name

    @property
    def is_vocabulary_config_enable(self):
        r"""Gets the is_vocabulary_config_enable of this ListTtscVocabularyConfigsRequest.

        是否应用词表配置，从周边服务传递

        :return: The is_vocabulary_config_enable of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._is_vocabulary_config_enable

    @is_vocabulary_config_enable.setter
    def is_vocabulary_config_enable(self, is_vocabulary_config_enable):
        r"""Sets the is_vocabulary_config_enable of this ListTtscVocabularyConfigsRequest.

        是否应用词表配置，从周边服务传递

        :param is_vocabulary_config_enable: The is_vocabulary_config_enable of this ListTtscVocabularyConfigsRequest.
        :type is_vocabulary_config_enable: str
        """
        self._is_vocabulary_config_enable = is_vocabulary_config_enable

    @property
    def group_id(self):
        r"""Gets the group_id of this ListTtscVocabularyConfigsRequest.

        分组id

        :return: The group_id of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListTtscVocabularyConfigsRequest.

        分组id

        :param group_id: The group_id of this ListTtscVocabularyConfigsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ListTtscVocabularyConfigsRequest.

        资产id

        :return: The asset_id of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ListTtscVocabularyConfigsRequest.

        资产id

        :param asset_id: The asset_id of this ListTtscVocabularyConfigsRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def limit(self):
        r"""Gets the limit of this ListTtscVocabularyConfigsRequest.

        每页显示的条目数量。

        :return: The limit of this ListTtscVocabularyConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTtscVocabularyConfigsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListTtscVocabularyConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTtscVocabularyConfigsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListTtscVocabularyConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTtscVocabularyConfigsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListTtscVocabularyConfigsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTtscVocabularyConfigsRequest.

        起始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The start_time of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTtscVocabularyConfigsRequest.

        起始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param start_time: The start_time of this ListTtscVocabularyConfigsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTtscVocabularyConfigsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :return: The end_time of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTtscVocabularyConfigsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :param end_time: The end_time of this ListTtscVocabularyConfigsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def search_key(self):
        r"""Gets the search_key of this ListTtscVocabularyConfigsRequest.

        搜索条件

        :return: The search_key of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        r"""Sets the search_key of this ListTtscVocabularyConfigsRequest.

        搜索条件

        :param search_key: The search_key of this ListTtscVocabularyConfigsRequest.
        :type search_key: str
        """
        self._search_key = search_key

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
        if not isinstance(other, ListTtscVocabularyConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
