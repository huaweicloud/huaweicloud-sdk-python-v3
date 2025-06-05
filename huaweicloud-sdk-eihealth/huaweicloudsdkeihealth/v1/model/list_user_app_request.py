# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_creator': 'bool',
        'id': 'str',
        'name': 'str',
        'summary': 'str',
        'eihealth_project_names': 'list[str]',
        'labels': 'list[str]',
        'start_create_time': 'int',
        'end_create_time': 'int',
        'start_update_time': 'int',
        'end_update_time': 'int',
        'sort_by': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'is_creator': 'is_creator',
        'id': 'id',
        'name': 'name',
        'summary': 'summary',
        'eihealth_project_names': 'eihealth_project_names',
        'labels': 'labels',
        'start_create_time': 'start_create_time',
        'end_create_time': 'end_create_time',
        'start_update_time': 'start_update_time',
        'end_update_time': 'end_update_time',
        'sort_by': 'sort_by',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, is_creator=None, id=None, name=None, summary=None, eihealth_project_names=None, labels=None, start_create_time=None, end_create_time=None, start_update_time=None, end_update_time=None, sort_by=None, sort_dir=None, limit=None, offset=None):
        r"""ListUserAppRequest

        The model defined in huaweicloud sdk

        :param is_creator: 是否仅展示本人创建资源。
        :type is_creator: bool
        :param id: 应用ID，支持精确搜索。
        :type id: str
        :param name: 应用名称，支持模糊搜索。
        :type name: str
        :param summary: 短描述，支持模糊搜索。
        :type summary: str
        :param eihealth_project_names: 空间名称列表，支持查询多个空间下的镜像。
        :type eihealth_project_names: list[str]
        :param labels: 标签列表。
        :type labels: list[str]
        :param start_create_time: 最小创建时间。
        :type start_create_time: int
        :param end_create_time: 最大创建时间。
        :type end_create_time: int
        :param start_update_time: 最小更新时间。
        :type start_update_time: int
        :param end_update_time: 最大更新时间。
        :type end_update_time: int
        :param sort_by: 排序规则，目前默认时间降序，支持根据create_time|update_time排序。
        :type sort_by: str
        :param sort_dir: 排序规则，目前默认时间降序。
        :type sort_dir: str
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。
        :type offset: int
        """
        
        

        self._is_creator = None
        self._id = None
        self._name = None
        self._summary = None
        self._eihealth_project_names = None
        self._labels = None
        self._start_create_time = None
        self._end_create_time = None
        self._start_update_time = None
        self._end_update_time = None
        self._sort_by = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if is_creator is not None:
            self.is_creator = is_creator
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if summary is not None:
            self.summary = summary
        if eihealth_project_names is not None:
            self.eihealth_project_names = eihealth_project_names
        if labels is not None:
            self.labels = labels
        if start_create_time is not None:
            self.start_create_time = start_create_time
        if end_create_time is not None:
            self.end_create_time = end_create_time
        if start_update_time is not None:
            self.start_update_time = start_update_time
        if end_update_time is not None:
            self.end_update_time = end_update_time
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def is_creator(self):
        r"""Gets the is_creator of this ListUserAppRequest.

        是否仅展示本人创建资源。

        :return: The is_creator of this ListUserAppRequest.
        :rtype: bool
        """
        return self._is_creator

    @is_creator.setter
    def is_creator(self, is_creator):
        r"""Sets the is_creator of this ListUserAppRequest.

        是否仅展示本人创建资源。

        :param is_creator: The is_creator of this ListUserAppRequest.
        :type is_creator: bool
        """
        self._is_creator = is_creator

    @property
    def id(self):
        r"""Gets the id of this ListUserAppRequest.

        应用ID，支持精确搜索。

        :return: The id of this ListUserAppRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListUserAppRequest.

        应用ID，支持精确搜索。

        :param id: The id of this ListUserAppRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListUserAppRequest.

        应用名称，支持模糊搜索。

        :return: The name of this ListUserAppRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListUserAppRequest.

        应用名称，支持模糊搜索。

        :param name: The name of this ListUserAppRequest.
        :type name: str
        """
        self._name = name

    @property
    def summary(self):
        r"""Gets the summary of this ListUserAppRequest.

        短描述，支持模糊搜索。

        :return: The summary of this ListUserAppRequest.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this ListUserAppRequest.

        短描述，支持模糊搜索。

        :param summary: The summary of this ListUserAppRequest.
        :type summary: str
        """
        self._summary = summary

    @property
    def eihealth_project_names(self):
        r"""Gets the eihealth_project_names of this ListUserAppRequest.

        空间名称列表，支持查询多个空间下的镜像。

        :return: The eihealth_project_names of this ListUserAppRequest.
        :rtype: list[str]
        """
        return self._eihealth_project_names

    @eihealth_project_names.setter
    def eihealth_project_names(self, eihealth_project_names):
        r"""Sets the eihealth_project_names of this ListUserAppRequest.

        空间名称列表，支持查询多个空间下的镜像。

        :param eihealth_project_names: The eihealth_project_names of this ListUserAppRequest.
        :type eihealth_project_names: list[str]
        """
        self._eihealth_project_names = eihealth_project_names

    @property
    def labels(self):
        r"""Gets the labels of this ListUserAppRequest.

        标签列表。

        :return: The labels of this ListUserAppRequest.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListUserAppRequest.

        标签列表。

        :param labels: The labels of this ListUserAppRequest.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def start_create_time(self):
        r"""Gets the start_create_time of this ListUserAppRequest.

        最小创建时间。

        :return: The start_create_time of this ListUserAppRequest.
        :rtype: int
        """
        return self._start_create_time

    @start_create_time.setter
    def start_create_time(self, start_create_time):
        r"""Sets the start_create_time of this ListUserAppRequest.

        最小创建时间。

        :param start_create_time: The start_create_time of this ListUserAppRequest.
        :type start_create_time: int
        """
        self._start_create_time = start_create_time

    @property
    def end_create_time(self):
        r"""Gets the end_create_time of this ListUserAppRequest.

        最大创建时间。

        :return: The end_create_time of this ListUserAppRequest.
        :rtype: int
        """
        return self._end_create_time

    @end_create_time.setter
    def end_create_time(self, end_create_time):
        r"""Sets the end_create_time of this ListUserAppRequest.

        最大创建时间。

        :param end_create_time: The end_create_time of this ListUserAppRequest.
        :type end_create_time: int
        """
        self._end_create_time = end_create_time

    @property
    def start_update_time(self):
        r"""Gets the start_update_time of this ListUserAppRequest.

        最小更新时间。

        :return: The start_update_time of this ListUserAppRequest.
        :rtype: int
        """
        return self._start_update_time

    @start_update_time.setter
    def start_update_time(self, start_update_time):
        r"""Sets the start_update_time of this ListUserAppRequest.

        最小更新时间。

        :param start_update_time: The start_update_time of this ListUserAppRequest.
        :type start_update_time: int
        """
        self._start_update_time = start_update_time

    @property
    def end_update_time(self):
        r"""Gets the end_update_time of this ListUserAppRequest.

        最大更新时间。

        :return: The end_update_time of this ListUserAppRequest.
        :rtype: int
        """
        return self._end_update_time

    @end_update_time.setter
    def end_update_time(self, end_update_time):
        r"""Sets the end_update_time of this ListUserAppRequest.

        最大更新时间。

        :param end_update_time: The end_update_time of this ListUserAppRequest.
        :type end_update_time: int
        """
        self._end_update_time = end_update_time

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListUserAppRequest.

        排序规则，目前默认时间降序，支持根据create_time|update_time排序。

        :return: The sort_by of this ListUserAppRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListUserAppRequest.

        排序规则，目前默认时间降序，支持根据create_time|update_time排序。

        :param sort_by: The sort_by of this ListUserAppRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListUserAppRequest.

        排序规则，目前默认时间降序。

        :return: The sort_dir of this ListUserAppRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListUserAppRequest.

        排序规则，目前默认时间降序。

        :param sort_dir: The sort_dir of this ListUserAppRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListUserAppRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :return: The limit of this ListUserAppRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserAppRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :param limit: The limit of this ListUserAppRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListUserAppRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :return: The offset of this ListUserAppRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserAppRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :param offset: The offset of this ListUserAppRequest.
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
        if not isinstance(other, ListUserAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
