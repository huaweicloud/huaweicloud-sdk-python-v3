# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserNotebookRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notebook_name': 'str',
        'description': 'str',
        'image_name': 'str',
        'is_creator': 'bool',
        'eihealth_project_names': 'list[str]',
        'statuses': 'list[str]',
        'start_create_time': 'int',
        'end_create_time': 'int',
        'start_update_time': 'int',
        'end_update_time': 'int',
        'sort_dir': 'str',
        'sort_by': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'notebook_name': 'notebook_name',
        'description': 'description',
        'image_name': 'image_name',
        'is_creator': 'is_creator',
        'eihealth_project_names': 'eihealth_project_names',
        'statuses': 'statuses',
        'start_create_time': 'start_create_time',
        'end_create_time': 'end_create_time',
        'start_update_time': 'start_update_time',
        'end_update_time': 'end_update_time',
        'sort_dir': 'sort_dir',
        'sort_by': 'sort_by',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, notebook_name=None, description=None, image_name=None, is_creator=None, eihealth_project_names=None, statuses=None, start_create_time=None, end_create_time=None, start_update_time=None, end_update_time=None, sort_dir=None, sort_by=None, limit=None, offset=None):
        r"""ListUserNotebookRequest

        The model defined in huaweicloud sdk

        :param notebook_name: notebook名称。
        :type notebook_name: str
        :param description: 描述。
        :type description: str
        :param image_name: 镜像名称。
        :type image_name: str
        :param is_creator: 是否仅展示当前用户创建的notebook。
        :type is_creator: bool
        :param eihealth_project_names: 空间名称列表。
        :type eihealth_project_names: list[str]
        :param statuses: 作业运行状态列表，支持RUNNING|ABNORMAL|HIBERNATE|SUCCEEDED|CREATING|DELETING|UPDATING|CREATEDFAILED|DELETEDFAILED|UPDATEDFAILED|UNKNOWN。
        :type statuses: list[str]
        :param start_create_time: 最小创建时间。
        :type start_create_time: int
        :param end_create_time: 最大创建时间。
        :type end_create_time: int
        :param start_update_time: 最小更新时间。
        :type start_update_time: int
        :param end_update_time: 最大更新时间。
        :type end_update_time: int
        :param sort_dir: 排序规则，目前默认时间降序。
        :type sort_dir: str
        :param sort_by: 排序规则，默认更新时间降序，支持根据create_time|update_time排序。
        :type sort_by: str
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。
        :type offset: int
        """
        
        

        self._notebook_name = None
        self._description = None
        self._image_name = None
        self._is_creator = None
        self._eihealth_project_names = None
        self._statuses = None
        self._start_create_time = None
        self._end_create_time = None
        self._start_update_time = None
        self._end_update_time = None
        self._sort_dir = None
        self._sort_by = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if notebook_name is not None:
            self.notebook_name = notebook_name
        if description is not None:
            self.description = description
        if image_name is not None:
            self.image_name = image_name
        if is_creator is not None:
            self.is_creator = is_creator
        if eihealth_project_names is not None:
            self.eihealth_project_names = eihealth_project_names
        if statuses is not None:
            self.statuses = statuses
        if start_create_time is not None:
            self.start_create_time = start_create_time
        if end_create_time is not None:
            self.end_create_time = end_create_time
        if start_update_time is not None:
            self.start_update_time = start_update_time
        if end_update_time is not None:
            self.end_update_time = end_update_time
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_by is not None:
            self.sort_by = sort_by
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def notebook_name(self):
        r"""Gets the notebook_name of this ListUserNotebookRequest.

        notebook名称。

        :return: The notebook_name of this ListUserNotebookRequest.
        :rtype: str
        """
        return self._notebook_name

    @notebook_name.setter
    def notebook_name(self, notebook_name):
        r"""Sets the notebook_name of this ListUserNotebookRequest.

        notebook名称。

        :param notebook_name: The notebook_name of this ListUserNotebookRequest.
        :type notebook_name: str
        """
        self._notebook_name = notebook_name

    @property
    def description(self):
        r"""Gets the description of this ListUserNotebookRequest.

        描述。

        :return: The description of this ListUserNotebookRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListUserNotebookRequest.

        描述。

        :param description: The description of this ListUserNotebookRequest.
        :type description: str
        """
        self._description = description

    @property
    def image_name(self):
        r"""Gets the image_name of this ListUserNotebookRequest.

        镜像名称。

        :return: The image_name of this ListUserNotebookRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListUserNotebookRequest.

        镜像名称。

        :param image_name: The image_name of this ListUserNotebookRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def is_creator(self):
        r"""Gets the is_creator of this ListUserNotebookRequest.

        是否仅展示当前用户创建的notebook。

        :return: The is_creator of this ListUserNotebookRequest.
        :rtype: bool
        """
        return self._is_creator

    @is_creator.setter
    def is_creator(self, is_creator):
        r"""Sets the is_creator of this ListUserNotebookRequest.

        是否仅展示当前用户创建的notebook。

        :param is_creator: The is_creator of this ListUserNotebookRequest.
        :type is_creator: bool
        """
        self._is_creator = is_creator

    @property
    def eihealth_project_names(self):
        r"""Gets the eihealth_project_names of this ListUserNotebookRequest.

        空间名称列表。

        :return: The eihealth_project_names of this ListUserNotebookRequest.
        :rtype: list[str]
        """
        return self._eihealth_project_names

    @eihealth_project_names.setter
    def eihealth_project_names(self, eihealth_project_names):
        r"""Sets the eihealth_project_names of this ListUserNotebookRequest.

        空间名称列表。

        :param eihealth_project_names: The eihealth_project_names of this ListUserNotebookRequest.
        :type eihealth_project_names: list[str]
        """
        self._eihealth_project_names = eihealth_project_names

    @property
    def statuses(self):
        r"""Gets the statuses of this ListUserNotebookRequest.

        作业运行状态列表，支持RUNNING|ABNORMAL|HIBERNATE|SUCCEEDED|CREATING|DELETING|UPDATING|CREATEDFAILED|DELETEDFAILED|UPDATEDFAILED|UNKNOWN。

        :return: The statuses of this ListUserNotebookRequest.
        :rtype: list[str]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        r"""Sets the statuses of this ListUserNotebookRequest.

        作业运行状态列表，支持RUNNING|ABNORMAL|HIBERNATE|SUCCEEDED|CREATING|DELETING|UPDATING|CREATEDFAILED|DELETEDFAILED|UPDATEDFAILED|UNKNOWN。

        :param statuses: The statuses of this ListUserNotebookRequest.
        :type statuses: list[str]
        """
        self._statuses = statuses

    @property
    def start_create_time(self):
        r"""Gets the start_create_time of this ListUserNotebookRequest.

        最小创建时间。

        :return: The start_create_time of this ListUserNotebookRequest.
        :rtype: int
        """
        return self._start_create_time

    @start_create_time.setter
    def start_create_time(self, start_create_time):
        r"""Sets the start_create_time of this ListUserNotebookRequest.

        最小创建时间。

        :param start_create_time: The start_create_time of this ListUserNotebookRequest.
        :type start_create_time: int
        """
        self._start_create_time = start_create_time

    @property
    def end_create_time(self):
        r"""Gets the end_create_time of this ListUserNotebookRequest.

        最大创建时间。

        :return: The end_create_time of this ListUserNotebookRequest.
        :rtype: int
        """
        return self._end_create_time

    @end_create_time.setter
    def end_create_time(self, end_create_time):
        r"""Sets the end_create_time of this ListUserNotebookRequest.

        最大创建时间。

        :param end_create_time: The end_create_time of this ListUserNotebookRequest.
        :type end_create_time: int
        """
        self._end_create_time = end_create_time

    @property
    def start_update_time(self):
        r"""Gets the start_update_time of this ListUserNotebookRequest.

        最小更新时间。

        :return: The start_update_time of this ListUserNotebookRequest.
        :rtype: int
        """
        return self._start_update_time

    @start_update_time.setter
    def start_update_time(self, start_update_time):
        r"""Sets the start_update_time of this ListUserNotebookRequest.

        最小更新时间。

        :param start_update_time: The start_update_time of this ListUserNotebookRequest.
        :type start_update_time: int
        """
        self._start_update_time = start_update_time

    @property
    def end_update_time(self):
        r"""Gets the end_update_time of this ListUserNotebookRequest.

        最大更新时间。

        :return: The end_update_time of this ListUserNotebookRequest.
        :rtype: int
        """
        return self._end_update_time

    @end_update_time.setter
    def end_update_time(self, end_update_time):
        r"""Sets the end_update_time of this ListUserNotebookRequest.

        最大更新时间。

        :param end_update_time: The end_update_time of this ListUserNotebookRequest.
        :type end_update_time: int
        """
        self._end_update_time = end_update_time

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListUserNotebookRequest.

        排序规则，目前默认时间降序。

        :return: The sort_dir of this ListUserNotebookRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListUserNotebookRequest.

        排序规则，目前默认时间降序。

        :param sort_dir: The sort_dir of this ListUserNotebookRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListUserNotebookRequest.

        排序规则，默认更新时间降序，支持根据create_time|update_time排序。

        :return: The sort_by of this ListUserNotebookRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListUserNotebookRequest.

        排序规则，默认更新时间降序，支持根据create_time|update_time排序。

        :param sort_by: The sort_by of this ListUserNotebookRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def limit(self):
        r"""Gets the limit of this ListUserNotebookRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :return: The limit of this ListUserNotebookRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserNotebookRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。

        :param limit: The limit of this ListUserNotebookRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListUserNotebookRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :return: The offset of this ListUserNotebookRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserNotebookRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。

        :param offset: The offset of this ListUserNotebookRequest.
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
        if not isinstance(other, ListUserNotebookRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
