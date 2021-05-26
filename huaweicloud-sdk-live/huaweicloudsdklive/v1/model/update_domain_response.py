# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


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
        'domain_source': 'DomainSourceInfo'
    }

    attribute_map = {
        'domain': 'domain',
        'domain_type': 'domain_type',
        'domain_cname': 'domain_cname',
        'region': 'region',
        'status': 'status',
        'create_time': 'create_time',
        'domain_source': 'domain_source'
    }

    def __init__(self, domain=None, domain_type=None, domain_cname=None, region=None, status=None, create_time=None, domain_source=None):
        """UpdateDomainResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateDomainResponse, self).__init__()

        self._domain = None
        self._domain_type = None
        self._domain_cname = None
        self._region = None
        self._status = None
        self._create_time = None
        self._domain_source = None
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
        if domain_source is not None:
            self.domain_source = domain_source

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
        :type: str
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
        :type: str
        """
        self._domain_type = domain_type

    @property
    def domain_cname(self):
        """Gets the domain_cname of this UpdateDomainResponse.

        直播域名的CName

        :return: The domain_cname of this UpdateDomainResponse.
        :rtype: str
        """
        return self._domain_cname

    @domain_cname.setter
    def domain_cname(self, domain_cname):
        """Sets the domain_cname of this UpdateDomainResponse.

        直播域名的CName

        :param domain_cname: The domain_cname of this UpdateDomainResponse.
        :type: str
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
        :type: str
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
        :type: str
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
        :type: datetime
        """
        self._create_time = create_time

    @property
    def domain_source(self):
        """Gets the domain_source of this UpdateDomainResponse.


        :return: The domain_source of this UpdateDomainResponse.
        :rtype: DomainSourceInfo
        """
        return self._domain_source

    @domain_source.setter
    def domain_source(self, domain_source):
        """Sets the domain_source of this UpdateDomainResponse.


        :param domain_source: The domain_source of this UpdateDomainResponse.
        :type: DomainSourceInfo
        """
        self._domain_source = domain_source

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
