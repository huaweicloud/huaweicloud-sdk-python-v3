# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateNodeExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_pods': 'int',
        'docker_lvm_config_override': 'str',
        'alpha_cce_pre_install': 'str',
        'alpha_cce_post_install': 'str',
        'alpha_cce_node_image_id': 'str'
    }

    attribute_map = {
        'max_pods': 'maxPods',
        'docker_lvm_config_override': 'DockerLVMConfigOverride',
        'alpha_cce_pre_install': 'alpha.cce/preInstall',
        'alpha_cce_post_install': 'alpha.cce/postInstall',
        'alpha_cce_node_image_id': 'alpha.cce/NodeImageID'
    }

    def __init__(self, max_pods=None, docker_lvm_config_override=None, alpha_cce_pre_install=None, alpha_cce_post_install=None, alpha_cce_node_image_id=None):
        """MigrateNodeExtendParam

        The model defined in huaweicloud sdk

        :param max_pods: 节点最大允许创建的实例数(Pod)，该数量包含系统默认实例，取值范围为16~256。 该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。 
        :type max_pods: int
        :param docker_lvm_config_override: Docker数据盘配置项（已废弃，请使用storage字段）。  待迁移节点的磁盘类型须和创建时一致（即“DockerLVMConfigOverride”参数中“diskType”字段的值须和创建时一致），请确保单次接口调用时批量选择的节点磁盘类型一致。  默认配置示例如下：  &#x60;&#x60;&#x60; \&quot;DockerLVMConfigOverride\&quot;:\&quot;dockerThinpool&#x3D;vgpaas/90%VG;kubernetesLV&#x3D;vgpaas/10%VG;diskType&#x3D;evs;lvType&#x3D;linear\&quot; &#x60;&#x60;&#x60;  包含如下字段：   - userLV（可选）：用户空间的大小，示例格式：vgpaas/20%VG   - userPath（可选）：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG 
        :type docker_lvm_config_override: str
        :param alpha_cce_pre_install: 安装前执行脚本 &gt; 输入的值需要经过Base64编码，方法为echo -n \&quot;待编码内容\&quot; | base64。 
        :type alpha_cce_pre_install: str
        :param alpha_cce_post_install: 安装后执行脚本 &gt; 输入的值需要经过Base64编码，方法为echo -n \&quot;待编码内容\&quot; | base64。 
        :type alpha_cce_post_install: str
        :param alpha_cce_node_image_id: 指定待切换目标操作系统所使用的用户镜像ID。 当指定“alpha.cce/NodeImageID”参数时，“os”参数必须和用户自定义镜像的操作系统一致。 
        :type alpha_cce_node_image_id: str
        """
        
        

        self._max_pods = None
        self._docker_lvm_config_override = None
        self._alpha_cce_pre_install = None
        self._alpha_cce_post_install = None
        self._alpha_cce_node_image_id = None
        self.discriminator = None

        if max_pods is not None:
            self.max_pods = max_pods
        if docker_lvm_config_override is not None:
            self.docker_lvm_config_override = docker_lvm_config_override
        if alpha_cce_pre_install is not None:
            self.alpha_cce_pre_install = alpha_cce_pre_install
        if alpha_cce_post_install is not None:
            self.alpha_cce_post_install = alpha_cce_post_install
        if alpha_cce_node_image_id is not None:
            self.alpha_cce_node_image_id = alpha_cce_node_image_id

    @property
    def max_pods(self):
        """Gets the max_pods of this MigrateNodeExtendParam.

        节点最大允许创建的实例数(Pod)，该数量包含系统默认实例，取值范围为16~256。 该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。 

        :return: The max_pods of this MigrateNodeExtendParam.
        :rtype: int
        """
        return self._max_pods

    @max_pods.setter
    def max_pods(self, max_pods):
        """Sets the max_pods of this MigrateNodeExtendParam.

        节点最大允许创建的实例数(Pod)，该数量包含系统默认实例，取值范围为16~256。 该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。 

        :param max_pods: The max_pods of this MigrateNodeExtendParam.
        :type max_pods: int
        """
        self._max_pods = max_pods

    @property
    def docker_lvm_config_override(self):
        """Gets the docker_lvm_config_override of this MigrateNodeExtendParam.

        Docker数据盘配置项（已废弃，请使用storage字段）。  待迁移节点的磁盘类型须和创建时一致（即“DockerLVMConfigOverride”参数中“diskType”字段的值须和创建时一致），请确保单次接口调用时批量选择的节点磁盘类型一致。  默认配置示例如下：  ``` \"DockerLVMConfigOverride\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\" ```  包含如下字段：   - userLV（可选）：用户空间的大小，示例格式：vgpaas/20%VG   - userPath（可选）：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG 

        :return: The docker_lvm_config_override of this MigrateNodeExtendParam.
        :rtype: str
        """
        return self._docker_lvm_config_override

    @docker_lvm_config_override.setter
    def docker_lvm_config_override(self, docker_lvm_config_override):
        """Sets the docker_lvm_config_override of this MigrateNodeExtendParam.

        Docker数据盘配置项（已废弃，请使用storage字段）。  待迁移节点的磁盘类型须和创建时一致（即“DockerLVMConfigOverride”参数中“diskType”字段的值须和创建时一致），请确保单次接口调用时批量选择的节点磁盘类型一致。  默认配置示例如下：  ``` \"DockerLVMConfigOverride\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\" ```  包含如下字段：   - userLV（可选）：用户空间的大小，示例格式：vgpaas/20%VG   - userPath（可选）：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG 

        :param docker_lvm_config_override: The docker_lvm_config_override of this MigrateNodeExtendParam.
        :type docker_lvm_config_override: str
        """
        self._docker_lvm_config_override = docker_lvm_config_override

    @property
    def alpha_cce_pre_install(self):
        """Gets the alpha_cce_pre_install of this MigrateNodeExtendParam.

        安装前执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :return: The alpha_cce_pre_install of this MigrateNodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_pre_install

    @alpha_cce_pre_install.setter
    def alpha_cce_pre_install(self, alpha_cce_pre_install):
        """Sets the alpha_cce_pre_install of this MigrateNodeExtendParam.

        安装前执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :param alpha_cce_pre_install: The alpha_cce_pre_install of this MigrateNodeExtendParam.
        :type alpha_cce_pre_install: str
        """
        self._alpha_cce_pre_install = alpha_cce_pre_install

    @property
    def alpha_cce_post_install(self):
        """Gets the alpha_cce_post_install of this MigrateNodeExtendParam.

        安装后执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :return: The alpha_cce_post_install of this MigrateNodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_post_install

    @alpha_cce_post_install.setter
    def alpha_cce_post_install(self, alpha_cce_post_install):
        """Sets the alpha_cce_post_install of this MigrateNodeExtendParam.

        安装后执行脚本 > 输入的值需要经过Base64编码，方法为echo -n \"待编码内容\" | base64。 

        :param alpha_cce_post_install: The alpha_cce_post_install of this MigrateNodeExtendParam.
        :type alpha_cce_post_install: str
        """
        self._alpha_cce_post_install = alpha_cce_post_install

    @property
    def alpha_cce_node_image_id(self):
        """Gets the alpha_cce_node_image_id of this MigrateNodeExtendParam.

        指定待切换目标操作系统所使用的用户镜像ID。 当指定“alpha.cce/NodeImageID”参数时，“os”参数必须和用户自定义镜像的操作系统一致。 

        :return: The alpha_cce_node_image_id of this MigrateNodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_node_image_id

    @alpha_cce_node_image_id.setter
    def alpha_cce_node_image_id(self, alpha_cce_node_image_id):
        """Sets the alpha_cce_node_image_id of this MigrateNodeExtendParam.

        指定待切换目标操作系统所使用的用户镜像ID。 当指定“alpha.cce/NodeImageID”参数时，“os”参数必须和用户自定义镜像的操作系统一致。 

        :param alpha_cce_node_image_id: The alpha_cce_node_image_id of this MigrateNodeExtendParam.
        :type alpha_cce_node_image_id: str
        """
        self._alpha_cce_node_image_id = alpha_cce_node_image_id

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
        if not isinstance(other, MigrateNodeExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
