# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApproverVO:

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
        'approver_name': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'email': 'str',
        'user_type': 'str',
        'phone_number': 'str',
        'create_by': 'str',
        'create_time': 'str',
        'app_name': 'str',
        'topic_urn': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'approver_name': 'approver_name',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'email': 'email',
        'user_type': 'user_type',
        'phone_number': 'phone_number',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'app_name': 'app_name',
        'topic_urn': 'topic_urn',
        'project_id': 'project_id'
    }

    def __init__(self, id=None, approver_name=None, user_id=None, user_name=None, email=None, user_type=None, phone_number=None, create_by=None, create_time=None, app_name=None, topic_urn=None, project_id=None):
        r"""ApproverVO

        The model defined in huaweicloud sdk

        :param id: 审批单ID，ID字符串。
        :type id: str
        :param approver_name: 审批人姓名。
        :type approver_name: str
        :param user_id: 审批人ID。
        :type user_id: str
        :param user_name: 审批人名称。
        :type user_name: str
        :param email: email信息。
        :type email: str
        :param user_type: 用户类型。 枚举值：   - BIZ_METRIC_OWNER: 业务指标责任人   - APPROVER: 审批人   - BIZ_METRIC_OWNER_AND_APPROVER: 业务指标责任人是审核人 
        :type user_type: str
        :param phone_number: 电话号码。
        :type phone_number: str
        :param create_by: 创建人。
        :type create_by: str
        :param create_time: 创建时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: str
        :param app_name: 业务系统名称。
        :type app_name: str
        :param topic_urn: smn主题urn。
        :type topic_urn: str
        :param project_id: 项目ID。
        :type project_id: str
        """
        
        

        self._id = None
        self._approver_name = None
        self._user_id = None
        self._user_name = None
        self._email = None
        self._user_type = None
        self._phone_number = None
        self._create_by = None
        self._create_time = None
        self._app_name = None
        self._topic_urn = None
        self._project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if approver_name is not None:
            self.approver_name = approver_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if email is not None:
            self.email = email
        if user_type is not None:
            self.user_type = user_type
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
        if project_id is not None:
            self.project_id = project_id

    @property
    def id(self):
        r"""Gets the id of this ApproverVO.

        审批单ID，ID字符串。

        :return: The id of this ApproverVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApproverVO.

        审批单ID，ID字符串。

        :param id: The id of this ApproverVO.
        :type id: str
        """
        self._id = id

    @property
    def approver_name(self):
        r"""Gets the approver_name of this ApproverVO.

        审批人姓名。

        :return: The approver_name of this ApproverVO.
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        r"""Sets the approver_name of this ApproverVO.

        审批人姓名。

        :param approver_name: The approver_name of this ApproverVO.
        :type approver_name: str
        """
        self._approver_name = approver_name

    @property
    def user_id(self):
        r"""Gets the user_id of this ApproverVO.

        审批人ID。

        :return: The user_id of this ApproverVO.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ApproverVO.

        审批人ID。

        :param user_id: The user_id of this ApproverVO.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ApproverVO.

        审批人名称。

        :return: The user_name of this ApproverVO.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ApproverVO.

        审批人名称。

        :param user_name: The user_name of this ApproverVO.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def email(self):
        r"""Gets the email of this ApproverVO.

        email信息。

        :return: The email of this ApproverVO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ApproverVO.

        email信息。

        :param email: The email of this ApproverVO.
        :type email: str
        """
        self._email = email

    @property
    def user_type(self):
        r"""Gets the user_type of this ApproverVO.

        用户类型。 枚举值：   - BIZ_METRIC_OWNER: 业务指标责任人   - APPROVER: 审批人   - BIZ_METRIC_OWNER_AND_APPROVER: 业务指标责任人是审核人 

        :return: The user_type of this ApproverVO.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this ApproverVO.

        用户类型。 枚举值：   - BIZ_METRIC_OWNER: 业务指标责任人   - APPROVER: 审批人   - BIZ_METRIC_OWNER_AND_APPROVER: 业务指标责任人是审核人 

        :param user_type: The user_type of this ApproverVO.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def phone_number(self):
        r"""Gets the phone_number of this ApproverVO.

        电话号码。

        :return: The phone_number of this ApproverVO.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        r"""Sets the phone_number of this ApproverVO.

        电话号码。

        :param phone_number: The phone_number of this ApproverVO.
        :type phone_number: str
        """
        self._phone_number = phone_number

    @property
    def create_by(self):
        r"""Gets the create_by of this ApproverVO.

        创建人。

        :return: The create_by of this ApproverVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ApproverVO.

        创建人。

        :param create_by: The create_by of this ApproverVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this ApproverVO.

        创建时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this ApproverVO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ApproverVO.

        创建时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this ApproverVO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def app_name(self):
        r"""Gets the app_name of this ApproverVO.

        业务系统名称。

        :return: The app_name of this ApproverVO.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ApproverVO.

        业务系统名称。

        :param app_name: The app_name of this ApproverVO.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ApproverVO.

        smn主题urn。

        :return: The topic_urn of this ApproverVO.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ApproverVO.

        smn主题urn。

        :param topic_urn: The topic_urn of this ApproverVO.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def project_id(self):
        r"""Gets the project_id of this ApproverVO.

        项目ID。

        :return: The project_id of this ApproverVO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ApproverVO.

        项目ID。

        :param project_id: The project_id of this ApproverVO.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ApproverVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
