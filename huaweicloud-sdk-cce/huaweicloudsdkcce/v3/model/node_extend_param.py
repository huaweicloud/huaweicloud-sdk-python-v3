# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ecsperformancetype': 'str',
        'order_id': 'str',
        'product_id': 'str',
        'max_pods': 'int',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'str',
        'is_auto_pay': 'str',
        'docker_lvm_config_override': 'str',
        'docker_base_size': 'int',
        'public_key': 'str',
        'alpha_cce_pre_install': 'str',
        'alpha_cce_post_install': 'str',
        'alpha_cce_node_image_id': 'str',
        'nic_multiqueue': 'str',
        'nic_threshold': 'str',
        'enterprise_project_id': 'str',
        'charging_mode': 'int'
    }

    attribute_map = {
        'ecsperformancetype': 'ecs:performancetype',
        'order_id': 'orderID',
        'product_id': 'productID',
        'max_pods': 'maxPods',
        'period_type': 'periodType',
        'period_num': 'periodNum',
        'is_auto_renew': 'isAutoRenew',
        'is_auto_pay': 'isAutoPay',
        'docker_lvm_config_override': 'DockerLVMConfigOverride',
        'docker_base_size': 'dockerBaseSize',
        'public_key': 'publicKey',
        'alpha_cce_pre_install': 'alpha.cce/preInstall',
        'alpha_cce_post_install': 'alpha.cce/postInstall',
        'alpha_cce_node_image_id': 'alpha.cce/NodeImageID',
        'nic_multiqueue': 'nicMultiqueue',
        'nic_threshold': 'nicThreshold',
        'enterprise_project_id': 'enterprise_project_id',
        'charging_mode': 'chargingMode'
    }

    def __init__(self, ecsperformancetype=None, order_id=None, product_id=None, max_pods=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, docker_lvm_config_override=None, docker_base_size=None, public_key=None, alpha_cce_pre_install=None, alpha_cce_post_install=None, alpha_cce_node_image_id=None, nic_multiqueue=None, nic_threshold=None, enterprise_project_id=None, charging_mode=None):
        """NodeExtendParam

        The model defined in huaweicloud sdk

        :param ecsperformancetype: 云服务器规格的分类。响应中会返回此字段。
        :type ecsperformancetype: str
        :param order_id: 订单ID，节点付费类型为自动付费包周期类型时，响应中会返回此字段。
        :type order_id: str
        :param product_id: 产品ID，节点付费类型为自动付费包周期类型时，响应中会返回此字段。
        :type product_id: str
        :param max_pods: 节点最大允许创建的实例数(Pod)，该数量包含系统默认实例，取值范围为16~256。  该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。  节点可以创建多少个Pod，受多个参数影响，具体请参见[节点最多可以创建多少Pod](maxPods.xml)。 
        :type max_pods: int
        :param period_type: - month：月 - year：年 &gt; billingMode为1（包周期）或2（已废弃：自动付费包周期）时生效，且为必选。 
        :type period_type: str
        :param period_num: 订购周期数，取值范围： - periodType&#x3D;month（周期类型为月）时，取值为[1-9]。 - periodType&#x3D;year（周期类型为年）时，取值为1。 &gt; billingMode为1或2（已废弃）时生效，且为必选。 
        :type period_num: int
        :param is_auto_renew: 是否自动续订 - “true”：自动续订 - “false”：不自动续订 &gt; billingMode为1或2（已废弃）时生效，不填写此参数时默认不会自动续费。 
        :type is_auto_renew: str
        :param is_auto_pay: 是否自动扣款 - “true”：自动扣款 - “false”：不自动扣款 &gt; billingMode为1或2（已废弃）时生效，billingMode为1时不填写此参数时默认不会自动扣款。（已废弃：billingMode为2时不填写此参数时默认会自动扣款） 
        :type is_auto_pay: str
        :param docker_lvm_config_override: Docker数据盘配置项。默认配置示例如下： &#x60;&#x60;&#x60; \&quot;DockerLVMConfigOverride\&quot;:\&quot;dockerThinpool&#x3D;vgpaas/90%VG;kubernetesLV&#x3D;vgpaas/10%VG;diskType&#x3D;evs;lvType&#x3D;linear\&quot; &#x60;&#x60;&#x60; 包含如下字段：   - userLV（可选）：用户空间的大小，示例格式：vgpaas/20%VG   - userPath（可选）：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG 
        :type docker_lvm_config_override: str
        :param docker_base_size: 节点上单容器的可用磁盘空间大小，单位G。不配置该值或值为0时将使用默认值，Devicemapper模式下默认值为10；OverlayFS模式默认不限制单容器可用空间大小，且dockerBaseSize设置仅在新版本集群的EulerOS节点上生效。CCE节点容器运行时空间配置请参考[数据盘空间分配说明](cce_01_0341.xml)。Devicemapper模式下建议dockerBaseSize配置不超过80G，设置过大时可能会导致容器运行时初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替。 
        :type docker_base_size: int
        :param public_key: 节点的公钥。
        :type public_key: str
        :param alpha_cce_pre_install: 安装前执行脚本 &gt; 输入的值需要经过Base64编码，方法为echo -n \&quot;待编码内容\&quot; | base64 
        :type alpha_cce_pre_install: str
        :param alpha_cce_post_install: 安装后执行脚本 &gt; 输入的值需要经过Base64编码，方法为echo -n \&quot;待编码内容\&quot; | base64。 
        :type alpha_cce_post_install: str
        :param alpha_cce_node_image_id: 如果创建裸金属节点，需要使用自定义镜像时用此参数。 
        :type alpha_cce_node_image_id: str
        :param nic_multiqueue: - 弹性网卡队列数配置，默认配置示例如下： &#x60;&#x60;&#x60; \&quot;[{\\\&quot;queue\\\&quot;:4}]\&quot; &#x60;&#x60;&#x60; 包含如下字段：   - queue: 弹性网卡队列数。 - 仅在turbo集群的BMS节点时，该字段才可配置。 - 当前支持可配置队列数以及弹性网卡数：{\&quot;1\&quot;:128, \&quot;2\&quot;:92, \&quot;4\&quot;:92, \&quot;8\&quot;:32, \&quot;16\&quot;:16, \&quot;28\&quot;:9}, 既1弹性网卡队列可绑定128张弹性网卡，2队列弹性网卡可绑定92张，以此类推。 - 弹性网卡队列数越多，性能越强，但可绑定弹性网卡数越少，请根据您的需求进行配置（创建后不可修改）。 
        :type nic_multiqueue: str
        :param nic_threshold: - 弹性网卡预绑定比例配置，默认配置示例如下： &#x60;&#x60;&#x60; \&quot;0.3:0.6\&quot; &#x60;&#x60;&#x60;   - 第一位小数：预绑定低水位，弹性网卡预绑定的最低比例（最小预绑定弹性网卡数 &#x3D; ⌊节点的总弹性网卡数 * 预绑定低水位⌋）   - 第二位小数：预绑定高水位，弹性网卡预绑定的最高比例（最大预绑定弹性网卡数 &#x3D; ⌊节点的总弹性网卡数 * 预绑定高水位⌋）   - BMS节点上绑定的弹性网卡数：Pod正在使用的弹性网卡数 + 最小预绑定弹性网卡数 &lt; BMS节点上绑定的弹性网卡数 &lt; Pod正在使用的弹性网卡数 + 最大预绑定弹性网卡数   - BMS节点上当预绑定弹性网卡数 &lt; 最小预绑定弹性网卡数时：会绑定弹性网卡，使得预绑定弹性网卡数 &#x3D; 最小预绑定弹性网卡数   - BMS节点上当预绑定弹性网卡数 &gt; 最大预绑定弹性网卡数时：会定时解绑弹性网卡（约2分钟一次），直到预绑定弹性网卡数 &#x3D; 最大预绑定弹性网卡数   - 取值范围：[0.0, 1.0]; 一位小数; 低水位 &lt;&#x3D; 高水位 - 仅在turbo集群的BMS节点时，该字段才可配置。 - 弹性网卡预绑定能加快工作负载的创建，但会占用IP，请根据您的需求进行配置。 
        :type nic_threshold: str
        :param enterprise_project_id: 节点所属的企业项目id。 
        :type enterprise_project_id: str
        :param charging_mode: 节点的计费模式。已废弃，请使用NodeSpec中的billingMode字段。 
        :type charging_mode: int
        """
        
        

        self._ecsperformancetype = None
        self._order_id = None
        self._product_id = None
        self._max_pods = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._docker_lvm_config_override = None
        self._docker_base_size = None
        self._public_key = None
        self._alpha_cce_pre_install = None
        self._alpha_cce_post_install = None
        self._alpha_cce_node_image_id = None
        self._nic_multiqueue = None
        self._nic_threshold = None
        self._enterprise_project_id = None
        self._charging_mode = None
        self.discriminator = None

        if ecsperformancetype is not None:
            self.ecsperformancetype = ecsperformancetype
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if max_pods is not None:
            self.max_pods = max_pods
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if docker_lvm_config_override is not None:
            self.docker_lvm_config_override = docker_lvm_config_override
        if docker_base_size is not None:
            self.docker_base_size = docker_base_size
        if public_key is not None:
            self.public_key = public_key
        if alpha_cce_pre_install is not None:
            self.alpha_cce_pre_install = alpha_cce_pre_install
        if alpha_cce_post_install is not None:
            self.alpha_cce_post_install = alpha_cce_post_install
        if alpha_cce_node_image_id is not None:
            self.alpha_cce_node_image_id = alpha_cce_node_image_id
        if nic_multiqueue is not None:
            self.nic_multiqueue = nic_multiqueue
        if nic_threshold is not None:
            self.nic_threshold = nic_threshold
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def ecsperformancetype(self):
        """Gets the ecsperformancetype of this NodeExtendParam.

        云服务器规格的分类。响应中会返回此字段。

        :return: The ecsperformancetype of this NodeExtendParam.
        :rtype: str
        """
        return self._ecsperformancetype

    @ecsperformancetype.setter
    def ecsperformancetype(self, ecsperformancetype):
        """Sets the ecsperformancetype of this NodeExtendParam.

        云服务器规格的分类。响应中会返回此字段。

        :param ecsperformancetype: The ecsperformancetype of this NodeExtendParam.
        :type ecsperformancetype: str
        """
        self._ecsperformancetype = ecsperformancetype

    @property
    def order_id(self):
        """Gets the order_id of this NodeExtendParam.

        订单ID，节点付费类型为自动付费包周期类型时，响应中会返回此字段。

        :return: The order_id of this NodeExtendParam.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this NodeExtendParam.

        订单ID，节点付费类型为自动付费包周期类型时，响应中会返回此字段。

        :param order_id: The order_id of this NodeExtendParam.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this NodeExtendParam.

        产品ID，节点付费类型为自动付费包周期类型时，响应中会返回此字段。

        :return: The product_id of this NodeExtendParam.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this NodeExtendParam.

        产品ID，节点付费类型为自动付费包周期类型时，响应中会返回此字段。

        :param product_id: The product_id of this NodeExtendParam.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def max_pods(self):
        """Gets the max_pods of this NodeExtendParam.

        节点最大允许创建的实例数(Pod)，该数量包含系统默认实例，取值范围为16~256。  该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。  节点可以创建多少个Pod，受多个参数影响，具体请参见[节点最多可以创建多少Pod](maxPods.xml)。 

        :return: The max_pods of this NodeExtendParam.
        :rtype: int
        """
        return self._max_pods

    @max_pods.setter
    def max_pods(self, max_pods):
        """Sets the max_pods of this NodeExtendParam.

        节点最大允许创建的实例数(Pod)，该数量包含系统默认实例，取值范围为16~256。  该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。  节点可以创建多少个Pod，受多个参数影响，具体请参见[节点最多可以创建多少Pod](maxPods.xml)。 

        :param max_pods: The max_pods of this NodeExtendParam.
        :type max_pods: int
        """
        self._max_pods = max_pods

    @property
    def period_type(self):
        """Gets the period_type of this NodeExtendParam.

        - month：月 - year：年 > billingMode为1（包周期）或2（已废弃：自动付费包周期）时生效，且为必选。 

        :return: The period_type of this NodeExtendParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this NodeExtendParam.

        - month：月 - year：年 > billingMode为1（包周期）或2（已废弃：自动付费包周期）时生效，且为必选。 

        :param period_type: The period_type of this NodeExtendParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this NodeExtendParam.

        订购周期数，取值范围： - periodType=month（周期类型为月）时，取值为[1-9]。 - periodType=year（周期类型为年）时，取值为1。 > billingMode为1或2（已废弃）时生效，且为必选。 

        :return: The period_num of this NodeExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this NodeExtendParam.

        订购周期数，取值范围： - periodType=month（周期类型为月）时，取值为[1-9]。 - periodType=year（周期类型为年）时，取值为1。 > billingMode为1或2（已废弃）时生效，且为必选。 

        :param period_num: The period_num of this NodeExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this NodeExtendParam.

        是否自动续订 - “true”：自动续订 - “false”：不自动续订 > billingMode为1或2（已废弃）时生效，不填写此参数时默认不会自动续费。 

        :return: The is_auto_renew of this NodeExtendParam.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this NodeExtendParam.

        是否自动续订 - “true”：自动续订 - “false”：不自动续订 > billingMode为1或2（已废弃）时生效，不填写此参数时默认不会自动续费。 

        :param is_auto_renew: The is_auto_renew of this NodeExtendParam.
        :type is_auto_renew: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this NodeExtendParam.

        是否自动扣款 - “true”：自动扣款 - “false”：不自动扣款 > billingMode为1或2（已废弃）时生效，billingMode为1时不填写此参数时默认不会自动扣款。（已废弃：billingMode为2时不填写此参数时默认会自动扣款） 

        :return: The is_auto_pay of this NodeExtendParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this NodeExtendParam.

        是否自动扣款 - “true”：自动扣款 - “false”：不自动扣款 > billingMode为1或2（已废弃）时生效，billingMode为1时不填写此参数时默认不会自动扣款。（已废弃：billingMode为2时不填写此参数时默认会自动扣款） 

        :param is_auto_pay: The is_auto_pay of this NodeExtendParam.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

    @property
    def docker_lvm_config_override(self):
        """Gets the docker_lvm_config_override of this NodeExtendParam.

        Docker数据盘配置项。默认配置示例如下： ``` \"DockerLVMConfigOverride\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\" ``` 包含如下字段：   - userLV（可选）：用户空间的大小，示例格式：vgpaas/20%VG   - userPath（可选）：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG 

        :return: The docker_lvm_config_override of this NodeExtendParam.
        :rtype: str
        """
        return self._docker_lvm_config_override

    @docker_lvm_config_override.setter
    def docker_lvm_config_override(self, docker_lvm_config_override):
        """Sets the docker_lvm_config_override of this NodeExtendParam.

        Docker数据盘配置项。默认配置示例如下： ``` \"DockerLVMConfigOverride\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\" ``` 包含如下字段：   - userLV（可选）：用户空间的大小，示例格式：vgpaas/20%VG   - userPath（可选）：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG 

        :param docker_lvm_config_override: The docker_lvm_config_override of this NodeExtendParam.
        :type docker_lvm_config_override: str
        """
        self._docker_lvm_config_override = docker_lvm_config_override

    @property
    def docker_base_size(self):
        """Gets the docker_base_size of this NodeExtendParam.

        节点上单容器的可用磁盘空间大小，单位G。不配置该值或值为0时将使用默认值，Devicemapper模式下默认值为10；OverlayFS模式默认不限制单容器可用空间大小，且dockerBaseSize设置仅在新版本集群的EulerOS节点上生效。CCE节点容器运行时空间配置请参考[数据盘空间分配说明](cce_01_0341.xml)。Devicemapper模式下建议dockerBaseSize配置不超过80G，设置过大时可能会导致容器运行时初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替。 

        :return: The docker_base_size of this NodeExtendParam.
        :rtype: int
        """
        return self._docker_base_size

    @docker_base_size.setter
    def docker_base_size(self, docker_base_size):
        """Sets the docker_base_size of this NodeExtendParam.

        节点上单容器的可用磁盘空间大小，单位G。不配置该值或值为0时将使用默认值，Devicemapper模式下默认值为10；OverlayFS模式默认不限制单容器可用空间大小，且dockerBaseSize设置仅在新版本集群的EulerOS节点上生效。CCE节点容器运行时空间配置请参考[数据盘空间分配说明](cce_01_0341.xml)。Devicemapper模式下建议dockerBaseSize配置不超过80G，设置过大时可能会导致容器运行时初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替。 

        :param docker_base_size: The docker_base_size of this NodeExtendParam.
        :type docker_base_size: int
        """
        self._docker_base_size = docker_base_size

    @property
    def public_key(self):
        """Gets the public_key of this NodeExtendParam.

        节点的公钥。

        :return: The public_key of this NodeExtendParam.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this NodeExtendParam.

        节点的公钥。

        :param public_key: The public_key of this NodeExtendParam.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def alpha_cce_pre_install(self):
        """Gets the alpha_cce_pre_install of this NodeExtendParam.

        安装前执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64 

        :return: The alpha_cce_pre_install of this NodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_pre_install

    @alpha_cce_pre_install.setter
    def alpha_cce_pre_install(self, alpha_cce_pre_install):
        """Sets the alpha_cce_pre_install of this NodeExtendParam.

        安装前执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64 

        :param alpha_cce_pre_install: The alpha_cce_pre_install of this NodeExtendParam.
        :type alpha_cce_pre_install: str
        """
        self._alpha_cce_pre_install = alpha_cce_pre_install

    @property
    def alpha_cce_post_install(self):
        """Gets the alpha_cce_post_install of this NodeExtendParam.

        安装后执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :return: The alpha_cce_post_install of this NodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_post_install

    @alpha_cce_post_install.setter
    def alpha_cce_post_install(self, alpha_cce_post_install):
        """Sets the alpha_cce_post_install of this NodeExtendParam.

        安装后执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :param alpha_cce_post_install: The alpha_cce_post_install of this NodeExtendParam.
        :type alpha_cce_post_install: str
        """
        self._alpha_cce_post_install = alpha_cce_post_install

    @property
    def alpha_cce_node_image_id(self):
        """Gets the alpha_cce_node_image_id of this NodeExtendParam.

        如果创建裸金属节点，需要使用自定义镜像时用此参数。 

        :return: The alpha_cce_node_image_id of this NodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_node_image_id

    @alpha_cce_node_image_id.setter
    def alpha_cce_node_image_id(self, alpha_cce_node_image_id):
        """Sets the alpha_cce_node_image_id of this NodeExtendParam.

        如果创建裸金属节点，需要使用自定义镜像时用此参数。 

        :param alpha_cce_node_image_id: The alpha_cce_node_image_id of this NodeExtendParam.
        :type alpha_cce_node_image_id: str
        """
        self._alpha_cce_node_image_id = alpha_cce_node_image_id

    @property
    def nic_multiqueue(self):
        """Gets the nic_multiqueue of this NodeExtendParam.

        - 弹性网卡队列数配置，默认配置示例如下： ``` \"[{\\\"queue\\\":4}]\" ``` 包含如下字段：   - queue: 弹性网卡队列数。 - 仅在turbo集群的BMS节点时，该字段才可配置。 - 当前支持可配置队列数以及弹性网卡数：{\"1\":128, \"2\":92, \"4\":92, \"8\":32, \"16\":16, \"28\":9}, 既1弹性网卡队列可绑定128张弹性网卡，2队列弹性网卡可绑定92张，以此类推。 - 弹性网卡队列数越多，性能越强，但可绑定弹性网卡数越少，请根据您的需求进行配置（创建后不可修改）。 

        :return: The nic_multiqueue of this NodeExtendParam.
        :rtype: str
        """
        return self._nic_multiqueue

    @nic_multiqueue.setter
    def nic_multiqueue(self, nic_multiqueue):
        """Sets the nic_multiqueue of this NodeExtendParam.

        - 弹性网卡队列数配置，默认配置示例如下： ``` \"[{\\\"queue\\\":4}]\" ``` 包含如下字段：   - queue: 弹性网卡队列数。 - 仅在turbo集群的BMS节点时，该字段才可配置。 - 当前支持可配置队列数以及弹性网卡数：{\"1\":128, \"2\":92, \"4\":92, \"8\":32, \"16\":16, \"28\":9}, 既1弹性网卡队列可绑定128张弹性网卡，2队列弹性网卡可绑定92张，以此类推。 - 弹性网卡队列数越多，性能越强，但可绑定弹性网卡数越少，请根据您的需求进行配置（创建后不可修改）。 

        :param nic_multiqueue: The nic_multiqueue of this NodeExtendParam.
        :type nic_multiqueue: str
        """
        self._nic_multiqueue = nic_multiqueue

    @property
    def nic_threshold(self):
        """Gets the nic_threshold of this NodeExtendParam.

        - 弹性网卡预绑定比例配置，默认配置示例如下： ``` \"0.3:0.6\" ```   - 第一位小数：预绑定低水位，弹性网卡预绑定的最低比例（最小预绑定弹性网卡数 = ⌊节点的总弹性网卡数 * 预绑定低水位⌋）   - 第二位小数：预绑定高水位，弹性网卡预绑定的最高比例（最大预绑定弹性网卡数 = ⌊节点的总弹性网卡数 * 预绑定高水位⌋）   - BMS节点上绑定的弹性网卡数：Pod正在使用的弹性网卡数 + 最小预绑定弹性网卡数 < BMS节点上绑定的弹性网卡数 < Pod正在使用的弹性网卡数 + 最大预绑定弹性网卡数   - BMS节点上当预绑定弹性网卡数 < 最小预绑定弹性网卡数时：会绑定弹性网卡，使得预绑定弹性网卡数 = 最小预绑定弹性网卡数   - BMS节点上当预绑定弹性网卡数 > 最大预绑定弹性网卡数时：会定时解绑弹性网卡（约2分钟一次），直到预绑定弹性网卡数 = 最大预绑定弹性网卡数   - 取值范围：[0.0, 1.0]; 一位小数; 低水位 <= 高水位 - 仅在turbo集群的BMS节点时，该字段才可配置。 - 弹性网卡预绑定能加快工作负载的创建，但会占用IP，请根据您的需求进行配置。 

        :return: The nic_threshold of this NodeExtendParam.
        :rtype: str
        """
        return self._nic_threshold

    @nic_threshold.setter
    def nic_threshold(self, nic_threshold):
        """Sets the nic_threshold of this NodeExtendParam.

        - 弹性网卡预绑定比例配置，默认配置示例如下： ``` \"0.3:0.6\" ```   - 第一位小数：预绑定低水位，弹性网卡预绑定的最低比例（最小预绑定弹性网卡数 = ⌊节点的总弹性网卡数 * 预绑定低水位⌋）   - 第二位小数：预绑定高水位，弹性网卡预绑定的最高比例（最大预绑定弹性网卡数 = ⌊节点的总弹性网卡数 * 预绑定高水位⌋）   - BMS节点上绑定的弹性网卡数：Pod正在使用的弹性网卡数 + 最小预绑定弹性网卡数 < BMS节点上绑定的弹性网卡数 < Pod正在使用的弹性网卡数 + 最大预绑定弹性网卡数   - BMS节点上当预绑定弹性网卡数 < 最小预绑定弹性网卡数时：会绑定弹性网卡，使得预绑定弹性网卡数 = 最小预绑定弹性网卡数   - BMS节点上当预绑定弹性网卡数 > 最大预绑定弹性网卡数时：会定时解绑弹性网卡（约2分钟一次），直到预绑定弹性网卡数 = 最大预绑定弹性网卡数   - 取值范围：[0.0, 1.0]; 一位小数; 低水位 <= 高水位 - 仅在turbo集群的BMS节点时，该字段才可配置。 - 弹性网卡预绑定能加快工作负载的创建，但会占用IP，请根据您的需求进行配置。 

        :param nic_threshold: The nic_threshold of this NodeExtendParam.
        :type nic_threshold: str
        """
        self._nic_threshold = nic_threshold

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this NodeExtendParam.

        节点所属的企业项目id。 

        :return: The enterprise_project_id of this NodeExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this NodeExtendParam.

        节点所属的企业项目id。 

        :param enterprise_project_id: The enterprise_project_id of this NodeExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def charging_mode(self):
        """Gets the charging_mode of this NodeExtendParam.

        节点的计费模式。已废弃，请使用NodeSpec中的billingMode字段。 

        :return: The charging_mode of this NodeExtendParam.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this NodeExtendParam.

        节点的计费模式。已废弃，请使用NodeSpec中的billingMode字段。 

        :param charging_mode: The charging_mode of this NodeExtendParam.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, NodeExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
