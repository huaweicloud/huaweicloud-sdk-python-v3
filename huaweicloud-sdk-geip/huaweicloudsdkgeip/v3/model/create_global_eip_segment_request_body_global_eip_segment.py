# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalEipSegmentRequestBodyGlobalEipSegment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'geip_pool_name': 'str',
        'access_site': 'str',
        'mask': 'int',
        'internet_bandwidth': 'CreateGlobalEipSegmentRequestBodyGlobalEipSegmentInternetBandwidth',
        'tags': 'list[CreateGlobalEipRequestBodyGlobalEipTags]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'geip_pool_name': 'geip_pool_name',
        'access_site': 'access_site',
        'mask': 'mask',
        'internet_bandwidth': 'internet_bandwidth',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, description=None, geip_pool_name=None, access_site=None, mask=None, internet_bandwidth=None, tags=None, enterprise_project_id=None):
        r"""CreateGlobalEipSegmentRequestBodyGlobalEipSegment

        The model defined in huaweicloud sdk

        :param name: - 功能说明：全域弹性公网IP段名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。
        :type description: str
        :param geip_pool_name: 全域弹性公网IP池子名称
        :type geip_pool_name: str
        :param access_site: 接入点信息
        :type access_site: str
        :param mask: 掩码长度。取值范围由GET /v3/{domain_id}/global-eip-segments/support-masks接口提供
        :type mask: int
        :param internet_bandwidth: 
        :type internet_bandwidth: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipSegmentRequestBodyGlobalEipSegmentInternetBandwidth`
        :param tags: 全域弹性公网IP段标签
        :type tags: list[:class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequestBodyGlobalEipTags`]
        :param enterprise_project_id: - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._description = None
        self._geip_pool_name = None
        self._access_site = None
        self._mask = None
        self._internet_bandwidth = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.geip_pool_name = geip_pool_name
        self.access_site = access_site
        self.mask = mask
        if internet_bandwidth is not None:
            self.internet_bandwidth = internet_bandwidth
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        - 功能说明：全域弹性公网IP段名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        - 功能说明：全域弹性公网IP段名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :return: The description of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :param description: The description of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type description: str
        """
        self._description = description

    @property
    def geip_pool_name(self):
        r"""Gets the geip_pool_name of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        全域弹性公网IP池子名称

        :return: The geip_pool_name of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._geip_pool_name

    @geip_pool_name.setter
    def geip_pool_name(self, geip_pool_name):
        r"""Sets the geip_pool_name of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        全域弹性公网IP池子名称

        :param geip_pool_name: The geip_pool_name of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type geip_pool_name: str
        """
        self._geip_pool_name = geip_pool_name

    @property
    def access_site(self):
        r"""Gets the access_site of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        接入点信息

        :return: The access_site of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        r"""Sets the access_site of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        接入点信息

        :param access_site: The access_site of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def mask(self):
        r"""Gets the mask of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        掩码长度。取值范围由GET /v3/{domain_id}/global-eip-segments/support-masks接口提供

        :return: The mask of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: int
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        r"""Sets the mask of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        掩码长度。取值范围由GET /v3/{domain_id}/global-eip-segments/support-masks接口提供

        :param mask: The mask of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type mask: int
        """
        self._mask = mask

    @property
    def internet_bandwidth(self):
        r"""Gets the internet_bandwidth of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        :return: The internet_bandwidth of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipSegmentRequestBodyGlobalEipSegmentInternetBandwidth`
        """
        return self._internet_bandwidth

    @internet_bandwidth.setter
    def internet_bandwidth(self, internet_bandwidth):
        r"""Sets the internet_bandwidth of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        :param internet_bandwidth: The internet_bandwidth of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type internet_bandwidth: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipSegmentRequestBodyGlobalEipSegmentInternetBandwidth`
        """
        self._internet_bandwidth = internet_bandwidth

    @property
    def tags(self):
        r"""Gets the tags of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        全域弹性公网IP段标签

        :return: The tags of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequestBodyGlobalEipTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        全域弹性公网IP段标签

        :param tags: The tags of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequestBodyGlobalEipTags`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :return: The enterprise_project_id of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.

        - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :param enterprise_project_id: The enterprise_project_id of this CreateGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateGlobalEipSegmentRequestBodyGlobalEipSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
