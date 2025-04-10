# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NPUDetailsDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'npu_type': 'str',
        'product_name': 'str',
        'ai_core': 'int',
        'health': 'str',
        'error_msg': 'str',
        'used_info': 'list[NpuUsedInfoDTO]'
    }

    attribute_map = {
        'device_id': 'device_id',
        'npu_type': 'npu_type',
        'product_name': 'product_name',
        'ai_core': 'ai_core',
        'health': 'health',
        'error_msg': 'error_msg',
        'used_info': 'used_info'
    }

    def __init__(self, device_id=None, npu_type=None, product_name=None, ai_core=None, health=None, error_msg=None, used_info=None):
        r"""NPUDetailsDTO

        The model defined in huaweicloud sdk

        :param device_id: 昇腾设备ID
        :type device_id: str
        :param npu_type: 华为AI加速卡型号，如D310推理卡、D310P推理卡、D910训练卡。
        :type npu_type: str
        :param product_name: 昇腾设备产品类型
        :type product_name: str
        :param ai_core: AI加速卡包含ai核个数
        :type ai_core: int
        :param health: 昇腾设备健康状态
        :type health: str
        :param error_msg: 昇腾设备故障信息
        :type error_msg: str
        :param used_info: NPU使用信息
        :type used_info: list[:class:`huaweicloudsdkiotedge.v2.NpuUsedInfoDTO`]
        """
        
        

        self._device_id = None
        self._npu_type = None
        self._product_name = None
        self._ai_core = None
        self._health = None
        self._error_msg = None
        self._used_info = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if npu_type is not None:
            self.npu_type = npu_type
        if product_name is not None:
            self.product_name = product_name
        if ai_core is not None:
            self.ai_core = ai_core
        if health is not None:
            self.health = health
        if error_msg is not None:
            self.error_msg = error_msg
        if used_info is not None:
            self.used_info = used_info

    @property
    def device_id(self):
        r"""Gets the device_id of this NPUDetailsDTO.

        昇腾设备ID

        :return: The device_id of this NPUDetailsDTO.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this NPUDetailsDTO.

        昇腾设备ID

        :param device_id: The device_id of this NPUDetailsDTO.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def npu_type(self):
        r"""Gets the npu_type of this NPUDetailsDTO.

        华为AI加速卡型号，如D310推理卡、D310P推理卡、D910训练卡。

        :return: The npu_type of this NPUDetailsDTO.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        r"""Sets the npu_type of this NPUDetailsDTO.

        华为AI加速卡型号，如D310推理卡、D310P推理卡、D910训练卡。

        :param npu_type: The npu_type of this NPUDetailsDTO.
        :type npu_type: str
        """
        self._npu_type = npu_type

    @property
    def product_name(self):
        r"""Gets the product_name of this NPUDetailsDTO.

        昇腾设备产品类型

        :return: The product_name of this NPUDetailsDTO.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this NPUDetailsDTO.

        昇腾设备产品类型

        :param product_name: The product_name of this NPUDetailsDTO.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def ai_core(self):
        r"""Gets the ai_core of this NPUDetailsDTO.

        AI加速卡包含ai核个数

        :return: The ai_core of this NPUDetailsDTO.
        :rtype: int
        """
        return self._ai_core

    @ai_core.setter
    def ai_core(self, ai_core):
        r"""Sets the ai_core of this NPUDetailsDTO.

        AI加速卡包含ai核个数

        :param ai_core: The ai_core of this NPUDetailsDTO.
        :type ai_core: int
        """
        self._ai_core = ai_core

    @property
    def health(self):
        r"""Gets the health of this NPUDetailsDTO.

        昇腾设备健康状态

        :return: The health of this NPUDetailsDTO.
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this NPUDetailsDTO.

        昇腾设备健康状态

        :param health: The health of this NPUDetailsDTO.
        :type health: str
        """
        self._health = health

    @property
    def error_msg(self):
        r"""Gets the error_msg of this NPUDetailsDTO.

        昇腾设备故障信息

        :return: The error_msg of this NPUDetailsDTO.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this NPUDetailsDTO.

        昇腾设备故障信息

        :param error_msg: The error_msg of this NPUDetailsDTO.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def used_info(self):
        r"""Gets the used_info of this NPUDetailsDTO.

        NPU使用信息

        :return: The used_info of this NPUDetailsDTO.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.NpuUsedInfoDTO`]
        """
        return self._used_info

    @used_info.setter
    def used_info(self, used_info):
        r"""Sets the used_info of this NPUDetailsDTO.

        NPU使用信息

        :param used_info: The used_info of this NPUDetailsDTO.
        :type used_info: list[:class:`huaweicloudsdkiotedge.v2.NpuUsedInfoDTO`]
        """
        self._used_info = used_info

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
        if not isinstance(other, NPUDetailsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
