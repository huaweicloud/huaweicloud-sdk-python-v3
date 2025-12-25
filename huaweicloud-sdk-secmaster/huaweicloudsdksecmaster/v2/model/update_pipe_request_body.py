# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePipeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipe_alias': 'str',
        'description': 'str',
        'directory': 'str',
        'category': 'str'
    }

    attribute_map = {
        'pipe_alias': 'pipe_alias',
        'description': 'description',
        'directory': 'directory',
        'category': 'category'
    }

    def __init__(self, pipe_alias=None, description=None, directory=None, category=None):
        r"""UpdatePipeRequestBody

        The model defined in huaweicloud sdk

        :param pipe_alias: 管道别名
        :type pipe_alias: str
        :param description: 管道描述
        :type description: str
        :param directory: directory 目录分组
        :type directory: str
        :param category: **参数解释**: 管道目录 - STREAMING_TO_INDEX 流式写入索引 - STREAMING_TO_LAKE 流式写入数据湖 - STREAMING_TO_INDEX_LAKE 流式写入索引和数据湖 - STREAMING  流式传输中  **约束限制** 不涉及  **取值范围**: - STREAMING_TO_INDEX - STREAMING_TO_LAKE - STREAMING_TO_INDEX_LAKE - STREAMING  **默认值** 不涉及       
        :type category: str
        """
        
        

        self._pipe_alias = None
        self._description = None
        self._directory = None
        self._category = None
        self.discriminator = None

        if pipe_alias is not None:
            self.pipe_alias = pipe_alias
        if description is not None:
            self.description = description
        if directory is not None:
            self.directory = directory
        if category is not None:
            self.category = category

    @property
    def pipe_alias(self):
        r"""Gets the pipe_alias of this UpdatePipeRequestBody.

        管道别名

        :return: The pipe_alias of this UpdatePipeRequestBody.
        :rtype: str
        """
        return self._pipe_alias

    @pipe_alias.setter
    def pipe_alias(self, pipe_alias):
        r"""Sets the pipe_alias of this UpdatePipeRequestBody.

        管道别名

        :param pipe_alias: The pipe_alias of this UpdatePipeRequestBody.
        :type pipe_alias: str
        """
        self._pipe_alias = pipe_alias

    @property
    def description(self):
        r"""Gets the description of this UpdatePipeRequestBody.

        管道描述

        :return: The description of this UpdatePipeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePipeRequestBody.

        管道描述

        :param description: The description of this UpdatePipeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def directory(self):
        r"""Gets the directory of this UpdatePipeRequestBody.

        directory 目录分组

        :return: The directory of this UpdatePipeRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this UpdatePipeRequestBody.

        directory 目录分组

        :param directory: The directory of this UpdatePipeRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def category(self):
        r"""Gets the category of this UpdatePipeRequestBody.

        **参数解释**: 管道目录 - STREAMING_TO_INDEX 流式写入索引 - STREAMING_TO_LAKE 流式写入数据湖 - STREAMING_TO_INDEX_LAKE 流式写入索引和数据湖 - STREAMING  流式传输中  **约束限制** 不涉及  **取值范围**: - STREAMING_TO_INDEX - STREAMING_TO_LAKE - STREAMING_TO_INDEX_LAKE - STREAMING  **默认值** 不涉及       

        :return: The category of this UpdatePipeRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this UpdatePipeRequestBody.

        **参数解释**: 管道目录 - STREAMING_TO_INDEX 流式写入索引 - STREAMING_TO_LAKE 流式写入数据湖 - STREAMING_TO_INDEX_LAKE 流式写入索引和数据湖 - STREAMING  流式传输中  **约束限制** 不涉及  **取值范围**: - STREAMING_TO_INDEX - STREAMING_TO_LAKE - STREAMING_TO_INDEX_LAKE - STREAMING  **默认值** 不涉及       

        :param category: The category of this UpdatePipeRequestBody.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, UpdatePipeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
