# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2JobSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'clusteruid': 'str',
        'resourceid': 'str',
        'resourcename': 'str',
        'extendparam': 'dict(str, str)',
        'subjobs': 'list[V2Job]'
    }

    attribute_map = {
        'type': 'type',
        'clusteruid': 'clusteruid',
        'resourceid': 'resourceid',
        'resourcename': 'resourcename',
        'extendparam': 'extendparam',
        'subjobs': 'subjobs'
    }

    def __init__(self, type=None, clusteruid=None, resourceid=None, resourcename=None, extendparam=None, subjobs=None):
        r"""V2JobSpec

        The model defined in huaweicloud sdk

        :param type: **参数解释**： Job 类型 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type type: str
        :param clusteruid: **参数解释**： 集群ID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type clusteruid: str
        :param resourceid: **参数解释**： 资源ID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type resourceid: str
        :param resourcename: **参数解释**： 资源名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type resourcename: str
        :param extendparam: **参数解释**： Job的扩容参数 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type extendparam: dict(str, str)
        :param subjobs: **参数解释**： 子Job详情列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type subjobs: list[:class:`huaweicloudsdkcce.v3.V2Job`]
        """
        
        

        self._type = None
        self._clusteruid = None
        self._resourceid = None
        self._resourcename = None
        self._extendparam = None
        self._subjobs = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if clusteruid is not None:
            self.clusteruid = clusteruid
        if resourceid is not None:
            self.resourceid = resourceid
        if resourcename is not None:
            self.resourcename = resourcename
        if extendparam is not None:
            self.extendparam = extendparam
        if subjobs is not None:
            self.subjobs = subjobs

    @property
    def type(self):
        r"""Gets the type of this V2JobSpec.

        **参数解释**： Job 类型 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The type of this V2JobSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this V2JobSpec.

        **参数解释**： Job 类型 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param type: The type of this V2JobSpec.
        :type type: str
        """
        self._type = type

    @property
    def clusteruid(self):
        r"""Gets the clusteruid of this V2JobSpec.

        **参数解释**： 集群ID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The clusteruid of this V2JobSpec.
        :rtype: str
        """
        return self._clusteruid

    @clusteruid.setter
    def clusteruid(self, clusteruid):
        r"""Sets the clusteruid of this V2JobSpec.

        **参数解释**： 集群ID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param clusteruid: The clusteruid of this V2JobSpec.
        :type clusteruid: str
        """
        self._clusteruid = clusteruid

    @property
    def resourceid(self):
        r"""Gets the resourceid of this V2JobSpec.

        **参数解释**： 资源ID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The resourceid of this V2JobSpec.
        :rtype: str
        """
        return self._resourceid

    @resourceid.setter
    def resourceid(self, resourceid):
        r"""Sets the resourceid of this V2JobSpec.

        **参数解释**： 资源ID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param resourceid: The resourceid of this V2JobSpec.
        :type resourceid: str
        """
        self._resourceid = resourceid

    @property
    def resourcename(self):
        r"""Gets the resourcename of this V2JobSpec.

        **参数解释**： 资源名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The resourcename of this V2JobSpec.
        :rtype: str
        """
        return self._resourcename

    @resourcename.setter
    def resourcename(self, resourcename):
        r"""Sets the resourcename of this V2JobSpec.

        **参数解释**： 资源名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param resourcename: The resourcename of this V2JobSpec.
        :type resourcename: str
        """
        self._resourcename = resourcename

    @property
    def extendparam(self):
        r"""Gets the extendparam of this V2JobSpec.

        **参数解释**： Job的扩容参数 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The extendparam of this V2JobSpec.
        :rtype: dict(str, str)
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        r"""Sets the extendparam of this V2JobSpec.

        **参数解释**： Job的扩容参数 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param extendparam: The extendparam of this V2JobSpec.
        :type extendparam: dict(str, str)
        """
        self._extendparam = extendparam

    @property
    def subjobs(self):
        r"""Gets the subjobs of this V2JobSpec.

        **参数解释**： 子Job详情列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The subjobs of this V2JobSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.V2Job`]
        """
        return self._subjobs

    @subjobs.setter
    def subjobs(self, subjobs):
        r"""Sets the subjobs of this V2JobSpec.

        **参数解释**： 子Job详情列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param subjobs: The subjobs of this V2JobSpec.
        :type subjobs: list[:class:`huaweicloudsdkcce.v3.V2Job`]
        """
        self._subjobs = subjobs

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
        if not isinstance(other, V2JobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
