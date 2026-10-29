# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpResourceResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extra_info': 'OpResourceExtraInfoResp',
        'id': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'extra_info': 'extra_info',
        'id': 'id',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, extra_info=None, id=None, name=None, type=None):
        r"""OpResourceResp

        The model defined in huaweicloud sdk

        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkcbr.v1.OpResourceExtraInfoResp`
        :param id: **参数解释：** 待备份资源ID，用于标识需要备份的资源。 [获取方法请参见\&quot;[查询存储库绑定资源信息](https://support.huaweicloud.com/api-cbr/ShowVault.html)\&quot;，\&quot;[查询资源可保护性](https://support.huaweicloud.com/api-cbr/ShowProtectable.html)\&quot;。](tag:hws) [获取方法请参见\&quot;[查询存储库绑定资源信息](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ShowVault.html)\&quot;，\&quot;[查询资源可保护性](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ShowProtectable.html)\&quot;。](tag:hws_hk) **取值范围：** 格式为UUID
        :type id: str
        :param name: **参数解释：** 待备份资源名称，用于标识待备份的资源名称。 **取值范围：** 长度为0~255个字符。
        :type name: str
        :param type: **参数解释：** 待备份资源的类型，用于指定待备份的资源类型，不同类型对应不同的云服务资源。 **取值范围：** [OS::Nova::Server：云服务器； OS::Cinder::Volume：云硬盘；OS::Ironic::BareMetalServer：裸金属服务器；OS::Sfs::Turbo：SFS Turbo文件系统；OS::Workspace::DesktopV2：云桌面。](tag:hws,hws_hk) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘；OS::Sfs::Turbo：SFS Turbo文件系统。](tag:hk_g42,sbc,dt) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘；OS::Ironic::BareMetalServer：裸金属服务器；OS::Sfs::Turbo：SFS Turbo文件系统。](tag:fcs_vm,ctc,ocb,tm) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘。](tag:tlf,cmcc,hcso_dt) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘；OS::Sfs::Turbo：SFS Turbo文件系统；OS::Workspace::DesktopV2：云桌面。](tag:g42)
        :type type: str
        """
        
        

        self._extra_info = None
        self._id = None
        self._name = None
        self._type = None
        self.discriminator = None

        if extra_info is not None:
            self.extra_info = extra_info
        self.id = id
        if name is not None:
            self.name = name
        self.type = type

    @property
    def extra_info(self):
        r"""Gets the extra_info of this OpResourceResp.

        :return: The extra_info of this OpResourceResp.
        :rtype: :class:`huaweicloudsdkcbr.v1.OpResourceExtraInfoResp`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this OpResourceResp.

        :param extra_info: The extra_info of this OpResourceResp.
        :type extra_info: :class:`huaweicloudsdkcbr.v1.OpResourceExtraInfoResp`
        """
        self._extra_info = extra_info

    @property
    def id(self):
        r"""Gets the id of this OpResourceResp.

        **参数解释：** 待备份资源ID，用于标识需要备份的资源。 [获取方法请参见\"[查询存储库绑定资源信息](https://support.huaweicloud.com/api-cbr/ShowVault.html)\"，\"[查询资源可保护性](https://support.huaweicloud.com/api-cbr/ShowProtectable.html)\"。](tag:hws) [获取方法请参见\"[查询存储库绑定资源信息](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ShowVault.html)\"，\"[查询资源可保护性](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ShowProtectable.html)\"。](tag:hws_hk) **取值范围：** 格式为UUID

        :return: The id of this OpResourceResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpResourceResp.

        **参数解释：** 待备份资源ID，用于标识需要备份的资源。 [获取方法请参见\"[查询存储库绑定资源信息](https://support.huaweicloud.com/api-cbr/ShowVault.html)\"，\"[查询资源可保护性](https://support.huaweicloud.com/api-cbr/ShowProtectable.html)\"。](tag:hws) [获取方法请参见\"[查询存储库绑定资源信息](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ShowVault.html)\"，\"[查询资源可保护性](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ShowProtectable.html)\"。](tag:hws_hk) **取值范围：** 格式为UUID

        :param id: The id of this OpResourceResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OpResourceResp.

        **参数解释：** 待备份资源名称，用于标识待备份的资源名称。 **取值范围：** 长度为0~255个字符。

        :return: The name of this OpResourceResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpResourceResp.

        **参数解释：** 待备份资源名称，用于标识待备份的资源名称。 **取值范围：** 长度为0~255个字符。

        :param name: The name of this OpResourceResp.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this OpResourceResp.

        **参数解释：** 待备份资源的类型，用于指定待备份的资源类型，不同类型对应不同的云服务资源。 **取值范围：** [OS::Nova::Server：云服务器； OS::Cinder::Volume：云硬盘；OS::Ironic::BareMetalServer：裸金属服务器；OS::Sfs::Turbo：SFS Turbo文件系统；OS::Workspace::DesktopV2：云桌面。](tag:hws,hws_hk) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘；OS::Sfs::Turbo：SFS Turbo文件系统。](tag:hk_g42,sbc,dt) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘；OS::Ironic::BareMetalServer：裸金属服务器；OS::Sfs::Turbo：SFS Turbo文件系统。](tag:fcs_vm,ctc,ocb,tm) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘。](tag:tlf,cmcc,hcso_dt) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘；OS::Sfs::Turbo：SFS Turbo文件系统；OS::Workspace::DesktopV2：云桌面。](tag:g42)

        :return: The type of this OpResourceResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpResourceResp.

        **参数解释：** 待备份资源的类型，用于指定待备份的资源类型，不同类型对应不同的云服务资源。 **取值范围：** [OS::Nova::Server：云服务器； OS::Cinder::Volume：云硬盘；OS::Ironic::BareMetalServer：裸金属服务器；OS::Sfs::Turbo：SFS Turbo文件系统；OS::Workspace::DesktopV2：云桌面。](tag:hws,hws_hk) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘；OS::Sfs::Turbo：SFS Turbo文件系统。](tag:hk_g42,sbc,dt) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘；OS::Ironic::BareMetalServer：裸金属服务器；OS::Sfs::Turbo：SFS Turbo文件系统。](tag:fcs_vm,ctc,ocb,tm) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘。](tag:tlf,cmcc,hcso_dt) [OS::Nova::Server：云服务器；OS::Cinder::Volume：云硬盘；OS::Sfs::Turbo：SFS Turbo文件系统；OS::Workspace::DesktopV2：云桌面。](tag:g42)

        :param type: The type of this OpResourceResp.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, OpResourceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
