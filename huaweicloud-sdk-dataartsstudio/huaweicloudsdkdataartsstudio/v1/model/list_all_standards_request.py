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
        'directory_id': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'directory_id': 'directory_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, directory_id=None, begin_time=None, end_time=None, limit=None, offset=None):
        """ListAllStandardsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param directory_id: 目录ID。获取该目录下的数据，如果有子目录，获取所有子目录的数据
        :type directory_id: str
        :param begin_time: 时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效
        :type begin_time: str
        :param end_time: 时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效
        :type end_time: str
        :param limit: 查询条数，即查询Y条数据。默认值50，取值范围[1,100]
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0
        :type offset: int
        """
        
        

        self._workspace = None
        self._directory_id = None
        self._begin_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if directory_id is not None:
            self.directory_id = directory_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListAllStandardsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListAllStandardsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListAllStandardsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListAllStandardsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def directory_id(self):
        """Gets the directory_id of this ListAllStandardsRequest.

        目录ID。获取该目录下的数据，如果有子目录，获取所有子目录的数据

        :return: The directory_id of this ListAllStandardsRequest.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this ListAllStandardsRequest.

        目录ID。获取该目录下的数据，如果有子目录，获取所有子目录的数据

        :param directory_id: The directory_id of this ListAllStandardsRequest.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def begin_time(self):
        """Gets the begin_time of this ListAllStandardsRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :return: The begin_time of this ListAllStandardsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListAllStandardsRequest.

        时间过滤左边界,与end_time一起使用,只支持时间范围过滤,单边过滤无效

        :param begin_time: The begin_time of this ListAllStandardsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAllStandardsRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :return: The end_time of this ListAllStandardsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAllStandardsRequest.

        时间过滤右边界,与begin_time一起使用只支持时间范围过滤,单边过滤无效

        :param end_time: The end_time of this ListAllStandardsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListAllStandardsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :return: The limit of this ListAllStandardsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAllStandardsRequest.

        查询条数，即查询Y条数据。默认值50，取值范围[1,100]

        :param limit: The limit of this ListAllStandardsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAllStandardsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

        :return: The offset of this ListAllStandardsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAllStandardsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整。默认值0

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
