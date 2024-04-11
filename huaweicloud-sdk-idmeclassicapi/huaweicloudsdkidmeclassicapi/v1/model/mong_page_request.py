# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MongPageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_last_modified_time': 'str',
        'id': 'str',
        'rdm_version': 'int',
        'source_id': 'str',
        'source_rdm_version': 'int',
        'start_last_modified_time': 'str',
        'target_id': 'str',
        'target_rdm_version': 'int',
        'target_type': 'str'
    }

    attribute_map = {
        'end_last_modified_time': 'endLastModifiedTime',
        'id': 'id',
        'rdm_version': 'rdmVersion',
        'source_id': 'sourceId',
        'source_rdm_version': 'sourceRdmVersion',
        'start_last_modified_time': 'startLastModifiedTime',
        'target_id': 'targetId',
        'target_rdm_version': 'targetRdmVersion',
        'target_type': 'targetType'
    }

    def __init__(self, end_last_modified_time=None, id=None, rdm_version=None, source_id=None, source_rdm_version=None, start_last_modified_time=None, target_id=None, target_rdm_version=None, target_type=None):
        """MongPageRequest

        The model defined in huaweicloud sdk

        :param end_last_modified_time: 结束时间。系统以数据实例的最后修改时间作为查询条件，您定义的开始时间和结束时间作为时间范围进行查询。
        :type end_last_modified_time: str
        :param id: 数据实例ID。
        :type id: str
        :param rdm_version: 版本号。
        :type rdm_version: int
        :param source_id: 关系实体源端ID。
        :type source_id: str
        :param source_rdm_version: 关系实体源端系统版本。
        :type source_rdm_version: int
        :param start_last_modified_time: 开始时间。系统以数据实例的最后修改时间作为查询条件，您定义的开始时间和结束时间作为时间范围进行查询。
        :type start_last_modified_time: str
        :param target_id: 关系实体目标端ID。
        :type target_id: str
        :param target_rdm_version: 关系实体目标端系统版本。
        :type target_rdm_version: int
        :param target_type: 单边不确定关系的目标端类型。
        :type target_type: str
        """
        
        

        self._end_last_modified_time = None
        self._id = None
        self._rdm_version = None
        self._source_id = None
        self._source_rdm_version = None
        self._start_last_modified_time = None
        self._target_id = None
        self._target_rdm_version = None
        self._target_type = None
        self.discriminator = None

        if end_last_modified_time is not None:
            self.end_last_modified_time = end_last_modified_time
        self.id = id
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if source_id is not None:
            self.source_id = source_id
        if source_rdm_version is not None:
            self.source_rdm_version = source_rdm_version
        if start_last_modified_time is not None:
            self.start_last_modified_time = start_last_modified_time
        if target_id is not None:
            self.target_id = target_id
        if target_rdm_version is not None:
            self.target_rdm_version = target_rdm_version
        if target_type is not None:
            self.target_type = target_type

    @property
    def end_last_modified_time(self):
        """Gets the end_last_modified_time of this MongPageRequest.

        结束时间。系统以数据实例的最后修改时间作为查询条件，您定义的开始时间和结束时间作为时间范围进行查询。

        :return: The end_last_modified_time of this MongPageRequest.
        :rtype: str
        """
        return self._end_last_modified_time

    @end_last_modified_time.setter
    def end_last_modified_time(self, end_last_modified_time):
        """Sets the end_last_modified_time of this MongPageRequest.

        结束时间。系统以数据实例的最后修改时间作为查询条件，您定义的开始时间和结束时间作为时间范围进行查询。

        :param end_last_modified_time: The end_last_modified_time of this MongPageRequest.
        :type end_last_modified_time: str
        """
        self._end_last_modified_time = end_last_modified_time

    @property
    def id(self):
        """Gets the id of this MongPageRequest.

        数据实例ID。

        :return: The id of this MongPageRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MongPageRequest.

        数据实例ID。

        :param id: The id of this MongPageRequest.
        :type id: str
        """
        self._id = id

    @property
    def rdm_version(self):
        """Gets the rdm_version of this MongPageRequest.

        版本号。

        :return: The rdm_version of this MongPageRequest.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        """Sets the rdm_version of this MongPageRequest.

        版本号。

        :param rdm_version: The rdm_version of this MongPageRequest.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def source_id(self):
        """Gets the source_id of this MongPageRequest.

        关系实体源端ID。

        :return: The source_id of this MongPageRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this MongPageRequest.

        关系实体源端ID。

        :param source_id: The source_id of this MongPageRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_rdm_version(self):
        """Gets the source_rdm_version of this MongPageRequest.

        关系实体源端系统版本。

        :return: The source_rdm_version of this MongPageRequest.
        :rtype: int
        """
        return self._source_rdm_version

    @source_rdm_version.setter
    def source_rdm_version(self, source_rdm_version):
        """Sets the source_rdm_version of this MongPageRequest.

        关系实体源端系统版本。

        :param source_rdm_version: The source_rdm_version of this MongPageRequest.
        :type source_rdm_version: int
        """
        self._source_rdm_version = source_rdm_version

    @property
    def start_last_modified_time(self):
        """Gets the start_last_modified_time of this MongPageRequest.

        开始时间。系统以数据实例的最后修改时间作为查询条件，您定义的开始时间和结束时间作为时间范围进行查询。

        :return: The start_last_modified_time of this MongPageRequest.
        :rtype: str
        """
        return self._start_last_modified_time

    @start_last_modified_time.setter
    def start_last_modified_time(self, start_last_modified_time):
        """Sets the start_last_modified_time of this MongPageRequest.

        开始时间。系统以数据实例的最后修改时间作为查询条件，您定义的开始时间和结束时间作为时间范围进行查询。

        :param start_last_modified_time: The start_last_modified_time of this MongPageRequest.
        :type start_last_modified_time: str
        """
        self._start_last_modified_time = start_last_modified_time

    @property
    def target_id(self):
        """Gets the target_id of this MongPageRequest.

        关系实体目标端ID。

        :return: The target_id of this MongPageRequest.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this MongPageRequest.

        关系实体目标端ID。

        :param target_id: The target_id of this MongPageRequest.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_rdm_version(self):
        """Gets the target_rdm_version of this MongPageRequest.

        关系实体目标端系统版本。

        :return: The target_rdm_version of this MongPageRequest.
        :rtype: int
        """
        return self._target_rdm_version

    @target_rdm_version.setter
    def target_rdm_version(self, target_rdm_version):
        """Sets the target_rdm_version of this MongPageRequest.

        关系实体目标端系统版本。

        :param target_rdm_version: The target_rdm_version of this MongPageRequest.
        :type target_rdm_version: int
        """
        self._target_rdm_version = target_rdm_version

    @property
    def target_type(self):
        """Gets the target_type of this MongPageRequest.

        单边不确定关系的目标端类型。

        :return: The target_type of this MongPageRequest.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this MongPageRequest.

        单边不确定关系的目标端类型。

        :param target_type: The target_type of this MongPageRequest.
        :type target_type: str
        """
        self._target_type = target_type

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
        if not isinstance(other, MongPageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
