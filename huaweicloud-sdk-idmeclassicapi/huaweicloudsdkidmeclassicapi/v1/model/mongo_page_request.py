# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MongoPageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'start_last_modified_time': 'str',
        'end_last_modified_time': 'str',
        'rdm_version': 'int',
        'source_id': 'str',
        'source_rdm_version': 'int',
        'target_id': 'str',
        'target_rdm_version': 'int',
        'target_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'start_last_modified_time': 'startLastModifiedTime',
        'end_last_modified_time': 'endLastModifiedTime',
        'rdm_version': 'rdmVersion',
        'source_id': 'sourceId',
        'source_rdm_version': 'sourceRdmVersion',
        'target_id': 'targetId',
        'target_rdm_version': 'targetRdmVersion',
        'target_type': 'targetType'
    }

    def __init__(self, id=None, start_last_modified_time=None, end_last_modified_time=None, rdm_version=None, source_id=None, source_rdm_version=None, target_id=None, target_rdm_version=None, target_type=None):
        r"""MongoPageRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  数据实例ID，用于指定待查询历史版本的数据实例。 获取方法请参见[分页查询实例 - ShowFindUsingPost](https://support.huaweicloud.com/api-idme/ShowFindUsingPost.html)。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。
        :type id: str
        :param start_last_modified_time: **参数解释：**  开始时间，用于指定查询时间区间的起始点。系统以数据实例的最后修改时间作为查询条件。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type start_last_modified_time: str
        :param end_last_modified_time: **参数解释：**  结束时间，用于指定查询时间区间的结束点。系统以数据实例的最后修改时间作为查询条件。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type end_last_modified_time: str
        :param rdm_version: **参数解释：**  系统版本号，用于指定查询特定版本的历史记录。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type rdm_version: int
        :param source_id: **参数解释：**  关系实体源端ID，用于查询关系实体的历史版本信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type source_id: str
        :param source_rdm_version: **参数解释：**  关系实体源端系统版本，用于指定源端实例的特定版本。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type source_rdm_version: int
        :param target_id: **参数解释：**  关系实体目标端ID，用于查询关系实体的历史版本信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type target_id: str
        :param target_rdm_version: **参数解释：**  关系实体目标端系统版本，用于指定目标端实例的特定版本。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type target_rdm_version: int
        :param target_type: **参数解释：**  单边不确定关系的目标端类型，用于指定关系实体的目标端模型类型。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type target_type: str
        """
        
        

        self._id = None
        self._start_last_modified_time = None
        self._end_last_modified_time = None
        self._rdm_version = None
        self._source_id = None
        self._source_rdm_version = None
        self._target_id = None
        self._target_rdm_version = None
        self._target_type = None
        self.discriminator = None

        self.id = id
        if start_last_modified_time is not None:
            self.start_last_modified_time = start_last_modified_time
        if end_last_modified_time is not None:
            self.end_last_modified_time = end_last_modified_time
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if source_id is not None:
            self.source_id = source_id
        if source_rdm_version is not None:
            self.source_rdm_version = source_rdm_version
        if target_id is not None:
            self.target_id = target_id
        if target_rdm_version is not None:
            self.target_rdm_version = target_rdm_version
        if target_type is not None:
            self.target_type = target_type

    @property
    def id(self):
        r"""Gets the id of this MongoPageRequest.

        **参数解释：**  数据实例ID，用于指定待查询历史版本的数据实例。 获取方法请参见[分页查询实例 - ShowFindUsingPost](https://support.huaweicloud.com/api-idme/ShowFindUsingPost.html)。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。

        :return: The id of this MongoPageRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MongoPageRequest.

        **参数解释：**  数据实例ID，用于指定待查询历史版本的数据实例。 获取方法请参见[分页查询实例 - ShowFindUsingPost](https://support.huaweicloud.com/api-idme/ShowFindUsingPost.html)。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。

        :param id: The id of this MongoPageRequest.
        :type id: str
        """
        self._id = id

    @property
    def start_last_modified_time(self):
        r"""Gets the start_last_modified_time of this MongoPageRequest.

        **参数解释：**  开始时间，用于指定查询时间区间的起始点。系统以数据实例的最后修改时间作为查询条件。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The start_last_modified_time of this MongoPageRequest.
        :rtype: str
        """
        return self._start_last_modified_time

    @start_last_modified_time.setter
    def start_last_modified_time(self, start_last_modified_time):
        r"""Sets the start_last_modified_time of this MongoPageRequest.

        **参数解释：**  开始时间，用于指定查询时间区间的起始点。系统以数据实例的最后修改时间作为查询条件。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param start_last_modified_time: The start_last_modified_time of this MongoPageRequest.
        :type start_last_modified_time: str
        """
        self._start_last_modified_time = start_last_modified_time

    @property
    def end_last_modified_time(self):
        r"""Gets the end_last_modified_time of this MongoPageRequest.

        **参数解释：**  结束时间，用于指定查询时间区间的结束点。系统以数据实例的最后修改时间作为查询条件。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The end_last_modified_time of this MongoPageRequest.
        :rtype: str
        """
        return self._end_last_modified_time

    @end_last_modified_time.setter
    def end_last_modified_time(self, end_last_modified_time):
        r"""Sets the end_last_modified_time of this MongoPageRequest.

        **参数解释：**  结束时间，用于指定查询时间区间的结束点。系统以数据实例的最后修改时间作为查询条件。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param end_last_modified_time: The end_last_modified_time of this MongoPageRequest.
        :type end_last_modified_time: str
        """
        self._end_last_modified_time = end_last_modified_time

    @property
    def rdm_version(self):
        r"""Gets the rdm_version of this MongoPageRequest.

        **参数解释：**  系统版本号，用于指定查询特定版本的历史记录。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The rdm_version of this MongoPageRequest.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        r"""Sets the rdm_version of this MongoPageRequest.

        **参数解释：**  系统版本号，用于指定查询特定版本的历史记录。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param rdm_version: The rdm_version of this MongoPageRequest.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def source_id(self):
        r"""Gets the source_id of this MongoPageRequest.

        **参数解释：**  关系实体源端ID，用于查询关系实体的历史版本信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The source_id of this MongoPageRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this MongoPageRequest.

        **参数解释：**  关系实体源端ID，用于查询关系实体的历史版本信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param source_id: The source_id of this MongoPageRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_rdm_version(self):
        r"""Gets the source_rdm_version of this MongoPageRequest.

        **参数解释：**  关系实体源端系统版本，用于指定源端实例的特定版本。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The source_rdm_version of this MongoPageRequest.
        :rtype: int
        """
        return self._source_rdm_version

    @source_rdm_version.setter
    def source_rdm_version(self, source_rdm_version):
        r"""Sets the source_rdm_version of this MongoPageRequest.

        **参数解释：**  关系实体源端系统版本，用于指定源端实例的特定版本。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param source_rdm_version: The source_rdm_version of this MongoPageRequest.
        :type source_rdm_version: int
        """
        self._source_rdm_version = source_rdm_version

    @property
    def target_id(self):
        r"""Gets the target_id of this MongoPageRequest.

        **参数解释：**  关系实体目标端ID，用于查询关系实体的历史版本信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The target_id of this MongoPageRequest.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this MongoPageRequest.

        **参数解释：**  关系实体目标端ID，用于查询关系实体的历史版本信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param target_id: The target_id of this MongoPageRequest.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_rdm_version(self):
        r"""Gets the target_rdm_version of this MongoPageRequest.

        **参数解释：**  关系实体目标端系统版本，用于指定目标端实例的特定版本。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The target_rdm_version of this MongoPageRequest.
        :rtype: int
        """
        return self._target_rdm_version

    @target_rdm_version.setter
    def target_rdm_version(self, target_rdm_version):
        r"""Sets the target_rdm_version of this MongoPageRequest.

        **参数解释：**  关系实体目标端系统版本，用于指定目标端实例的特定版本。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param target_rdm_version: The target_rdm_version of this MongoPageRequest.
        :type target_rdm_version: int
        """
        self._target_rdm_version = target_rdm_version

    @property
    def target_type(self):
        r"""Gets the target_type of this MongoPageRequest.

        **参数解释：**  单边不确定关系的目标端类型，用于指定关系实体的目标端模型类型。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The target_type of this MongoPageRequest.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this MongoPageRequest.

        **参数解释：**  单边不确定关系的目标端类型，用于指定关系实体的目标端模型类型。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param target_type: The target_type of this MongoPageRequest.
        :type target_type: str
        """
        self._target_type = target_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MongoPageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
