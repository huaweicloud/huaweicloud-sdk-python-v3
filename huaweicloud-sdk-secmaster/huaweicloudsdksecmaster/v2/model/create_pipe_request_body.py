# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePipeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipe_name': 'str',
        'pipe_alias': 'str',
        'category': 'str',
        'directory': 'str',
        'description': 'str',
        'schema': 'PipeSchema',
        'storage_setting': 'PipeStorageSetting',
        'display_setting': 'TableDisplaySetting'
    }

    attribute_map = {
        'pipe_name': 'pipe_name',
        'pipe_alias': 'pipe_alias',
        'category': 'category',
        'directory': 'directory',
        'description': 'description',
        'schema': 'schema',
        'storage_setting': 'storage_setting',
        'display_setting': 'display_setting'
    }

    def __init__(self, pipe_name=None, pipe_alias=None, category=None, directory=None, description=None, schema=None, storage_setting=None, display_setting=None):
        r"""CreatePipeRequestBody

        The model defined in huaweicloud sdk

        :param pipe_name: 管道名称
        :type pipe_name: str
        :param pipe_alias: 管道别名
        :type pipe_alias: str
        :param category: **参数解释**: 管道目录 - STREAMING_TO_INDEX 流式写入索引 - STREAMING_TO_LAKE 流式写入数据湖 - STREAMING_TO_INDEX_LAKE 流式写入索引和数据湖 - STREAMING  流式传输中  **约束限制** 不涉及  **取值范围**: - STREAMING_TO_INDEX - STREAMING_TO_LAKE - STREAMING_TO_INDEX_LAKE - STREAMING  **默认值** 不涉及       
        :type category: str
        :param directory: directory 目录分组
        :type directory: str
        :param description: 管道描述
        :type description: str
        :param schema: 
        :type schema: :class:`huaweicloudsdksecmaster.v2.PipeSchema`
        :param storage_setting: 
        :type storage_setting: :class:`huaweicloudsdksecmaster.v2.PipeStorageSetting`
        :param display_setting: 
        :type display_setting: :class:`huaweicloudsdksecmaster.v2.TableDisplaySetting`
        """
        
        

        self._pipe_name = None
        self._pipe_alias = None
        self._category = None
        self._directory = None
        self._description = None
        self._schema = None
        self._storage_setting = None
        self._display_setting = None
        self.discriminator = None

        self.pipe_name = pipe_name
        self.pipe_alias = pipe_alias
        self.category = category
        if directory is not None:
            self.directory = directory
        if description is not None:
            self.description = description
        self.schema = schema
        self.storage_setting = storage_setting
        if display_setting is not None:
            self.display_setting = display_setting

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this CreatePipeRequestBody.

        管道名称

        :return: The pipe_name of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this CreatePipeRequestBody.

        管道名称

        :param pipe_name: The pipe_name of this CreatePipeRequestBody.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def pipe_alias(self):
        r"""Gets the pipe_alias of this CreatePipeRequestBody.

        管道别名

        :return: The pipe_alias of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._pipe_alias

    @pipe_alias.setter
    def pipe_alias(self, pipe_alias):
        r"""Sets the pipe_alias of this CreatePipeRequestBody.

        管道别名

        :param pipe_alias: The pipe_alias of this CreatePipeRequestBody.
        :type pipe_alias: str
        """
        self._pipe_alias = pipe_alias

    @property
    def category(self):
        r"""Gets the category of this CreatePipeRequestBody.

        **参数解释**: 管道目录 - STREAMING_TO_INDEX 流式写入索引 - STREAMING_TO_LAKE 流式写入数据湖 - STREAMING_TO_INDEX_LAKE 流式写入索引和数据湖 - STREAMING  流式传输中  **约束限制** 不涉及  **取值范围**: - STREAMING_TO_INDEX - STREAMING_TO_LAKE - STREAMING_TO_INDEX_LAKE - STREAMING  **默认值** 不涉及       

        :return: The category of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreatePipeRequestBody.

        **参数解释**: 管道目录 - STREAMING_TO_INDEX 流式写入索引 - STREAMING_TO_LAKE 流式写入数据湖 - STREAMING_TO_INDEX_LAKE 流式写入索引和数据湖 - STREAMING  流式传输中  **约束限制** 不涉及  **取值范围**: - STREAMING_TO_INDEX - STREAMING_TO_LAKE - STREAMING_TO_INDEX_LAKE - STREAMING  **默认值** 不涉及       

        :param category: The category of this CreatePipeRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def directory(self):
        r"""Gets the directory of this CreatePipeRequestBody.

        directory 目录分组

        :return: The directory of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this CreatePipeRequestBody.

        directory 目录分组

        :param directory: The directory of this CreatePipeRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def description(self):
        r"""Gets the description of this CreatePipeRequestBody.

        管道描述

        :return: The description of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePipeRequestBody.

        管道描述

        :param description: The description of this CreatePipeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def schema(self):
        r"""Gets the schema of this CreatePipeRequestBody.

        :return: The schema of this CreatePipeRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.PipeSchema`
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this CreatePipeRequestBody.

        :param schema: The schema of this CreatePipeRequestBody.
        :type schema: :class:`huaweicloudsdksecmaster.v2.PipeSchema`
        """
        self._schema = schema

    @property
    def storage_setting(self):
        r"""Gets the storage_setting of this CreatePipeRequestBody.

        :return: The storage_setting of this CreatePipeRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.PipeStorageSetting`
        """
        return self._storage_setting

    @storage_setting.setter
    def storage_setting(self, storage_setting):
        r"""Sets the storage_setting of this CreatePipeRequestBody.

        :param storage_setting: The storage_setting of this CreatePipeRequestBody.
        :type storage_setting: :class:`huaweicloudsdksecmaster.v2.PipeStorageSetting`
        """
        self._storage_setting = storage_setting

    @property
    def display_setting(self):
        r"""Gets the display_setting of this CreatePipeRequestBody.

        :return: The display_setting of this CreatePipeRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.TableDisplaySetting`
        """
        return self._display_setting

    @display_setting.setter
    def display_setting(self, display_setting):
        r"""Sets the display_setting of this CreatePipeRequestBody.

        :param display_setting: The display_setting of this CreatePipeRequestBody.
        :type display_setting: :class:`huaweicloudsdksecmaster.v2.TableDisplaySetting`
        """
        self._display_setting = display_setting

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
        if not isinstance(other, CreatePipeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
