# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateInternetBandwidthRequestBodyInternetBandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ingress_size': 'int',
        'charge_mode': 'str',
        'isp': 'str',
        'access_site': 'str',
        'size': 'int',
        'name': 'str',
        'description': 'str',
        'count': 'int',
        'tags': 'list[CreateGlobalEipRequestBodyGlobalEipTags]',
        'enterprise_project_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'ingress_size': 'ingress_size',
        'charge_mode': 'charge_mode',
        'isp': 'isp',
        'access_site': 'access_site',
        'size': 'size',
        'name': 'name',
        'description': 'description',
        'count': 'count',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type'
    }

    def __init__(self, ingress_size=None, charge_mode=None, isp=None, access_site=None, size=None, name=None, description=None, count=None, tags=None, enterprise_project_id=None, type=None):
        """BatchCreateInternetBandwidthRequestBodyInternetBandwidth

        The model defined in huaweicloud sdk

        :param ingress_size: 全域公网带宽大小（入云方向）
        :type ingress_size: int
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param isp: 全域弹性公网IP所属线路
        :type isp: str
        :param access_site: 接入点信息
        :type access_site: str
        :param size: 全域公网带宽大小（出云方向）
        :type size: int
        :param name: - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。
        :type description: str
        :param count: 批创个数
        :type count: int
        :param tags: 全域公网带宽标签
        :type tags: list[:class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequestBodyGlobalEipTags`]
        :param enterprise_project_id: - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。
        :type enterprise_project_id: str
        :param type: 全域公网带宽类型
        :type type: str
        """
        
        

        self._ingress_size = None
        self._charge_mode = None
        self._isp = None
        self._access_site = None
        self._size = None
        self._name = None
        self._description = None
        self._count = None
        self._tags = None
        self._enterprise_project_id = None
        self._type = None
        self.discriminator = None

        if ingress_size is not None:
            self.ingress_size = ingress_size
        if charge_mode is not None:
            self.charge_mode = charge_mode
        self.isp = isp
        self.access_site = access_site
        self.size = size
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type

    @property
    def ingress_size(self):
        """Gets the ingress_size of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽大小（入云方向）

        :return: The ingress_size of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: int
        """
        return self._ingress_size

    @ingress_size.setter
    def ingress_size(self, ingress_size):
        """Sets the ingress_size of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽大小（入云方向）

        :param ingress_size: The ingress_size of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type ingress_size: int
        """
        self._ingress_size = ingress_size

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        计费模式

        :return: The charge_mode of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        计费模式

        :param charge_mode: The charge_mode of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def isp(self):
        """Gets the isp of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域弹性公网IP所属线路

        :return: The isp of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域弹性公网IP所属线路

        :param isp: The isp of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type isp: str
        """
        self._isp = isp

    @property
    def access_site(self):
        """Gets the access_site of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        接入点信息

        :return: The access_site of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        接入点信息

        :param access_site: The access_site of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def size(self):
        """Gets the size of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽大小（出云方向）

        :return: The size of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽大小（出云方向）

        :param size: The size of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def name(self):
        """Gets the name of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :return: The description of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :param description: The description of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type description: str
        """
        self._description = description

    @property
    def count(self):
        """Gets the count of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        批创个数

        :return: The count of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        批创个数

        :param count: The count of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type count: int
        """
        self._count = count

    @property
    def tags(self):
        """Gets the tags of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽标签

        :return: The tags of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequestBodyGlobalEipTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽标签

        :param tags: The tags of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequestBodyGlobalEipTags`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :return: The enterprise_project_id of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :param enterprise_project_id: The enterprise_project_id of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽类型

        :return: The type of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.

        全域公网带宽类型

        :param type: The type of this BatchCreateInternetBandwidthRequestBodyInternetBandwidth.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, BatchCreateInternetBandwidthRequestBodyInternetBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
