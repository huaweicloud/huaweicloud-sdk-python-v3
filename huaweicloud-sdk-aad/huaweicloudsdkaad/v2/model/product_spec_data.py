# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductSpecData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_uuid': 'str',
        'isp_spec': 'str',
        'data_center': 'str',
        'spec_type': 'int',
        'basic_bandwidth': 'int',
        'elastic_bandwidth': 'int',
        'service_bandwidth': 'int',
        'port_num': 'int',
        'bind_domain_num': 'int',
        'elastic_service_bandwidth': 'int',
        'elastic_service_bandwidth_type': 'int',
        'main_resource_type': 'str',
        'main_resource_spec_code': 'str',
        'main_resource_product_id': 'str'
    }

    attribute_map = {
        'product_uuid': 'product_uuid',
        'isp_spec': 'isp_spec',
        'data_center': 'data_center',
        'spec_type': 'spec_type',
        'basic_bandwidth': 'basic_bandwidth',
        'elastic_bandwidth': 'elastic_bandwidth',
        'service_bandwidth': 'service_bandwidth',
        'port_num': 'port_num',
        'bind_domain_num': 'bind_domain_num',
        'elastic_service_bandwidth': 'elastic_service_bandwidth',
        'elastic_service_bandwidth_type': 'elastic_service_bandwidth_type',
        'main_resource_type': 'main_resource_type',
        'main_resource_spec_code': 'main_resource_spec_code',
        'main_resource_product_id': 'main_resource_product_id'
    }

    def __init__(self, product_uuid=None, isp_spec=None, data_center=None, spec_type=None, basic_bandwidth=None, elastic_bandwidth=None, service_bandwidth=None, port_num=None, bind_domain_num=None, elastic_service_bandwidth=None, elastic_service_bandwidth_type=None, main_resource_type=None, main_resource_spec_code=None, main_resource_product_id=None):
        r"""ProductSpecData

        The model defined in huaweicloud sdk

        :param product_uuid: 产品规格UUID
        :type product_uuid: str
        :param isp_spec: 套餐线路
        :type isp_spec: str
        :param data_center: 机房
        :type data_center: str
        :param spec_type: 产品规格类型
        :type spec_type: int
        :param basic_bandwidth: 保底带宽值
        :type basic_bandwidth: int
        :param elastic_bandwidth: 弹性带宽值
        :type elastic_bandwidth: int
        :param service_bandwidth: 业务带宽值
        :type service_bandwidth: int
        :param port_num: 端口数
        :type port_num: int
        :param bind_domain_num: 域名数
        :type bind_domain_num: int
        :param elastic_service_bandwidth: 弹性业务带宽值
        :type elastic_service_bandwidth: int
        :param elastic_service_bandwidth_type: 弹性业务带宽类型
        :type elastic_service_bandwidth_type: int
        :param main_resource_type: 主资源类型
        :type main_resource_type: str
        :param main_resource_spec_code: 主资源规格编码
        :type main_resource_spec_code: str
        :param main_resource_product_id: 主资源产品id
        :type main_resource_product_id: str
        """
        
        

        self._product_uuid = None
        self._isp_spec = None
        self._data_center = None
        self._spec_type = None
        self._basic_bandwidth = None
        self._elastic_bandwidth = None
        self._service_bandwidth = None
        self._port_num = None
        self._bind_domain_num = None
        self._elastic_service_bandwidth = None
        self._elastic_service_bandwidth_type = None
        self._main_resource_type = None
        self._main_resource_spec_code = None
        self._main_resource_product_id = None
        self.discriminator = None

        if product_uuid is not None:
            self.product_uuid = product_uuid
        if isp_spec is not None:
            self.isp_spec = isp_spec
        if data_center is not None:
            self.data_center = data_center
        if spec_type is not None:
            self.spec_type = spec_type
        if basic_bandwidth is not None:
            self.basic_bandwidth = basic_bandwidth
        if elastic_bandwidth is not None:
            self.elastic_bandwidth = elastic_bandwidth
        if service_bandwidth is not None:
            self.service_bandwidth = service_bandwidth
        if port_num is not None:
            self.port_num = port_num
        if bind_domain_num is not None:
            self.bind_domain_num = bind_domain_num
        if elastic_service_bandwidth is not None:
            self.elastic_service_bandwidth = elastic_service_bandwidth
        if elastic_service_bandwidth_type is not None:
            self.elastic_service_bandwidth_type = elastic_service_bandwidth_type
        if main_resource_type is not None:
            self.main_resource_type = main_resource_type
        if main_resource_spec_code is not None:
            self.main_resource_spec_code = main_resource_spec_code
        if main_resource_product_id is not None:
            self.main_resource_product_id = main_resource_product_id

    @property
    def product_uuid(self):
        r"""Gets the product_uuid of this ProductSpecData.

        产品规格UUID

        :return: The product_uuid of this ProductSpecData.
        :rtype: str
        """
        return self._product_uuid

    @product_uuid.setter
    def product_uuid(self, product_uuid):
        r"""Sets the product_uuid of this ProductSpecData.

        产品规格UUID

        :param product_uuid: The product_uuid of this ProductSpecData.
        :type product_uuid: str
        """
        self._product_uuid = product_uuid

    @property
    def isp_spec(self):
        r"""Gets the isp_spec of this ProductSpecData.

        套餐线路

        :return: The isp_spec of this ProductSpecData.
        :rtype: str
        """
        return self._isp_spec

    @isp_spec.setter
    def isp_spec(self, isp_spec):
        r"""Sets the isp_spec of this ProductSpecData.

        套餐线路

        :param isp_spec: The isp_spec of this ProductSpecData.
        :type isp_spec: str
        """
        self._isp_spec = isp_spec

    @property
    def data_center(self):
        r"""Gets the data_center of this ProductSpecData.

        机房

        :return: The data_center of this ProductSpecData.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        r"""Sets the data_center of this ProductSpecData.

        机房

        :param data_center: The data_center of this ProductSpecData.
        :type data_center: str
        """
        self._data_center = data_center

    @property
    def spec_type(self):
        r"""Gets the spec_type of this ProductSpecData.

        产品规格类型

        :return: The spec_type of this ProductSpecData.
        :rtype: int
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        r"""Sets the spec_type of this ProductSpecData.

        产品规格类型

        :param spec_type: The spec_type of this ProductSpecData.
        :type spec_type: int
        """
        self._spec_type = spec_type

    @property
    def basic_bandwidth(self):
        r"""Gets the basic_bandwidth of this ProductSpecData.

        保底带宽值

        :return: The basic_bandwidth of this ProductSpecData.
        :rtype: int
        """
        return self._basic_bandwidth

    @basic_bandwidth.setter
    def basic_bandwidth(self, basic_bandwidth):
        r"""Sets the basic_bandwidth of this ProductSpecData.

        保底带宽值

        :param basic_bandwidth: The basic_bandwidth of this ProductSpecData.
        :type basic_bandwidth: int
        """
        self._basic_bandwidth = basic_bandwidth

    @property
    def elastic_bandwidth(self):
        r"""Gets the elastic_bandwidth of this ProductSpecData.

        弹性带宽值

        :return: The elastic_bandwidth of this ProductSpecData.
        :rtype: int
        """
        return self._elastic_bandwidth

    @elastic_bandwidth.setter
    def elastic_bandwidth(self, elastic_bandwidth):
        r"""Sets the elastic_bandwidth of this ProductSpecData.

        弹性带宽值

        :param elastic_bandwidth: The elastic_bandwidth of this ProductSpecData.
        :type elastic_bandwidth: int
        """
        self._elastic_bandwidth = elastic_bandwidth

    @property
    def service_bandwidth(self):
        r"""Gets the service_bandwidth of this ProductSpecData.

        业务带宽值

        :return: The service_bandwidth of this ProductSpecData.
        :rtype: int
        """
        return self._service_bandwidth

    @service_bandwidth.setter
    def service_bandwidth(self, service_bandwidth):
        r"""Sets the service_bandwidth of this ProductSpecData.

        业务带宽值

        :param service_bandwidth: The service_bandwidth of this ProductSpecData.
        :type service_bandwidth: int
        """
        self._service_bandwidth = service_bandwidth

    @property
    def port_num(self):
        r"""Gets the port_num of this ProductSpecData.

        端口数

        :return: The port_num of this ProductSpecData.
        :rtype: int
        """
        return self._port_num

    @port_num.setter
    def port_num(self, port_num):
        r"""Sets the port_num of this ProductSpecData.

        端口数

        :param port_num: The port_num of this ProductSpecData.
        :type port_num: int
        """
        self._port_num = port_num

    @property
    def bind_domain_num(self):
        r"""Gets the bind_domain_num of this ProductSpecData.

        域名数

        :return: The bind_domain_num of this ProductSpecData.
        :rtype: int
        """
        return self._bind_domain_num

    @bind_domain_num.setter
    def bind_domain_num(self, bind_domain_num):
        r"""Sets the bind_domain_num of this ProductSpecData.

        域名数

        :param bind_domain_num: The bind_domain_num of this ProductSpecData.
        :type bind_domain_num: int
        """
        self._bind_domain_num = bind_domain_num

    @property
    def elastic_service_bandwidth(self):
        r"""Gets the elastic_service_bandwidth of this ProductSpecData.

        弹性业务带宽值

        :return: The elastic_service_bandwidth of this ProductSpecData.
        :rtype: int
        """
        return self._elastic_service_bandwidth

    @elastic_service_bandwidth.setter
    def elastic_service_bandwidth(self, elastic_service_bandwidth):
        r"""Sets the elastic_service_bandwidth of this ProductSpecData.

        弹性业务带宽值

        :param elastic_service_bandwidth: The elastic_service_bandwidth of this ProductSpecData.
        :type elastic_service_bandwidth: int
        """
        self._elastic_service_bandwidth = elastic_service_bandwidth

    @property
    def elastic_service_bandwidth_type(self):
        r"""Gets the elastic_service_bandwidth_type of this ProductSpecData.

        弹性业务带宽类型

        :return: The elastic_service_bandwidth_type of this ProductSpecData.
        :rtype: int
        """
        return self._elastic_service_bandwidth_type

    @elastic_service_bandwidth_type.setter
    def elastic_service_bandwidth_type(self, elastic_service_bandwidth_type):
        r"""Sets the elastic_service_bandwidth_type of this ProductSpecData.

        弹性业务带宽类型

        :param elastic_service_bandwidth_type: The elastic_service_bandwidth_type of this ProductSpecData.
        :type elastic_service_bandwidth_type: int
        """
        self._elastic_service_bandwidth_type = elastic_service_bandwidth_type

    @property
    def main_resource_type(self):
        r"""Gets the main_resource_type of this ProductSpecData.

        主资源类型

        :return: The main_resource_type of this ProductSpecData.
        :rtype: str
        """
        return self._main_resource_type

    @main_resource_type.setter
    def main_resource_type(self, main_resource_type):
        r"""Sets the main_resource_type of this ProductSpecData.

        主资源类型

        :param main_resource_type: The main_resource_type of this ProductSpecData.
        :type main_resource_type: str
        """
        self._main_resource_type = main_resource_type

    @property
    def main_resource_spec_code(self):
        r"""Gets the main_resource_spec_code of this ProductSpecData.

        主资源规格编码

        :return: The main_resource_spec_code of this ProductSpecData.
        :rtype: str
        """
        return self._main_resource_spec_code

    @main_resource_spec_code.setter
    def main_resource_spec_code(self, main_resource_spec_code):
        r"""Sets the main_resource_spec_code of this ProductSpecData.

        主资源规格编码

        :param main_resource_spec_code: The main_resource_spec_code of this ProductSpecData.
        :type main_resource_spec_code: str
        """
        self._main_resource_spec_code = main_resource_spec_code

    @property
    def main_resource_product_id(self):
        r"""Gets the main_resource_product_id of this ProductSpecData.

        主资源产品id

        :return: The main_resource_product_id of this ProductSpecData.
        :rtype: str
        """
        return self._main_resource_product_id

    @main_resource_product_id.setter
    def main_resource_product_id(self, main_resource_product_id):
        r"""Sets the main_resource_product_id of this ProductSpecData.

        主资源产品id

        :param main_resource_product_id: The main_resource_product_id of this ProductSpecData.
        :type main_resource_product_id: str
        """
        self._main_resource_product_id = main_resource_product_id

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
        if not isinstance(other, ProductSpecData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
