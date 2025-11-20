# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceByInstanceIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'enterprise_project_id': 'str',
        'version': 'str',
        'expire_time': 'int',
        'create_time': 'int',
        'current_time': 'int',
        'product_spec_data': 'ProductSpecData',
        'instance_config': 'InstanceConfig',
        'elastic_service_bw_update_enable': 'bool'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'enterprise_project_id': 'enterprise_project_id',
        'version': 'version',
        'expire_time': 'expire_time',
        'create_time': 'create_time',
        'current_time': 'current_time',
        'product_spec_data': 'product_spec_data',
        'instance_config': 'instance_config',
        'elastic_service_bw_update_enable': 'elastic_service_bw_update_enable'
    }

    def __init__(self, instance_name=None, enterprise_project_id=None, version=None, expire_time=None, create_time=None, current_time=None, product_spec_data=None, instance_config=None, elastic_service_bw_update_enable=None):
        r"""ShowInstanceByInstanceIdResponse

        The model defined in huaweicloud sdk

        :param instance_name: 实例名称
        :type instance_name: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param version: 版本
        :type version: str
        :param expire_time: 过期时间
        :type expire_time: int
        :param create_time: 创建时间
        :type create_time: int
        :param current_time: 当前时间
        :type current_time: int
        :param product_spec_data: 
        :type product_spec_data: :class:`huaweicloudsdkaad.v2.ProductSpecData`
        :param instance_config: 
        :type instance_config: :class:`huaweicloudsdkaad.v2.InstanceConfig`
        :param elastic_service_bw_update_enable: 弹性业务带宽是否可更新
        :type elastic_service_bw_update_enable: bool
        """
        
        super().__init__()

        self._instance_name = None
        self._enterprise_project_id = None
        self._version = None
        self._expire_time = None
        self._create_time = None
        self._current_time = None
        self._product_spec_data = None
        self._instance_config = None
        self._elastic_service_bw_update_enable = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if version is not None:
            self.version = version
        if expire_time is not None:
            self.expire_time = expire_time
        if create_time is not None:
            self.create_time = create_time
        if current_time is not None:
            self.current_time = current_time
        if product_spec_data is not None:
            self.product_spec_data = product_spec_data
        if instance_config is not None:
            self.instance_config = instance_config
        if elastic_service_bw_update_enable is not None:
            self.elastic_service_bw_update_enable = elastic_service_bw_update_enable

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowInstanceByInstanceIdResponse.

        实例名称

        :return: The instance_name of this ShowInstanceByInstanceIdResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowInstanceByInstanceIdResponse.

        实例名称

        :param instance_name: The instance_name of this ShowInstanceByInstanceIdResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowInstanceByInstanceIdResponse.

        企业项目id

        :return: The enterprise_project_id of this ShowInstanceByInstanceIdResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowInstanceByInstanceIdResponse.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowInstanceByInstanceIdResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def version(self):
        r"""Gets the version of this ShowInstanceByInstanceIdResponse.

        版本

        :return: The version of this ShowInstanceByInstanceIdResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowInstanceByInstanceIdResponse.

        版本

        :param version: The version of this ShowInstanceByInstanceIdResponse.
        :type version: str
        """
        self._version = version

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ShowInstanceByInstanceIdResponse.

        过期时间

        :return: The expire_time of this ShowInstanceByInstanceIdResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ShowInstanceByInstanceIdResponse.

        过期时间

        :param expire_time: The expire_time of this ShowInstanceByInstanceIdResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowInstanceByInstanceIdResponse.

        创建时间

        :return: The create_time of this ShowInstanceByInstanceIdResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowInstanceByInstanceIdResponse.

        创建时间

        :param create_time: The create_time of this ShowInstanceByInstanceIdResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def current_time(self):
        r"""Gets the current_time of this ShowInstanceByInstanceIdResponse.

        当前时间

        :return: The current_time of this ShowInstanceByInstanceIdResponse.
        :rtype: int
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        r"""Sets the current_time of this ShowInstanceByInstanceIdResponse.

        当前时间

        :param current_time: The current_time of this ShowInstanceByInstanceIdResponse.
        :type current_time: int
        """
        self._current_time = current_time

    @property
    def product_spec_data(self):
        r"""Gets the product_spec_data of this ShowInstanceByInstanceIdResponse.

        :return: The product_spec_data of this ShowInstanceByInstanceIdResponse.
        :rtype: :class:`huaweicloudsdkaad.v2.ProductSpecData`
        """
        return self._product_spec_data

    @product_spec_data.setter
    def product_spec_data(self, product_spec_data):
        r"""Sets the product_spec_data of this ShowInstanceByInstanceIdResponse.

        :param product_spec_data: The product_spec_data of this ShowInstanceByInstanceIdResponse.
        :type product_spec_data: :class:`huaweicloudsdkaad.v2.ProductSpecData`
        """
        self._product_spec_data = product_spec_data

    @property
    def instance_config(self):
        r"""Gets the instance_config of this ShowInstanceByInstanceIdResponse.

        :return: The instance_config of this ShowInstanceByInstanceIdResponse.
        :rtype: :class:`huaweicloudsdkaad.v2.InstanceConfig`
        """
        return self._instance_config

    @instance_config.setter
    def instance_config(self, instance_config):
        r"""Sets the instance_config of this ShowInstanceByInstanceIdResponse.

        :param instance_config: The instance_config of this ShowInstanceByInstanceIdResponse.
        :type instance_config: :class:`huaweicloudsdkaad.v2.InstanceConfig`
        """
        self._instance_config = instance_config

    @property
    def elastic_service_bw_update_enable(self):
        r"""Gets the elastic_service_bw_update_enable of this ShowInstanceByInstanceIdResponse.

        弹性业务带宽是否可更新

        :return: The elastic_service_bw_update_enable of this ShowInstanceByInstanceIdResponse.
        :rtype: bool
        """
        return self._elastic_service_bw_update_enable

    @elastic_service_bw_update_enable.setter
    def elastic_service_bw_update_enable(self, elastic_service_bw_update_enable):
        r"""Sets the elastic_service_bw_update_enable of this ShowInstanceByInstanceIdResponse.

        弹性业务带宽是否可更新

        :param elastic_service_bw_update_enable: The elastic_service_bw_update_enable of this ShowInstanceByInstanceIdResponse.
        :type elastic_service_bw_update_enable: bool
        """
        self._elastic_service_bw_update_enable = elastic_service_bw_update_enable

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceByInstanceIdResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowInstanceByInstanceIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
