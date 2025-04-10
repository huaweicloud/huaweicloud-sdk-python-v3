# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageRiskConfigsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_id': 'str',
        'check_name': 'str',
        'severity': 'str',
        'standard': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'image_type': 'image_type',
        'offset': 'offset',
        'limit': 'limit',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_id': 'image_id',
        'check_name': 'check_name',
        'severity': 'severity',
        'standard': 'standard',
        'instance_id': 'instance_id'
    }

    def __init__(self, region=None, enterprise_project_id=None, image_type=None, offset=None, limit=None, namespace=None, image_name=None, image_version=None, image_id=None, check_name=None, severity=None, standard=None, instance_id=None):
        r"""ListImageRiskConfigsRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param image_type: 镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - local_image : 本地镜像   - instance_image : 企业镜像
        :type image_type: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示数量
        :type limit: int
        :param namespace: 组织名称
        :type namespace: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本名称
        :type image_version: str
        :param image_id: 镜像id
        :type image_id: str
        :param check_name: 基线名称
        :type check_name: str
        :param severity: 风险等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危
        :type severity: str
        :param standard: 标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准
        :type standard: str
        :param instance_id: 企业仓库实例ID，swr共享版无需使用该参数
        :type instance_id: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._image_type = None
        self._offset = None
        self._limit = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._image_id = None
        self._check_name = None
        self._severity = None
        self._standard = None
        self._instance_id = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.image_type = image_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_id is not None:
            self.image_id = image_id
        if check_name is not None:
            self.check_name = check_name
        if severity is not None:
            self.severity = severity
        if standard is not None:
            self.standard = standard
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def region(self):
        r"""Gets the region of this ListImageRiskConfigsRequest.

        Region ID

        :return: The region of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListImageRiskConfigsRequest.

        Region ID

        :param region: The region of this ListImageRiskConfigsRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageRiskConfigsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageRiskConfigsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListImageRiskConfigsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_type(self):
        r"""Gets the image_type of this ListImageRiskConfigsRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - local_image : 本地镜像   - instance_image : 企业镜像

        :return: The image_type of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListImageRiskConfigsRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - local_image : 本地镜像   - instance_image : 企业镜像

        :param image_type: The image_type of this ListImageRiskConfigsRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def offset(self):
        r"""Gets the offset of this ListImageRiskConfigsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListImageRiskConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageRiskConfigsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListImageRiskConfigsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImageRiskConfigsRequest.

        每页显示数量

        :return: The limit of this ListImageRiskConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageRiskConfigsRequest.

        每页显示数量

        :param limit: The limit of this ListImageRiskConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def namespace(self):
        r"""Gets the namespace of this ListImageRiskConfigsRequest.

        组织名称

        :return: The namespace of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListImageRiskConfigsRequest.

        组织名称

        :param namespace: The namespace of this ListImageRiskConfigsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ListImageRiskConfigsRequest.

        镜像名称

        :return: The image_name of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListImageRiskConfigsRequest.

        镜像名称

        :param image_name: The image_name of this ListImageRiskConfigsRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListImageRiskConfigsRequest.

        镜像版本名称

        :return: The image_version of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListImageRiskConfigsRequest.

        镜像版本名称

        :param image_version: The image_version of this ListImageRiskConfigsRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_id(self):
        r"""Gets the image_id of this ListImageRiskConfigsRequest.

        镜像id

        :return: The image_id of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListImageRiskConfigsRequest.

        镜像id

        :param image_id: The image_id of this ListImageRiskConfigsRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def check_name(self):
        r"""Gets the check_name of this ListImageRiskConfigsRequest.

        基线名称

        :return: The check_name of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ListImageRiskConfigsRequest.

        基线名称

        :param check_name: The check_name of this ListImageRiskConfigsRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def severity(self):
        r"""Gets the severity of this ListImageRiskConfigsRequest.

        风险等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危

        :return: The severity of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListImageRiskConfigsRequest.

        风险等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危

        :param severity: The severity of this ListImageRiskConfigsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def standard(self):
        r"""Gets the standard of this ListImageRiskConfigsRequest.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准

        :return: The standard of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ListImageRiskConfigsRequest.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准

        :param standard: The standard of this ListImageRiskConfigsRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListImageRiskConfigsRequest.

        企业仓库实例ID，swr共享版无需使用该参数

        :return: The instance_id of this ListImageRiskConfigsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListImageRiskConfigsRequest.

        企业仓库实例ID，swr共享版无需使用该参数

        :param instance_id: The instance_id of this ListImageRiskConfigsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListImageRiskConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
