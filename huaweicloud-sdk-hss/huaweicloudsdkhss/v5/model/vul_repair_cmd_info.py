# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulRepairCmdInfo:

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
        'vul_name': 'str',
        'vul_id': 'str',
        'repair_cmd': 'str',
        'image_name': 'str',
        'image_id': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'asset_value': 'asset_value',
        'vul_name': 'vul_name',
        'vul_id': 'vul_id',
        'repair_cmd': 'repair_cmd',
        'image_name': 'image_name',
        'image_id': 'image_id'
    }

    def __init__(self, host_id=None, host_name=None, public_ip=None, private_ip=None, asset_value=None, vul_name=None, vul_id=None, repair_cmd=None, image_name=None, image_id=None):
        r"""VulRepairCmdInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 主机ID **取值范围**: 字符长度1-128 
        :type host_id: str
        :param host_name: **参数解释**: 主机名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param public_ip: **参数解释**: 服务器公网IP **取值范围**: 字符长度0-128 
        :type public_ip: str
        :param private_ip: **参数解释**: 服务器私网IP **取值范围**: 字符长度0-128 
        :type private_ip: str
        :param asset_value: **参数解释**: 主机的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 
        :type asset_value: str
        :param vul_name: **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 
        :type vul_name: str
        :param vul_id: **参数解释**: 漏洞ID **取值范围**: 字符长度0-64位 
        :type vul_id: str
        :param repair_cmd: **参数解释**: 修复命令行 **取值范围**: 字符范围1-256位 
        :type repair_cmd: str
        :param image_name: **参数解释**: 关联镜像名称 **取值范围**: 字符范围1-256位 
        :type image_name: str
        :param image_id: **参数解释**: 关联镜像ID **取值范围**: 字符范围1-256位 
        :type image_id: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._asset_value = None
        self._vul_name = None
        self._vul_id = None
        self._repair_cmd = None
        self._image_name = None
        self._image_id = None
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
        if vul_name is not None:
            self.vul_name = vul_name
        if vul_id is not None:
            self.vul_id = vul_id
        if repair_cmd is not None:
            self.repair_cmd = repair_cmd
        if image_name is not None:
            self.image_name = image_name
        if image_id is not None:
            self.image_id = image_id

    @property
    def host_id(self):
        r"""Gets the host_id of this VulRepairCmdInfo.

        **参数解释**: 主机ID **取值范围**: 字符长度1-128 

        :return: The host_id of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this VulRepairCmdInfo.

        **参数解释**: 主机ID **取值范围**: 字符长度1-128 

        :param host_id: The host_id of this VulRepairCmdInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this VulRepairCmdInfo.

        **参数解释**: 主机名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulRepairCmdInfo.

        **参数解释**: 主机名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this VulRepairCmdInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this VulRepairCmdInfo.

        **参数解释**: 服务器公网IP **取值范围**: 字符长度0-128 

        :return: The public_ip of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this VulRepairCmdInfo.

        **参数解释**: 服务器公网IP **取值范围**: 字符长度0-128 

        :param public_ip: The public_ip of this VulRepairCmdInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this VulRepairCmdInfo.

        **参数解释**: 服务器私网IP **取值范围**: 字符长度0-128 

        :return: The private_ip of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this VulRepairCmdInfo.

        **参数解释**: 服务器私网IP **取值范围**: 字符长度0-128 

        :param private_ip: The private_ip of this VulRepairCmdInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this VulRepairCmdInfo.

        **参数解释**: 主机的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 

        :return: The asset_value of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this VulRepairCmdInfo.

        **参数解释**: 主机的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 

        :param asset_value: The asset_value of this VulRepairCmdInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def vul_name(self):
        r"""Gets the vul_name of this VulRepairCmdInfo.

        **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 

        :return: The vul_name of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this VulRepairCmdInfo.

        **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 

        :param vul_name: The vul_name of this VulRepairCmdInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulRepairCmdInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度0-64位 

        :return: The vul_id of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulRepairCmdInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度0-64位 

        :param vul_id: The vul_id of this VulRepairCmdInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def repair_cmd(self):
        r"""Gets the repair_cmd of this VulRepairCmdInfo.

        **参数解释**: 修复命令行 **取值范围**: 字符范围1-256位 

        :return: The repair_cmd of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._repair_cmd

    @repair_cmd.setter
    def repair_cmd(self, repair_cmd):
        r"""Sets the repair_cmd of this VulRepairCmdInfo.

        **参数解释**: 修复命令行 **取值范围**: 字符范围1-256位 

        :param repair_cmd: The repair_cmd of this VulRepairCmdInfo.
        :type repair_cmd: str
        """
        self._repair_cmd = repair_cmd

    @property
    def image_name(self):
        r"""Gets the image_name of this VulRepairCmdInfo.

        **参数解释**: 关联镜像名称 **取值范围**: 字符范围1-256位 

        :return: The image_name of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this VulRepairCmdInfo.

        **参数解释**: 关联镜像名称 **取值范围**: 字符范围1-256位 

        :param image_name: The image_name of this VulRepairCmdInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_id(self):
        r"""Gets the image_id of this VulRepairCmdInfo.

        **参数解释**: 关联镜像ID **取值范围**: 字符范围1-256位 

        :return: The image_id of this VulRepairCmdInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this VulRepairCmdInfo.

        **参数解释**: 关联镜像ID **取值范围**: 字符范围1-256位 

        :param image_id: The image_id of this VulRepairCmdInfo.
        :type image_id: str
        """
        self._image_id = image_id

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
        if not isinstance(other, VulRepairCmdInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
