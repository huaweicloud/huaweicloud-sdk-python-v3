# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWhiteListDetailResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'vul_id': 'str',
        'vul_name': 'str',
        'vul_type': 'str',
        'cves': 'list[ImageWhiteListDetailResponseInfoCves]',
        'rule_type': 'str',
        'query_info': 'ImageWhiteListDetailResponseInfoQueryInfo',
        'image_info': 'list[ImageWhiteListDetailResponseInfoImageInfo]',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'vul_type': 'vul_type',
        'cves': 'cves',
        'rule_type': 'rule_type',
        'query_info': 'query_info',
        'image_info': 'image_info',
        'description': 'description'
    }

    def __init__(self, id=None, vul_id=None, vul_name=None, vul_type=None, cves=None, rule_type=None, query_info=None, image_info=None, description=None):
        r"""ImageWhiteListDetailResponseInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 白名单ID **取值范围**： 字符长度0-64位 
        :type id: str
        :param vul_id: **参数解释**： 漏洞ID（只在查询漏洞白名单时返回） **取值范围**： 字符长度0-256位 
        :type vul_id: str
        :param vul_name: **参数解释**： 漏洞名称（只在查询漏洞白名单时返回） **取值范围**： 字符长度0-256位 
        :type vul_name: str
        :param vul_type: **参数解释**： 漏洞类型（只在查询漏洞白名单时返回） **取值范围**: - linux_vul：linux漏洞。 - app_vul：应用漏洞。 
        :type vul_type: str
        :param cves: **参数解释**: 漏洞对应的CVE列表（只在查询漏洞白名单时返回） **取值范围**: 最小值0，最大值1000 
        :type cves: list[:class:`huaweicloudsdkhss.v5.ImageWhiteListDetailResponseInfoCves`]
        :param rule_type: 白名单规则类型，包含如下：   -all_images : 白名单应用于全部镜像   -specific_image_types : 白名单应用于指定镜像类型(仅用于指定仓库镜像类型)   -specific_images : 白名单应用于指定镜像
        :type rule_type: str
        :param query_info: 
        :type query_info: :class:`huaweicloudsdkhss.v5.ImageWhiteListDetailResponseInfoQueryInfo`
        :param image_info: 白名单规则为“specific_images”时，指定的镜像列表。只在查询镜像白名单详情时返回数据。
        :type image_info: list[:class:`huaweicloudsdkhss.v5.ImageWhiteListDetailResponseInfoImageInfo`]
        :param description: **参数解释**： 白名单的描述信息 **取值范围**： 字符长度0-1024位 
        :type description: str
        """
        
        

        self._id = None
        self._vul_id = None
        self._vul_name = None
        self._vul_type = None
        self._cves = None
        self._rule_type = None
        self._query_info = None
        self._image_info = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if vul_type is not None:
            self.vul_type = vul_type
        if cves is not None:
            self.cves = cves
        if rule_type is not None:
            self.rule_type = rule_type
        if query_info is not None:
            self.query_info = query_info
        if image_info is not None:
            self.image_info = image_info
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 白名单ID **取值范围**： 字符长度0-64位 

        :return: The id of this ImageWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 白名单ID **取值范围**： 字符长度0-64位 

        :param id: The id of this ImageWhiteListDetailResponseInfo.
        :type id: str
        """
        self._id = id

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 漏洞ID（只在查询漏洞白名单时返回） **取值范围**： 字符长度0-256位 

        :return: The vul_id of this ImageWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 漏洞ID（只在查询漏洞白名单时返回） **取值范围**： 字符长度0-256位 

        :param vul_id: The vul_id of this ImageWhiteListDetailResponseInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 漏洞名称（只在查询漏洞白名单时返回） **取值范围**： 字符长度0-256位 

        :return: The vul_name of this ImageWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 漏洞名称（只在查询漏洞白名单时返回） **取值范围**： 字符长度0-256位 

        :param vul_name: The vul_name of this ImageWhiteListDetailResponseInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_type(self):
        r"""Gets the vul_type of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 漏洞类型（只在查询漏洞白名单时返回） **取值范围**: - linux_vul：linux漏洞。 - app_vul：应用漏洞。 

        :return: The vul_type of this ImageWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        r"""Sets the vul_type of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 漏洞类型（只在查询漏洞白名单时返回） **取值范围**: - linux_vul：linux漏洞。 - app_vul：应用漏洞。 

        :param vul_type: The vul_type of this ImageWhiteListDetailResponseInfo.
        :type vul_type: str
        """
        self._vul_type = vul_type

    @property
    def cves(self):
        r"""Gets the cves of this ImageWhiteListDetailResponseInfo.

        **参数解释**: 漏洞对应的CVE列表（只在查询漏洞白名单时返回） **取值范围**: 最小值0，最大值1000 

        :return: The cves of this ImageWhiteListDetailResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ImageWhiteListDetailResponseInfoCves`]
        """
        return self._cves

    @cves.setter
    def cves(self, cves):
        r"""Sets the cves of this ImageWhiteListDetailResponseInfo.

        **参数解释**: 漏洞对应的CVE列表（只在查询漏洞白名单时返回） **取值范围**: 最小值0，最大值1000 

        :param cves: The cves of this ImageWhiteListDetailResponseInfo.
        :type cves: list[:class:`huaweicloudsdkhss.v5.ImageWhiteListDetailResponseInfoCves`]
        """
        self._cves = cves

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ImageWhiteListDetailResponseInfo.

        白名单规则类型，包含如下：   -all_images : 白名单应用于全部镜像   -specific_image_types : 白名单应用于指定镜像类型(仅用于指定仓库镜像类型)   -specific_images : 白名单应用于指定镜像

        :return: The rule_type of this ImageWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ImageWhiteListDetailResponseInfo.

        白名单规则类型，包含如下：   -all_images : 白名单应用于全部镜像   -specific_image_types : 白名单应用于指定镜像类型(仅用于指定仓库镜像类型)   -specific_images : 白名单应用于指定镜像

        :param rule_type: The rule_type of this ImageWhiteListDetailResponseInfo.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def query_info(self):
        r"""Gets the query_info of this ImageWhiteListDetailResponseInfo.

        :return: The query_info of this ImageWhiteListDetailResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ImageWhiteListDetailResponseInfoQueryInfo`
        """
        return self._query_info

    @query_info.setter
    def query_info(self, query_info):
        r"""Sets the query_info of this ImageWhiteListDetailResponseInfo.

        :param query_info: The query_info of this ImageWhiteListDetailResponseInfo.
        :type query_info: :class:`huaweicloudsdkhss.v5.ImageWhiteListDetailResponseInfoQueryInfo`
        """
        self._query_info = query_info

    @property
    def image_info(self):
        r"""Gets the image_info of this ImageWhiteListDetailResponseInfo.

        白名单规则为“specific_images”时，指定的镜像列表。只在查询镜像白名单详情时返回数据。

        :return: The image_info of this ImageWhiteListDetailResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ImageWhiteListDetailResponseInfoImageInfo`]
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        r"""Sets the image_info of this ImageWhiteListDetailResponseInfo.

        白名单规则为“specific_images”时，指定的镜像列表。只在查询镜像白名单详情时返回数据。

        :param image_info: The image_info of this ImageWhiteListDetailResponseInfo.
        :type image_info: list[:class:`huaweicloudsdkhss.v5.ImageWhiteListDetailResponseInfoImageInfo`]
        """
        self._image_info = image_info

    @property
    def description(self):
        r"""Gets the description of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 白名单的描述信息 **取值范围**： 字符长度0-1024位 

        :return: The description of this ImageWhiteListDetailResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageWhiteListDetailResponseInfo.

        **参数解释**： 白名单的描述信息 **取值范围**： 字符长度0-1024位 

        :param description: The description of this ImageWhiteListDetailResponseInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ImageWhiteListDetailResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
