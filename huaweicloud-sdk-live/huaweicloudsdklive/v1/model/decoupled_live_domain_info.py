# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecoupledLiveDomainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'domain_type': 'str',
        'vendor': 'str',
        'region': 'str',
        'domain_cname': 'str',
        'status': 'str',
        'related_domain': 'str',
        'create_time': 'datetime',
        'status_describe': 'str',
        'service_area': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'domain_type': 'domain_type',
        'vendor': 'vendor',
        'region': 'region',
        'domain_cname': 'domain_cname',
        'status': 'status',
        'related_domain': 'related_domain',
        'create_time': 'create_time',
        'status_describe': 'status_describe',
        'service_area': 'service_area'
    }

    def __init__(self, domain=None, domain_type=None, vendor=None, region=None, domain_cname=None, status=None, related_domain=None, create_time=None, status_describe=None, service_area=None):
        """DecoupledLiveDomainInfo

        The model defined in huaweicloud sdk

        :param domain: 直播域名
        :type domain: str
        :param domain_type: 域名类型
        :type domain_type: str
        :param vendor: CDN厂商
        :type vendor: str
        :param region: 直播所属直播中心
        :type region: str
        :param domain_cname: 直播域名的CName
        :type domain_cname: str
        :param status: 直播域名的状态
        :type status: str
        :param related_domain: 播放域名关联的推流域名（只有domain_type为pull的时候有效）
        :type related_domain: str
        :param create_time: 域名创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间
        :type create_time: datetime
        :param status_describe: 状态描述
        :type status_describe: str
        :param service_area: 域名应用区域 - mainland_china表示中国大陆区域 - outside_mainland_china表示中国大陆以外区域 
        :type service_area: str
        """
        
        

        self._domain = None
        self._domain_type = None
        self._vendor = None
        self._region = None
        self._domain_cname = None
        self._status = None
        self._related_domain = None
        self._create_time = None
        self._status_describe = None
        self._service_area = None
        self.discriminator = None

        self.domain = domain
        self.domain_type = domain_type
        self.vendor = vendor
        self.region = region
        self.domain_cname = domain_cname
        self.status = status
        self.related_domain = related_domain
        self.create_time = create_time
        if status_describe is not None:
            self.status_describe = status_describe
        if service_area is not None:
            self.service_area = service_area

    @property
    def domain(self):
        """Gets the domain of this DecoupledLiveDomainInfo.

        直播域名

        :return: The domain of this DecoupledLiveDomainInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DecoupledLiveDomainInfo.

        直播域名

        :param domain: The domain of this DecoupledLiveDomainInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def domain_type(self):
        """Gets the domain_type of this DecoupledLiveDomainInfo.

        域名类型

        :return: The domain_type of this DecoupledLiveDomainInfo.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this DecoupledLiveDomainInfo.

        域名类型

        :param domain_type: The domain_type of this DecoupledLiveDomainInfo.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def vendor(self):
        """Gets the vendor of this DecoupledLiveDomainInfo.

        CDN厂商

        :return: The vendor of this DecoupledLiveDomainInfo.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this DecoupledLiveDomainInfo.

        CDN厂商

        :param vendor: The vendor of this DecoupledLiveDomainInfo.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def region(self):
        """Gets the region of this DecoupledLiveDomainInfo.

        直播所属直播中心

        :return: The region of this DecoupledLiveDomainInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DecoupledLiveDomainInfo.

        直播所属直播中心

        :param region: The region of this DecoupledLiveDomainInfo.
        :type region: str
        """
        self._region = region

    @property
    def domain_cname(self):
        """Gets the domain_cname of this DecoupledLiveDomainInfo.

        直播域名的CName

        :return: The domain_cname of this DecoupledLiveDomainInfo.
        :rtype: str
        """
        return self._domain_cname

    @domain_cname.setter
    def domain_cname(self, domain_cname):
        """Sets the domain_cname of this DecoupledLiveDomainInfo.

        直播域名的CName

        :param domain_cname: The domain_cname of this DecoupledLiveDomainInfo.
        :type domain_cname: str
        """
        self._domain_cname = domain_cname

    @property
    def status(self):
        """Gets the status of this DecoupledLiveDomainInfo.

        直播域名的状态

        :return: The status of this DecoupledLiveDomainInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DecoupledLiveDomainInfo.

        直播域名的状态

        :param status: The status of this DecoupledLiveDomainInfo.
        :type status: str
        """
        self._status = status

    @property
    def related_domain(self):
        """Gets the related_domain of this DecoupledLiveDomainInfo.

        播放域名关联的推流域名（只有domain_type为pull的时候有效）

        :return: The related_domain of this DecoupledLiveDomainInfo.
        :rtype: str
        """
        return self._related_domain

    @related_domain.setter
    def related_domain(self, related_domain):
        """Sets the related_domain of this DecoupledLiveDomainInfo.

        播放域名关联的推流域名（只有domain_type为pull的时候有效）

        :param related_domain: The related_domain of this DecoupledLiveDomainInfo.
        :type related_domain: str
        """
        self._related_domain = related_domain

    @property
    def create_time(self):
        """Gets the create_time of this DecoupledLiveDomainInfo.

        域名创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间

        :return: The create_time of this DecoupledLiveDomainInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DecoupledLiveDomainInfo.

        域名创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间

        :param create_time: The create_time of this DecoupledLiveDomainInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def status_describe(self):
        """Gets the status_describe of this DecoupledLiveDomainInfo.

        状态描述

        :return: The status_describe of this DecoupledLiveDomainInfo.
        :rtype: str
        """
        return self._status_describe

    @status_describe.setter
    def status_describe(self, status_describe):
        """Sets the status_describe of this DecoupledLiveDomainInfo.

        状态描述

        :param status_describe: The status_describe of this DecoupledLiveDomainInfo.
        :type status_describe: str
        """
        self._status_describe = status_describe

    @property
    def service_area(self):
        """Gets the service_area of this DecoupledLiveDomainInfo.

        域名应用区域 - mainland_china表示中国大陆区域 - outside_mainland_china表示中国大陆以外区域 

        :return: The service_area of this DecoupledLiveDomainInfo.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this DecoupledLiveDomainInfo.

        域名应用区域 - mainland_china表示中国大陆区域 - outside_mainland_china表示中国大陆以外区域 

        :param service_area: The service_area of this DecoupledLiveDomainInfo.
        :type service_area: str
        """
        self._service_area = service_area

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
        if not isinstance(other, DecoupledLiveDomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
