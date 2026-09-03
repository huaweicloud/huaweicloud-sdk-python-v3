# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseBasicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_template': 'AlertTemplate',
        'case_type': 'int',
        'executor_type': 'str',
        'id': 'str',
        'is_forbidden': 'bool',
        'name': 'str',
        'number': 'str',
        'project_update_time': 'int',
        'script_project_name': 'str',
        'state': 'int',
        'svn_script_path': 'str',
        'tmss_version_uri': 'str'
    }

    attribute_map = {
        'alert_template': 'alert_template',
        'case_type': 'caseType',
        'executor_type': 'executor_type',
        'id': 'id',
        'is_forbidden': 'is_forbidden',
        'name': 'name',
        'number': 'number',
        'project_update_time': 'project_update_time',
        'script_project_name': 'scriptProjectName',
        'state': 'state',
        'svn_script_path': 'svn_script_path',
        'tmss_version_uri': 'tmssVersionUri'
    }

    def __init__(self, alert_template=None, case_type=None, executor_type=None, id=None, is_forbidden=None, name=None, number=None, project_update_time=None, script_project_name=None, state=None, svn_script_path=None, tmss_version_uri=None):
        r"""TestCaseBasicInfo

        The model defined in huaweicloud sdk

        :param alert_template: 
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        :param case_type: tmss用例类型
        :type case_type: int
        :param executor_type: 执行机类型
        :type executor_type: str
        :param id: 用例id
        :type id: str
        :param is_forbidden: 是否收藏
        :type is_forbidden: bool
        :param name: 用例id
        :type name: str
        :param number: 用例编号
        :type number: str
        :param project_update_time: 用例包更新时间
        :type project_update_time: int
        :param script_project_name: 用例包名
        :type script_project_name: str
        :param state: 用例状态
        :type state: int
        :param svn_script_path: svn脚本路径
        :type svn_script_path: str
        :param tmss_version_uri: tmss版本地址
        :type tmss_version_uri: str
        """
        
        

        self._alert_template = None
        self._case_type = None
        self._executor_type = None
        self._id = None
        self._is_forbidden = None
        self._name = None
        self._number = None
        self._project_update_time = None
        self._script_project_name = None
        self._state = None
        self._svn_script_path = None
        self._tmss_version_uri = None
        self.discriminator = None

        if alert_template is not None:
            self.alert_template = alert_template
        if case_type is not None:
            self.case_type = case_type
        if executor_type is not None:
            self.executor_type = executor_type
        if id is not None:
            self.id = id
        if is_forbidden is not None:
            self.is_forbidden = is_forbidden
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if project_update_time is not None:
            self.project_update_time = project_update_time
        if script_project_name is not None:
            self.script_project_name = script_project_name
        if state is not None:
            self.state = state
        if svn_script_path is not None:
            self.svn_script_path = svn_script_path
        if tmss_version_uri is not None:
            self.tmss_version_uri = tmss_version_uri

    @property
    def alert_template(self):
        r"""Gets the alert_template of this TestCaseBasicInfo.

        :return: The alert_template of this TestCaseBasicInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        return self._alert_template

    @alert_template.setter
    def alert_template(self, alert_template):
        r"""Sets the alert_template of this TestCaseBasicInfo.

        :param alert_template: The alert_template of this TestCaseBasicInfo.
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        self._alert_template = alert_template

    @property
    def case_type(self):
        r"""Gets the case_type of this TestCaseBasicInfo.

        tmss用例类型

        :return: The case_type of this TestCaseBasicInfo.
        :rtype: int
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        r"""Sets the case_type of this TestCaseBasicInfo.

        tmss用例类型

        :param case_type: The case_type of this TestCaseBasicInfo.
        :type case_type: int
        """
        self._case_type = case_type

    @property
    def executor_type(self):
        r"""Gets the executor_type of this TestCaseBasicInfo.

        执行机类型

        :return: The executor_type of this TestCaseBasicInfo.
        :rtype: str
        """
        return self._executor_type

    @executor_type.setter
    def executor_type(self, executor_type):
        r"""Sets the executor_type of this TestCaseBasicInfo.

        执行机类型

        :param executor_type: The executor_type of this TestCaseBasicInfo.
        :type executor_type: str
        """
        self._executor_type = executor_type

    @property
    def id(self):
        r"""Gets the id of this TestCaseBasicInfo.

        用例id

        :return: The id of this TestCaseBasicInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TestCaseBasicInfo.

        用例id

        :param id: The id of this TestCaseBasicInfo.
        :type id: str
        """
        self._id = id

    @property
    def is_forbidden(self):
        r"""Gets the is_forbidden of this TestCaseBasicInfo.

        是否收藏

        :return: The is_forbidden of this TestCaseBasicInfo.
        :rtype: bool
        """
        return self._is_forbidden

    @is_forbidden.setter
    def is_forbidden(self, is_forbidden):
        r"""Sets the is_forbidden of this TestCaseBasicInfo.

        是否收藏

        :param is_forbidden: The is_forbidden of this TestCaseBasicInfo.
        :type is_forbidden: bool
        """
        self._is_forbidden = is_forbidden

    @property
    def name(self):
        r"""Gets the name of this TestCaseBasicInfo.

        用例id

        :return: The name of this TestCaseBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TestCaseBasicInfo.

        用例id

        :param name: The name of this TestCaseBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def number(self):
        r"""Gets the number of this TestCaseBasicInfo.

        用例编号

        :return: The number of this TestCaseBasicInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this TestCaseBasicInfo.

        用例编号

        :param number: The number of this TestCaseBasicInfo.
        :type number: str
        """
        self._number = number

    @property
    def project_update_time(self):
        r"""Gets the project_update_time of this TestCaseBasicInfo.

        用例包更新时间

        :return: The project_update_time of this TestCaseBasicInfo.
        :rtype: int
        """
        return self._project_update_time

    @project_update_time.setter
    def project_update_time(self, project_update_time):
        r"""Sets the project_update_time of this TestCaseBasicInfo.

        用例包更新时间

        :param project_update_time: The project_update_time of this TestCaseBasicInfo.
        :type project_update_time: int
        """
        self._project_update_time = project_update_time

    @property
    def script_project_name(self):
        r"""Gets the script_project_name of this TestCaseBasicInfo.

        用例包名

        :return: The script_project_name of this TestCaseBasicInfo.
        :rtype: str
        """
        return self._script_project_name

    @script_project_name.setter
    def script_project_name(self, script_project_name):
        r"""Sets the script_project_name of this TestCaseBasicInfo.

        用例包名

        :param script_project_name: The script_project_name of this TestCaseBasicInfo.
        :type script_project_name: str
        """
        self._script_project_name = script_project_name

    @property
    def state(self):
        r"""Gets the state of this TestCaseBasicInfo.

        用例状态

        :return: The state of this TestCaseBasicInfo.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TestCaseBasicInfo.

        用例状态

        :param state: The state of this TestCaseBasicInfo.
        :type state: int
        """
        self._state = state

    @property
    def svn_script_path(self):
        r"""Gets the svn_script_path of this TestCaseBasicInfo.

        svn脚本路径

        :return: The svn_script_path of this TestCaseBasicInfo.
        :rtype: str
        """
        return self._svn_script_path

    @svn_script_path.setter
    def svn_script_path(self, svn_script_path):
        r"""Sets the svn_script_path of this TestCaseBasicInfo.

        svn脚本路径

        :param svn_script_path: The svn_script_path of this TestCaseBasicInfo.
        :type svn_script_path: str
        """
        self._svn_script_path = svn_script_path

    @property
    def tmss_version_uri(self):
        r"""Gets the tmss_version_uri of this TestCaseBasicInfo.

        tmss版本地址

        :return: The tmss_version_uri of this TestCaseBasicInfo.
        :rtype: str
        """
        return self._tmss_version_uri

    @tmss_version_uri.setter
    def tmss_version_uri(self, tmss_version_uri):
        r"""Sets the tmss_version_uri of this TestCaseBasicInfo.

        tmss版本地址

        :param tmss_version_uri: The tmss_version_uri of this TestCaseBasicInfo.
        :type tmss_version_uri: str
        """
        self._tmss_version_uri = tmss_version_uri

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
        if not isinstance(other, TestCaseBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
