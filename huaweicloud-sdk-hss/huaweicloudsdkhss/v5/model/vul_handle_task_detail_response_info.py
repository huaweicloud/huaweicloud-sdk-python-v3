# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHandleTaskDetailResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'asset_value': 'str',
        'vul_id': 'str',
        'vul_name': 'str',
        'handle_status': 'str',
        'failed_reason': 'str',
        'failed_reason_description': 'str',
        'failed_reason_solution': 'str',
        'app_name': 'str',
        'app_version': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'asset_value': 'asset_value',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'handle_status': 'handle_status',
        'failed_reason': 'failed_reason',
        'failed_reason_description': 'failed_reason_description',
        'failed_reason_solution': 'failed_reason_solution',
        'app_name': 'app_name',
        'app_version': 'app_version'
    }

    def __init__(self, host_id=None, host_name=None, public_ip=None, private_ip=None, asset_value=None, vul_id=None, vul_name=None, handle_status=None, failed_reason=None, failed_reason_description=None, failed_reason_solution=None, app_name=None, app_version=None):
        r"""VulHandleTaskDetailResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 主机ID **取值范围**: 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 主机名称 **取值范围**: 字符长度0-256位 
        :type host_name: str
        :param public_ip: **参数解释**: 公网IP **取值范围**: 字符长度0-128位 
        :type public_ip: str
        :param private_ip: **参数解释**: 私网IP **取值范围**: 字符长度0-128位 
        :type private_ip: str
        :param asset_value: **参数解释**: 资产重要性 **取值范围**: - important：重要。 - common：一般。 - test：测试。 
        :type asset_value: str
        :param vul_id: **参数解释**: 漏洞ID **取值范围**: 字符长度1-512位 
        :type vul_id: str
        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 
        :type vul_name: str
        :param handle_status: **参数解释**: 处置状态 **取值范围**: - ready：待执行。 - running：执行中。 - success：处置成功。 - failed：处置失败。 
        :type handle_status: str
        :param failed_reason: **参数解释**: 失败原因 **取值范围**: 字符长度0-512位 
        :type failed_reason: str
        :param failed_reason_description: **参数解释**: 失败原因的业务语言描述 **取值范围**: 字符长度0-512位 
        :type failed_reason_description: str
        :param failed_reason_solution: **参数解释**: 失败原因的解决方案 **取值范围**: 字符长度0-512位 
        :type failed_reason_solution: str
        :param app_name: **参数解释**: 存在漏洞的软件名称 **取值范围**: 字符长度0-128位 
        :type app_name: str
        :param app_version: **参数解释**: 存在漏洞的软件版本 **取值范围**: 字符长度0-128位 
        :type app_version: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._asset_value = None
        self._vul_id = None
        self._vul_name = None
        self._handle_status = None
        self._failed_reason = None
        self._failed_reason_description = None
        self._failed_reason_solution = None
        self._app_name = None
        self._app_version = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if asset_value is not None:
            self.asset_value = asset_value
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if handle_status is not None:
            self.handle_status = handle_status
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if failed_reason_description is not None:
            self.failed_reason_description = failed_reason_description
        if failed_reason_solution is not None:
            self.failed_reason_solution = failed_reason_solution
        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version

    @property
    def host_id(self):
        r"""Gets the host_id of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 主机ID **取值范围**: 字符长度1-64位 

        :return: The host_id of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 主机ID **取值范围**: 字符长度1-64位 

        :param host_id: The host_id of this VulHandleTaskDetailResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 主机名称 **取值范围**: 字符长度0-256位 

        :return: The host_name of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 主机名称 **取值范围**: 字符长度0-256位 

        :param host_name: The host_name of this VulHandleTaskDetailResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 公网IP **取值范围**: 字符长度0-128位 

        :return: The public_ip of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 公网IP **取值范围**: 字符长度0-128位 

        :param public_ip: The public_ip of this VulHandleTaskDetailResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 私网IP **取值范围**: 字符长度0-128位 

        :return: The private_ip of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 私网IP **取值范围**: 字符长度0-128位 

        :param private_ip: The private_ip of this VulHandleTaskDetailResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 资产重要性 **取值范围**: - important：重要。 - common：一般。 - test：测试。 

        :return: The asset_value of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 资产重要性 **取值范围**: - important：重要。 - common：一般。 - test：测试。 

        :param asset_value: The asset_value of this VulHandleTaskDetailResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度1-512位 

        :return: The vul_id of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度1-512位 

        :param vul_id: The vul_id of this VulHandleTaskDetailResponseInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 

        :return: The vul_name of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 

        :param vul_name: The vul_name of this VulHandleTaskDetailResponseInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def handle_status(self):
        r"""Gets the handle_status of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 处置状态 **取值范围**: - ready：待执行。 - running：执行中。 - success：处置成功。 - failed：处置失败。 

        :return: The handle_status of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 处置状态 **取值范围**: - ready：待执行。 - running：执行中。 - success：处置成功。 - failed：处置失败。 

        :param handle_status: The handle_status of this VulHandleTaskDetailResponseInfo.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 失败原因 **取值范围**: 字符长度0-512位 

        :return: The failed_reason of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 失败原因 **取值范围**: 字符长度0-512位 

        :param failed_reason: The failed_reason of this VulHandleTaskDetailResponseInfo.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def failed_reason_description(self):
        r"""Gets the failed_reason_description of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 失败原因的业务语言描述 **取值范围**: 字符长度0-512位 

        :return: The failed_reason_description of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._failed_reason_description

    @failed_reason_description.setter
    def failed_reason_description(self, failed_reason_description):
        r"""Sets the failed_reason_description of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 失败原因的业务语言描述 **取值范围**: 字符长度0-512位 

        :param failed_reason_description: The failed_reason_description of this VulHandleTaskDetailResponseInfo.
        :type failed_reason_description: str
        """
        self._failed_reason_description = failed_reason_description

    @property
    def failed_reason_solution(self):
        r"""Gets the failed_reason_solution of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 失败原因的解决方案 **取值范围**: 字符长度0-512位 

        :return: The failed_reason_solution of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._failed_reason_solution

    @failed_reason_solution.setter
    def failed_reason_solution(self, failed_reason_solution):
        r"""Sets the failed_reason_solution of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 失败原因的解决方案 **取值范围**: 字符长度0-512位 

        :param failed_reason_solution: The failed_reason_solution of this VulHandleTaskDetailResponseInfo.
        :type failed_reason_solution: str
        """
        self._failed_reason_solution = failed_reason_solution

    @property
    def app_name(self):
        r"""Gets the app_name of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 存在漏洞的软件名称 **取值范围**: 字符长度0-128位 

        :return: The app_name of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 存在漏洞的软件名称 **取值范围**: 字符长度0-128位 

        :param app_name: The app_name of this VulHandleTaskDetailResponseInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        r"""Gets the app_version of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 存在漏洞的软件版本 **取值范围**: 字符长度0-128位 

        :return: The app_version of this VulHandleTaskDetailResponseInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this VulHandleTaskDetailResponseInfo.

        **参数解释**: 存在漏洞的软件版本 **取值范围**: 字符长度0-128位 

        :param app_version: The app_version of this VulHandleTaskDetailResponseInfo.
        :type app_version: str
        """
        self._app_version = app_version

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
        if not isinstance(other, VulHandleTaskDetailResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
