# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLinksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'job_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_type': 'job_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, job_type=None, offset=None, limit=None):
        r"""ListLinksRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文 - zh-cn：中文  **默认取值**：  en-us
        :type x_language: str
        :param job_type: **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - replay：流量回放  **默认取值**：  不涉及
        :type job_type: str
        :param offset: **参数解释**：  偏移量，表示查询该偏移量后面的记录，用于分页查询。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0
        :type offset: int
        :param limit: **参数解释**：  查询返回记录的数量限制，用于分页查询时控制每页返回的数据条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type limit: int
        """
        
        

        self._x_language = None
        self._job_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_type = job_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListLinksRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文 - zh-cn：中文  **默认取值**：  en-us

        :return: The x_language of this ListLinksRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListLinksRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文 - zh-cn：中文  **默认取值**：  en-us

        :param x_language: The x_language of this ListLinksRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_type(self):
        r"""Gets the job_type of this ListLinksRequest.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - replay：流量回放  **默认取值**：  不涉及

        :return: The job_type of this ListLinksRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListLinksRequest.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - replay：流量回放  **默认取值**：  不涉及

        :param job_type: The job_type of this ListLinksRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def offset(self):
        r"""Gets the offset of this ListLinksRequest.

        **参数解释**：  偏移量，表示查询该偏移量后面的记录，用于分页查询。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0

        :return: The offset of this ListLinksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLinksRequest.

        **参数解释**：  偏移量，表示查询该偏移量后面的记录，用于分页查询。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0

        :param offset: The offset of this ListLinksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLinksRequest.

        **参数解释**：  查询返回记录的数量限制，用于分页查询时控制每页返回的数据条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The limit of this ListLinksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLinksRequest.

        **参数解释**：  查询返回记录的数量限制，用于分页查询时控制每页返回的数据条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param limit: The limit of this ListLinksRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListLinksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
