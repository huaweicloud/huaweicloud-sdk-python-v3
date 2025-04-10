# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetChargeModesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'product_type': 'str',
        'effective_time': 'int',
        'create_time': 'int',
        'service_area': 'str',
        'status': 'str'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'product_type': 'product_type',
        'effective_time': 'effective_time',
        'create_time': 'create_time',
        'service_area': 'service_area',
        'status': 'status'
    }

    def __init__(self, charge_mode=None, product_type=None, effective_time=None, create_time=None, service_area=None, status=None):
        r"""SetChargeModesResponse

        The model defined in huaweicloud sdk

        :param charge_mode: 账号的计费模式
        :type charge_mode: str
        :param product_type: 加速类型
        :type product_type: str
        :param effective_time: 该模式生效时间
        :type effective_time: int
        :param create_time: 创建时间
        :type create_time: int
        :param service_area: 该模式的区域
        :type service_area: str
        :param status: 状态,首次开通状态为active,之后修改为upcoming
        :type status: str
        """
        
        super(SetChargeModesResponse, self).__init__()

        self._charge_mode = None
        self._product_type = None
        self._effective_time = None
        self._create_time = None
        self._service_area = None
        self._status = None
        self.discriminator = None

        if charge_mode is not None:
            self.charge_mode = charge_mode
        if product_type is not None:
            self.product_type = product_type
        if effective_time is not None:
            self.effective_time = effective_time
        if create_time is not None:
            self.create_time = create_time
        if service_area is not None:
            self.service_area = service_area
        if status is not None:
            self.status = status

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this SetChargeModesResponse.

        账号的计费模式

        :return: The charge_mode of this SetChargeModesResponse.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this SetChargeModesResponse.

        账号的计费模式

        :param charge_mode: The charge_mode of this SetChargeModesResponse.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def product_type(self):
        r"""Gets the product_type of this SetChargeModesResponse.

        加速类型

        :return: The product_type of this SetChargeModesResponse.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this SetChargeModesResponse.

        加速类型

        :param product_type: The product_type of this SetChargeModesResponse.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def effective_time(self):
        r"""Gets the effective_time of this SetChargeModesResponse.

        该模式生效时间

        :return: The effective_time of this SetChargeModesResponse.
        :rtype: int
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this SetChargeModesResponse.

        该模式生效时间

        :param effective_time: The effective_time of this SetChargeModesResponse.
        :type effective_time: int
        """
        self._effective_time = effective_time

    @property
    def create_time(self):
        r"""Gets the create_time of this SetChargeModesResponse.

        创建时间

        :return: The create_time of this SetChargeModesResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SetChargeModesResponse.

        创建时间

        :param create_time: The create_time of this SetChargeModesResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def service_area(self):
        r"""Gets the service_area of this SetChargeModesResponse.

        该模式的区域

        :return: The service_area of this SetChargeModesResponse.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        r"""Sets the service_area of this SetChargeModesResponse.

        该模式的区域

        :param service_area: The service_area of this SetChargeModesResponse.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def status(self):
        r"""Gets the status of this SetChargeModesResponse.

        状态,首次开通状态为active,之后修改为upcoming

        :return: The status of this SetChargeModesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SetChargeModesResponse.

        状态,首次开通状态为active,之后修改为upcoming

        :param status: The status of this SetChargeModesResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, SetChargeModesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
