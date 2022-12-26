# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Script:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approve_info': 'ApproveInfo',
        'create_by': 'str',
        'create_time': 'int',
        'description': 'str',
        'enterprise_project_id': 'str',
        'id': 'str',
        'name': 'str',
        'online_exist_status': 'bool',
        'online_id': 'str',
        'project_id': 'str',
        'rate_control': 'RateControl',
        'script_language': 'str',
        'update_by': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'approve_info': 'approve_info',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'name': 'name',
        'online_exist_status': 'online_exist_status',
        'online_id': 'online_id',
        'project_id': 'project_id',
        'rate_control': 'rate_control',
        'script_language': 'script_language',
        'update_by': 'update_by',
        'update_time': 'update_time'
    }

    def __init__(self, approve_info=None, create_by=None, create_time=None, description=None, enterprise_project_id=None, id=None, name=None, online_exist_status=None, online_id=None, project_id=None, rate_control=None, script_language=None, update_by=None, update_time=None):
        """Script

        The model defined in huaweicloud sdk

        :param approve_info: 
        :type approve_info: :class:`huaweicloudsdkaom.v1.ApproveInfo`
        :param create_by: 创建人，比如为：张三
        :type create_by: str
        :param create_time: 创建时间
        :type create_time: int
        :param description: 脚本描述，脚本描述,对脚本进行描述，最大长度为1000
        :type description: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param id: 脚本id,根据project_id、脚本名称的和，用guava计算hash(md5)方式获取，比如为：c279d73a0b4e0f0927721e366c736880
        :type id: str
        :param name: 脚本名称，支持数字，下划线，大小写字母 ,中文
        :type name: str
        :param online_exist_status: 脚本中是否有已上线的版本，true表示有已上线的版本，false表示没有已上线的版本
        :type online_exist_status: bool
        :param online_id: 已上线版本id
        :type online_id: str
        :param project_id: 租户从IAM申请到的projectid，一般为32位字符串
        :type project_id: str
        :param rate_control: 
        :type rate_control: :class:`huaweicloudsdkaom.v1.RateControl`
        :param script_language: 脚本语言，目前支持四种，分别是：SHELL BAT PYTHON POWER_SHELL
        :type script_language: str
        :param update_by: 修改人
        :type update_by: str
        :param update_time: 实体的最后更新时间戳。 注意：执行创建/修改/删除操作时，update_time将更新。
        :type update_time: int
        """
        
        

        self._approve_info = None
        self._create_by = None
        self._create_time = None
        self._description = None
        self._enterprise_project_id = None
        self._id = None
        self._name = None
        self._online_exist_status = None
        self._online_id = None
        self._project_id = None
        self._rate_control = None
        self._script_language = None
        self._update_by = None
        self._update_time = None
        self.discriminator = None

        if approve_info is not None:
            self.approve_info = approve_info
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        self.name = name
        if online_exist_status is not None:
            self.online_exist_status = online_exist_status
        if online_id is not None:
            self.online_id = online_id
        if project_id is not None:
            self.project_id = project_id
        if rate_control is not None:
            self.rate_control = rate_control
        self.script_language = script_language
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time

    @property
    def approve_info(self):
        """Gets the approve_info of this Script.

        :return: The approve_info of this Script.
        :rtype: :class:`huaweicloudsdkaom.v1.ApproveInfo`
        """
        return self._approve_info

    @approve_info.setter
    def approve_info(self, approve_info):
        """Sets the approve_info of this Script.

        :param approve_info: The approve_info of this Script.
        :type approve_info: :class:`huaweicloudsdkaom.v1.ApproveInfo`
        """
        self._approve_info = approve_info

    @property
    def create_by(self):
        """Gets the create_by of this Script.

        创建人，比如为：张三

        :return: The create_by of this Script.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this Script.

        创建人，比如为：张三

        :param create_by: The create_by of this Script.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        """Gets the create_time of this Script.

        创建时间

        :return: The create_time of this Script.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Script.

        创建时间

        :param create_time: The create_time of this Script.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this Script.

        脚本描述，脚本描述,对脚本进行描述，最大长度为1000

        :return: The description of this Script.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Script.

        脚本描述，脚本描述,对脚本进行描述，最大长度为1000

        :param description: The description of this Script.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Script.

        企业项目id

        :return: The enterprise_project_id of this Script.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Script.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this Script.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this Script.

        脚本id,根据project_id、脚本名称的和，用guava计算hash(md5)方式获取，比如为：c279d73a0b4e0f0927721e366c736880

        :return: The id of this Script.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Script.

        脚本id,根据project_id、脚本名称的和，用guava计算hash(md5)方式获取，比如为：c279d73a0b4e0f0927721e366c736880

        :param id: The id of this Script.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Script.

        脚本名称，支持数字，下划线，大小写字母 ,中文

        :return: The name of this Script.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Script.

        脚本名称，支持数字，下划线，大小写字母 ,中文

        :param name: The name of this Script.
        :type name: str
        """
        self._name = name

    @property
    def online_exist_status(self):
        """Gets the online_exist_status of this Script.

        脚本中是否有已上线的版本，true表示有已上线的版本，false表示没有已上线的版本

        :return: The online_exist_status of this Script.
        :rtype: bool
        """
        return self._online_exist_status

    @online_exist_status.setter
    def online_exist_status(self, online_exist_status):
        """Sets the online_exist_status of this Script.

        脚本中是否有已上线的版本，true表示有已上线的版本，false表示没有已上线的版本

        :param online_exist_status: The online_exist_status of this Script.
        :type online_exist_status: bool
        """
        self._online_exist_status = online_exist_status

    @property
    def online_id(self):
        """Gets the online_id of this Script.

        已上线版本id

        :return: The online_id of this Script.
        :rtype: str
        """
        return self._online_id

    @online_id.setter
    def online_id(self, online_id):
        """Sets the online_id of this Script.

        已上线版本id

        :param online_id: The online_id of this Script.
        :type online_id: str
        """
        self._online_id = online_id

    @property
    def project_id(self):
        """Gets the project_id of this Script.

        租户从IAM申请到的projectid，一般为32位字符串

        :return: The project_id of this Script.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Script.

        租户从IAM申请到的projectid，一般为32位字符串

        :param project_id: The project_id of this Script.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def rate_control(self):
        """Gets the rate_control of this Script.

        :return: The rate_control of this Script.
        :rtype: :class:`huaweicloudsdkaom.v1.RateControl`
        """
        return self._rate_control

    @rate_control.setter
    def rate_control(self, rate_control):
        """Sets the rate_control of this Script.

        :param rate_control: The rate_control of this Script.
        :type rate_control: :class:`huaweicloudsdkaom.v1.RateControl`
        """
        self._rate_control = rate_control

    @property
    def script_language(self):
        """Gets the script_language of this Script.

        脚本语言，目前支持四种，分别是：SHELL BAT PYTHON POWER_SHELL

        :return: The script_language of this Script.
        :rtype: str
        """
        return self._script_language

    @script_language.setter
    def script_language(self, script_language):
        """Sets the script_language of this Script.

        脚本语言，目前支持四种，分别是：SHELL BAT PYTHON POWER_SHELL

        :param script_language: The script_language of this Script.
        :type script_language: str
        """
        self._script_language = script_language

    @property
    def update_by(self):
        """Gets the update_by of this Script.

        修改人

        :return: The update_by of this Script.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this Script.

        修改人

        :param update_by: The update_by of this Script.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        """Gets the update_time of this Script.

        实体的最后更新时间戳。 注意：执行创建/修改/删除操作时，update_time将更新。

        :return: The update_time of this Script.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Script.

        实体的最后更新时间戳。 注意：执行创建/修改/删除操作时，update_time将更新。

        :param update_time: The update_time of this Script.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, Script):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
