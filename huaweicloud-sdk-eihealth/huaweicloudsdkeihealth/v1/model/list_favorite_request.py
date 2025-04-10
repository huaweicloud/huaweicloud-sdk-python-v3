# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFavoriteRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'resource_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'user_name_list': 'list[str]',
        'resource_type_list': 'list[str]',
        'type_list': 'list[str]',
        'start_time': 'int',
        'end_time': 'int',
        'key_word': 'str',
        'sort_dir': 'str',
        'sort_key': 'str'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'resource_id': 'resource_id',
        'offset': 'offset',
        'limit': 'limit',
        'user_name_list': 'user_name_list',
        'resource_type_list': 'resource_type_list',
        'type_list': 'type_list',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'key_word': 'key_word',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key'
    }

    def __init__(self, eihealth_project_id=None, resource_id=None, offset=None, limit=None, user_name_list=None, resource_type_list=None, type_list=None, start_time=None, end_time=None, key_word=None, sort_dir=None, sort_key=None):
        r"""ListFavoriteRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。
        :type offset: int
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。
        :type limit: int
        :param user_name_list: 收藏人名称列表。
        :type user_name_list: list[str]
        :param resource_type_list: 资源类型列表。
        :type resource_type_list: list[str]
        :param type_list: 收藏类型列表，支持MICROMOLECULE|PROTEIN。
        :type type_list: list[str]
        :param start_time: 查询收藏信息的起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间。
        :type start_time: int
        :param end_time: 查询收藏信息的结束时间，UNIX时间戳，单位毫秒，不填时默认为当前时间。
        :type end_time: int
        :param key_word: 关键字，支持在display_info字段中内容的模糊搜索。
        :type key_word: str
        :param sort_dir: 排序规则，目前默认时间降序。
        :type sort_dir: str
        :param sort_key: 排序规则，目前默认按收藏时间降序，支持根据create_time|user_name|resource_name|resource_type排序。
        :type sort_key: str
        """
        
        

        self._eihealth_project_id = None
        self._resource_id = None
        self._offset = None
        self._limit = None
        self._user_name_list = None
        self._resource_type_list = None
        self._type_list = None
        self._start_time = None
        self._end_time = None
        self._key_word = None
        self._sort_dir = None
        self._sort_key = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        if resource_id is not None:
            self.resource_id = resource_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if user_name_list is not None:
            self.user_name_list = user_name_list
        if resource_type_list is not None:
            self.resource_type_list = resource_type_list
        if type_list is not None:
            self.type_list = type_list
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if key_word is not None:
            self.key_word = key_word
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this ListFavoriteRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ListFavoriteRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this ListFavoriteRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ListFavoriteRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListFavoriteRequest.

        资源ID。

        :return: The resource_id of this ListFavoriteRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListFavoriteRequest.

        资源ID。

        :param resource_id: The resource_id of this ListFavoriteRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def offset(self):
        r"""Gets the offset of this ListFavoriteRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :return: The offset of this ListFavoriteRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFavoriteRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :param offset: The offset of this ListFavoriteRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFavoriteRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :return: The limit of this ListFavoriteRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFavoriteRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :param limit: The limit of this ListFavoriteRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def user_name_list(self):
        r"""Gets the user_name_list of this ListFavoriteRequest.

        收藏人名称列表。

        :return: The user_name_list of this ListFavoriteRequest.
        :rtype: list[str]
        """
        return self._user_name_list

    @user_name_list.setter
    def user_name_list(self, user_name_list):
        r"""Sets the user_name_list of this ListFavoriteRequest.

        收藏人名称列表。

        :param user_name_list: The user_name_list of this ListFavoriteRequest.
        :type user_name_list: list[str]
        """
        self._user_name_list = user_name_list

    @property
    def resource_type_list(self):
        r"""Gets the resource_type_list of this ListFavoriteRequest.

        资源类型列表。

        :return: The resource_type_list of this ListFavoriteRequest.
        :rtype: list[str]
        """
        return self._resource_type_list

    @resource_type_list.setter
    def resource_type_list(self, resource_type_list):
        r"""Sets the resource_type_list of this ListFavoriteRequest.

        资源类型列表。

        :param resource_type_list: The resource_type_list of this ListFavoriteRequest.
        :type resource_type_list: list[str]
        """
        self._resource_type_list = resource_type_list

    @property
    def type_list(self):
        r"""Gets the type_list of this ListFavoriteRequest.

        收藏类型列表，支持MICROMOLECULE|PROTEIN。

        :return: The type_list of this ListFavoriteRequest.
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        r"""Sets the type_list of this ListFavoriteRequest.

        收藏类型列表，支持MICROMOLECULE|PROTEIN。

        :param type_list: The type_list of this ListFavoriteRequest.
        :type type_list: list[str]
        """
        self._type_list = type_list

    @property
    def start_time(self):
        r"""Gets the start_time of this ListFavoriteRequest.

        查询收藏信息的起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间。

        :return: The start_time of this ListFavoriteRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListFavoriteRequest.

        查询收藏信息的起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间。

        :param start_time: The start_time of this ListFavoriteRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListFavoriteRequest.

        查询收藏信息的结束时间，UNIX时间戳，单位毫秒，不填时默认为当前时间。

        :return: The end_time of this ListFavoriteRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListFavoriteRequest.

        查询收藏信息的结束时间，UNIX时间戳，单位毫秒，不填时默认为当前时间。

        :param end_time: The end_time of this ListFavoriteRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def key_word(self):
        r"""Gets the key_word of this ListFavoriteRequest.

        关键字，支持在display_info字段中内容的模糊搜索。

        :return: The key_word of this ListFavoriteRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this ListFavoriteRequest.

        关键字，支持在display_info字段中内容的模糊搜索。

        :param key_word: The key_word of this ListFavoriteRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListFavoriteRequest.

        排序规则，目前默认时间降序。

        :return: The sort_dir of this ListFavoriteRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListFavoriteRequest.

        排序规则，目前默认时间降序。

        :param sort_dir: The sort_dir of this ListFavoriteRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListFavoriteRequest.

        排序规则，目前默认按收藏时间降序，支持根据create_time|user_name|resource_name|resource_type排序。

        :return: The sort_key of this ListFavoriteRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListFavoriteRequest.

        排序规则，目前默认按收藏时间降序，支持根据create_time|user_name|resource_name|resource_type排序。

        :param sort_key: The sort_key of this ListFavoriteRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

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
        if not isinstance(other, ListFavoriteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
