# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllStandardsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'directory_id': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'need_path': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'directory_id': 'directory_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'need_path': 'need_path',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, x_project_id=None, directory_id=None, begin_time=None, end_time=None, need_path=None, limit=None, offset=None):
        r"""ListAllStandardsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param directory_id: 目录ID。获取该目录下的数据标准，如果有子目录，同时获取所有子目录的数据标准。
        :type directory_id: str
        :param begin_time: 时间过滤左边界，与end_time一起使用，只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type begin_time: str
        :param end_time: 时间过滤右边界，与begin_time一起使用只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type end_time: str
        :param need_path: 查询数据标准目录时，是否查询数据标准目录信息。
        :type need_path: bool
        :param limit: 每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。
        :type offset: int
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._directory_id = None
        self._begin_time = None
        self._end_time = None
        self._need_path = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if directory_id is not None:
            self.directory_id = directory_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if need_path is not None:
            self.need_path = need_path
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        r"""Gets the workspace of this ListAllStandardsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListAllStandardsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListAllStandardsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListAllStandardsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListAllStandardsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListAllStandardsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListAllStandardsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListAllStandardsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def directory_id(self):
        r"""Gets the directory_id of this ListAllStandardsRequest.

        目录ID。获取该目录下的数据标准，如果有子目录，同时获取所有子目录的数据标准。

        :return: The directory_id of this ListAllStandardsRequest.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        r"""Sets the directory_id of this ListAllStandardsRequest.

        目录ID。获取该目录下的数据标准，如果有子目录，同时获取所有子目录的数据标准。

        :param directory_id: The directory_id of this ListAllStandardsRequest.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListAllStandardsRequest.

        时间过滤左边界，与end_time一起使用，只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The begin_time of this ListAllStandardsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListAllStandardsRequest.

        时间过滤左边界，与end_time一起使用，只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param begin_time: The begin_time of this ListAllStandardsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAllStandardsRequest.

        时间过滤右边界，与begin_time一起使用只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The end_time of this ListAllStandardsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAllStandardsRequest.

        时间过滤右边界，与begin_time一起使用只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param end_time: The end_time of this ListAllStandardsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def need_path(self):
        r"""Gets the need_path of this ListAllStandardsRequest.

        查询数据标准目录时，是否查询数据标准目录信息。

        :return: The need_path of this ListAllStandardsRequest.
        :rtype: bool
        """
        return self._need_path

    @need_path.setter
    def need_path(self, need_path):
        r"""Sets the need_path of this ListAllStandardsRequest.

        查询数据标准目录时，是否查询数据标准目录信息。

        :param need_path: The need_path of this ListAllStandardsRequest.
        :type need_path: bool
        """
        self._need_path = need_path

    @property
    def limit(self):
        r"""Gets the limit of this ListAllStandardsRequest.

        每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。

        :return: The limit of this ListAllStandardsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAllStandardsRequest.

        每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。

        :param limit: The limit of this ListAllStandardsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAllStandardsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。

        :return: The offset of this ListAllStandardsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAllStandardsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。

        :param offset: The offset of this ListAllStandardsRequest.
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
        if not isinstance(other, ListAllStandardsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
