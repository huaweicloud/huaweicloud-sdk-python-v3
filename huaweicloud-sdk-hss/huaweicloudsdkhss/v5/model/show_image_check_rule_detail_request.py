# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageCheckRuleDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'image_type': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'check_name': 'str',
        'check_type': 'str',
        'check_rule_id': 'str',
        'standard': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'image_type': 'image_type',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'check_name': 'check_name',
        'check_type': 'check_type',
        'check_rule_id': 'check_rule_id',
        'standard': 'standard'
    }

    def __init__(self, region=None, enterprise_project_id=None, image_type=None, namespace=None, image_name=None, image_version=None, check_name=None, check_type=None, check_rule_id=None, standard=None):
        """ShowImageCheckRuleDetailRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 租户企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param image_type: 镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库
        :type image_type: str
        :param namespace: 组织名称（没有镜像相关信息时，表示查询所有镜像）
        :type namespace: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本名称
        :type image_version: str
        :param check_name: 基线名称
        :type check_name: str
        :param check_type: 基线类型
        :type check_type: str
        :param check_rule_id: 检查项id
        :type check_rule_id: str
        :param standard: 标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准
        :type standard: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._image_type = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._check_name = None
        self._check_type = None
        self._check_rule_id = None
        self._standard = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.image_type = image_type
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        self.check_name = check_name
        self.check_type = check_type
        self.check_rule_id = check_rule_id
        self.standard = standard

    @property
    def region(self):
        """Gets the region of this ShowImageCheckRuleDetailRequest.

        region id

        :return: The region of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowImageCheckRuleDetailRequest.

        region id

        :param region: The region of this ShowImageCheckRuleDetailRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowImageCheckRuleDetailRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowImageCheckRuleDetailRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ShowImageCheckRuleDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_type(self):
        """Gets the image_type of this ShowImageCheckRuleDetailRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库

        :return: The image_type of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ShowImageCheckRuleDetailRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库

        :param image_type: The image_type of this ShowImageCheckRuleDetailRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def namespace(self):
        """Gets the namespace of this ShowImageCheckRuleDetailRequest.

        组织名称（没有镜像相关信息时，表示查询所有镜像）

        :return: The namespace of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowImageCheckRuleDetailRequest.

        组织名称（没有镜像相关信息时，表示查询所有镜像）

        :param namespace: The namespace of this ShowImageCheckRuleDetailRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        """Gets the image_name of this ShowImageCheckRuleDetailRequest.

        镜像名称

        :return: The image_name of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ShowImageCheckRuleDetailRequest.

        镜像名称

        :param image_name: The image_name of this ShowImageCheckRuleDetailRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        """Gets the image_version of this ShowImageCheckRuleDetailRequest.

        镜像版本名称

        :return: The image_version of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this ShowImageCheckRuleDetailRequest.

        镜像版本名称

        :param image_version: The image_version of this ShowImageCheckRuleDetailRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def check_name(self):
        """Gets the check_name of this ShowImageCheckRuleDetailRequest.

        基线名称

        :return: The check_name of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        """Sets the check_name of this ShowImageCheckRuleDetailRequest.

        基线名称

        :param check_name: The check_name of this ShowImageCheckRuleDetailRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_type(self):
        """Gets the check_type of this ShowImageCheckRuleDetailRequest.

        基线类型

        :return: The check_type of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this ShowImageCheckRuleDetailRequest.

        基线类型

        :param check_type: The check_type of this ShowImageCheckRuleDetailRequest.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def check_rule_id(self):
        """Gets the check_rule_id of this ShowImageCheckRuleDetailRequest.

        检查项id

        :return: The check_rule_id of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        """Sets the check_rule_id of this ShowImageCheckRuleDetailRequest.

        检查项id

        :param check_rule_id: The check_rule_id of this ShowImageCheckRuleDetailRequest.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def standard(self):
        """Gets the standard of this ShowImageCheckRuleDetailRequest.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准

        :return: The standard of this ShowImageCheckRuleDetailRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this ShowImageCheckRuleDetailRequest.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 华为标准   - qt_standard : 青腾标准

        :param standard: The standard of this ShowImageCheckRuleDetailRequest.
        :type standard: str
        """
        self._standard = standard

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
        if not isinstance(other, ShowImageCheckRuleDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
