# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCbcOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'change_mode': 'int',
        'is_auto_pay': 'int',
        'cloud_service_type': 'str',
        'project_id': 'str',
        'resource_id': 'str',
        'product_info': 'UpdateCbcOrderRequestBodyProductInfo'
    }

    attribute_map = {
        'change_mode': 'change_mode',
        'is_auto_pay': 'is_auto_pay',
        'cloud_service_type': 'cloud_service_type',
        'project_id': 'project_id',
        'resource_id': 'resource_id',
        'product_info': 'product_info'
    }

    def __init__(self, change_mode=None, is_auto_pay=None, cloud_service_type=None, project_id=None, resource_id=None, product_info=None):
        r"""UpdateCbcOrderRequestBody

        The model defined in huaweicloud sdk

        :param change_mode: change_mode
        :type change_mode: int
        :param is_auto_pay: 该请求参数为预留参数，当前不支持自动支付，使用接口时该参数请使用0 0：不自动支付 1：自动支付
        :type is_auto_pay: int
        :param cloud_service_type: 发起规格变更操作的云服务类型
        :type cloud_service_type: str
        :param project_id: project_id
        :type project_id: str
        :param resource_id: 资源标识ID
        :type resource_id: str
        :param product_info: 
        :type product_info: :class:`huaweicloudsdkcodeartsinspector.v2.UpdateCbcOrderRequestBodyProductInfo`
        """
        
        

        self._change_mode = None
        self._is_auto_pay = None
        self._cloud_service_type = None
        self._project_id = None
        self._resource_id = None
        self._product_info = None
        self.discriminator = None

        self.change_mode = change_mode
        self.is_auto_pay = is_auto_pay
        self.cloud_service_type = cloud_service_type
        self.project_id = project_id
        self.resource_id = resource_id
        self.product_info = product_info

    @property
    def change_mode(self):
        r"""Gets the change_mode of this UpdateCbcOrderRequestBody.

        change_mode

        :return: The change_mode of this UpdateCbcOrderRequestBody.
        :rtype: int
        """
        return self._change_mode

    @change_mode.setter
    def change_mode(self, change_mode):
        r"""Sets the change_mode of this UpdateCbcOrderRequestBody.

        change_mode

        :param change_mode: The change_mode of this UpdateCbcOrderRequestBody.
        :type change_mode: int
        """
        self._change_mode = change_mode

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this UpdateCbcOrderRequestBody.

        该请求参数为预留参数，当前不支持自动支付，使用接口时该参数请使用0 0：不自动支付 1：自动支付

        :return: The is_auto_pay of this UpdateCbcOrderRequestBody.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this UpdateCbcOrderRequestBody.

        该请求参数为预留参数，当前不支持自动支付，使用接口时该参数请使用0 0：不自动支付 1：自动支付

        :param is_auto_pay: The is_auto_pay of this UpdateCbcOrderRequestBody.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this UpdateCbcOrderRequestBody.

        发起规格变更操作的云服务类型

        :return: The cloud_service_type of this UpdateCbcOrderRequestBody.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this UpdateCbcOrderRequestBody.

        发起规格变更操作的云服务类型

        :param cloud_service_type: The cloud_service_type of this UpdateCbcOrderRequestBody.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateCbcOrderRequestBody.

        project_id

        :return: The project_id of this UpdateCbcOrderRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateCbcOrderRequestBody.

        project_id

        :param project_id: The project_id of this UpdateCbcOrderRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this UpdateCbcOrderRequestBody.

        资源标识ID

        :return: The resource_id of this UpdateCbcOrderRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this UpdateCbcOrderRequestBody.

        资源标识ID

        :param resource_id: The resource_id of this UpdateCbcOrderRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def product_info(self):
        r"""Gets the product_info of this UpdateCbcOrderRequestBody.

        :return: The product_info of this UpdateCbcOrderRequestBody.
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v2.UpdateCbcOrderRequestBodyProductInfo`
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        r"""Sets the product_info of this UpdateCbcOrderRequestBody.

        :param product_info: The product_info of this UpdateCbcOrderRequestBody.
        :type product_info: :class:`huaweicloudsdkcodeartsinspector.v2.UpdateCbcOrderRequestBodyProductInfo`
        """
        self._product_info = product_info

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
        if not isinstance(other, UpdateCbcOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
