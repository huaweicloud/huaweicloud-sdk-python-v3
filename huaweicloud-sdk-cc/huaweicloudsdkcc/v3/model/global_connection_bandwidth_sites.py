# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalConnectionBandwidthSites:

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
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'name_en': 'str',
        'name_cn': 'str',
        'site_code': 'str',
        'site_type': 'str',
        'service_list': 'str',
        'group_list': 'list[SiteGroupReferenceInfo]',
        'region_id': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'name_en': 'name_en',
        'name_cn': 'name_cn',
        'site_code': 'site_code',
        'site_type': 'site_type',
        'service_list': 'service_list',
        'group_list': 'group_list',
        'region_id': 'region_id',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, id=None, description=None, created_at=None, updated_at=None, name_en=None, name_cn=None, site_code=None, site_type=None, service_list=None, group_list=None, region_id=None, public_border_group=None):
        r"""GlobalConnectionBandwidthSites

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param name_en: 功能说明：站点信息自定义的英文名字。 取值范围：1-255个字符
        :type name_en: str
        :param name_cn: 功能说明：站点信息自定义的中文名字。 取值范围：1-64个字符。
        :type name_cn: str
        :param site_code: 功能说明：站点编码，格式为&lt;area_code&gt;[-&lt;subarea_code&gt;[-&lt;region_code&gt;]]。 取值范围：1-64个字符。
        :type site_code: str
        :param site_type: 功能说明：站点类型，必须跟站点编码对应，一段编码为大区，两段编码为区域，三段编码为城域。 取值范围： - Area: 大区站点 - SubArea: 区域站点 - Region: 城域站点
        :type site_type: str
        :param service_list: 功能说明：站点支持的服务列表，多个服务用\&quot;,\&quot;分隔。 取值范围：0-255个字符
        :type service_list: str
        :param group_list: 
        :type group_list: list[:class:`huaweicloudsdkcc.v3.SiteGroupReferenceInfo`]
        :param region_id: 功能说明：对应华为云标准region的id，该站点继承自华为云region时才需要填写该字段。 取值范围：0-64个字符。
        :type region_id: str
        :param public_border_group: 功能说明：用于标记是中心还是边缘站点。中心：center 取值范围：0-255个字符。
        :type public_border_group: str
        """
        
        

        self._id = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._name_en = None
        self._name_cn = None
        self._site_code = None
        self._site_type = None
        self._service_list = None
        self._group_list = None
        self._region_id = None
        self._public_border_group = None
        self.discriminator = None

        self.id = id
        if description is not None:
            self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        if name_en is not None:
            self.name_en = name_en
        if name_cn is not None:
            self.name_cn = name_cn
        if site_code is not None:
            self.site_code = site_code
        if site_type is not None:
            self.site_type = site_type
        if service_list is not None:
            self.service_list = service_list
        if group_list is not None:
            self.group_list = group_list
        if region_id is not None:
            self.region_id = region_id
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def id(self):
        r"""Gets the id of this GlobalConnectionBandwidthSites.

        实例ID。

        :return: The id of this GlobalConnectionBandwidthSites.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GlobalConnectionBandwidthSites.

        实例ID。

        :param id: The id of this GlobalConnectionBandwidthSites.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this GlobalConnectionBandwidthSites.

        实例描述。不支持 <>。

        :return: The description of this GlobalConnectionBandwidthSites.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GlobalConnectionBandwidthSites.

        实例描述。不支持 <>。

        :param description: The description of this GlobalConnectionBandwidthSites.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this GlobalConnectionBandwidthSites.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this GlobalConnectionBandwidthSites.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GlobalConnectionBandwidthSites.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this GlobalConnectionBandwidthSites.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GlobalConnectionBandwidthSites.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this GlobalConnectionBandwidthSites.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GlobalConnectionBandwidthSites.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this GlobalConnectionBandwidthSites.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def name_en(self):
        r"""Gets the name_en of this GlobalConnectionBandwidthSites.

        功能说明：站点信息自定义的英文名字。 取值范围：1-255个字符

        :return: The name_en of this GlobalConnectionBandwidthSites.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this GlobalConnectionBandwidthSites.

        功能说明：站点信息自定义的英文名字。 取值范围：1-255个字符

        :param name_en: The name_en of this GlobalConnectionBandwidthSites.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_cn(self):
        r"""Gets the name_cn of this GlobalConnectionBandwidthSites.

        功能说明：站点信息自定义的中文名字。 取值范围：1-64个字符。

        :return: The name_cn of this GlobalConnectionBandwidthSites.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this GlobalConnectionBandwidthSites.

        功能说明：站点信息自定义的中文名字。 取值范围：1-64个字符。

        :param name_cn: The name_cn of this GlobalConnectionBandwidthSites.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def site_code(self):
        r"""Gets the site_code of this GlobalConnectionBandwidthSites.

        功能说明：站点编码，格式为<area_code>[-<subarea_code>[-<region_code>]]。 取值范围：1-64个字符。

        :return: The site_code of this GlobalConnectionBandwidthSites.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this GlobalConnectionBandwidthSites.

        功能说明：站点编码，格式为<area_code>[-<subarea_code>[-<region_code>]]。 取值范围：1-64个字符。

        :param site_code: The site_code of this GlobalConnectionBandwidthSites.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def site_type(self):
        r"""Gets the site_type of this GlobalConnectionBandwidthSites.

        功能说明：站点类型，必须跟站点编码对应，一段编码为大区，两段编码为区域，三段编码为城域。 取值范围： - Area: 大区站点 - SubArea: 区域站点 - Region: 城域站点

        :return: The site_type of this GlobalConnectionBandwidthSites.
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        r"""Sets the site_type of this GlobalConnectionBandwidthSites.

        功能说明：站点类型，必须跟站点编码对应，一段编码为大区，两段编码为区域，三段编码为城域。 取值范围： - Area: 大区站点 - SubArea: 区域站点 - Region: 城域站点

        :param site_type: The site_type of this GlobalConnectionBandwidthSites.
        :type site_type: str
        """
        self._site_type = site_type

    @property
    def service_list(self):
        r"""Gets the service_list of this GlobalConnectionBandwidthSites.

        功能说明：站点支持的服务列表，多个服务用\",\"分隔。 取值范围：0-255个字符

        :return: The service_list of this GlobalConnectionBandwidthSites.
        :rtype: str
        """
        return self._service_list

    @service_list.setter
    def service_list(self, service_list):
        r"""Sets the service_list of this GlobalConnectionBandwidthSites.

        功能说明：站点支持的服务列表，多个服务用\",\"分隔。 取值范围：0-255个字符

        :param service_list: The service_list of this GlobalConnectionBandwidthSites.
        :type service_list: str
        """
        self._service_list = service_list

    @property
    def group_list(self):
        r"""Gets the group_list of this GlobalConnectionBandwidthSites.

        :return: The group_list of this GlobalConnectionBandwidthSites.
        :rtype: list[:class:`huaweicloudsdkcc.v3.SiteGroupReferenceInfo`]
        """
        return self._group_list

    @group_list.setter
    def group_list(self, group_list):
        r"""Sets the group_list of this GlobalConnectionBandwidthSites.

        :param group_list: The group_list of this GlobalConnectionBandwidthSites.
        :type group_list: list[:class:`huaweicloudsdkcc.v3.SiteGroupReferenceInfo`]
        """
        self._group_list = group_list

    @property
    def region_id(self):
        r"""Gets the region_id of this GlobalConnectionBandwidthSites.

        功能说明：对应华为云标准region的id，该站点继承自华为云region时才需要填写该字段。 取值范围：0-64个字符。

        :return: The region_id of this GlobalConnectionBandwidthSites.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this GlobalConnectionBandwidthSites.

        功能说明：对应华为云标准region的id，该站点继承自华为云region时才需要填写该字段。 取值范围：0-64个字符。

        :param region_id: The region_id of this GlobalConnectionBandwidthSites.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this GlobalConnectionBandwidthSites.

        功能说明：用于标记是中心还是边缘站点。中心：center 取值范围：0-255个字符。

        :return: The public_border_group of this GlobalConnectionBandwidthSites.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this GlobalConnectionBandwidthSites.

        功能说明：用于标记是中心还是边缘站点。中心：center 取值范围：0-255个字符。

        :param public_border_group: The public_border_group of this GlobalConnectionBandwidthSites.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, GlobalConnectionBandwidthSites):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
