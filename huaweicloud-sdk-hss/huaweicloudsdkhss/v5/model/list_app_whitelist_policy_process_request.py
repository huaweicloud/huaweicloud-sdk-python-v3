# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppWhitelistPolicyProcessRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'policy_id': 'str',
        'process_status': 'str',
        'process_type': 'str',
        'process_name': 'str',
        'process_hash': 'str',
        'process_path': 'str',
        'handle_status': 'str',
        'os_type': 'str',
        'file_signer': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'policy_id': 'policy_id',
        'process_status': 'process_status',
        'process_type': 'process_type',
        'process_name': 'process_name',
        'process_hash': 'process_hash',
        'process_path': 'process_path',
        'handle_status': 'handle_status',
        'os_type': 'os_type',
        'file_signer': 'file_signer'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, policy_id=None, process_status=None, process_type=None, process_name=None, process_hash=None, process_path=None, handle_status=None, os_type=None, file_signer=None):
        r"""ListAppWhitelistPolicyProcessRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param policy_id: **参数解释**： 策略ID **约束限制**： 必填 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 
        :type policy_id: str
        :param process_status: **参数解释**： 信任状态 **约束限制**: 不涉及 **取值范围**: - trust：可信 - suspicious：可疑 - malicious：未知 - unknown：未知  **默认取值**: 不涉及 
        :type process_status: str
        :param process_type: **参数解释**： 进程类型 **约束限制**: 不涉及 **取值范围**: - system：系统程序 - interpretive：解释类程序 - normal：普通可执行程序  **默认取值**: 不涉及 
        :type process_type: str
        :param process_name: **参数解释**： 进程名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type process_name: str
        :param process_hash: **参数解释**： 进程hash **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type process_hash: str
        :param process_path: **参数解释**： 进程路径 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type process_path: str
        :param handle_status: **参数解释**： 确认状态 **约束限制**: 不涉及 **取值范围**: - confirmed：已确认 - unconfirmed：未确认  **默认取值**: 不涉及 
        :type handle_status: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux：Linux。   - Windows：Windows。
        :type os_type: str
        :param file_signer: **参数解释**： 文件签名 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type file_signer: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._policy_id = None
        self._process_status = None
        self._process_type = None
        self._process_name = None
        self._process_hash = None
        self._process_path = None
        self._handle_status = None
        self._os_type = None
        self._file_signer = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        self.policy_id = policy_id
        if process_status is not None:
            self.process_status = process_status
        if process_type is not None:
            self.process_type = process_type
        if process_name is not None:
            self.process_name = process_name
        if process_hash is not None:
            self.process_hash = process_hash
        if process_path is not None:
            self.process_path = process_path
        if handle_status is not None:
            self.handle_status = handle_status
        if os_type is not None:
            self.os_type = os_type
        if file_signer is not None:
            self.file_signer = file_signer

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAppWhitelistPolicyProcessRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListAppWhitelistPolicyProcessRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListAppWhitelistPolicyProcessRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAppWhitelistPolicyProcessRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAppWhitelistPolicyProcessRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 策略ID **约束限制**： 必填 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :return: The policy_id of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 策略ID **约束限制**： 必填 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :param policy_id: The policy_id of this ListAppWhitelistPolicyProcessRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def process_status(self):
        r"""Gets the process_status of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 信任状态 **约束限制**: 不涉及 **取值范围**: - trust：可信 - suspicious：可疑 - malicious：未知 - unknown：未知  **默认取值**: 不涉及 

        :return: The process_status of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 信任状态 **约束限制**: 不涉及 **取值范围**: - trust：可信 - suspicious：可疑 - malicious：未知 - unknown：未知  **默认取值**: 不涉及 

        :param process_status: The process_status of this ListAppWhitelistPolicyProcessRequest.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def process_type(self):
        r"""Gets the process_type of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 进程类型 **约束限制**: 不涉及 **取值范围**: - system：系统程序 - interpretive：解释类程序 - normal：普通可执行程序  **默认取值**: 不涉及 

        :return: The process_type of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        r"""Sets the process_type of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 进程类型 **约束限制**: 不涉及 **取值范围**: - system：系统程序 - interpretive：解释类程序 - normal：普通可执行程序  **默认取值**: 不涉及 

        :param process_type: The process_type of this ListAppWhitelistPolicyProcessRequest.
        :type process_type: str
        """
        self._process_type = process_type

    @property
    def process_name(self):
        r"""Gets the process_name of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 进程名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The process_name of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        r"""Sets the process_name of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 进程名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param process_name: The process_name of this ListAppWhitelistPolicyProcessRequest.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def process_hash(self):
        r"""Gets the process_hash of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 进程hash **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The process_hash of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._process_hash

    @process_hash.setter
    def process_hash(self, process_hash):
        r"""Sets the process_hash of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 进程hash **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param process_hash: The process_hash of this ListAppWhitelistPolicyProcessRequest.
        :type process_hash: str
        """
        self._process_hash = process_hash

    @property
    def process_path(self):
        r"""Gets the process_path of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 进程路径 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The process_path of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        r"""Sets the process_path of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 进程路径 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param process_path: The process_path of this ListAppWhitelistPolicyProcessRequest.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 确认状态 **约束限制**: 不涉及 **取值范围**: - confirmed：已确认 - unconfirmed：未确认  **默认取值**: 不涉及 

        :return: The handle_status of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 确认状态 **约束限制**: 不涉及 **取值范围**: - confirmed：已确认 - unconfirmed：未确认  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ListAppWhitelistPolicyProcessRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def os_type(self):
        r"""Gets the os_type of this ListAppWhitelistPolicyProcessRequest.

        操作系统类型，包含如下2种。   - Linux：Linux。   - Windows：Windows。

        :return: The os_type of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListAppWhitelistPolicyProcessRequest.

        操作系统类型，包含如下2种。   - Linux：Linux。   - Windows：Windows。

        :param os_type: The os_type of this ListAppWhitelistPolicyProcessRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def file_signer(self):
        r"""Gets the file_signer of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 文件签名 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The file_signer of this ListAppWhitelistPolicyProcessRequest.
        :rtype: str
        """
        return self._file_signer

    @file_signer.setter
    def file_signer(self, file_signer):
        r"""Sets the file_signer of this ListAppWhitelistPolicyProcessRequest.

        **参数解释**： 文件签名 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param file_signer: The file_signer of this ListAppWhitelistPolicyProcessRequest.
        :type file_signer: str
        """
        self._file_signer = file_signer

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
        if not isinstance(other, ListAppWhitelistPolicyProcessRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
