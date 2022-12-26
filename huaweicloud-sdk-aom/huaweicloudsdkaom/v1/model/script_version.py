# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'create_by': 'str',
        'create_time': 'int',
        'enterprise_project_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'reference_number': 'int',
        'script_id': 'str',
        'script_language': 'str',
        'status_desc': 'int',
        'update_by': 'str',
        'update_time': 'int',
        'version_id': 'str',
        'version_number': 'str',
        'script_reference': 'list[ScriptReferenceDetail]'
    }

    attribute_map = {
        'content': 'content',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'project_id': 'project_id',
        'reference_number': 'reference_number',
        'script_id': 'script_id',
        'script_language': 'script_language',
        'status_desc': 'status_desc',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'version_id': 'version_id',
        'version_number': 'version_number',
        'script_reference': 'script_reference'
    }

    def __init__(self, content=None, create_by=None, create_time=None, enterprise_project_id=None, name=None, project_id=None, reference_number=None, script_id=None, script_language=None, status_desc=None, update_by=None, update_time=None, version_id=None, version_number=None, script_reference=None):
        """ScriptVersion

        The model defined in huaweicloud sdk

        :param content: 脚本内容，脚本内容不能为空
        :type content: str
        :param create_by: 创建人，比如为：张三
        :type create_by: str
        :param create_time: 创建时间
        :type create_time: int
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param name: 脚本名称，支持数字，下划线，大小写字母 ,中文
        :type name: str
        :param project_id: 租户从IAM申请到的projectid，一般为32位字符串
        :type project_id: str
        :param reference_number: 脚本引用次数，脚本被任务和模板引用的次数。默认是0次,引用次数未非负整数，不能出现负数
        :type reference_number: int
        :param script_id: 版本所在的脚本id,根据project_id、脚本名称的和，用guava计算hash(md5)方式获取，比如为：d648c682ef5750f700c050b41692b2b8
        :type script_id: str
        :param script_language: 脚本语言，目前支持四种，分别是：SHELL BAT PYTHON POWER_SHELL
        :type script_language: str
        :param status_desc: 状态说明  0代表 未上线，1代表已上线  2代表已下线   3代表已禁用
        :type status_desc: int
        :param update_by: 修改人
        :type update_by: str
        :param update_time: 实体的最后更新时间戳。 注意：执行创建/修补/删除操作时，update_time将更新。
        :type update_time: int
        :param version_id: 版本id，唯一标识，根据project_id、脚本名称、脚本版本号的和，用guava计算hash(md5)方式获取，比如为：d648c682ef5750f700c050b41692b2b8
        :type version_id: str
        :param version_number: 脚本版本号，支持数字，下划线，大小写字母和小数点
        :type version_number: str
        :param script_reference: 脚本引用详情
        :type script_reference: list[:class:`huaweicloudsdkaom.v1.ScriptReferenceDetail`]
        """
        
        

        self._content = None
        self._create_by = None
        self._create_time = None
        self._enterprise_project_id = None
        self._name = None
        self._project_id = None
        self._reference_number = None
        self._script_id = None
        self._script_language = None
        self._status_desc = None
        self._update_by = None
        self._update_time = None
        self._version_id = None
        self._version_number = None
        self._script_reference = None
        self.discriminator = None

        self.content = content
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if reference_number is not None:
            self.reference_number = reference_number
        if script_id is not None:
            self.script_id = script_id
        if script_language is not None:
            self.script_language = script_language
        if status_desc is not None:
            self.status_desc = status_desc
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time
        if version_id is not None:
            self.version_id = version_id
        if version_number is not None:
            self.version_number = version_number
        if script_reference is not None:
            self.script_reference = script_reference

    @property
    def content(self):
        """Gets the content of this ScriptVersion.

        脚本内容，脚本内容不能为空

        :return: The content of this ScriptVersion.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ScriptVersion.

        脚本内容，脚本内容不能为空

        :param content: The content of this ScriptVersion.
        :type content: str
        """
        self._content = content

    @property
    def create_by(self):
        """Gets the create_by of this ScriptVersion.

        创建人，比如为：张三

        :return: The create_by of this ScriptVersion.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this ScriptVersion.

        创建人，比如为：张三

        :param create_by: The create_by of this ScriptVersion.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        """Gets the create_time of this ScriptVersion.

        创建时间

        :return: The create_time of this ScriptVersion.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScriptVersion.

        创建时间

        :param create_time: The create_time of this ScriptVersion.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ScriptVersion.

        企业项目id

        :return: The enterprise_project_id of this ScriptVersion.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ScriptVersion.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ScriptVersion.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this ScriptVersion.

        脚本名称，支持数字，下划线，大小写字母 ,中文

        :return: The name of this ScriptVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScriptVersion.

        脚本名称，支持数字，下划线，大小写字母 ,中文

        :param name: The name of this ScriptVersion.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this ScriptVersion.

        租户从IAM申请到的projectid，一般为32位字符串

        :return: The project_id of this ScriptVersion.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ScriptVersion.

        租户从IAM申请到的projectid，一般为32位字符串

        :param project_id: The project_id of this ScriptVersion.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def reference_number(self):
        """Gets the reference_number of this ScriptVersion.

        脚本引用次数，脚本被任务和模板引用的次数。默认是0次,引用次数未非负整数，不能出现负数

        :return: The reference_number of this ScriptVersion.
        :rtype: int
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this ScriptVersion.

        脚本引用次数，脚本被任务和模板引用的次数。默认是0次,引用次数未非负整数，不能出现负数

        :param reference_number: The reference_number of this ScriptVersion.
        :type reference_number: int
        """
        self._reference_number = reference_number

    @property
    def script_id(self):
        """Gets the script_id of this ScriptVersion.

        版本所在的脚本id,根据project_id、脚本名称的和，用guava计算hash(md5)方式获取，比如为：d648c682ef5750f700c050b41692b2b8

        :return: The script_id of this ScriptVersion.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this ScriptVersion.

        版本所在的脚本id,根据project_id、脚本名称的和，用guava计算hash(md5)方式获取，比如为：d648c682ef5750f700c050b41692b2b8

        :param script_id: The script_id of this ScriptVersion.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def script_language(self):
        """Gets the script_language of this ScriptVersion.

        脚本语言，目前支持四种，分别是：SHELL BAT PYTHON POWER_SHELL

        :return: The script_language of this ScriptVersion.
        :rtype: str
        """
        return self._script_language

    @script_language.setter
    def script_language(self, script_language):
        """Sets the script_language of this ScriptVersion.

        脚本语言，目前支持四种，分别是：SHELL BAT PYTHON POWER_SHELL

        :param script_language: The script_language of this ScriptVersion.
        :type script_language: str
        """
        self._script_language = script_language

    @property
    def status_desc(self):
        """Gets the status_desc of this ScriptVersion.

        状态说明  0代表 未上线，1代表已上线  2代表已下线   3代表已禁用

        :return: The status_desc of this ScriptVersion.
        :rtype: int
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        """Sets the status_desc of this ScriptVersion.

        状态说明  0代表 未上线，1代表已上线  2代表已下线   3代表已禁用

        :param status_desc: The status_desc of this ScriptVersion.
        :type status_desc: int
        """
        self._status_desc = status_desc

    @property
    def update_by(self):
        """Gets the update_by of this ScriptVersion.

        修改人

        :return: The update_by of this ScriptVersion.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this ScriptVersion.

        修改人

        :param update_by: The update_by of this ScriptVersion.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        """Gets the update_time of this ScriptVersion.

        实体的最后更新时间戳。 注意：执行创建/修补/删除操作时，update_time将更新。

        :return: The update_time of this ScriptVersion.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ScriptVersion.

        实体的最后更新时间戳。 注意：执行创建/修补/删除操作时，update_time将更新。

        :param update_time: The update_time of this ScriptVersion.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def version_id(self):
        """Gets the version_id of this ScriptVersion.

        版本id，唯一标识，根据project_id、脚本名称、脚本版本号的和，用guava计算hash(md5)方式获取，比如为：d648c682ef5750f700c050b41692b2b8

        :return: The version_id of this ScriptVersion.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ScriptVersion.

        版本id，唯一标识，根据project_id、脚本名称、脚本版本号的和，用guava计算hash(md5)方式获取，比如为：d648c682ef5750f700c050b41692b2b8

        :param version_id: The version_id of this ScriptVersion.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def version_number(self):
        """Gets the version_number of this ScriptVersion.

        脚本版本号，支持数字，下划线，大小写字母和小数点

        :return: The version_number of this ScriptVersion.
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this ScriptVersion.

        脚本版本号，支持数字，下划线，大小写字母和小数点

        :param version_number: The version_number of this ScriptVersion.
        :type version_number: str
        """
        self._version_number = version_number

    @property
    def script_reference(self):
        """Gets the script_reference of this ScriptVersion.

        脚本引用详情

        :return: The script_reference of this ScriptVersion.
        :rtype: list[:class:`huaweicloudsdkaom.v1.ScriptReferenceDetail`]
        """
        return self._script_reference

    @script_reference.setter
    def script_reference(self, script_reference):
        """Sets the script_reference of this ScriptVersion.

        脚本引用详情

        :param script_reference: The script_reference of this ScriptVersion.
        :type script_reference: list[:class:`huaweicloudsdkaom.v1.ScriptReferenceDetail`]
        """
        self._script_reference = script_reference

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
        if not isinstance(other, ScriptVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
