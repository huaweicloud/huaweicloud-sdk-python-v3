# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetadataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ecm_res_status': 'str',
        'charging_mode': 'str',
        'metering_order_id': 'str',
        'metering_product_id': 'str',
        'vpc_id': 'str',
        'metering_image_id': 'str',
        'metering_imagetype': 'str',
        'baremetal_port_id_list': 'str',
        'metering_resourcespeccode': 'str',
        'metering_resourcetype': 'str',
        'image_name': 'str',
        'op_svc_userid': 'str',
        'os_type': 'str',
        'bms_support_evs': 'str',
        'os_bit': 'str'
    }

    attribute_map = {
        'ecm_res_status': 'EcmResStatus',
        'charging_mode': 'chargingMode',
        'metering_order_id': 'metering.order_id',
        'metering_product_id': 'metering.product_id',
        'vpc_id': 'vpc_id',
        'metering_image_id': 'metering.image_id',
        'metering_imagetype': 'metering.imagetype',
        'baremetal_port_id_list': 'baremetalPortIDList',
        'metering_resourcespeccode': 'metering.resourcespeccode',
        'metering_resourcetype': 'metering.resourcetype',
        'image_name': 'image_name',
        'op_svc_userid': 'op_svc_userid',
        'os_type': 'os_type',
        'bms_support_evs': '__bms_support_evs',
        'os_bit': 'os_bit'
    }

    def __init__(self, ecm_res_status=None, charging_mode=None, metering_order_id=None, metering_product_id=None, vpc_id=None, metering_image_id=None, metering_imagetype=None, baremetal_port_id_list=None, metering_resourcespeccode=None, metering_resourcetype=None, image_name=None, op_svc_userid=None, os_type=None, bms_support_evs=None, os_bit=None):
        r"""MetadataList

        The model defined in huaweicloud sdk

        :param ecm_res_status: 裸机的冻结状态
        :type ecm_res_status: str
        :param charging_mode: 裸金属服务器的计费类型。1：按包年包月计费（即prePaid：预付费方式）。
        :type charging_mode: str
        :param metering_order_id: 按“包年/包月”计费的裸金属服务器对应的订单ID。
        :type metering_order_id: str
        :param metering_product_id: 按“包年/包月”计费的裸金属服务器对应的产品ID
        :type metering_product_id: str
        :param vpc_id: 裸金属服务器所属的虚拟私有云ID
        :type vpc_id: str
        :param metering_image_id: 裸金属服务器操作系统对应的镜像ID
        :type metering_image_id: str
        :param metering_imagetype: 镜像类型，目前支持：公共镜像（gold）私有镜像（private）共享镜像（shared）
        :type metering_imagetype: str
        :param baremetal_port_id_list: 裸金属服务器的网卡列表。
        :type baremetal_port_id_list: str
        :param metering_resourcespeccode: 裸金属服务器对应的资源规格编码，格式为：{规格ID}.{os_type}，例如physical.o2.medium.linux。
        :type metering_resourcespeccode: str
        :param metering_resourcetype: 裸金属服务器对应的资源类型，取值为：hws.resource.type.pm
        :type metering_resourcetype: str
        :param image_name: 裸金属服务器操作系统对应的镜像名称
        :type image_name: str
        :param op_svc_userid: 用户ID（登录管理控制台，进入我的凭证，即可看到“用户ID”）
        :type op_svc_userid: str
        :param os_type: 操作系统类型，取值为：Linux、Windows
        :type os_type: str
        :param bms_support_evs: 裸金属服务器是否支持EVS卷。
        :type bms_support_evs: str
        :param os_bit: 操作系统位数，一般取值为“32”或者“64”。
        :type os_bit: str
        """
        
        

        self._ecm_res_status = None
        self._charging_mode = None
        self._metering_order_id = None
        self._metering_product_id = None
        self._vpc_id = None
        self._metering_image_id = None
        self._metering_imagetype = None
        self._baremetal_port_id_list = None
        self._metering_resourcespeccode = None
        self._metering_resourcetype = None
        self._image_name = None
        self._op_svc_userid = None
        self._os_type = None
        self._bms_support_evs = None
        self._os_bit = None
        self.discriminator = None

        if ecm_res_status is not None:
            self.ecm_res_status = ecm_res_status
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if metering_order_id is not None:
            self.metering_order_id = metering_order_id
        if metering_product_id is not None:
            self.metering_product_id = metering_product_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if metering_image_id is not None:
            self.metering_image_id = metering_image_id
        if metering_imagetype is not None:
            self.metering_imagetype = metering_imagetype
        if baremetal_port_id_list is not None:
            self.baremetal_port_id_list = baremetal_port_id_list
        if metering_resourcespeccode is not None:
            self.metering_resourcespeccode = metering_resourcespeccode
        if metering_resourcetype is not None:
            self.metering_resourcetype = metering_resourcetype
        if image_name is not None:
            self.image_name = image_name
        if op_svc_userid is not None:
            self.op_svc_userid = op_svc_userid
        if os_type is not None:
            self.os_type = os_type
        if bms_support_evs is not None:
            self.bms_support_evs = bms_support_evs
        if os_bit is not None:
            self.os_bit = os_bit

    @property
    def ecm_res_status(self):
        r"""Gets the ecm_res_status of this MetadataList.

        裸机的冻结状态

        :return: The ecm_res_status of this MetadataList.
        :rtype: str
        """
        return self._ecm_res_status

    @ecm_res_status.setter
    def ecm_res_status(self, ecm_res_status):
        r"""Sets the ecm_res_status of this MetadataList.

        裸机的冻结状态

        :param ecm_res_status: The ecm_res_status of this MetadataList.
        :type ecm_res_status: str
        """
        self._ecm_res_status = ecm_res_status

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this MetadataList.

        裸金属服务器的计费类型。1：按包年包月计费（即prePaid：预付费方式）。

        :return: The charging_mode of this MetadataList.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this MetadataList.

        裸金属服务器的计费类型。1：按包年包月计费（即prePaid：预付费方式）。

        :param charging_mode: The charging_mode of this MetadataList.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def metering_order_id(self):
        r"""Gets the metering_order_id of this MetadataList.

        按“包年/包月”计费的裸金属服务器对应的订单ID。

        :return: The metering_order_id of this MetadataList.
        :rtype: str
        """
        return self._metering_order_id

    @metering_order_id.setter
    def metering_order_id(self, metering_order_id):
        r"""Sets the metering_order_id of this MetadataList.

        按“包年/包月”计费的裸金属服务器对应的订单ID。

        :param metering_order_id: The metering_order_id of this MetadataList.
        :type metering_order_id: str
        """
        self._metering_order_id = metering_order_id

    @property
    def metering_product_id(self):
        r"""Gets the metering_product_id of this MetadataList.

        按“包年/包月”计费的裸金属服务器对应的产品ID

        :return: The metering_product_id of this MetadataList.
        :rtype: str
        """
        return self._metering_product_id

    @metering_product_id.setter
    def metering_product_id(self, metering_product_id):
        r"""Sets the metering_product_id of this MetadataList.

        按“包年/包月”计费的裸金属服务器对应的产品ID

        :param metering_product_id: The metering_product_id of this MetadataList.
        :type metering_product_id: str
        """
        self._metering_product_id = metering_product_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this MetadataList.

        裸金属服务器所属的虚拟私有云ID

        :return: The vpc_id of this MetadataList.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this MetadataList.

        裸金属服务器所属的虚拟私有云ID

        :param vpc_id: The vpc_id of this MetadataList.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def metering_image_id(self):
        r"""Gets the metering_image_id of this MetadataList.

        裸金属服务器操作系统对应的镜像ID

        :return: The metering_image_id of this MetadataList.
        :rtype: str
        """
        return self._metering_image_id

    @metering_image_id.setter
    def metering_image_id(self, metering_image_id):
        r"""Sets the metering_image_id of this MetadataList.

        裸金属服务器操作系统对应的镜像ID

        :param metering_image_id: The metering_image_id of this MetadataList.
        :type metering_image_id: str
        """
        self._metering_image_id = metering_image_id

    @property
    def metering_imagetype(self):
        r"""Gets the metering_imagetype of this MetadataList.

        镜像类型，目前支持：公共镜像（gold）私有镜像（private）共享镜像（shared）

        :return: The metering_imagetype of this MetadataList.
        :rtype: str
        """
        return self._metering_imagetype

    @metering_imagetype.setter
    def metering_imagetype(self, metering_imagetype):
        r"""Sets the metering_imagetype of this MetadataList.

        镜像类型，目前支持：公共镜像（gold）私有镜像（private）共享镜像（shared）

        :param metering_imagetype: The metering_imagetype of this MetadataList.
        :type metering_imagetype: str
        """
        self._metering_imagetype = metering_imagetype

    @property
    def baremetal_port_id_list(self):
        r"""Gets the baremetal_port_id_list of this MetadataList.

        裸金属服务器的网卡列表。

        :return: The baremetal_port_id_list of this MetadataList.
        :rtype: str
        """
        return self._baremetal_port_id_list

    @baremetal_port_id_list.setter
    def baremetal_port_id_list(self, baremetal_port_id_list):
        r"""Sets the baremetal_port_id_list of this MetadataList.

        裸金属服务器的网卡列表。

        :param baremetal_port_id_list: The baremetal_port_id_list of this MetadataList.
        :type baremetal_port_id_list: str
        """
        self._baremetal_port_id_list = baremetal_port_id_list

    @property
    def metering_resourcespeccode(self):
        r"""Gets the metering_resourcespeccode of this MetadataList.

        裸金属服务器对应的资源规格编码，格式为：{规格ID}.{os_type}，例如physical.o2.medium.linux。

        :return: The metering_resourcespeccode of this MetadataList.
        :rtype: str
        """
        return self._metering_resourcespeccode

    @metering_resourcespeccode.setter
    def metering_resourcespeccode(self, metering_resourcespeccode):
        r"""Sets the metering_resourcespeccode of this MetadataList.

        裸金属服务器对应的资源规格编码，格式为：{规格ID}.{os_type}，例如physical.o2.medium.linux。

        :param metering_resourcespeccode: The metering_resourcespeccode of this MetadataList.
        :type metering_resourcespeccode: str
        """
        self._metering_resourcespeccode = metering_resourcespeccode

    @property
    def metering_resourcetype(self):
        r"""Gets the metering_resourcetype of this MetadataList.

        裸金属服务器对应的资源类型，取值为：hws.resource.type.pm

        :return: The metering_resourcetype of this MetadataList.
        :rtype: str
        """
        return self._metering_resourcetype

    @metering_resourcetype.setter
    def metering_resourcetype(self, metering_resourcetype):
        r"""Sets the metering_resourcetype of this MetadataList.

        裸金属服务器对应的资源类型，取值为：hws.resource.type.pm

        :param metering_resourcetype: The metering_resourcetype of this MetadataList.
        :type metering_resourcetype: str
        """
        self._metering_resourcetype = metering_resourcetype

    @property
    def image_name(self):
        r"""Gets the image_name of this MetadataList.

        裸金属服务器操作系统对应的镜像名称

        :return: The image_name of this MetadataList.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this MetadataList.

        裸金属服务器操作系统对应的镜像名称

        :param image_name: The image_name of this MetadataList.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def op_svc_userid(self):
        r"""Gets the op_svc_userid of this MetadataList.

        用户ID（登录管理控制台，进入我的凭证，即可看到“用户ID”）

        :return: The op_svc_userid of this MetadataList.
        :rtype: str
        """
        return self._op_svc_userid

    @op_svc_userid.setter
    def op_svc_userid(self, op_svc_userid):
        r"""Sets the op_svc_userid of this MetadataList.

        用户ID（登录管理控制台，进入我的凭证，即可看到“用户ID”）

        :param op_svc_userid: The op_svc_userid of this MetadataList.
        :type op_svc_userid: str
        """
        self._op_svc_userid = op_svc_userid

    @property
    def os_type(self):
        r"""Gets the os_type of this MetadataList.

        操作系统类型，取值为：Linux、Windows

        :return: The os_type of this MetadataList.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this MetadataList.

        操作系统类型，取值为：Linux、Windows

        :param os_type: The os_type of this MetadataList.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def bms_support_evs(self):
        r"""Gets the bms_support_evs of this MetadataList.

        裸金属服务器是否支持EVS卷。

        :return: The bms_support_evs of this MetadataList.
        :rtype: str
        """
        return self._bms_support_evs

    @bms_support_evs.setter
    def bms_support_evs(self, bms_support_evs):
        r"""Sets the bms_support_evs of this MetadataList.

        裸金属服务器是否支持EVS卷。

        :param bms_support_evs: The bms_support_evs of this MetadataList.
        :type bms_support_evs: str
        """
        self._bms_support_evs = bms_support_evs

    @property
    def os_bit(self):
        r"""Gets the os_bit of this MetadataList.

        操作系统位数，一般取值为“32”或者“64”。

        :return: The os_bit of this MetadataList.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this MetadataList.

        操作系统位数，一般取值为“32”或者“64”。

        :param os_bit: The os_bit of this MetadataList.
        :type os_bit: str
        """
        self._os_bit = os_bit

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
        if not isinstance(other, MetadataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
