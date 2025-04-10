# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NpuUsedInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'module_id': 'str',
        'used_ai_core_num': 'int',
        'used_cpu_core_num': 'int'
    }

    attribute_map = {
        'module_id': 'module_id',
        'used_ai_core_num': 'used_ai_core_num',
        'used_cpu_core_num': 'used_cpu_core_num'
    }

    def __init__(self, module_id=None, used_ai_core_num=None, used_cpu_core_num=None):
        r"""NpuUsedInfoDTO

        The model defined in huaweicloud sdk

        :param module_id: 模块名称
        :type module_id: str
        :param used_ai_core_num: 模块使用AI核的个数
        :type used_ai_core_num: int
        :param used_cpu_core_num: 模块使用NPU芯片中的cpu核数
        :type used_cpu_core_num: int
        """
        
        

        self._module_id = None
        self._used_ai_core_num = None
        self._used_cpu_core_num = None
        self.discriminator = None

        if module_id is not None:
            self.module_id = module_id
        if used_ai_core_num is not None:
            self.used_ai_core_num = used_ai_core_num
        if used_cpu_core_num is not None:
            self.used_cpu_core_num = used_cpu_core_num

    @property
    def module_id(self):
        r"""Gets the module_id of this NpuUsedInfoDTO.

        模块名称

        :return: The module_id of this NpuUsedInfoDTO.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this NpuUsedInfoDTO.

        模块名称

        :param module_id: The module_id of this NpuUsedInfoDTO.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def used_ai_core_num(self):
        r"""Gets the used_ai_core_num of this NpuUsedInfoDTO.

        模块使用AI核的个数

        :return: The used_ai_core_num of this NpuUsedInfoDTO.
        :rtype: int
        """
        return self._used_ai_core_num

    @used_ai_core_num.setter
    def used_ai_core_num(self, used_ai_core_num):
        r"""Sets the used_ai_core_num of this NpuUsedInfoDTO.

        模块使用AI核的个数

        :param used_ai_core_num: The used_ai_core_num of this NpuUsedInfoDTO.
        :type used_ai_core_num: int
        """
        self._used_ai_core_num = used_ai_core_num

    @property
    def used_cpu_core_num(self):
        r"""Gets the used_cpu_core_num of this NpuUsedInfoDTO.

        模块使用NPU芯片中的cpu核数

        :return: The used_cpu_core_num of this NpuUsedInfoDTO.
        :rtype: int
        """
        return self._used_cpu_core_num

    @used_cpu_core_num.setter
    def used_cpu_core_num(self, used_cpu_core_num):
        r"""Sets the used_cpu_core_num of this NpuUsedInfoDTO.

        模块使用NPU芯片中的cpu核数

        :param used_cpu_core_num: The used_cpu_core_num of this NpuUsedInfoDTO.
        :type used_cpu_core_num: int
        """
        self._used_cpu_core_num = used_cpu_core_num

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
        if not isinstance(other, NpuUsedInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
