# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRegistryRequestBody:

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
        'type': 'str',
        'project_id': 'str',
        'region_id': 'str',
        'instance_id': 'str',
        'url': 'str',
        'credential': 'Credential',
        'dns_conf': 'DnsConf',
        'insecure': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'instance_id': 'instance_id',
        'url': 'url',
        'credential': 'credential',
        'dns_conf': 'dns_conf',
        'insecure': 'insecure'
    }

    def __init__(self, name=None, description=None, type=None, project_id=None, region_id=None, instance_id=None, url=None, credential=None, dns_conf=None, insecure=None):
        r"""CreateRegistryRequestBody

        The model defined in huaweicloud sdk

        :param name: 目标仓库名称，1-64字符组成，只能包含英文大小写、数字、汉字、中划线和下划线。
        :type name: str
        :param description: 目标仓库描述
        :type description: str
        :param type: 仓库类型，swr-pro(开源harbor仓库)、swr-pro-internal(SWR企业版仓库)、huawei-SWR(SWR共享版仓库)
        :type type: str
        :param project_id: 企业仓库实例所属的项目ID，当type为swr-pro-internal时必填
        :type project_id: str
        :param region_id: 区域ID，当type为swr-pro-internal时必填
        :type region_id: str
        :param instance_id: 企业仓库实例ID，当type为swr-pro-internal时必填
        :type instance_id: str
        :param url: 目标仓库的地址
        :type url: str
        :param credential: 
        :type credential: :class:`huaweicloudsdkswr.v2.Credential`
        :param dns_conf: 
        :type dns_conf: :class:`huaweicloudsdkswr.v2.DnsConf`
        :param insecure: 是否验证远程证书
        :type insecure: bool
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._project_id = None
        self._region_id = None
        self._instance_id = None
        self._url = None
        self._credential = None
        self._dns_conf = None
        self._insecure = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id
        if instance_id is not None:
            self.instance_id = instance_id
        self.url = url
        self.credential = credential
        if dns_conf is not None:
            self.dns_conf = dns_conf
        self.insecure = insecure

    @property
    def name(self):
        r"""Gets the name of this CreateRegistryRequestBody.

        目标仓库名称，1-64字符组成，只能包含英文大小写、数字、汉字、中划线和下划线。

        :return: The name of this CreateRegistryRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateRegistryRequestBody.

        目标仓库名称，1-64字符组成，只能包含英文大小写、数字、汉字、中划线和下划线。

        :param name: The name of this CreateRegistryRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateRegistryRequestBody.

        目标仓库描述

        :return: The description of this CreateRegistryRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateRegistryRequestBody.

        目标仓库描述

        :param description: The description of this CreateRegistryRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CreateRegistryRequestBody.

        仓库类型，swr-pro(开源harbor仓库)、swr-pro-internal(SWR企业版仓库)、huawei-SWR(SWR共享版仓库)

        :return: The type of this CreateRegistryRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateRegistryRequestBody.

        仓库类型，swr-pro(开源harbor仓库)、swr-pro-internal(SWR企业版仓库)、huawei-SWR(SWR共享版仓库)

        :param type: The type of this CreateRegistryRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateRegistryRequestBody.

        企业仓库实例所属的项目ID，当type为swr-pro-internal时必填

        :return: The project_id of this CreateRegistryRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateRegistryRequestBody.

        企业仓库实例所属的项目ID，当type为swr-pro-internal时必填

        :param project_id: The project_id of this CreateRegistryRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateRegistryRequestBody.

        区域ID，当type为swr-pro-internal时必填

        :return: The region_id of this CreateRegistryRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateRegistryRequestBody.

        区域ID，当type为swr-pro-internal时必填

        :param region_id: The region_id of this CreateRegistryRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateRegistryRequestBody.

        企业仓库实例ID，当type为swr-pro-internal时必填

        :return: The instance_id of this CreateRegistryRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateRegistryRequestBody.

        企业仓库实例ID，当type为swr-pro-internal时必填

        :param instance_id: The instance_id of this CreateRegistryRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def url(self):
        r"""Gets the url of this CreateRegistryRequestBody.

        目标仓库的地址

        :return: The url of this CreateRegistryRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateRegistryRequestBody.

        目标仓库的地址

        :param url: The url of this CreateRegistryRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def credential(self):
        r"""Gets the credential of this CreateRegistryRequestBody.

        :return: The credential of this CreateRegistryRequestBody.
        :rtype: :class:`huaweicloudsdkswr.v2.Credential`
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        r"""Sets the credential of this CreateRegistryRequestBody.

        :param credential: The credential of this CreateRegistryRequestBody.
        :type credential: :class:`huaweicloudsdkswr.v2.Credential`
        """
        self._credential = credential

    @property
    def dns_conf(self):
        r"""Gets the dns_conf of this CreateRegistryRequestBody.

        :return: The dns_conf of this CreateRegistryRequestBody.
        :rtype: :class:`huaweicloudsdkswr.v2.DnsConf`
        """
        return self._dns_conf

    @dns_conf.setter
    def dns_conf(self, dns_conf):
        r"""Sets the dns_conf of this CreateRegistryRequestBody.

        :param dns_conf: The dns_conf of this CreateRegistryRequestBody.
        :type dns_conf: :class:`huaweicloudsdkswr.v2.DnsConf`
        """
        self._dns_conf = dns_conf

    @property
    def insecure(self):
        r"""Gets the insecure of this CreateRegistryRequestBody.

        是否验证远程证书

        :return: The insecure of this CreateRegistryRequestBody.
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        r"""Sets the insecure of this CreateRegistryRequestBody.

        是否验证远程证书

        :param insecure: The insecure of this CreateRegistryRequestBody.
        :type insecure: bool
        """
        self._insecure = insecure

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
        if not isinstance(other, CreateRegistryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
