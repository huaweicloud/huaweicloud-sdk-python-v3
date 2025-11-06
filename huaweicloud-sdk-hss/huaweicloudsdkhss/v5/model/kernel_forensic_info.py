# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KernelForensicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'read_addr': 'int',
        'syscall_num': 'int',
        'function': 'str',
        'module': 'str',
        'ext_info': 'str'
    }

    attribute_map = {
        'read_addr': 'read_addr',
        'syscall_num': 'syscall_num',
        'function': 'function',
        'module': 'module',
        'ext_info': 'ext_info'
    }

    def __init__(self, read_addr=None, syscall_num=None, function=None, module=None, ext_info=None):
        r"""KernelForensicInfo

        The model defined in huaweicloud sdk

        :param read_addr: **参数解释**： 地址 **取值范围**： 不涉及
        :type read_addr: int
        :param syscall_num: **参数解释**： 系统调用编号 **取值范围**： 不涉及
        :type syscall_num: int
        :param function: **参数解释**： 系统函数 **取值范围**： 不涉及
        :type function: str
        :param module: **参数解释**： 内核模块 **取值范围**： 不涉及
        :type module: str
        :param ext_info: **参数解释**： 扩展信息 **取值范围**： 不涉及
        :type ext_info: str
        """
        
        

        self._read_addr = None
        self._syscall_num = None
        self._function = None
        self._module = None
        self._ext_info = None
        self.discriminator = None

        if read_addr is not None:
            self.read_addr = read_addr
        if syscall_num is not None:
            self.syscall_num = syscall_num
        if function is not None:
            self.function = function
        if module is not None:
            self.module = module
        if ext_info is not None:
            self.ext_info = ext_info

    @property
    def read_addr(self):
        r"""Gets the read_addr of this KernelForensicInfo.

        **参数解释**： 地址 **取值范围**： 不涉及

        :return: The read_addr of this KernelForensicInfo.
        :rtype: int
        """
        return self._read_addr

    @read_addr.setter
    def read_addr(self, read_addr):
        r"""Sets the read_addr of this KernelForensicInfo.

        **参数解释**： 地址 **取值范围**： 不涉及

        :param read_addr: The read_addr of this KernelForensicInfo.
        :type read_addr: int
        """
        self._read_addr = read_addr

    @property
    def syscall_num(self):
        r"""Gets the syscall_num of this KernelForensicInfo.

        **参数解释**： 系统调用编号 **取值范围**： 不涉及

        :return: The syscall_num of this KernelForensicInfo.
        :rtype: int
        """
        return self._syscall_num

    @syscall_num.setter
    def syscall_num(self, syscall_num):
        r"""Sets the syscall_num of this KernelForensicInfo.

        **参数解释**： 系统调用编号 **取值范围**： 不涉及

        :param syscall_num: The syscall_num of this KernelForensicInfo.
        :type syscall_num: int
        """
        self._syscall_num = syscall_num

    @property
    def function(self):
        r"""Gets the function of this KernelForensicInfo.

        **参数解释**： 系统函数 **取值范围**： 不涉及

        :return: The function of this KernelForensicInfo.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        r"""Sets the function of this KernelForensicInfo.

        **参数解释**： 系统函数 **取值范围**： 不涉及

        :param function: The function of this KernelForensicInfo.
        :type function: str
        """
        self._function = function

    @property
    def module(self):
        r"""Gets the module of this KernelForensicInfo.

        **参数解释**： 内核模块 **取值范围**： 不涉及

        :return: The module of this KernelForensicInfo.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this KernelForensicInfo.

        **参数解释**： 内核模块 **取值范围**： 不涉及

        :param module: The module of this KernelForensicInfo.
        :type module: str
        """
        self._module = module

    @property
    def ext_info(self):
        r"""Gets the ext_info of this KernelForensicInfo.

        **参数解释**： 扩展信息 **取值范围**： 不涉及

        :return: The ext_info of this KernelForensicInfo.
        :rtype: str
        """
        return self._ext_info

    @ext_info.setter
    def ext_info(self, ext_info):
        r"""Sets the ext_info of this KernelForensicInfo.

        **参数解释**： 扩展信息 **取值范围**： 不涉及

        :param ext_info: The ext_info of this KernelForensicInfo.
        :type ext_info: str
        """
        self._ext_info = ext_info

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
        if not isinstance(other, KernelForensicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
