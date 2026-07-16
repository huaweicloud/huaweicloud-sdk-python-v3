# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportOpsResultsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'dataset_id': 'str',
        'task_id': 'str',
        'dataset_name': 'str',
        'dataset_description': 'str',
        'is_published': 'bool',
        'overwrite': 'bool',
        'schema_mapping': 'list[ImportOpsResultsRequestBodySchemaMapping]',
        'ids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'dataset_id': 'dataset_id',
        'task_id': 'task_id',
        'dataset_name': 'dataset_name',
        'dataset_description': 'dataset_description',
        'is_published': 'is_published',
        'overwrite': 'overwrite',
        'schema_mapping': 'schema_mapping',
        'ids': 'ids'
    }

    def __init__(self, type=None, dataset_id=None, task_id=None, dataset_name=None, dataset_description=None, is_published=None, overwrite=None, schema_mapping=None, ids=None):
        r"""ImportOpsResultsRequestBody

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 指定导入来源的任务类型。 **约束限制：** 枚举值。 **取值范围：** 字符长度1-100，evaluation-task(评测记录)，datasets-synthesis(合成样本)。 **默认取值：** 不涉及。 
        :type type: str
        :param dataset_id: **参数解释：** 目标评测集的唯一标识符。为空时将触发创建新评测集。 **约束限制：** 1-64个字符。 **取值范围：** 字符长度1-64，已存在的评测集ID。 **默认取值：** 不涉及。 
        :type dataset_id: str
        :param task_id: **参数解释：** 待导入数据所属的源任务ID。 **约束限制：** 1-64个字符。 **取值范围：** 字符长度1-64，合法的任务ID。 **默认取值：** 不涉及。 
        :type task_id: str
        :param dataset_name: **参数解释：** 当 dataset_id 为空时，定义新建评测集的名称。 **约束限制：** 2-100个字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。 
        :type dataset_name: str
        :param dataset_description: **参数解释：** 为新建评测集提供的详细功能或内容描述。 **约束限制：** 0-400个字符。 **取值范围：** 字符长度0-400，任意描述性文本。 **默认取值：** 不涉及。 
        :type dataset_description: str
        :param is_published: **参数解释：** 是否在导入完成后自动发布为一个正式版本。 **约束限制：** 布尔值。 **取值范围：** true(自动发布)，false(存入草稿)。 **默认取值：** false。 
        :type is_published: bool
        :param overwrite: **参数解释：** 当目标评测集已存在数据时，是否清空原有数据再执行导入。 **约束限制：** 布尔值。 **取值范围：** true(全量覆盖)，false(增量追加)。 **默认取值：** false。 
        :type overwrite: bool
        :param schema_mapping: **参数解释：** 字段映射规则列表，定义源字段如何对应到目标评测集字段。 **约束限制：** 数组长度1-100。 **取值范围：** 包含source, target, type的对象。 **默认取值：** 不涉及。 
        :type schema_mapping: list[:class:`huaweicloudsdkagentarts.v1.ImportOpsResultsRequestBodySchemaMapping`]
        :param ids: **参数解释：** 需要执行导入操作的具体条目ID列表，通过数据集列表接口获取。 **约束限制：** 包含1-500个数据项ID。 **取值范围：** 每项1-64个字符。 **默认取值：** 不涉及。 
        :type ids: list[str]
        """
        
        

        self._type = None
        self._dataset_id = None
        self._task_id = None
        self._dataset_name = None
        self._dataset_description = None
        self._is_published = None
        self._overwrite = None
        self._schema_mapping = None
        self._ids = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if task_id is not None:
            self.task_id = task_id
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if dataset_description is not None:
            self.dataset_description = dataset_description
        if is_published is not None:
            self.is_published = is_published
        if overwrite is not None:
            self.overwrite = overwrite
        if schema_mapping is not None:
            self.schema_mapping = schema_mapping
        if ids is not None:
            self.ids = ids

    @property
    def type(self):
        r"""Gets the type of this ImportOpsResultsRequestBody.

        **参数解释：** 指定导入来源的任务类型。 **约束限制：** 枚举值。 **取值范围：** 字符长度1-100，evaluation-task(评测记录)，datasets-synthesis(合成样本)。 **默认取值：** 不涉及。 

        :return: The type of this ImportOpsResultsRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ImportOpsResultsRequestBody.

        **参数解释：** 指定导入来源的任务类型。 **约束限制：** 枚举值。 **取值范围：** 字符长度1-100，evaluation-task(评测记录)，datasets-synthesis(合成样本)。 **默认取值：** 不涉及。 

        :param type: The type of this ImportOpsResultsRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this ImportOpsResultsRequestBody.

        **参数解释：** 目标评测集的唯一标识符。为空时将触发创建新评测集。 **约束限制：** 1-64个字符。 **取值范围：** 字符长度1-64，已存在的评测集ID。 **默认取值：** 不涉及。 

        :return: The dataset_id of this ImportOpsResultsRequestBody.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this ImportOpsResultsRequestBody.

        **参数解释：** 目标评测集的唯一标识符。为空时将触发创建新评测集。 **约束限制：** 1-64个字符。 **取值范围：** 字符长度1-64，已存在的评测集ID。 **默认取值：** 不涉及。 

        :param dataset_id: The dataset_id of this ImportOpsResultsRequestBody.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ImportOpsResultsRequestBody.

        **参数解释：** 待导入数据所属的源任务ID。 **约束限制：** 1-64个字符。 **取值范围：** 字符长度1-64，合法的任务ID。 **默认取值：** 不涉及。 

        :return: The task_id of this ImportOpsResultsRequestBody.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ImportOpsResultsRequestBody.

        **参数解释：** 待导入数据所属的源任务ID。 **约束限制：** 1-64个字符。 **取值范围：** 字符长度1-64，合法的任务ID。 **默认取值：** 不涉及。 

        :param task_id: The task_id of this ImportOpsResultsRequestBody.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def dataset_name(self):
        r"""Gets the dataset_name of this ImportOpsResultsRequestBody.

        **参数解释：** 当 dataset_id 为空时，定义新建评测集的名称。 **约束限制：** 2-100个字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。 

        :return: The dataset_name of this ImportOpsResultsRequestBody.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        r"""Sets the dataset_name of this ImportOpsResultsRequestBody.

        **参数解释：** 当 dataset_id 为空时，定义新建评测集的名称。 **约束限制：** 2-100个字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。 

        :param dataset_name: The dataset_name of this ImportOpsResultsRequestBody.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def dataset_description(self):
        r"""Gets the dataset_description of this ImportOpsResultsRequestBody.

        **参数解释：** 为新建评测集提供的详细功能或内容描述。 **约束限制：** 0-400个字符。 **取值范围：** 字符长度0-400，任意描述性文本。 **默认取值：** 不涉及。 

        :return: The dataset_description of this ImportOpsResultsRequestBody.
        :rtype: str
        """
        return self._dataset_description

    @dataset_description.setter
    def dataset_description(self, dataset_description):
        r"""Sets the dataset_description of this ImportOpsResultsRequestBody.

        **参数解释：** 为新建评测集提供的详细功能或内容描述。 **约束限制：** 0-400个字符。 **取值范围：** 字符长度0-400，任意描述性文本。 **默认取值：** 不涉及。 

        :param dataset_description: The dataset_description of this ImportOpsResultsRequestBody.
        :type dataset_description: str
        """
        self._dataset_description = dataset_description

    @property
    def is_published(self):
        r"""Gets the is_published of this ImportOpsResultsRequestBody.

        **参数解释：** 是否在导入完成后自动发布为一个正式版本。 **约束限制：** 布尔值。 **取值范围：** true(自动发布)，false(存入草稿)。 **默认取值：** false。 

        :return: The is_published of this ImportOpsResultsRequestBody.
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published):
        r"""Sets the is_published of this ImportOpsResultsRequestBody.

        **参数解释：** 是否在导入完成后自动发布为一个正式版本。 **约束限制：** 布尔值。 **取值范围：** true(自动发布)，false(存入草稿)。 **默认取值：** false。 

        :param is_published: The is_published of this ImportOpsResultsRequestBody.
        :type is_published: bool
        """
        self._is_published = is_published

    @property
    def overwrite(self):
        r"""Gets the overwrite of this ImportOpsResultsRequestBody.

        **参数解释：** 当目标评测集已存在数据时，是否清空原有数据再执行导入。 **约束限制：** 布尔值。 **取值范围：** true(全量覆盖)，false(增量追加)。 **默认取值：** false。 

        :return: The overwrite of this ImportOpsResultsRequestBody.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        r"""Sets the overwrite of this ImportOpsResultsRequestBody.

        **参数解释：** 当目标评测集已存在数据时，是否清空原有数据再执行导入。 **约束限制：** 布尔值。 **取值范围：** true(全量覆盖)，false(增量追加)。 **默认取值：** false。 

        :param overwrite: The overwrite of this ImportOpsResultsRequestBody.
        :type overwrite: bool
        """
        self._overwrite = overwrite

    @property
    def schema_mapping(self):
        r"""Gets the schema_mapping of this ImportOpsResultsRequestBody.

        **参数解释：** 字段映射规则列表，定义源字段如何对应到目标评测集字段。 **约束限制：** 数组长度1-100。 **取值范围：** 包含source, target, type的对象。 **默认取值：** 不涉及。 

        :return: The schema_mapping of this ImportOpsResultsRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ImportOpsResultsRequestBodySchemaMapping`]
        """
        return self._schema_mapping

    @schema_mapping.setter
    def schema_mapping(self, schema_mapping):
        r"""Sets the schema_mapping of this ImportOpsResultsRequestBody.

        **参数解释：** 字段映射规则列表，定义源字段如何对应到目标评测集字段。 **约束限制：** 数组长度1-100。 **取值范围：** 包含source, target, type的对象。 **默认取值：** 不涉及。 

        :param schema_mapping: The schema_mapping of this ImportOpsResultsRequestBody.
        :type schema_mapping: list[:class:`huaweicloudsdkagentarts.v1.ImportOpsResultsRequestBodySchemaMapping`]
        """
        self._schema_mapping = schema_mapping

    @property
    def ids(self):
        r"""Gets the ids of this ImportOpsResultsRequestBody.

        **参数解释：** 需要执行导入操作的具体条目ID列表，通过数据集列表接口获取。 **约束限制：** 包含1-500个数据项ID。 **取值范围：** 每项1-64个字符。 **默认取值：** 不涉及。 

        :return: The ids of this ImportOpsResultsRequestBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ImportOpsResultsRequestBody.

        **参数解释：** 需要执行导入操作的具体条目ID列表，通过数据集列表接口获取。 **约束限制：** 包含1-500个数据项ID。 **取值范围：** 每项1-64个字符。 **默认取值：** 不涉及。 

        :param ids: The ids of this ImportOpsResultsRequestBody.
        :type ids: list[str]
        """
        self._ids = ids

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
        if not isinstance(other, ImportOpsResultsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
