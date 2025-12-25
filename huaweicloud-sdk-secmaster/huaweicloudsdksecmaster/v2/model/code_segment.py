# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CodeSegment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code_segment_id': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'code_segment_name': 'str',
        'description': 'str',
        'code': 'str',
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'code_segment_id': 'code_segment_id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'code_segment_name': 'code_segment_name',
        'description': 'description',
        'code': 'code',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'update_time': 'update_time'
    }

    def __init__(self, code_segment_id=None, project_id=None, workspace_id=None, code_segment_name=None, description=None, code=None, create_by=None, create_time=None, update_by=None, update_time=None):
        r"""CodeSegment

        The model defined in huaweicloud sdk

        :param code_segment_id: UUID
        :type code_segment_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param code_segment_name: 代码段名称
        :type code_segment_name: str
        :param description: 代码段描述信息
        :type description: str
        :param code: 代码片段
        :type code: str
        :param create_by: Iam用户ID
        :type create_by: str
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param update_by: Iam用户ID
        :type update_by: str
        :param update_time: 毫秒时间戳
        :type update_time: int
        """
        
        

        self._code_segment_id = None
        self._project_id = None
        self._workspace_id = None
        self._code_segment_name = None
        self._description = None
        self._code = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._update_time = None
        self.discriminator = None

        if code_segment_id is not None:
            self.code_segment_id = code_segment_id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if code_segment_name is not None:
            self.code_segment_name = code_segment_name
        if description is not None:
            self.description = description
        if code is not None:
            self.code = code
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time

    @property
    def code_segment_id(self):
        r"""Gets the code_segment_id of this CodeSegment.

        UUID

        :return: The code_segment_id of this CodeSegment.
        :rtype: str
        """
        return self._code_segment_id

    @code_segment_id.setter
    def code_segment_id(self, code_segment_id):
        r"""Sets the code_segment_id of this CodeSegment.

        UUID

        :param code_segment_id: The code_segment_id of this CodeSegment.
        :type code_segment_id: str
        """
        self._code_segment_id = code_segment_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CodeSegment.

        项目ID

        :return: The project_id of this CodeSegment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CodeSegment.

        项目ID

        :param project_id: The project_id of this CodeSegment.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CodeSegment.

        工作空间ID

        :return: The workspace_id of this CodeSegment.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CodeSegment.

        工作空间ID

        :param workspace_id: The workspace_id of this CodeSegment.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def code_segment_name(self):
        r"""Gets the code_segment_name of this CodeSegment.

        代码段名称

        :return: The code_segment_name of this CodeSegment.
        :rtype: str
        """
        return self._code_segment_name

    @code_segment_name.setter
    def code_segment_name(self, code_segment_name):
        r"""Sets the code_segment_name of this CodeSegment.

        代码段名称

        :param code_segment_name: The code_segment_name of this CodeSegment.
        :type code_segment_name: str
        """
        self._code_segment_name = code_segment_name

    @property
    def description(self):
        r"""Gets the description of this CodeSegment.

        代码段描述信息

        :return: The description of this CodeSegment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CodeSegment.

        代码段描述信息

        :param description: The description of this CodeSegment.
        :type description: str
        """
        self._description = description

    @property
    def code(self):
        r"""Gets the code of this CodeSegment.

        代码片段

        :return: The code of this CodeSegment.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CodeSegment.

        代码片段

        :param code: The code of this CodeSegment.
        :type code: str
        """
        self._code = code

    @property
    def create_by(self):
        r"""Gets the create_by of this CodeSegment.

        Iam用户ID

        :return: The create_by of this CodeSegment.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this CodeSegment.

        Iam用户ID

        :param create_by: The create_by of this CodeSegment.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this CodeSegment.

        毫秒时间戳

        :return: The create_time of this CodeSegment.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CodeSegment.

        毫秒时间戳

        :param create_time: The create_time of this CodeSegment.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        r"""Gets the update_by of this CodeSegment.

        Iam用户ID

        :return: The update_by of this CodeSegment.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this CodeSegment.

        Iam用户ID

        :param update_by: The update_by of this CodeSegment.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this CodeSegment.

        毫秒时间戳

        :return: The update_time of this CodeSegment.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CodeSegment.

        毫秒时间戳

        :param update_time: The update_time of this CodeSegment.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, CodeSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
