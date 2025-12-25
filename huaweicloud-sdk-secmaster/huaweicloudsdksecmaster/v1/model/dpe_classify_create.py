# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DpeClassifyCreate:

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
        'project_id': 'str',
        'workspace_id': 'str',
        'dataclass_id': 'str',
        'dataclass_name': 'str',
        'mapping_id': 'str',
        'direct_classifier': 'object',
        'direct_classifier_type_id': 'str',
        'create_time': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'update_time': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'mapping_info': 'DpeInfo',
        'classifier_item_list': 'list[DpeClassifyItemDetail]'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'dataclass_id': 'dataclass_id',
        'dataclass_name': 'dataclass_name',
        'mapping_id': 'mapping_id',
        'direct_classifier': 'direct_classifier',
        'direct_classifier_type_id': 'direct_classifier_type_id',
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'update_time': 'update_time',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'mapping_info': 'mapping_info',
        'classifier_item_list': 'classifier_item_list'
    }

    def __init__(self, id=None, project_id=None, workspace_id=None, dataclass_id=None, dataclass_name=None, mapping_id=None, direct_classifier=None, direct_classifier_type_id=None, create_time=None, creator_id=None, creator_name=None, update_time=None, modifier_id=None, modifier_name=None, mapping_info=None, classifier_item_list=None):
        r"""DpeClassifyCreate

        The model defined in huaweicloud sdk

        :param id: 映射id
        :type id: str
        :param project_id: 映射id
        :type project_id: str
        :param workspace_id: 映射id
        :type workspace_id: str
        :param dataclass_id: 映射id
        :type dataclass_id: str
        :param dataclass_name: 数据类名称
        :type dataclass_name: str
        :param mapping_id: 映射id
        :type mapping_id: str
        :param direct_classifier: 分类方式
        :type direct_classifier: object
        :param direct_classifier_type_id: 映射id
        :type direct_classifier_type_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator_id: 创建者id
        :type creator_id: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param update_time: 更新时间
        :type update_time: str
        :param modifier_id: 修改者id
        :type modifier_id: str
        :param modifier_name: 修改者名称
        :type modifier_name: str
        :param mapping_info: 
        :type mapping_info: :class:`huaweicloudsdksecmaster.v1.DpeInfo`
        :param classifier_item_list: 分类集合元素
        :type classifier_item_list: list[:class:`huaweicloudsdksecmaster.v1.DpeClassifyItemDetail`]
        """
        
        

        self._id = None
        self._project_id = None
        self._workspace_id = None
        self._dataclass_id = None
        self._dataclass_name = None
        self._mapping_id = None
        self._direct_classifier = None
        self._direct_classifier_type_id = None
        self._create_time = None
        self._creator_id = None
        self._creator_name = None
        self._update_time = None
        self._modifier_id = None
        self._modifier_name = None
        self._mapping_info = None
        self._classifier_item_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if mapping_id is not None:
            self.mapping_id = mapping_id
        if direct_classifier is not None:
            self.direct_classifier = direct_classifier
        if direct_classifier_type_id is not None:
            self.direct_classifier_type_id = direct_classifier_type_id
        if create_time is not None:
            self.create_time = create_time
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if update_time is not None:
            self.update_time = update_time
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if mapping_info is not None:
            self.mapping_info = mapping_info
        if classifier_item_list is not None:
            self.classifier_item_list = classifier_item_list

    @property
    def id(self):
        r"""Gets the id of this DpeClassifyCreate.

        映射id

        :return: The id of this DpeClassifyCreate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DpeClassifyCreate.

        映射id

        :param id: The id of this DpeClassifyCreate.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this DpeClassifyCreate.

        映射id

        :return: The project_id of this DpeClassifyCreate.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DpeClassifyCreate.

        映射id

        :param project_id: The project_id of this DpeClassifyCreate.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DpeClassifyCreate.

        映射id

        :return: The workspace_id of this DpeClassifyCreate.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DpeClassifyCreate.

        映射id

        :param workspace_id: The workspace_id of this DpeClassifyCreate.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this DpeClassifyCreate.

        映射id

        :return: The dataclass_id of this DpeClassifyCreate.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this DpeClassifyCreate.

        映射id

        :param dataclass_id: The dataclass_id of this DpeClassifyCreate.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def dataclass_name(self):
        r"""Gets the dataclass_name of this DpeClassifyCreate.

        数据类名称

        :return: The dataclass_name of this DpeClassifyCreate.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        r"""Sets the dataclass_name of this DpeClassifyCreate.

        数据类名称

        :param dataclass_name: The dataclass_name of this DpeClassifyCreate.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def mapping_id(self):
        r"""Gets the mapping_id of this DpeClassifyCreate.

        映射id

        :return: The mapping_id of this DpeClassifyCreate.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        r"""Sets the mapping_id of this DpeClassifyCreate.

        映射id

        :param mapping_id: The mapping_id of this DpeClassifyCreate.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

    @property
    def direct_classifier(self):
        r"""Gets the direct_classifier of this DpeClassifyCreate.

        分类方式

        :return: The direct_classifier of this DpeClassifyCreate.
        :rtype: object
        """
        return self._direct_classifier

    @direct_classifier.setter
    def direct_classifier(self, direct_classifier):
        r"""Sets the direct_classifier of this DpeClassifyCreate.

        分类方式

        :param direct_classifier: The direct_classifier of this DpeClassifyCreate.
        :type direct_classifier: object
        """
        self._direct_classifier = direct_classifier

    @property
    def direct_classifier_type_id(self):
        r"""Gets the direct_classifier_type_id of this DpeClassifyCreate.

        映射id

        :return: The direct_classifier_type_id of this DpeClassifyCreate.
        :rtype: str
        """
        return self._direct_classifier_type_id

    @direct_classifier_type_id.setter
    def direct_classifier_type_id(self, direct_classifier_type_id):
        r"""Sets the direct_classifier_type_id of this DpeClassifyCreate.

        映射id

        :param direct_classifier_type_id: The direct_classifier_type_id of this DpeClassifyCreate.
        :type direct_classifier_type_id: str
        """
        self._direct_classifier_type_id = direct_classifier_type_id

    @property
    def create_time(self):
        r"""Gets the create_time of this DpeClassifyCreate.

        创建时间

        :return: The create_time of this DpeClassifyCreate.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DpeClassifyCreate.

        创建时间

        :param create_time: The create_time of this DpeClassifyCreate.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        r"""Gets the creator_id of this DpeClassifyCreate.

        创建者id

        :return: The creator_id of this DpeClassifyCreate.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this DpeClassifyCreate.

        创建者id

        :param creator_id: The creator_id of this DpeClassifyCreate.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this DpeClassifyCreate.

        创建者名称

        :return: The creator_name of this DpeClassifyCreate.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this DpeClassifyCreate.

        创建者名称

        :param creator_name: The creator_name of this DpeClassifyCreate.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def update_time(self):
        r"""Gets the update_time of this DpeClassifyCreate.

        更新时间

        :return: The update_time of this DpeClassifyCreate.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DpeClassifyCreate.

        更新时间

        :param update_time: The update_time of this DpeClassifyCreate.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this DpeClassifyCreate.

        修改者id

        :return: The modifier_id of this DpeClassifyCreate.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this DpeClassifyCreate.

        修改者id

        :param modifier_id: The modifier_id of this DpeClassifyCreate.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this DpeClassifyCreate.

        修改者名称

        :return: The modifier_name of this DpeClassifyCreate.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this DpeClassifyCreate.

        修改者名称

        :param modifier_name: The modifier_name of this DpeClassifyCreate.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def mapping_info(self):
        r"""Gets the mapping_info of this DpeClassifyCreate.

        :return: The mapping_info of this DpeClassifyCreate.
        :rtype: :class:`huaweicloudsdksecmaster.v1.DpeInfo`
        """
        return self._mapping_info

    @mapping_info.setter
    def mapping_info(self, mapping_info):
        r"""Sets the mapping_info of this DpeClassifyCreate.

        :param mapping_info: The mapping_info of this DpeClassifyCreate.
        :type mapping_info: :class:`huaweicloudsdksecmaster.v1.DpeInfo`
        """
        self._mapping_info = mapping_info

    @property
    def classifier_item_list(self):
        r"""Gets the classifier_item_list of this DpeClassifyCreate.

        分类集合元素

        :return: The classifier_item_list of this DpeClassifyCreate.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.DpeClassifyItemDetail`]
        """
        return self._classifier_item_list

    @classifier_item_list.setter
    def classifier_item_list(self, classifier_item_list):
        r"""Sets the classifier_item_list of this DpeClassifyCreate.

        分类集合元素

        :param classifier_item_list: The classifier_item_list of this DpeClassifyCreate.
        :type classifier_item_list: list[:class:`huaweicloudsdksecmaster.v1.DpeClassifyItemDetail`]
        """
        self._classifier_item_list = classifier_item_list

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
        if not isinstance(other, DpeClassifyCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
