# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApproverListApprovers:

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
        'email': 'str',
        'department': 'str',
        'description': 'str',
        'character': 'str',
        'approver_name': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'phone_number': 'str',
        'create_by': 'str',
        'create_time': 'int',
        'app_name': 'str',
        'topic_urn': 'str',
        'template_id': 'str',
        'project_id': 'str',
        'approver_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'department': 'department',
        'description': 'description',
        'character': 'character',
        'approver_name': 'approver_name',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'phone_number': 'phone_number',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'app_name': 'app_name',
        'topic_urn': 'topic_urn',
        'template_id': 'template_id',
        'project_id': 'project_id',
        'approver_type': 'approver_type'
    }

    def __init__(self, id=None, email=None, department=None, description=None, character=None, approver_name=None, user_id=None, user_name=None, phone_number=None, create_by=None, create_time=None, app_name=None, topic_urn=None, template_id=None, project_id=None, approver_type=None):
        r"""ApproverListApprovers

        The model defined in huaweicloud sdk

        :param id: 审核人ID
        :type id: str
        :param email: 邮箱
        :type email: str
        :param department: 部门
        :type department: str
        :param description: 描述信息
        :type description: str
        :param character: 角色
        :type character: str
        :param approver_name: 审核人名字
        :type approver_name: str
        :param user_id: 用户ID
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param phone_number: 电话号码
        :type phone_number: str
        :param create_by: 创建人
        :type create_by: str
        :param create_time: 创建时间
        :type create_time: int
        :param app_name: APP名称
        :type app_name: str
        :param topic_urn: 主题URN
        :type topic_urn: str
        :param template_id: 模板ID
        :type template_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param approver_type: 审核人类型
        :type approver_type: int
        """
        
        

        self._id = None
        self._email = None
        self._department = None
        self._description = None
        self._character = None
        self._approver_name = None
        self._user_id = None
        self._user_name = None
        self._phone_number = None
        self._create_by = None
        self._create_time = None
        self._app_name = None
        self._topic_urn = None
        self._template_id = None
        self._project_id = None
        self._approver_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if department is not None:
            self.department = department
        if description is not None:
            self.description = description
        if character is not None:
            self.character = character
        if approver_name is not None:
            self.approver_name = approver_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if phone_number is not None:
            self.phone_number = phone_number
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if app_name is not None:
            self.app_name = app_name
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if template_id is not None:
            self.template_id = template_id
        if project_id is not None:
            self.project_id = project_id
        if approver_type is not None:
            self.approver_type = approver_type

    @property
    def id(self):
        r"""Gets the id of this ApproverListApprovers.

        审核人ID

        :return: The id of this ApproverListApprovers.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApproverListApprovers.

        审核人ID

        :param id: The id of this ApproverListApprovers.
        :type id: str
        """
        self._id = id

    @property
    def email(self):
        r"""Gets the email of this ApproverListApprovers.

        邮箱

        :return: The email of this ApproverListApprovers.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ApproverListApprovers.

        邮箱

        :param email: The email of this ApproverListApprovers.
        :type email: str
        """
        self._email = email

    @property
    def department(self):
        r"""Gets the department of this ApproverListApprovers.

        部门

        :return: The department of this ApproverListApprovers.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        r"""Sets the department of this ApproverListApprovers.

        部门

        :param department: The department of this ApproverListApprovers.
        :type department: str
        """
        self._department = department

    @property
    def description(self):
        r"""Gets the description of this ApproverListApprovers.

        描述信息

        :return: The description of this ApproverListApprovers.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ApproverListApprovers.

        描述信息

        :param description: The description of this ApproverListApprovers.
        :type description: str
        """
        self._description = description

    @property
    def character(self):
        r"""Gets the character of this ApproverListApprovers.

        角色

        :return: The character of this ApproverListApprovers.
        :rtype: str
        """
        return self._character

    @character.setter
    def character(self, character):
        r"""Sets the character of this ApproverListApprovers.

        角色

        :param character: The character of this ApproverListApprovers.
        :type character: str
        """
        self._character = character

    @property
    def approver_name(self):
        r"""Gets the approver_name of this ApproverListApprovers.

        审核人名字

        :return: The approver_name of this ApproverListApprovers.
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        r"""Sets the approver_name of this ApproverListApprovers.

        审核人名字

        :param approver_name: The approver_name of this ApproverListApprovers.
        :type approver_name: str
        """
        self._approver_name = approver_name

    @property
    def user_id(self):
        r"""Gets the user_id of this ApproverListApprovers.

        用户ID

        :return: The user_id of this ApproverListApprovers.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ApproverListApprovers.

        用户ID

        :param user_id: The user_id of this ApproverListApprovers.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ApproverListApprovers.

        用户名

        :return: The user_name of this ApproverListApprovers.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ApproverListApprovers.

        用户名

        :param user_name: The user_name of this ApproverListApprovers.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def phone_number(self):
        r"""Gets the phone_number of this ApproverListApprovers.

        电话号码

        :return: The phone_number of this ApproverListApprovers.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        r"""Sets the phone_number of this ApproverListApprovers.

        电话号码

        :param phone_number: The phone_number of this ApproverListApprovers.
        :type phone_number: str
        """
        self._phone_number = phone_number

    @property
    def create_by(self):
        r"""Gets the create_by of this ApproverListApprovers.

        创建人

        :return: The create_by of this ApproverListApprovers.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ApproverListApprovers.

        创建人

        :param create_by: The create_by of this ApproverListApprovers.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this ApproverListApprovers.

        创建时间

        :return: The create_time of this ApproverListApprovers.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ApproverListApprovers.

        创建时间

        :param create_time: The create_time of this ApproverListApprovers.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def app_name(self):
        r"""Gets the app_name of this ApproverListApprovers.

        APP名称

        :return: The app_name of this ApproverListApprovers.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ApproverListApprovers.

        APP名称

        :param app_name: The app_name of this ApproverListApprovers.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ApproverListApprovers.

        主题URN

        :return: The topic_urn of this ApproverListApprovers.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ApproverListApprovers.

        主题URN

        :param topic_urn: The topic_urn of this ApproverListApprovers.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def template_id(self):
        r"""Gets the template_id of this ApproverListApprovers.

        模板ID

        :return: The template_id of this ApproverListApprovers.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ApproverListApprovers.

        模板ID

        :param template_id: The template_id of this ApproverListApprovers.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ApproverListApprovers.

        项目ID

        :return: The project_id of this ApproverListApprovers.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ApproverListApprovers.

        项目ID

        :param project_id: The project_id of this ApproverListApprovers.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def approver_type(self):
        r"""Gets the approver_type of this ApproverListApprovers.

        审核人类型

        :return: The approver_type of this ApproverListApprovers.
        :rtype: int
        """
        return self._approver_type

    @approver_type.setter
    def approver_type(self, approver_type):
        r"""Sets the approver_type of this ApproverListApprovers.

        审核人类型

        :param approver_type: The approver_type of this ApproverListApprovers.
        :type approver_type: int
        """
        self._approver_type = approver_type

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
        if not isinstance(other, ApproverListApprovers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
