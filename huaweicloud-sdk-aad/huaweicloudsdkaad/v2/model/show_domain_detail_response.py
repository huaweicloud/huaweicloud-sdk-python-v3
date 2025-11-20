# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'cname': 'str',
        'domain_status': 'str',
        'pp_enable': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'cname': 'cname',
        'domain_status': 'domain_status',
        'pp_enable': 'pp_enable'
    }

    def __init__(self, domain_id=None, domain_name=None, cname=None, domain_status=None, pp_enable=None):
        r"""ShowDomainDetailResponse

        The model defined in huaweicloud sdk

        :param domain_id: 域名id
        :type domain_id: str
        :param domain_name: 域名
        :type domain_name: str
        :param cname: cname
        :type cname: str
        :param domain_status: 域名状态 0-正常，1-冻结
        :type domain_status: str
        :param pp_enable: 是否开启pp 0-关闭，1-开启
        :type pp_enable: int
        """
        
        super().__init__()

        self._domain_id = None
        self._domain_name = None
        self._cname = None
        self._domain_status = None
        self._pp_enable = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if cname is not None:
            self.cname = cname
        if domain_status is not None:
            self.domain_status = domain_status
        if pp_enable is not None:
            self.pp_enable = pp_enable

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowDomainDetailResponse.

        域名id

        :return: The domain_id of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowDomainDetailResponse.

        域名id

        :param domain_id: The domain_id of this ShowDomainDetailResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainDetailResponse.

        域名

        :return: The domain_name of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainDetailResponse.

        域名

        :param domain_name: The domain_name of this ShowDomainDetailResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def cname(self):
        r"""Gets the cname of this ShowDomainDetailResponse.

        cname

        :return: The cname of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        r"""Sets the cname of this ShowDomainDetailResponse.

        cname

        :param cname: The cname of this ShowDomainDetailResponse.
        :type cname: str
        """
        self._cname = cname

    @property
    def domain_status(self):
        r"""Gets the domain_status of this ShowDomainDetailResponse.

        域名状态 0-正常，1-冻结

        :return: The domain_status of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        r"""Sets the domain_status of this ShowDomainDetailResponse.

        域名状态 0-正常，1-冻结

        :param domain_status: The domain_status of this ShowDomainDetailResponse.
        :type domain_status: str
        """
        self._domain_status = domain_status

    @property
    def pp_enable(self):
        r"""Gets the pp_enable of this ShowDomainDetailResponse.

        是否开启pp 0-关闭，1-开启

        :return: The pp_enable of this ShowDomainDetailResponse.
        :rtype: int
        """
        return self._pp_enable

    @pp_enable.setter
    def pp_enable(self, pp_enable):
        r"""Sets the pp_enable of this ShowDomainDetailResponse.

        是否开启pp 0-关闭，1-开启

        :param pp_enable: The pp_enable of this ShowDomainDetailResponse.
        :type pp_enable: int
        """
        self._pp_enable = pp_enable

    def to_dict(self):
        import warnings
        warnings.warn("ShowDomainDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowDomainDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
