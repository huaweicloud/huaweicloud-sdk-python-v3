# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DescribeStoreData:

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
        'store_name': 'str',
        'status': 'str',
        'create_time': 'str',
        'region': 'str',
        'availability_zones': 'list[str]',
        'flavor': 'Flavor',
        'charge_info': 'ChargeInfo',
        'description': 'str',
        'private_link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'store_name': 'store_name',
        'status': 'status',
        'create_time': 'create_time',
        'region': 'region',
        'availability_zones': 'availability_zones',
        'flavor': 'flavor',
        'charge_info': 'charge_info',
        'description': 'description',
        'private_link': 'private_link'
    }

    def __init__(self, id=None, store_name=None, status=None, create_time=None, region=None, availability_zones=None, flavor=None, charge_info=None, description=None, private_link=None):
        r"""DescribeStoreData

        The model defined in huaweicloud sdk

        :param id: 知识仓实例id
        :type id: str
        :param store_name: 知识仓实例名称，全域唯一。  支持字符，数字，_。必须以字母或下划线 (_) 开头；字符长度是1-64个字节；
        :type store_name: str
        :param status: 知识仓实例状态。取值范围： \&quot;CREATING\&quot; - 创建中, \&quot;NORMAL\&quot; - 正常, \&quot;CREATED_FAILED\&quot; - 创建失败, \&quot;ABNORMAL\&quot; - 异常, \&quot;FROZEN\&quot; - 被冻结, \&quot;DISK_FULL\&quot;-存储空间已满,  \&quot;DROPPING\&quot; - 删除中,\&quot;DELETE_FAILED\&quot; - 删除失败
        :type status: str
        :param create_time: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。
        :type create_time: str
        :param region: 区域ID。  取值范围：非空，请参见地区和终端节点。
        :type region: str
        :param availability_zones: 可用区ID。
        :type availability_zones: list[str]
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkdwr.v1.Flavor`
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkdwr.v1.ChargeInfo`
        :param description: 知识仓描述信息。
        :type description: str
        :param private_link: 知识仓的私网链接信息。
        :type private_link: str
        """
        
        

        self._id = None
        self._store_name = None
        self._status = None
        self._create_time = None
        self._region = None
        self._availability_zones = None
        self._flavor = None
        self._charge_info = None
        self._description = None
        self._private_link = None
        self.discriminator = None

        self.id = id
        self.store_name = store_name
        self.status = status
        if create_time is not None:
            self.create_time = create_time
        if region is not None:
            self.region = region
        if availability_zones is not None:
            self.availability_zones = availability_zones
        if flavor is not None:
            self.flavor = flavor
        if charge_info is not None:
            self.charge_info = charge_info
        if description is not None:
            self.description = description
        self.private_link = private_link

    @property
    def id(self):
        r"""Gets the id of this DescribeStoreData.

        知识仓实例id

        :return: The id of this DescribeStoreData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DescribeStoreData.

        知识仓实例id

        :param id: The id of this DescribeStoreData.
        :type id: str
        """
        self._id = id

    @property
    def store_name(self):
        r"""Gets the store_name of this DescribeStoreData.

        知识仓实例名称，全域唯一。  支持字符，数字，_。必须以字母或下划线 (_) 开头；字符长度是1-64个字节；

        :return: The store_name of this DescribeStoreData.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this DescribeStoreData.

        知识仓实例名称，全域唯一。  支持字符，数字，_。必须以字母或下划线 (_) 开头；字符长度是1-64个字节；

        :param store_name: The store_name of this DescribeStoreData.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def status(self):
        r"""Gets the status of this DescribeStoreData.

        知识仓实例状态。取值范围： \"CREATING\" - 创建中, \"NORMAL\" - 正常, \"CREATED_FAILED\" - 创建失败, \"ABNORMAL\" - 异常, \"FROZEN\" - 被冻结, \"DISK_FULL\"-存储空间已满,  \"DROPPING\" - 删除中,\"DELETE_FAILED\" - 删除失败

        :return: The status of this DescribeStoreData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DescribeStoreData.

        知识仓实例状态。取值范围： \"CREATING\" - 创建中, \"NORMAL\" - 正常, \"CREATED_FAILED\" - 创建失败, \"ABNORMAL\" - 异常, \"FROZEN\" - 被冻结, \"DISK_FULL\"-存储空间已满,  \"DROPPING\" - 删除中,\"DELETE_FAILED\" - 删除失败

        :param status: The status of this DescribeStoreData.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this DescribeStoreData.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。

        :return: The create_time of this DescribeStoreData.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DescribeStoreData.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。

        :param create_time: The create_time of this DescribeStoreData.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def region(self):
        r"""Gets the region of this DescribeStoreData.

        区域ID。  取值范围：非空，请参见地区和终端节点。

        :return: The region of this DescribeStoreData.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DescribeStoreData.

        区域ID。  取值范围：非空，请参见地区和终端节点。

        :param region: The region of this DescribeStoreData.
        :type region: str
        """
        self._region = region

    @property
    def availability_zones(self):
        r"""Gets the availability_zones of this DescribeStoreData.

        可用区ID。

        :return: The availability_zones of this DescribeStoreData.
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        r"""Sets the availability_zones of this DescribeStoreData.

        可用区ID。

        :param availability_zones: The availability_zones of this DescribeStoreData.
        :type availability_zones: list[str]
        """
        self._availability_zones = availability_zones

    @property
    def flavor(self):
        r"""Gets the flavor of this DescribeStoreData.

        :return: The flavor of this DescribeStoreData.
        :rtype: :class:`huaweicloudsdkdwr.v1.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this DescribeStoreData.

        :param flavor: The flavor of this DescribeStoreData.
        :type flavor: :class:`huaweicloudsdkdwr.v1.Flavor`
        """
        self._flavor = flavor

    @property
    def charge_info(self):
        r"""Gets the charge_info of this DescribeStoreData.

        :return: The charge_info of this DescribeStoreData.
        :rtype: :class:`huaweicloudsdkdwr.v1.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this DescribeStoreData.

        :param charge_info: The charge_info of this DescribeStoreData.
        :type charge_info: :class:`huaweicloudsdkdwr.v1.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def description(self):
        r"""Gets the description of this DescribeStoreData.

        知识仓描述信息。

        :return: The description of this DescribeStoreData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DescribeStoreData.

        知识仓描述信息。

        :param description: The description of this DescribeStoreData.
        :type description: str
        """
        self._description = description

    @property
    def private_link(self):
        r"""Gets the private_link of this DescribeStoreData.

        知识仓的私网链接信息。

        :return: The private_link of this DescribeStoreData.
        :rtype: str
        """
        return self._private_link

    @private_link.setter
    def private_link(self, private_link):
        r"""Sets the private_link of this DescribeStoreData.

        知识仓的私网链接信息。

        :param private_link: The private_link of this DescribeStoreData.
        :type private_link: str
        """
        self._private_link = private_link

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
        if not isinstance(other, DescribeStoreData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
