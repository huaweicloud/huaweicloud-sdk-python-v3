# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'int',
        'region_id': 'str',
        'period_type': 'int',
        'period_num': 'int',
        'subscription_num': 'int',
        'period_product_id': 'str',
        'period_resource_spec_code': 'str',
        'cluster_name': 'str',
        'service_type': 'str',
        'share_type': 'str',
        'image_id': 'str',
        'is_auto_renew': 'int',
        'promotion_info': 'str',
        'app_id': 'str',
        'enterprise_project_id': 'str',
        'type': 'str',
        'az': 'str'
    }

    attribute_map = {
        'charging_mode': 'charging_mode',
        'region_id': 'region_id',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'subscription_num': 'subscription_num',
        'period_product_id': 'period_product_id',
        'period_resource_spec_code': 'period_resource_spec_code',
        'cluster_name': 'cluster_name',
        'service_type': 'service_type',
        'share_type': 'share_type',
        'image_id': 'image_id',
        'is_auto_renew': 'is_auto_renew',
        'promotion_info': 'promotion_info',
        'app_id': 'app_id',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'az': 'az'
    }

    def __init__(self, charging_mode=None, region_id=None, period_type=None, period_num=None, subscription_num=None, period_product_id=None, period_resource_spec_code=None, cluster_name=None, service_type=None, share_type=None, image_id=None, is_auto_renew=None, promotion_info=None, app_id=None, enterprise_project_id=None, type=None, az=None):
        r"""CreateClusterRequestBody

        The model defined in huaweicloud sdk

        :param charging_mode: 计费模式  - 0：包年/包月。
        :type charging_mode: int
        :param region_id: 局点ID
        :type region_id: str
        :param period_type: 周期类型  - 2：月。  - 3：年。
        :type period_type: int
        :param period_num: 周期数量
        :type period_num: int
        :param subscription_num: 实例数量
        :type subscription_num: int
        :param period_product_id: 产品id
        :type period_product_id: str
        :param period_resource_spec_code: 产品规格code
        :type period_resource_spec_code: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param service_type: 服务类型  - ENCRYPT_DECRYPT：加解密服务。  - SIGN_VERIFY：签名验签服务。  - KMS：密钥管理服务。  - TIMESTAMP：时间戳服务。  - COLLA_SIGN：协同签名服务。  - OTP：动态令牌服务。  - DB_ENCRYPT：数据库加密服务。  - FILE_ENCRYPT：文件加密服务。  - DIGIT_SEAL：电子签章服务。  - SSL_VPN：SSL_VPN服务。  - IAS：身份认证服务。
        :type service_type: str
        :param share_type: 共享类型  - EXCLUSIVE：应用独享。  - SHARED：应用共享。
        :type share_type: str
        :param image_id: 镜像id
        :type image_id: str
        :param is_auto_renew: 是否自动续费
        :type is_auto_renew: int
        :param promotion_info: 折扣
        :type promotion_info: str
        :param app_id: 应用id
        :type app_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param type: 实例类型  - SINGLE：单机。  - STANDBY：主备。
        :type type: str
        :param az: az
        :type az: str
        """
        
        

        self._charging_mode = None
        self._region_id = None
        self._period_type = None
        self._period_num = None
        self._subscription_num = None
        self._period_product_id = None
        self._period_resource_spec_code = None
        self._cluster_name = None
        self._service_type = None
        self._share_type = None
        self._image_id = None
        self._is_auto_renew = None
        self._promotion_info = None
        self._app_id = None
        self._enterprise_project_id = None
        self._type = None
        self._az = None
        self.discriminator = None

        self.charging_mode = charging_mode
        self.region_id = region_id
        self.period_type = period_type
        self.period_num = period_num
        self.subscription_num = subscription_num
        self.period_product_id = period_product_id
        self.period_resource_spec_code = period_resource_spec_code
        self.cluster_name = cluster_name
        self.service_type = service_type
        self.share_type = share_type
        if image_id is not None:
            self.image_id = image_id
        self.is_auto_renew = is_auto_renew
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if app_id is not None:
            self.app_id = app_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        self.az = az

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CreateClusterRequestBody.

        计费模式  - 0：包年/包月。

        :return: The charging_mode of this CreateClusterRequestBody.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CreateClusterRequestBody.

        计费模式  - 0：包年/包月。

        :param charging_mode: The charging_mode of this CreateClusterRequestBody.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateClusterRequestBody.

        局点ID

        :return: The region_id of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateClusterRequestBody.

        局点ID

        :param region_id: The region_id of this CreateClusterRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def period_type(self):
        r"""Gets the period_type of this CreateClusterRequestBody.

        周期类型  - 2：月。  - 3：年。

        :return: The period_type of this CreateClusterRequestBody.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this CreateClusterRequestBody.

        周期类型  - 2：月。  - 3：年。

        :param period_type: The period_type of this CreateClusterRequestBody.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this CreateClusterRequestBody.

        周期数量

        :return: The period_num of this CreateClusterRequestBody.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this CreateClusterRequestBody.

        周期数量

        :param period_num: The period_num of this CreateClusterRequestBody.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def subscription_num(self):
        r"""Gets the subscription_num of this CreateClusterRequestBody.

        实例数量

        :return: The subscription_num of this CreateClusterRequestBody.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        r"""Sets the subscription_num of this CreateClusterRequestBody.

        实例数量

        :param subscription_num: The subscription_num of this CreateClusterRequestBody.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

    @property
    def period_product_id(self):
        r"""Gets the period_product_id of this CreateClusterRequestBody.

        产品id

        :return: The period_product_id of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._period_product_id

    @period_product_id.setter
    def period_product_id(self, period_product_id):
        r"""Sets the period_product_id of this CreateClusterRequestBody.

        产品id

        :param period_product_id: The period_product_id of this CreateClusterRequestBody.
        :type period_product_id: str
        """
        self._period_product_id = period_product_id

    @property
    def period_resource_spec_code(self):
        r"""Gets the period_resource_spec_code of this CreateClusterRequestBody.

        产品规格code

        :return: The period_resource_spec_code of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._period_resource_spec_code

    @period_resource_spec_code.setter
    def period_resource_spec_code(self, period_resource_spec_code):
        r"""Sets the period_resource_spec_code of this CreateClusterRequestBody.

        产品规格code

        :param period_resource_spec_code: The period_resource_spec_code of this CreateClusterRequestBody.
        :type period_resource_spec_code: str
        """
        self._period_resource_spec_code = period_resource_spec_code

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CreateClusterRequestBody.

        集群名称

        :return: The cluster_name of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CreateClusterRequestBody.

        集群名称

        :param cluster_name: The cluster_name of this CreateClusterRequestBody.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def service_type(self):
        r"""Gets the service_type of this CreateClusterRequestBody.

        服务类型  - ENCRYPT_DECRYPT：加解密服务。  - SIGN_VERIFY：签名验签服务。  - KMS：密钥管理服务。  - TIMESTAMP：时间戳服务。  - COLLA_SIGN：协同签名服务。  - OTP：动态令牌服务。  - DB_ENCRYPT：数据库加密服务。  - FILE_ENCRYPT：文件加密服务。  - DIGIT_SEAL：电子签章服务。  - SSL_VPN：SSL_VPN服务。  - IAS：身份认证服务。

        :return: The service_type of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this CreateClusterRequestBody.

        服务类型  - ENCRYPT_DECRYPT：加解密服务。  - SIGN_VERIFY：签名验签服务。  - KMS：密钥管理服务。  - TIMESTAMP：时间戳服务。  - COLLA_SIGN：协同签名服务。  - OTP：动态令牌服务。  - DB_ENCRYPT：数据库加密服务。  - FILE_ENCRYPT：文件加密服务。  - DIGIT_SEAL：电子签章服务。  - SSL_VPN：SSL_VPN服务。  - IAS：身份认证服务。

        :param service_type: The service_type of this CreateClusterRequestBody.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def share_type(self):
        r"""Gets the share_type of this CreateClusterRequestBody.

        共享类型  - EXCLUSIVE：应用独享。  - SHARED：应用共享。

        :return: The share_type of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this CreateClusterRequestBody.

        共享类型  - EXCLUSIVE：应用独享。  - SHARED：应用共享。

        :param share_type: The share_type of this CreateClusterRequestBody.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def image_id(self):
        r"""Gets the image_id of this CreateClusterRequestBody.

        镜像id

        :return: The image_id of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CreateClusterRequestBody.

        镜像id

        :param image_id: The image_id of this CreateClusterRequestBody.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this CreateClusterRequestBody.

        是否自动续费

        :return: The is_auto_renew of this CreateClusterRequestBody.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this CreateClusterRequestBody.

        是否自动续费

        :param is_auto_renew: The is_auto_renew of this CreateClusterRequestBody.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this CreateClusterRequestBody.

        折扣

        :return: The promotion_info of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this CreateClusterRequestBody.

        折扣

        :param promotion_info: The promotion_info of this CreateClusterRequestBody.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateClusterRequestBody.

        应用id

        :return: The app_id of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateClusterRequestBody.

        应用id

        :param app_id: The app_id of this CreateClusterRequestBody.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateClusterRequestBody.

        企业项目id

        :return: The enterprise_project_id of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateClusterRequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CreateClusterRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this CreateClusterRequestBody.

        实例类型  - SINGLE：单机。  - STANDBY：主备。

        :return: The type of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateClusterRequestBody.

        实例类型  - SINGLE：单机。  - STANDBY：主备。

        :param type: The type of this CreateClusterRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def az(self):
        r"""Gets the az of this CreateClusterRequestBody.

        az

        :return: The az of this CreateClusterRequestBody.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this CreateClusterRequestBody.

        az

        :param az: The az of this CreateClusterRequestBody.
        :type az: str
        """
        self._az = az

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
        if not isinstance(other, CreateClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
