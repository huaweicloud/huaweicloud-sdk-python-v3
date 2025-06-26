# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceRequestBody:

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
        'spec': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'project_id': 'str',
        'charge_mode': 'str',
        'enterprise_project_id': 'str',
        'resource_tags': 'list[CreateInstanceRequestBodyResourceTags]',
        'obs_encrypt': 'bool',
        'encrypt_type': 'str',
        'obs_bucket_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'spec': 'spec',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'project_id': 'project_id',
        'charge_mode': 'charge_mode',
        'enterprise_project_id': 'enterprise_project_id',
        'resource_tags': 'resource_tags',
        'obs_encrypt': 'obs_encrypt',
        'encrypt_type': 'encrypt_type',
        'obs_bucket_name': 'obs_bucket_name'
    }

    def __init__(self, name=None, description=None, spec=None, vpc_id=None, subnet_id=None, project_id=None, charge_mode=None, enterprise_project_id=None, resource_tags=None, obs_encrypt=None, encrypt_type=None, obs_bucket_name=None):
        r"""CreateInstanceRequestBody

        The model defined in huaweicloud sdk

        :param name: 企业仓库实例名称，小写字母或数字开头，后面跟小写字母、数字、点、下划线或中划线（其中点、下划线、中划线不能直接连续），小写字母或数字结尾，3-64个字符。
        :type name: str
        :param description: 企业仓库实例描述
        :type description: str
        :param spec: 企业仓库实例规格，目前支持基础版(swr.ee.basic)，企业版(swr.ee.professional)
        :type spec: str
        :param vpc_id: 用户虚拟私有云ID
        :type vpc_id: str
        :param subnet_id: 用户子网的网络ID
        :type subnet_id: str
        :param project_id: vpc和子网所在项目编号
        :type project_id: str
        :param charge_mode: 实例计费模式，目前只支持按需(postPaid)
        :type charge_mode: str
        :param enterprise_project_id: 企业项目编号
        :type enterprise_project_id: str
        :param resource_tags: 指定资源tag.
        :type resource_tags: list[:class:`huaweicloudsdkswr.v2.CreateInstanceRequestBodyResourceTags`]
        :param obs_encrypt: obs桶是否开启加密, 如果开启了加密，则可以根据encrypt_type指定加密算法
        :type obs_encrypt: bool
        :param encrypt_type: obs桶加密类型，空值使用AES-256加密算法, gm为国密加密算法
        :type encrypt_type: str
        :param obs_bucket_name: 指定obs桶的名称，当指定自定义obs桶之后，则无需对obs_encrypt、encrypt_type进行传值。
        :type obs_bucket_name: str
        """
        
        

        self._name = None
        self._description = None
        self._spec = None
        self._vpc_id = None
        self._subnet_id = None
        self._project_id = None
        self._charge_mode = None
        self._enterprise_project_id = None
        self._resource_tags = None
        self._obs_encrypt = None
        self._encrypt_type = None
        self._obs_bucket_name = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.spec = spec
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.project_id = project_id
        self.charge_mode = charge_mode
        self.enterprise_project_id = enterprise_project_id
        if resource_tags is not None:
            self.resource_tags = resource_tags
        if obs_encrypt is not None:
            self.obs_encrypt = obs_encrypt
        if encrypt_type is not None:
            self.encrypt_type = encrypt_type
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name

    @property
    def name(self):
        r"""Gets the name of this CreateInstanceRequestBody.

        企业仓库实例名称，小写字母或数字开头，后面跟小写字母、数字、点、下划线或中划线（其中点、下划线、中划线不能直接连续），小写字母或数字结尾，3-64个字符。

        :return: The name of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstanceRequestBody.

        企业仓库实例名称，小写字母或数字开头，后面跟小写字母、数字、点、下划线或中划线（其中点、下划线、中划线不能直接连续），小写字母或数字结尾，3-64个字符。

        :param name: The name of this CreateInstanceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateInstanceRequestBody.

        企业仓库实例描述

        :return: The description of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateInstanceRequestBody.

        企业仓库实例描述

        :param description: The description of this CreateInstanceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        r"""Gets the spec of this CreateInstanceRequestBody.

        企业仓库实例规格，目前支持基础版(swr.ee.basic)，企业版(swr.ee.professional)

        :return: The spec of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this CreateInstanceRequestBody.

        企业仓库实例规格，目前支持基础版(swr.ee.basic)，企业版(swr.ee.professional)

        :param spec: The spec of this CreateInstanceRequestBody.
        :type spec: str
        """
        self._spec = spec

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateInstanceRequestBody.

        用户虚拟私有云ID

        :return: The vpc_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateInstanceRequestBody.

        用户虚拟私有云ID

        :param vpc_id: The vpc_id of this CreateInstanceRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateInstanceRequestBody.

        用户子网的网络ID

        :return: The subnet_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateInstanceRequestBody.

        用户子网的网络ID

        :param subnet_id: The subnet_id of this CreateInstanceRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateInstanceRequestBody.

        vpc和子网所在项目编号

        :return: The project_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateInstanceRequestBody.

        vpc和子网所在项目编号

        :param project_id: The project_id of this CreateInstanceRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this CreateInstanceRequestBody.

        实例计费模式，目前只支持按需(postPaid)

        :return: The charge_mode of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this CreateInstanceRequestBody.

        实例计费模式，目前只支持按需(postPaid)

        :param charge_mode: The charge_mode of this CreateInstanceRequestBody.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateInstanceRequestBody.

        企业项目编号

        :return: The enterprise_project_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateInstanceRequestBody.

        企业项目编号

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def resource_tags(self):
        r"""Gets the resource_tags of this CreateInstanceRequestBody.

        指定资源tag.

        :return: The resource_tags of this CreateInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdkswr.v2.CreateInstanceRequestBodyResourceTags`]
        """
        return self._resource_tags

    @resource_tags.setter
    def resource_tags(self, resource_tags):
        r"""Sets the resource_tags of this CreateInstanceRequestBody.

        指定资源tag.

        :param resource_tags: The resource_tags of this CreateInstanceRequestBody.
        :type resource_tags: list[:class:`huaweicloudsdkswr.v2.CreateInstanceRequestBodyResourceTags`]
        """
        self._resource_tags = resource_tags

    @property
    def obs_encrypt(self):
        r"""Gets the obs_encrypt of this CreateInstanceRequestBody.

        obs桶是否开启加密, 如果开启了加密，则可以根据encrypt_type指定加密算法

        :return: The obs_encrypt of this CreateInstanceRequestBody.
        :rtype: bool
        """
        return self._obs_encrypt

    @obs_encrypt.setter
    def obs_encrypt(self, obs_encrypt):
        r"""Sets the obs_encrypt of this CreateInstanceRequestBody.

        obs桶是否开启加密, 如果开启了加密，则可以根据encrypt_type指定加密算法

        :param obs_encrypt: The obs_encrypt of this CreateInstanceRequestBody.
        :type obs_encrypt: bool
        """
        self._obs_encrypt = obs_encrypt

    @property
    def encrypt_type(self):
        r"""Gets the encrypt_type of this CreateInstanceRequestBody.

        obs桶加密类型，空值使用AES-256加密算法, gm为国密加密算法

        :return: The encrypt_type of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, encrypt_type):
        r"""Sets the encrypt_type of this CreateInstanceRequestBody.

        obs桶加密类型，空值使用AES-256加密算法, gm为国密加密算法

        :param encrypt_type: The encrypt_type of this CreateInstanceRequestBody.
        :type encrypt_type: str
        """
        self._encrypt_type = encrypt_type

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this CreateInstanceRequestBody.

        指定obs桶的名称，当指定自定义obs桶之后，则无需对obs_encrypt、encrypt_type进行传值。

        :return: The obs_bucket_name of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this CreateInstanceRequestBody.

        指定obs桶的名称，当指定自定义obs桶之后，则无需对obs_encrypt、encrypt_type进行传值。

        :param obs_bucket_name: The obs_bucket_name of this CreateInstanceRequestBody.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

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
        if not isinstance(other, CreateInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
