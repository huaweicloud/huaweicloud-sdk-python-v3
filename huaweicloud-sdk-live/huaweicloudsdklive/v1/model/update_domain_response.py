# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainResponse(SdkResponse):

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
        'domain_cname': 'str',
        'region': 'str',
        'status': 'str',
        'create_time': 'datetime',
        'status_describe': 'str',
        'service_area': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'domain_type': 'domain_type',
        'domain_cname': 'domain_cname',
        'region': 'region',
        'status': 'status',
        'create_time': 'create_time',
        'status_describe': 'status_describe',
        'service_area': 'service_area',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain=None, domain_type=None, domain_cname=None, region=None, status=None, create_time=None, status_describe=None, service_area=None, enterprise_project_id=None):
        """UpdateDomainResponse

        The model defined in huaweicloud sdk

        :param domain: 直播域名
        :type domain: str
        :param domain_type: 域名类型 - pull表示播放域名 - push表示推流域名 
        :type domain_type: str
        :param domain_cname: 直播域名的CNAME
        :type domain_cname: str
        :param region: 直播所属直播中心
        :type region: str
        :param status: 直播域名的状态
        :type status: str
        :param create_time: 域名创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间
        :type create_time: datetime
        :param status_describe: 状态描述
        :type status_describe: str
        :param service_area: 域名应用区域 - mainland_china表示中国大陆区域 - outside_mainland_china表示中国大陆以外区域 
        :type service_area: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        super(UpdateDomainResponse, self).__init__()

        self._domain = None
        self._domain_type = None
        self._domain_cname = None
        self._region = None
        self._status = None
        self._create_time = None
        self._status_describe = None
        self._service_area = None
        self._enterprise_project_id = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if domain_type is not None:
            self.domain_type = domain_type
        if domain_cname is not None:
            self.domain_cname = domain_cname
        if region is not None:
            self.region = region
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if status_describe is not None:
            self.status_describe = status_describe
        if service_area is not None:
            self.service_area = service_area
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain(self):
        """Gets the domain of this UpdateDomainResponse.

        直播域名

        :return: The domain of this UpdateDomainResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UpdateDomainResponse.

        直播域名

        :param domain: The domain of this UpdateDomainResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def domain_type(self):
        """Gets the domain_type of this UpdateDomainResponse.

        域名类型 - pull表示播放域名 - push表示推流域名 

        :return: The domain_type of this UpdateDomainResponse.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this UpdateDomainResponse.

        域名类型 - pull表示播放域名 - push表示推流域名 

        :param domain_type: The domain_type of this UpdateDomainResponse.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def domain_cname(self):
        """Gets the domain_cname of this UpdateDomainResponse.

        直播域名的CNAME

        :return: The domain_cname of this UpdateDomainResponse.
        :rtype: str
        """
        return self._domain_cname

    @domain_cname.setter
    def domain_cname(self, domain_cname):
        """Sets the domain_cname of this UpdateDomainResponse.

        直播域名的CNAME

        :param domain_cname: The domain_cname of this UpdateDomainResponse.
        :type domain_cname: str
        """
        self._domain_cname = domain_cname

    @property
    def region(self):
        """Gets the region of this UpdateDomainResponse.

        直播所属直播中心

        :return: The region of this UpdateDomainResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this UpdateDomainResponse.

        直播所属直播中心

        :param region: The region of this UpdateDomainResponse.
        :type region: str
        """
        self._region = region

    @property
    def status(self):
        """Gets the status of this UpdateDomainResponse.

        直播域名的状态

        :return: The status of this UpdateDomainResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateDomainResponse.

        直播域名的状态

        :param status: The status of this UpdateDomainResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this UpdateDomainResponse.

        域名创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间

        :return: The create_time of this UpdateDomainResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateDomainResponse.

        域名创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间

        :param create_time: The create_time of this UpdateDomainResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def status_describe(self):
        """Gets the status_describe of this UpdateDomainResponse.

        状态描述

        :return: The status_describe of this UpdateDomainResponse.
        :rtype: str
        """
        return self._status_describe

    @status_describe.setter
    def status_describe(self, status_describe):
        """Sets the status_describe of this UpdateDomainResponse.

        状态描述

        :param status_describe: The status_describe of this UpdateDomainResponse.
        :type status_describe: str
        """
        self._status_describe = status_describe

    @property
    def service_area(self):
        """Gets the service_area of this UpdateDomainResponse.

        域名应用区域 - mainland_china表示中国大陆区域 - outside_mainland_china表示中国大陆以外区域 

        :return: The service_area of this UpdateDomainResponse.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this UpdateDomainResponse.

        域名应用区域 - mainland_china表示中国大陆区域 - outside_mainland_china表示中国大陆以外区域 

        :param service_area: The service_area of this UpdateDomainResponse.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this UpdateDomainResponse.

        企业项目ID

        :return: The enterprise_project_id of this UpdateDomainResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this UpdateDomainResponse.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this UpdateDomainResponse.
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
        if not isinstance(other, UpdateDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
